#!/usr/bin/env python3
"""Quick import test to verify all modules can be imported."""

import sys

try:
    print("✓ Testing imports...")
    
    print("  • Importing config...")
    from app.core.config import settings
    
    print("  • Importing database...")
    from app.db.base import Base, SessionLocal, engine, get_db
    
    print("  • Importing models...")
    from app.models import AirQuality, School, EducationQuality, User, AIAnalysis
    
    print("  • Importing schemas...")
    from app.schemas import air_quality, user, ai_result
    
    print("  • Importing services...")
    from app.services import OpenDataService, AIService
    
    print("  • Importing endpoints...")
    from app.api.endpoints import air_quality as aq_endpoints
    from app.api.endpoints import ai_analysis as ai_endpoints
    
    print("  • Importing router...")
    from app.api.router import api_router
    
    print("  • Importing main app...")
    from main import app
    
    print("\n✅ All imports successful!")
    print(f"   App: {app.title}")
    print(f"   Version: {settings.app_version}")
    print(f"   Database: {settings.database_url[:50]}...")
    
except Exception as e:
    print(f"\n❌ Import failed: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
