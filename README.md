# 🌍 Live Currency Converter Web Application

## 🔗 Live Demo
https://live-currency-converter-web-application.onrender.com


A Flask-based web application that converts 160+ global currencies using live daily exchange rates fetched from a public REST API.

This project demonstrates REST API integration, backend validation, dynamic UI rendering, and production-level error handling.

---

## 🚀 Features

- 🌎 Supports 160+ international currencies
- 🔄 Swap functionality for quick currency exchange
- 📡 Fetches live daily exchange rates dynamically
- 🛡 Input validation and robust error handling
- 🎨 Clean and responsive user interface
- ⚙️ Production-ready configuration using Gunicorn

---

## 🛠 Tech Stack

- **Backend:** Python, Flask  
- **API Integration:** Requests (REST API)  
- **Currency Data:** PyCountry (ISO currency names)  
- **Frontend:** HTML, CSS  
- **Deployment:** Gunicorn, Render  

---

## ⚙️ How It Works

The application fetches the latest exchange rates from:

https://open.er-api.com/v6/latest/

When a user selects currencies and enters an amount:

1. The app retrieves the latest exchange rates dynamically.
2. Performs real-time conversion.
3. Displays formatted results with proper validation.
4. Handles network/API errors gracefully.

---

## 📦 Local Setup Instructions

1. Clone the repository:
