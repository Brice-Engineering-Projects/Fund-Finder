/flask_funding_app
│
├── /app
│   ├── __init__.py         # Initializes Flask app and loads configuration
│   ├── views.py            # Contains route and view logic
│   ├── business_logic.py   # Business logic for API calls
│
├── /config
│   ├── __init__.py         # Allows this folder to be treated as a module
│   ├── config.py           # Configuration variables
│
├── .env                    # Stores environment variables like API keys
├── main.py                 # Entry point for the Flask app
├── requirements.txt        # Python package dependencies
└── README.md               # Project documentation
└── /.vscode               # VS Code configuration folder
│   └── settings.json      # Workspace-specific VS Code settings
│
├── /templates
│   ├── base.html          # base html file that is extended to all other html files
│   ├── home.html          # home html file which renders the homepage