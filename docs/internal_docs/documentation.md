See directory_structure.md for file structure.

app and config folder both contain __init__.py which contain different information.  These files allow python to read the file folders as modules, thus creating a better file structure.

The typical app.py needed to be renamed to main.py as the name was conflicting with the folder "app".

.vscode folder was created to add in the settings.json file to help Flask find the app folder with the views.py file.

The config file contains an __init__.py file to allow python to read the folder as a module.  The folder contains the configuration settings in config.py.

.env file contains all passwords to be protected on the server.  

business_logic.py is placed in the app folder.  This file will contain all of the logic used to search and return funding opportunities.  This file is using classes to run the functions.  This will keep the file more organized and easier to scale in the future.

## Development ##

The API is from grants.gov, which requires the program administrator to provide keys to the site.  While waiting for API keys, fake API keys and responses were made by using the "responses" library to Mock HTTP Requests.

json-server was used to run a local Fake API

