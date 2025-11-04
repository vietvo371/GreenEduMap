
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2024-01-15

### Added

#### Frontend
- 🌱 **Initial Release**
  - Public citizen routes: `/`, `/map`, `/actions`, `/feedback`, `/stats`
  - School dashboard: `/school/*`
  - Admin panel: `/admin/*`
  - AI GreenBot: `/chat`, `/recommendations`
  - 3D interactive map with CesiumJS/Mapbox
  - Dark mode support
  - Responsive design (mobile, tablet, desktop)
  - Role-based authentication & middleware

#### Backend
- **Core Services:**
  - FastAPI with JWT authentication
  - PostgreSQL + PostGIS spatial database
  - FiWARE Orion-LD integration for NGSI-LD entities
  - MongoDB for document storage
  - AI correlation analysis (env ↔ edu ↔ energy)
  - LOD converter (JSON-LD, RDF, Turtle)
  - Open Data integration (OpenAQ, OpenWeather, OSM)

- **Database:**
  - 8 core tables with full schema
  - Spatial indexes for location queries
  - Sample data for demo

- **APIs:**
  - `/auth/*` - User authentication
  - `/api/air-quality` - AQI data
  - `/api/weather` - Weather data
  - `/api/schools` - School management
  - `/api/courses` - Course management
  - `/api/ai/*` - AI analysis & recommendations
  - `/api/ngsi-ld/*` - NGSI-LD entities
  - `/api/lod/*` - LOD export

#### Infrastructure
- Docker Compose setup for all services
- GitHub Actions CI/CD pipeline
- Database initialization scripts
- Sample data loading
- LOD publishing to Orion-LD

### Security
- JWT token-based authentication
- Role-based access control (RBAC)
- Password hashing with bcrypt
- CORS configuration
- Input validation via Pydantic

### Documentation
- Comprehensive README
- API reference guide
- Architecture diagrams
- Contributing guidelines
- Code of Conduct

---

## Unreleased

### Planned Features
- [ ] Mobile app (React Native)
- [ ] Advanced data visualization
- [ ] Blockchain integration for certifications
- [ ] Multilingual support
- [ ] Real-time notifications
- [ ] Advanced search & filtering
- [ ] Export data to various formats
- [ ] API rate limiting & pagination

---

[1.0.0]: https://github.com/yourusername/greenedumap/releases/tag/v1.0.0
