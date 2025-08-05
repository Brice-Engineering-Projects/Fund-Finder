# Project Structure

fundfinder/
├── app/
│   ├── __init__.py                   # App factory: register blueprints, load config
│   ├── models/                     # User model (can be extended for auth)
│   ├── templates/
│   │   ├── auth/
│   │   ├── main/
│   │   └── shared/                   # Optional partials (navbar, layout)
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
│   │   ├── routes.py                  # Your existing `/search` route
│   │   └── business_logic.py         # Your real funding logic (not mock)
│   ├── services/
│   │   └── mocky_api.py              # MockyAPI: fake API calls
│   ├── utils.py                      # Optional: helper functions, constants
│   └── config.py                     # Config classes (already exists)
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
