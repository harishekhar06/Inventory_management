Product Inventory System
Description
The Product Inventory System is a comprehensive web application designed for managing products, variants, and stock levels. Built using Flask for the backend and React for the frontend, this system allows users to:

Add and manage products.
Add and manage variants and sub-variants for products.
Track and update stock levels.
Features
Product Management: Create, view, and manage products including their ID, code, name, and stock levels.
Variant Management: Add and manage variants for products.
Sub-Variant Management: Add and manage sub-variants and their stock levels.
Stock Management: Update and track stock levels for products and their variants.
Technology Stack
Backend: Flask (Python)
Frontend: React.js
Database: SQLite
Environment Management: Python Dotenv for environment variables
Routing: Flask Routes and React Router
Installation
Backend
1. Navigate to the Backend Directory:

cd backend
Create a Virtual Environment:
python -m venv venv
Activate the Virtual Environment:

On Windows:
venv\Scripts\activate

On macOS/Linux:
source venv/bin/activate

2. Install Dependencies:
pip install -r requirements.txt
Set Up Environment Variables: Create a .env file in the root of the backend directory and add:

makefile
SECRET_KEY=<your-secret-key>
DATABASE_URI=sqlite:///inventory.db
for the secret key geneartion, you could use the secret_key.py file

3. Run Migrations:
flask db upgrade

4. Start the Backend Server:
python run.py

Frontend
1. Navigate to the Frontend Directory:
cd frontend

2. Install Dependencies:
npm install



Usage
Open your web browser and navigate to http://localhost:5000 to access the frontend.
Use the provided interfaces to add products, variants, sub-variants, and manage stock levels.
Known Issues
Incomplete Features: Certain features and functionalities are still under development and may require additional work.
Known Bugs: There may be some bugs or issues that are yet to be resolved.