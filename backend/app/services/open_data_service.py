"""Open Data service - Fetch data from external APIs."""

import httpx
import asyncio
from datetime import datetime, timedelta
from app.core.config import settings

class OpenDataService:
    """Service for fetching open data from external sources."""
    
    @staticmethod
    async def fetch_openaq_data(city: str = "Hanoi") -> dict:
        """Fetch air quality data from OpenAQ API."""
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    f"{settings.openaq_api_url}/locations",
                    params={
                        "city": city,
                        "limit": 100,
                    },
                    headers={"X-API-Key": settings.openaq_api_key} if settings.openaq_api_key != "demo" else {},
                    timeout=30.0
                )
                
                if response.status_code == 200:
                    data = response.json()
                    return {
                        "success": True,
                        "source": "OpenAQ",
                        "city": city,
                        "locations": data.get("results", [])
                    }
                else:
                    return {
                        "success": False,
                        "error": f"OpenAQ API returned {response.status_code}",
                        "locations": []
                    }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "locations": []
            }
    
    @staticmethod
    async def fetch_openweather_data(city: str = "Hanoi") -> dict:
        """Fetch weather data from OpenWeather API."""
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    f"{settings.openweather_api_url}/weather",
                    params={
                        "q": city,
                        "appid": settings.openweather_api_key,
                        "units": "metric"
                    },
                    timeout=30.0
                )
                
                if response.status_code == 200:
                    data = response.json()
                    return {
                        "success": True,
                        "source": "OpenWeather",
                        "city": city,
                        "weather": {
                            "temperature": data["main"]["temp"],
                            "humidity": data["main"]["humidity"],
                            "pressure": data["main"]["pressure"],
                            "wind_speed": data["wind"]["speed"],
                            "description": data["weather"][0]["description"],
                            "timestamp": datetime.utcnow().isoformat()
                        }
                    }
                else:
                    return {
                        "success": False,
                        "error": f"OpenWeather API returned {response.status_code}",
                        "weather": {}
                    }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "weather": {}
            }
    
    @staticmethod
    async def fetch_osm_schools(bbox: tuple = None) -> dict:
        """Fetch schools from OpenStreetMap Overpass API."""
        try:
            # Default bbox for Hanoi
            if bbox is None:
                bbox = (21.0, 105.8, 21.1, 105.9)  # (lat_min, lon_min, lat_max, lon_max)
            
            query = f"""
            [bbox:{bbox[0]},{bbox[1]},{bbox[2]},{bbox[3]}]
            [out:json];
            (
                node["amenity"="school"];
                way["amenity"="school"];
            );
            out center;
            """
            
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    "https://overpass-api.de/api/interpreter",
                    data=query,
                    timeout=30.0
                )
                
                if response.status_code == 200:
                    data = response.json()
                    schools = []
                    
                    for elem in data.get("elements", []):
                        school_data = {
                            "id": elem.get("id"),
                            "name": elem.get("tags", {}).get("name", "Unknown School"),
                            "latitude": elem.get("lat", elem.get("center", {}).get("lat")),
                            "longitude": elem.get("lon", elem.get("center", {}).get("lon")),
                            "address": elem.get("tags", {}).get("addr:full", ""),
                        }
                        
                        if school_data["latitude"] and school_data["longitude"]:
                            schools.append(school_data)
                    
                    return {
                        "success": True,
                        "source": "OpenStreetMap",
                        "bbox": bbox,
                        "schools": schools
                    }
                else:
                    return {
                        "success": False,
                        "error": f"OSM API returned {response.status_code}",
                        "schools": []
                    }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "schools": []
            }
    
    @staticmethod
    async def fetch_all_data(city: str = "Hanoi") -> dict:
        """Fetch all open data concurrently."""
        try:
            results = await asyncio.gather(
                OpenDataService.fetch_openaq_data(city),
                OpenDataService.fetch_openweather_data(city),
                OpenDataService.fetch_osm_schools(),
            )
            
            return {
                "success": all(r.get("success", False) for r in results),
                "timestamp": datetime.utcnow().isoformat(),
                "data": {
                    "air_quality": results[0],
                    "weather": results[1],
                    "schools": results[2],
                }
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "data": {}
            }
    
    @staticmethod
    def transform_openaq_to_schema(location: dict) -> dict:
        """Transform OpenAQ data to our schema."""
        return {
            "ward_name": location.get("city", "Unknown"),
            "aqi": location.get("aqi", 0),
            "pm25": location.get("measurements", [{}])[0].get("value", 0) if location.get("measurements") else 0,
            "latitude": location.get("coordinates", {}).get("latitude", 0),
            "longitude": location.get("coordinates", {}).get("longitude", 0),
            "measurement_time": datetime.utcnow().isoformat(),
        }
    
    @staticmethod
    def transform_openweather_to_schema(weather: dict, city: str) -> dict:
        """Transform OpenWeather data to our schema."""
        return {
            "ward_name": city,
            "temperature": weather["main"]["temp"],
            "humidity": weather["main"]["humidity"],
            "pressure": weather["main"]["pressure"],
            "wind_speed": weather["wind"]["speed"],
            "latitude": weather.get("coord", {}).get("lat", 0),
            "longitude": weather.get("coord", {}).get("lon", 0),
            "measurement_time": datetime.utcnow().isoformat(),
        }
