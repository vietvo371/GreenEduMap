
# 🌱 GreenEduMap - Smart City Open Data Platform

![GreenEduMap](./docs/architecture.png)

**Một nền tảng open-source kết nối Giáo dục 🎓, Môi trường 🌿, và Năng lượng ⚡ cho các thành phố bền vững**

---

## 📌 Giới thiệu

GreenEduMap là giải pháp toàn diện cho quản lý dữ liệu mở thành phố thông minh, tích hợp:

- 📍 **Bản đồ 3D thời gian thực** - Hiển thị AQI, nhiệt độ, năng lượng xanh
- 🤖 **AI GreenBot** - Gợi ý hành động xanh cá nhân hóa
- 🎓 **Nền tảng giáo dục xanh** - Khóa học môi trường cho trường học
- 🌐 **Open Data Integration** - OpenAQ, OpenWeather, OpenStreetMap
- 🔗 **NGSI-LD Semantic Web** - FiWARE Orion-LD & Linked Open Data (LOD)
- 📊 **Phân tích AI** - Correlation giữa môi trường, giáo dục, năng lượng

---

## 🎯 Các tác nhân (Roles)

| Role | Quyền hạn | Screens |
|------|----------|---------|
| **👨‍💻 Admin** | Quản lý hệ thống, dữ liệu AI | Dashboard, Wards, AI Insights, Users, Logs |
| **🧑‍🏫 School** | Quản lý khóa học xanh | Dashboard, Courses, New Course, Profile |
| **👩‍💼 Citizen** | Xem bản đồ, feedback, gợi ý | Map, Actions, Feedback, Stats, Chat AI |

---

## 🛠️ Tech Stack

| Tầng | Công nghệ | Mục đích |
|-----|-----------|---------|
| **Frontend** | Next.js 15, TypeScript, Tailwind, CesiumJS | Web UI, 3D Map, Dashboards |
| **Backend** | FastAPI, Python 3.11, scikit-learn | APIs, AI Analysis, LOD |
| **Database** | PostgreSQL 16 + PostGIS | Spatial & Relational Data |
| **Semantic** | FiWARE Orion-LD, MongoDB | NGSI-LD Entities |
| **DevOps** | Docker Compose, GitHub Actions | CI/CD, Containerization |
| **Auth** | JWT (HS256) | Role-Based Access |

---

## 🚀 Quick Start

### 🐳 Option 1: Docker Compose (Recommended)

```bash
# Clone
git clone https://github.com/yourusername/greenedumap.git
cd GreenEduMap

# Start all services
docker compose -f docker/docker-compose.yml up --build

# Access
# - Frontend: http://localhost:3000
# - API Docs: http://localhost:8000/docs
# - Orion-LD: http://localhost:1026
```

### 💻 Option 2: Local Development

```bash
# Backend
cd backend
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python -m app.main

# Frontend (new terminal)
cd frontend
yarn install && yarn dev

# PostgreSQL must be running
# psql -U postgres -d greenedumap -f ../data/init.sql
```

---

## 📁 Project Structure

```
GreenEduMap/
├── .github/workflows/        # CI/CD pipelines
├── docker/                   # Docker configs
│   ├── frontend.Dockerfile
│   ├── backend.Dockerfile
│   └── docker-compose.yml
├── docs/                     # Documentation & diagrams
├── scripts/                  # Init, seed, LOD conversion
├── data/                     # Sample open data
├── frontend/                 # Next.js application
│   ├── src/app/             # Routes: /, /map, /actions, /school/*, /admin/*, /chat
│   ├── src/components/      # React components
│   └── package.json
├── backend/                  # FastAPI application
│   ├── app/
│   │   ├── routes/          # API endpoints
│   │   ├── services/        # FiWARE, AI, LOD
│   │   └── models/          # Database schemas
│   └── requirements.txt
└── README.md
```

---

## 🌍 API Endpoints

### Authentication
```bash
POST /auth/register
POST /auth/login
GET /auth/me
POST /auth/refresh
```

### Data APIs
```bash
GET /api/air-quality?ward=Ba Dinh
GET /api/weather?ward=Ba Dinh
GET /api/schools
GET /api/courses
POST /api/feedback
```

### AI & Analysis
```bash
GET /api/ai/analysis?ward=Ba Dinh
GET /api/ai/recommendations
POST /api/ai/cluster-wards
```

### NGSI-LD & LOD
```bash
GET /api/ngsi-ld/entities?type=AirQualityObserved
GET /api/lod/export?format=json-ld
GET /api/lod/export?format=turtle
GET /api/lod/export?format=rdf-xml
```

**📚 Full API Docs:** http://localhost:8000/docs

---

## 🔗 FiWARE Integration

```
┌─────────────────┐
│  Open Data APIs │ (OpenAQ, OpenWeather, OSM)
└────────┬────────┘
         │
         ▼
┌─────────────────────┐
│  FastAPI Backend    │ (Transform to NGSI-LD)
└────────┬────────────┘
         │
         ▼
┌──────────────────────────┐
│  FiWARE Orion-LD         │ (Publish & Store)
│  + MongoDB               │
└──────────────────────────┘
         │
         ▼
┌──────────────────────────┐
│  Frontend (Visualization)│
│  + LOD Export (JSON-LD)  │
└──────────────────────────┘
```

---

## 📦 Database Schema

**Core Tables:**
- `users` (3 roles: admin, school, citizen)
- `schools` (Green institutions)
- `courses` (Environmental courses)
- `air_quality` (Real-time AQI with location)
- `weather` (Temperature, humidity, wind)
- `energy_data` (Solar/renewable generation)
- `citizen_feedback` (User suggestions)
- `ai_analysis` (Correlation results)

**Spatial Support:** PostGIS `GEOMETRY(Point, 4326)` + GiST indexes

---

## 🧪 Testing

```bash
# Backend tests
cd backend
pytest tests/ -v --cov=app

# Frontend tests
cd frontend
npm run test
```

---

## 📖 Documentation

- [Architecture](./docs/architecture.md) - System design
- [API Reference](./docs/api_reference.md) - Endpoint details
- [Open Data Standards](./docs/open_data_standards.md) - NGSI-LD, LOD, SOSA/SSN
- [Contributing](./CONTRIBUTING.md) - Development guide

---

## 🤝 Contributing

1. Fork repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

**Guidelines:**
- Follow [Code of Conduct](./CODE_OF_CONDUCT.md)
- Write tests for new features
- Update documentation
- Use conventional commits

---

## 📜 License

MIT License - See [LICENSE](./LICENSE) file

---

## 🙏 Acknowledgments

- **FiWARE Foundation** - Orion-LD & Smart Data Models
- **W3C** - SOSA/SSN ontology
- **OpenAQ, OpenWeather, OSM** - Open data sources
- **Open Source Community** - FastAPI, Next.js, PostgreSQL, etc.

---

## 📞 Support

- 🐛 **Report Bugs:** [GitHub Issues](../../issues)
- 💬 **Discussions:** [GitHub Discussions](../../discussions)
- 📧 **Email:** greenedumap@example.org

---

**Built for OLP 2025 Smart City Challenge** 🌍🌱

*Kết nối Giáo dục 🎓, Môi trường 🌿, và Năng lượng ⚡ cho Thành phố Bền vững*
