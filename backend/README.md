
# GreenEduMap Backend

FastAPI backend for GreenEduMap - Smart City Open Data Platform with FiWARE Orion-LD Integration.

## 🧠 Architecture

- **FastAPI** - High-performance Python web framework
- **PostgreSQL + PostGIS** - Spatial database
- **FiWARE Orion-LD** - Semantic broker for NGSI-LD entities
- **MongoDB** - Document store for Orion-LD
- **scikit-learn** - AI correlation analysis
- **Docker** - Containerization

## 📁 Project Structure

```
backend/
├── main.py                 # FastAPI application entry point
├── requirements.txt        # Python dependencies
├── Dockerfile             # Docker image definition
├── .env.example           # Environment variables template
│
├── app/
│   ├── __init__.py
│   ├── core/
│   │   ├── config.py      # Configuration management
│   │   ├── security.py    # JWT and auth helpers
│   │   └── constants.py   # Application constants
│   │
│   ├── db/
│   │   ├── base.py        # SQLAlchemy setup
│   │   ├── session.py     # Database session
│   │   ├── init_db.py     # Database initialization
│   │   └── models.py      # SQLAlchemy ORM models
│   │
│   ├── models/
│   │   ├── air_quality.py # AirQualityObserved
│   │   ├── weather.py     # WeatherObserved
│   │   ├── energy.py      # EnergyData
│   │   ├── school.py      # School & Course models
│   │   ├── user.py        # User model
│   │   └── feedback.py    # CitizenFeedback
│   │
│   ├── schemas/
│   │   ├── air_quality.py # Pydantic schemas
│   │   ├── school.py
│   │   ├── user.py
│   │   └── ai_result.py
│   │
│   ├── services/
│   │   ├── open_data_service.py   # OpenAQ, OpenWeather, OSM
│   │   ├── fiware_service.py      # Orion-LD communication
│   │   ├── lod_converter.py       # JSON → JSON-LD converter
│   │   ├── ai_service.py          # Correlation analysis
│   │   └── auth_service.py        # JWT tokens
│   │
│   ├── api/
│   │   ├── __init__.py
│   │   ├── endpoints/
│   │   │   ├── __init__.py
│   │   │   ├── auth.py           # POST /auth/login, /auth/register
│   │   │   ├── air_quality.py    # GET /api/air-quality
│   │   │   ├── weather.py        # GET /api/weather
│   │   │   ├── schools.py        # CRUD /api/schools
│   │   │   ├── courses.py        # CRUD /api/courses
│   │   │   ├── ai.py            # GET /api/ai/analysis
│   │   │   ├── ngsi_ld.py       # GET /api/ngsi-ld/entities
│   │   │   └── feedback.py      # POST /api/feedback
│   │   │
│   │   └── api.py               # API router
│   │
│   ├── utils/
│   │   ├── http_client.py       # Async HTTP client
│   │   ├── geojson_helper.py    # GeoJSON utilities
│   │   └── rdf_builder.py       # RDF/JSON-LD builder
│   │
│   └── ontologies/
│       ├── sosa_ssn.py          # SOSA/SSN ontology definitions
│       ├── ngsi_ld_context.json # NGSI-LD context
│       └── fiware_models.py     # FiWARE data models

├── tests/
│   ├── __init__.py
│   ├── test_auth.py
│   ├── test_air_quality.py
│   └── test_ai_service.py

└── migrations/               # Alembic database migrations
    ├── env.py
    └── versions/
```

## 🚀 Getting Started

### Installation (Docker Compose - Recommended)

From project root:
```bash
docker compose up --build
```

### Installation (Local Development)

1. **Create virtual environment:**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment:**
   ```bash
   cp .env.example .env
   ```

4. **Run development server:**
   ```bash
   uvicorn app.main:app --reload --port 8000
   ```

## 🌍 API Endpoints

- `POST /auth/register` - Register new user
- `POST /auth/login` - Login and get JWT token
- `GET /api/air-quality` - Get air quality data
- `GET /api/schools` - List schools
- `GET /api/ai/analysis` - Get AI correlation analysis
- `GET /api/ngsi-ld/entities` - Get NGSI-LD entities

## 📚 Documentation

- API Docs: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 📄 License

MIT
