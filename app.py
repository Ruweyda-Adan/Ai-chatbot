from routes import create_app  # Import create_app from routes.py

app = create_app()  # Create the app using the function from routes.py

if __name__ == "__main__":
    app.run(debug=True)  # Run the app in debug mode
