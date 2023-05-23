# Svelte.js + Python Flask Inventory Management Application

Example of using Flask to serve a Svelte app and use it as a backend server.

# Activate the virtual environment. 
```bash
# Windows
env/Scripts/activate

# Linux, WSL or macOS
source env/bin/activate
```

# Create the database tables

When running this Flask application for the first time, make sure to create the database tables before starting the server (This should only be done once.) 
This can be done by running the following command:
```bash
python create_db.py
```

Run the following for development:

- `python3 server.py` to start the Flask server.
- `cd frontend; npm run dev` to start the Svelte frontend.

Open `localhost:8080` in your browser to see the app.