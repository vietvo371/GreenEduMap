
# 🤝 Contributing to GreenEduMap

Cảm ơn bạn muốn đóng góp cho GreenEduMap! Đây là hướng dẫn chi tiết.

## 📋 Code of Conduct

Dự án này tuân thủ [Code of Conduct](./CODE_OF_CONDUCT.md). Tất cả contributors được yêu cầu tuân thủ.

---

## 🎯 Quy trình đóng góp

### 1. Setup Development Environment

**Backend:**
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

**Frontend:**
```bash
cd frontend
npm install
# or yarn install
```

### 2. Create a Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

**Branch naming conventions:**
- `feature/` - New features
- `fix/` - Bug fixes
- `docs/` - Documentation
- `refactor/` - Code refactoring
- `test/` - Test improvements

### 3. Commit Guidelines

Use conventional commits:

```bash
git commit -m "type(scope): description"
```

**Types:**
- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation
- `style:` - Code style (formatting, etc)
- `refactor:` - Code refactoring
- `test:` - Add/update tests
- `chore:` - Build, dependencies, etc

**Examples:**
```bash
git commit -m "feat(auth): add JWT refresh token"
git commit -m "fix(map): resolve zoom level bug"
git commit -m "docs: update API reference"
```

### 4. Push & Create Pull Request

```bash
git push origin feature/your-feature-name
```

Then create PR on GitHub with:
- Clear title
- Description of changes
- Related issues (Closes #123)
- Screenshots if UI changes

---

## 📝 Code Style Guidelines

### Python (Backend)

**Follow PEP 8:**
```bash
# Install & run black
pip install black
black app/

# Run ruff for linting
ruff check app/
```

**Type hints required:**
```python
async def fetch_data(city: str) -> dict:
    """Fetch air quality data for a city."""
    pass

def correlate(x: list, y: list) -> float:
    """Calculate correlation coefficient."""
    pass
```

**Docstrings:**
```python
def analyze_correlation(data: dict) -> dict:
    """
    Analyze correlation between environment and education.
    
    Args:
        data: Dictionary with environmental and educational metrics
        
    Returns:
        Dictionary with correlation analysis results
        
    Raises:
        ValueError: If data is incomplete
    """
    pass
```

### TypeScript/React (Frontend)

**Follow ESLint config:**
```bash
npm run lint
npm run lint:fix
```

**Type safety:**
```typescript
interface AirQualityData {
  wardName: string;
  aqi: number;
  pm25: number;
  timestamp: Date;
}

async function fetchAirQuality(ward: string): Promise<AirQualityData> {
  // ...
}
```

---

## 🧪 Testing Requirements

### Backend

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=app --cov-report=html

# Run specific test file
pytest tests/test_auth.py -v
```

**Test example:**
```python
async def test_fetch_openaq_data():
    """Test fetching air quality from OpenAQ API."""
    result = await OpenDataService.fetch_openaq_data("Hanoi")
    assert result["success"] is True
    assert "locations" in result
```

### Frontend

```bash
# Run tests
npm run test

# Watch mode
npm run test:watch

# Coverage
npm run test:coverage
```

---

## 🔍 Code Review Checklist

Before submitting PR, ensure:

- [ ] Code follows style guidelines
- [ ] All tests pass
- [ ] Added tests for new features
- [ ] Documentation updated
- [ ] No console.log/print statements
- [ ] No hardcoded credentials
- [ ] Branch is up to date with main

---

## 📚 Documentation

If contributing a new feature, update docs:

1. **API endpoints** → `docs/api_reference.md`
2. **Architecture changes** → `docs/architecture.md`
3. **Database schema** → Add migration notes
4. **Deployment** → Update deployment guide

---

## 🐛 Bug Reports

Include in bug report:

- Steps to reproduce
- Expected behavior
- Actual behavior
- Screenshots (if applicable)
- Environment (OS, browser, versions)
- Logs/error messages

**Template:**
```markdown
## Description
Clear description of the bug

## Steps to Reproduce
1. Go to...
2. Click...
3. See...

## Expected Behavior
What should happen

## Actual Behavior
What actually happens

## Screenshots
[if applicable]

## Environment
- OS: macOS/Windows/Linux
- Browser: Chrome/Firefox/Safari
- Node version: 18.x
- Python version: 3.11.x
```

---

## ✨ Feature Requests

Include in feature request:

- Use case/motivation
- Proposed solution
- Alternatives considered
- Additional context

---

## 🚀 Release Process

1. Update version in `release/version.json`
2. Update `CHANGELOG.md`
3. Create git tag: `git tag v1.2.3`
4. Push tag: `git push origin v1.2.3`
5. GitHub Actions triggers CI/CD pipeline

---

## 💬 Getting Help

- 💭 **Questions:** Use GitHub Discussions
- 🐛 **Bugs:** Create GitHub Issues
- 💬 **Chat:** Join our Discord server
- 📧 **Email:** greenedumap@example.org

---

## 🙏 Thank You!

Your contributions make GreenEduMap better for everyone. We appreciate your effort! 🌱

---

**Happy Contributing!** 🚀
