from application import app

# Key for SQL
app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'

# Main trick
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

# REMINDER!!!
# Go onto data_provider_service.py and uncomment the line depending if you are MAC/WINDOWS user before running it
