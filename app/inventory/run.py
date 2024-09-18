from dotenv import load_dotenv
import os
from app import create_app

load_dotenv()

app = create_app()

if __name__ == "__main__":
    debug_mode = os.getenv('FLASK_ENV') == 'development'
    
    app.run(host='0.0.0.0', port=5000, debug=debug_mode)
