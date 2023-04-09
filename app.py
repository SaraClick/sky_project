from application import app

# Key for SQL
app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'

# Main trick
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
