"""Linked Open Data (LOD) converter service."""

import json
from rdflib import Graph, Namespace, Literal, URIRef
from datetime import datetime

class LODConverter:
    """Convert data to Linked Open Data formats (JSON-LD, RDF)."""
    
    SOSA = Namespace("http://www.w3.org/ns/sosa/")
    SSN = Namespace("http://www.w3.org/ns/ssn/")
    NGSI = Namespace("https://uri.etsi.org/ngsi-ld/")
    QUDT = Namespace("http://qudt.org/schema/qudt/")
    WGS84 = Namespace("http://www.w3.org/2003/01/geo/wgs84_pos#")
    
    @staticmethod
    def air_quality_to_json_ld(data: dict) -> dict:
        """Convert air quality data to JSON-LD."""
        return {
            "@context": {
                "@vocab": "http://www.w3.org/ns/sosa/",
                "aqi": "http://example.org/aqi",
                "pm25": "http://example.org/pm25",
                "location": "http://www.w3.org/2003/01/geo/wgs84_pos#",
            },
            "@type": "Observation",
            "observedProperty": data.get("ward_name"),
            "hasSimpleResult": {
                "aqi": data.get("aqi"),
                "pm25": data.get("pm25"),
                "pm10": data.get("pm10"),
            },
            "resultTime": data.get("measurement_time", datetime.utcnow().isoformat()),
            "madeBySensor": {
                "@type": "Sensor",
                "location": {
                    "latitude": data.get("latitude"),
                    "longitude": data.get("longitude"),
                }
            }
        }
    
    @staticmethod
    def to_rdf(data: dict, data_type: str = "AirQuality") -> str:
        """Convert data to RDF/Turtle format."""
        g = Graph()
        
        # Define namespaces
        g.bind("sosa", LODConverter.SOSA)
        g.bind("ssn", LODConverter.SSN)
        g.bind("ngsi", LODConverter.NGSI)
        g.bind("qudt", LODConverter.QUDT)
        g.bind("wgs84", LODConverter.WGS84)
        
        # Create resource URI
        resource_uri = URIRef(f"http://example.org/{data_type}/{data.get('id', 'default')}")
        
        # Add observation triples
        g.add((resource_uri, LODConverter.SOSA.observedProperty, Literal(data.get("ward_name"))))
        
        if data_type == "AirQuality":
            g.add((resource_uri, URIRef("http://example.org/aqi"), Literal(data.get("aqi"))))
            g.add((resource_uri, URIRef("http://example.org/pm25"), Literal(data.get("pm25"))))
        
        # Add location
        if "latitude" in data and "longitude" in data:
            g.add((resource_uri, LODConverter.WGS84.lat, Literal(data["latitude"])))
            g.add((resource_uri, LODConverter.WGS84.long, Literal(data["longitude"])))
        
        return g.serialize(format="turtle")
    
    @staticmethod
    def to_jsonld(data: dict, context_url: str = None) -> dict:
        """Convert data to JSON-LD format."""
        if context_url is None:
            context_url = "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"
        
        return {
            "@context": context_url,
            "@type": "Thing",
            "id": data.get("id", f"urn:uuid:{datetime.utcnow().timestamp()}"),
            "name": data.get("ward_name", "Unknown"),
            "data": {
                "@type": "ObservationData",
                **{k: v for k, v in data.items() if k not in ["id", "ward_name", "measurement_time"]}
            },
            "observationDateTime": data.get("measurement_time", datetime.utcnow().isoformat()),
        }
    
    @staticmethod
    def to_rdf_xml(data: dict) -> str:
        """Convert data to RDF/XML format."""
        g = Graph()
        
        # Define namespaces
        g.bind("sosa", LODConverter.SOSA)
        g.bind("wgs84", LODConverter.WGS84)
        
        # Create resource URI
        resource_uri = URIRef(f"http://example.org/data/{data.get('id', 'default')}")
        g.add((resource_uri, URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type"), LODConverter.SOSA.Observation))
        
        # Add properties
        for key, value in data.items():
            if isinstance(value, (int, float)):
                g.add((resource_uri, URIRef(f"http://example.org/{key}"), Literal(value)))
            else:
                g.add((resource_uri, URIRef(f"http://example.org/{key}"), Literal(str(value))))
        
        return g.serialize(format="xml")
