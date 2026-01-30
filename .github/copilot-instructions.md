# OctoFit Tracker - AI Copilot Instructions

## Project Overview

OctoFit Tracker is a full-stack fitness application (Django + React) that enables students to log activities, track progress, form teams, and compete on leaderboards. The project is scaffolded with detailed role-specific instruction files in `.github/instructions/`.

## Critical Workflows & Commands

### Never change directories in agent mode
- Always use absolute paths or point to directories with commands
- Example: `python -m venv octofit-tracker/backend/venv` (not `cd octofit-tracker/backend`)

### Backend Setup (Django + MongoDB)
```bash
# Create Python venv
python3 -m venv octofit-tracker/backend/venv
source octofit-tracker/backend/venv/bin/activate

# Install dependencies from requirements.txt
pip install -r octofit-tracker/backend/requirements.txt

# Check MongoDB running
ps aux | grep mongod
```

### Frontend Setup (React)
```bash
npx create-react-app octofit-tracker/frontend --template cra-template --use-npm
npm install bootstrap --prefix octofit-tracker/frontend
npm install react-router-dom --prefix octofit-tracker/frontend
```

## Architecture & Component Boundaries

**Backend** (`octofit-tracker/backend/octofit_tracker/`)
- Django REST Framework API with djongo (MongoDB ORM)
- Core features: authentication (django-allauth + dj-rest-auth), activity logging, team management, leaderboards
- Ports: 8000 (public)

**Frontend** (`octofit-tracker/frontend/`)
- React app with Bootstrap styling and React Router navigation
- Ports: 3000 (public)

**Database** (MongoDB)
- Port: 27017 (private)
- Use Django ORM for all operations, never direct MongoDB scripts

## Key Conventions

### Django Backend Settings
- `settings.py` must include codespace hostname detection for ALLOWED_HOSTS:
  ```python
  ALLOWED_HOSTS = ['localhost', '127.0.0.1']
  if os.environ.get('CODESPACE_NAME'):
      ALLOWED_HOSTS.append(f"{os.environ.get('CODESPACE_NAME')}-8000.app.github.dev")
  ```

### REST API & URLs
- Use codespace environment for URL construction in `urls.py`:
  ```python
  codespace_name = os.environ.get('CODESPACE_NAME')
  base_url = f"https://{codespace_name}-8000.app.github.dev" if codespace_name else "http://localhost:8000"
  ```

### Serializers
- Convert MongoDB ObjectId fields to strings in serializers

### Testing API
- Use `curl` to test REST endpoints

## Dependencies & External Integrations

**Backend Stack**: Django 4.1.7, DRF 3.14.0, djongo 1.3.6, MongoDB, django-allauth, dj-rest-auth, django-cors-headers
**Frontend Stack**: React (Create React App), Bootstrap, React Router DOM

## Role-Specific Instructions
Detailed instructions exist for specific domains:
- `.github/instructions/octofit_tracker_setup_project.instructions.md` - Overall setup
- `.github/instructions/octofit_tracker_django_backend.instructions.md` - Backend patterns
- `.github/instructions/octofit_tracker_react_frontend.instructions.md` - Frontend patterns

Refer to these when working on component-specific features.
