"""FiWARE Orion-LD integration service."""

import httpx
import json
from datetime import datetime
from app.core.config import settings
from app.core.constants import (
    ENTITY_TYPE_AIR_QUALITY,
    ENTITY_TYPE_WEATHER,
    ENTITY_TYPE_ENERGY,
)

class FiwareService:
    """Service for interacting with FiWARE Orion-LD."""
    
    BASE_URL = f"{settings.orion_url}/ngsi-ld/v1"
    CONTEXT = "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"
    
    @staticmethod
    async def create_air_quality_entity(ward_name: str, aqi: int, pm25: float, **kwargs):
        """Create AirQualityObserved NGSI-LD entity."""
        entity = {
            "@context": FiwareService.CONTEXT,
            "id": f"urn:ngsi-ld:AirQualityObserved:{ward_name}:{datetime.now().isoformat()}",
            "type": ENTITY_TYPE_AIR_QUALITY,
            "address": {"value": ward_name},
            "aqi": {"value": aqi},
            "pm25": {"value": pm25},
            "observationDateTime": {"value": datetime.utcnow().isoformat() + "Z"},
            "location": {
                "value": {
                    "type": "Point",
                    "coordinates": [kwargs.get("longitude", 0), kwargs.get("latitude", 0)]
                }
            }
        }
        
        return await FiwareService.publish_entity(entity)
    
    @staticmethod
    async def create_weather_entity(ward_name: str, temperature: float, humidity: int, **kwargs):
        """Create WeatherObserved NGSI-LD entity."""
        entity = {
            "@context": FiwareService.CONTEXT,
            "id": f"urn:ngsi-ld:WeatherObserved:{ward_name}:{datetime.now().isoformat()}",
            "type": ENTITY_TYPE_WEATHER,
            "address": {"value": ward_name},
            "temperature": {"value": temperature, "unitCode": "CEL"},
            "relativeHumidity": {"value": humidity},
            "observationDateTime": {"value": datetime.utcnow().isoformat() + "Z"},
            "location": {
                "value": {
                    "type": "Point",
                    "coordinates": [kwargs.get("longitude", 0), kwargs.get("latitude", 0)]
                }
            }
        }
        
        return await FiwareService.publish_entity(entity)
    
    @staticmethod
    async def create_energy_entity(ward_name: str, solar_potential_kw: float, **kwargs):
        """Create EnergyData NGSI-LD entity."""
        entity = {
            "@context": FiwareService.CONTEXT,
            "id": f"urn:ngsi-ld:EnergyData:{ward_name}:{datetime.now().isoformat()}",
            "type": ENTITY_TYPE_ENERGY,
            "address": {"value": ward_name},
            "solarPotential": {"value": solar_potential_kw, "unitCode": "KWT"},
            "renewablePercentage": {"value": kwargs.get("renewable_percentage", 0)},
            "observationDateTime": {"value": datetime.utcnow().isoformat() + "Z"},
            "location": {
                "value": {
                    "type": "Point",
                    "coordinates": [kwargs.get("longitude", 0), kwargs.get("latitude", 0)]
                }
            }
        }
        
        return await FiwareService.publish_entity(entity)
    
    @staticmethod
    async def publish_entity(entity: dict):
        """Publish entity to Orion-LD."""
        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(
                    f"{FiwareService.BASE_URL}/entities",
                    json=entity,
                    headers={"Content-Type": "application/ld+json"},
                    timeout=30.0
                )
                return {
                    "status": response.status_code,
                    "success": response.status_code in [201, 204],
                    "entity_id": entity.get("id")
                }
            except Exception as e:
                return {
                    "status": 500,
                    "success": False,
                    "error": str(e)
                }
    
    @staticmethod
    async def get_entities(entity_type: str = None, ward_name: str = None):
        """Get NGSI-LD entities from Orion-LD."""
        async with httpx.AsyncClient() as client:
            try:
                params = {}
                if entity_type:
                    params["type"] = entity_type
                if ward_name:
                    params["q"] = f"address=={ward_name}"
                
                response = await client.get(
                    f"{FiwareService.BASE_URL}/entities",
                    params=params,
                    headers={"Accept": "application/ld+json"},
                    timeout=30.0
                )
                
                return {
                    "status": response.status_code,
                    "success": response.status_code == 200,
                    "entities": response.json() if response.status_code == 200 else []
                }
            except Exception as e:
                return {
                    "status": 500,
                    "success": False,
                    "error": str(e),
                    "entities": []
                }
    
    @staticmethod
    async def delete_entity(entity_id: str):
        """Delete entity from Orion-LD."""
        async with httpx.AsyncClient() as client:
            try:
                response = await client.delete(
                    f"{FiwareService.BASE_URL}/entities/{entity_id}",
                    timeout=30.0
                )
                return {
                    "status": response.status_code,
                    "success": response.status_code in [204],
                }
            except Exception as e:
                return {
                    "status": 500,
                    "success": False,
                    "error": str(e)
                }
