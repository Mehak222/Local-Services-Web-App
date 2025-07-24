# Local Services Web App

A web application built using **Flask** and **SQLite** to help local professionals manage their services, bookings, and feedback digitally.

## 🚀 Features

### ✅ For Service Providers
- Registration with name, email, service type, and password
- View customer service requests
- Simple service provider homepage interface

### ✅ For Customers
- Register with name, email, and password
- Browse and search services (Electrician, Plumber, etc.)
- Interactive service cards with popup booking and feedback
- Book services by selecting providers and dates
- Leave feedback and ratings for services
- My Profile page with customer details

### ✅ Admin Dashboard
- View all service providers
- View all bookings
- View feedback from customers

## 🛠️ Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python (Flask)
- **Database**: SQLite

## 🌐 Live Demo

🔗 [Click here to view the deployed web app](https://local-services-web-app.onrender.com)

> *Note: Hosted on Render. May take 30–60 seconds to spin up if idle.*

## 📁 Project Structure

Mini Project/
│
├── app.py # Flask app main file
├── database.db # SQLite database
├── templates/ # HTML templates
│ ├── register_customer.html
│ ├── register_service_provider.html
│ ├── customer_homepage.html
│ ├── service_provider_homepage.html
│ ├── booking.html
│ ├── feedback.html
│ ├── profile.html
│ └── admin.html
├── static/ # (Optional) Static assets like CSS/JS/images
└── README.md # This file

## 🔧 How to Run Locally

1. **Clone the repository**  
```bash
git clone https://github.com/Mehak222/Local-Services-Web-App.git
cd Local-Services-Web-App
```
2. **(Optional) Create virtual environment**
```bash
python -m venv venv
venv\Scripts\activate   # For Windows
```
3. **Install dependencies**
```bash
pip install flask
```
4. **Run the application**
```bash
python app.py
```
6. **Open in browser**
```bash
http://127.0.0.1:5000
```
## 💡 Future Improvements

- Add login/logout and session management  
- Email notifications  
- Real-time booking status  
- Payment gateway integration  
