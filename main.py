from app import app  # Убедитесь, что ваш Dash-приложение в файле app.py

if __name__ == "__main__":
    app.run_server(host='0.0.0.0', port=8080, debug=True)
