# Inventory Management Application Svelte.js + Python Flask 

A practical example of a web app using Flask serving a Svelte app, acting as the backend server. The frontend is constructed using Svelte with webpack as the bundler.

# Create a virtual environment

```bash
# Windows
python -m venv env
```
```bash
# Linux, WSL or macOS
python3 -m venv env
```

# Activate the virtual environment. 
```bash
# Windows
env/Scripts/activate
```
```bash
# Linux, WSL or macOS
source env/bin/activate
```

# Install the dependencies
```bash
pip install -r requirements.txt
```

# Create the database tables

When running this Flask application for the first time, make sure to create the database tables before starting the server (This should only be done once.) 
This can be done by running the following command:
```bash
python create_db.py
```

Run the following to start the Flask server.
```bash
python server.py
``` 
Open a new terminal and run the following:
- `cd frontend;` then `npm install` to install the Svelte frontend dependencies.
- `npm run dev` to start the Svelte frontend.

Open `localhost:8080` in your browser to see the app.