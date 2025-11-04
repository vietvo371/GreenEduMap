"""AI correlation analysis service."""

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from scipy.stats import pearsonr
from app.core.config import settings
from app.core.constants import MIN_CORRELATION_THRESHOLD

class AIService:
    """AI analysis service for environmental-educational-energy correlations."""
    
    @staticmethod
    def analyze_correlation(
        air_quality_data: list,
        school_data: list,
        energy_data: list,
        ward_name: str
    ) -> dict:
        """Analyze correlation between environment, education, and energy."""
        
        try:
            # Prepare data for analysis
            aqi_scores = np.array([d.get("aqi", 0) for d in air_quality_data]) if air_quality_data else np.array([])
            school_scores = np.array([d.get("avg_score", 0) * 100 for d in school_data]) if school_data else np.array([])
            energy_renewable = np.array([d.get("renewable_percentage", 0) for d in energy_data]) if energy_data else np.array([])
            
            results = {
                "ward": ward_name,
                "correlations": {},
                "recommendations": [],
                "confidence": 0.0
            }
            
            # Calculate correlations
            if len(aqi_scores) > 1 and len(school_scores) > 1:
                corr_env_edu, p_value = pearsonr(aqi_scores, school_scores)
                results["correlations"]["environment_education"] = float(corr_env_edu)
                results["correlations"]["env_edu_p_value"] = float(p_value)
            
            if len(energy_renewable) > 1 and len(aqi_scores) > 1:
                corr_energy_env, p_value = pearsonr(energy_renewable, aqi_scores)
                results["correlations"]["energy_environment"] = float(corr_energy_env)
                results["correlations"]["energy_env_p_value"] = float(p_value)
            
            # Generate recommendations based on correlations
            results["recommendations"] = AIService._generate_recommendations(
                ward_name,
                results["correlations"],
                len(school_data),
                len(energy_data)
            )
            
            # Calculate overall confidence
            if results["correlations"]:
                confidence = np.mean([abs(v) for v in results["correlations"].values() if isinstance(v, (int, float))])
                results["confidence"] = float(min(confidence, 1.0))
            
            return results
        
        except Exception as e:
            return {
                "ward": ward_name,
                "error": str(e),
                "correlations": {},
                "recommendations": [],
                "confidence": 0.0
            }
    
    @staticmethod
    def _generate_recommendations(ward: str, correlations: dict, num_schools: int, num_energy: int) -> list:
        """Generate green action recommendations based on correlation analysis."""
        recommendations = []
        
        # Environmental-Education correlation
        env_edu_corr = correlations.get("environment_education", 0)
        if abs(env_edu_corr) > MIN_CORRELATION_THRESHOLD:
            if env_edu_corr < -0.5:  # Negative correlation: better AQI, worse education
                recommendations.append({
                    "action": "Kết hợp môi trường với giáo dục",
                    "description": f"Huyền bí: môi trường tốt nhưng giáo dục yếu ở {ward}. Cần tạo khóa học môi trường.",
                    "impact": "high",
                    "target": "schools"
                })
        
        # Energy recommendation
        if num_energy > 0:
            recommendations.append({
                "action": "Tăng năng lượng tái tạo",
                "description": f"Lắp đặt 5-10 hệ thống pin mặt trời tại trường học và tòa nhà công cộng ở {ward}",
                "impact": "medium",
                "target": "energy"
            })
        
        # Green program recommendation
        if num_schools > 0:
            recommendations.append({
                "action": "Tạo chương trình xanh",
                "description": f"Mở {max(1, num_schools // 2)} khóa học về bảo vệ môi trường cho {num_schools} trường học",
                "impact": "high",
                "target": "education"
            })
        
        # Tree planting recommendation
        recommendations.append({
            "action": "Trồng cây xanh",
            "description": f"Trồng 500-1000 cây xanh tại {ward} để cải thiện chất lượng không khí",
            "impact": "high",
            "target": "environment",
            "estimated_co2_reduction": "50-100 tấn CO2/năm"
        })
        
        return recommendations
    
    @staticmethod
    def cluster_wards(wards_data: list, n_clusters: int = None) -> dict:
        """Cluster wards based on environmental and educational metrics."""
        
        if not wards_data:
            return {"error": "No data provided", "clusters": {}}
        
        n_clusters = n_clusters or settings.ai_cluster_count
        
        try:
            # Prepare features
            features = []
            ward_names = []
            
            for ward in wards_data:
                ward_names.append(ward["name"])
                feature = [
                    ward.get("aqi", 0),
                    ward.get("avg_school_score", 0),
                    ward.get("renewable_energy", 0),
                    ward.get("num_schools", 0),
                ]
                features.append(feature)
            
            # Standardize features
            scaler = StandardScaler()
            features_scaled = scaler.fit_transform(features)
            
            # Clustering
            kmeans = KMeans(n_clusters=min(n_clusters, len(ward_names)), random_state=42)
            labels = kmeans.fit_predict(features_scaled)
            
            # Organize results
            clusters = {}
            for ward_name, label in zip(ward_names, labels):
                if label not in clusters:
                    clusters[label] = []
                clusters[label].append(ward_name)
            
            return {
                "success": True,
                "clusters": clusters,
                "n_clusters": len(clusters)
            }
        
        except Exception as e:
            return {
                "error": str(e),
                "success": False,
                "clusters": {}
            }
    
    @staticmethod
    def predict_impact(action: str, current_aqi: int, current_energy: float) -> dict:
        """Predict impact of a green action."""
        
        impacts = {
            "tree_planting": {
                "aqi_reduction": 5 * (current_aqi / 100),  # Scale with current AQI
                "co2_reduction": 50,  # kg CO2/year per 100 trees
                "timeline": "1-2 years"
            },
            "solar_installation": {
                "energy_generation": 5000,  # kWh/year
                "co2_reduction": 2500,  # kg CO2/year
                "roi_years": 5
            },
            "green_education": {
                "awareness_increase": 30,  # percent
                "estimated_participants": 500,
                "co2_awareness": "High"
            }
        }
        
        return impacts.get(action, {
            "note": f"No specific data for action: {action}",
            "general_impact": "Positive environmental effect expected"
        })
