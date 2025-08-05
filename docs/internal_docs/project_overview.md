# FundFinder: Smart Funding Search Engine for Public Projects

## 🎯 Project Purpose

**FundFinder** is a Flask-based web application designed to help municipalities and infrastructure professionals discover and explore funding opportunities. The platform simplifies the funding discovery process by combining structured intake forms, API-driven search, and modular architecture for future scalability.

FundFinder is designed for:
- **Public sector engineers and planners** looking to match projects with available funding.
- **Grant writers and administrators** who need a streamlined tool for eligibility and submission readiness.

---

## 🧠 Project Vision

The long-term vision is to create a fully scalable platform that municipalities can use to:
- Filter funding sources by eligibility, community needs, and project types
- Save and manage grant searches
- Automate recurring funding scans and alerts
- Incorporate real-time APIs from federal/state sources

---

## 🛠️ Key Features

- **Multi-Step Intake Workflow**  
  Captures applicant and project data across multiple sections including basic information, project details, and community demographics.

- **API-Powered Search Functionality**  
  Retrieves mock or real funding data from external APIs based on user-submitted project criteria.

- **Authentication and Role Handling**  
  Secure user login, session handling, and extendable role-based logic (in progress).

- **Environment-Based Configurations**  
  Fully separated development, testing, and production configs using `.env` and `settings.py`.

- **Modular Flask App Architecture**  
  - Follows best practices using Blueprints (`auth`, `main`, `api`)
  - Uses factory pattern via `create_app()` for scalable config handling
  - Services and business logic are clearly separated

- **Clean Code Organization**  
  - Includes `docs/`, `tests/`, `services/`, and well-separated business logic for maintainability and clarity.
  - Structured testing suite with Pytest and professional documentation in `docs/`.

---

## 📁 Project Structure Overview

```
fundfinder/
├── app/
│   ├── __init__.py                   # App factory: register blueprints, load config
│   ├── config/                
│   │   ├── __init__.py
│   │   └── settings.py               # Config classes (already exists)
│   ├── models/                       # User model (can be extended for auth)
│   │   ├── __init__.py
│   │   └── models.py                 # Models
│   ├── templates/
│   │   ├── auth/
│   │   ├── main/
│   │   ├── shared/                   # Optional partials (navbar, layout)
│   │   └── base.html
│   ├── static/                       # CSS/JS
│   ├── auth/                         # Authentication blueprint
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── forms.py
│   ├── main/                         # Main blueprint (user-facing form flows)
│   │   ├── __init__.py
│   │   ├── routes.py                 # Your current multi-step form routes
│   │   └── forms.py                  # Optional if using WTForms
│   ├── api/                          # API-focused logic
│   │   ├── __init__.py
│   │   ├── routes.py                 # Your existing `/search` route
│   │   └── business_logic.py         # Your real funding logic (not mock)
│   ├── services/
│   │   ├── __init__.py
│   │   └── mocky_api.py              # MockyAPI: fake API calls
│   └── utils/                        # Optional: helper functions, constants 
│
├── docs/
│   ├── internal_docs/                # Internal project notes, architecture
│   │   ├── endpoints.md              # API routes, structure
│   │   ├── data_flows.md             # How form → logic → API → result
│   │   └── auth_logic.md             # How login/session/roles work
│   ├── README.md                     # Public-facing GitHub README
│   └── ARCHITECTURE.md              # Optional deeper explanation
│
├── tests/
│   ├── conftest.py
│   ├── test_auth.py
│   ├── test_search.py
│   └── test_forms.py
│
├── main.py                           # Entry point: imports create_app
├── requirements.txt
├── .env
└── .flaskenv                         # Optional if using Flask CLI  
```

---

## 🧪 Tech Stack

- **Backend**: Python (Flask), Jinja2, Flask Blueprints, Flask-Session
- **API Layer**: Custom logic + Mocky (placeholder for real API integrations)
- **Frontend**: HTML, CSS, Jinja2 templates (Bootstrap optional)
- **Testing**: Pytest
- **Configuration**: dotenv + class-based settings
- **Documentation**: Markdown-based project documentation in `docs/`

---

## 🚀 Deployment Considerations

- Planned for Heroku, Fly.io, or self-hosted Docker environment
- Security (auth, input validation) is being built into the foundation
- Form submission currently uses `session` for data handling

---

## 🚀 Summary

**FundFinder** offers a scalable foundation for helping municipalities explore funding avenues for critical public projects. It showcases modular Flask architecture, API integration, and form-driven data workflows—making it a strong candidate for backend-focused portfolios and civic tech applications.