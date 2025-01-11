# Django Mini App_1

A simple Django project to register first names and display them using the MVT architecture.

## Project Directory Structure

django-mini-app/  
├── myproject/                 # Project settings and URLs  
├── myapp/                     # App folder containing models, views, templates  
│   ├── models.py              # Database models (Details model)  
│   ├── views.py               # Logic to handle form submissions and display data  
│   ├── templates/             # HTML templates (home.html, Inquiry.html)  
└── db.sqlite3                 # SQLite database file  


## Features
- **Registration**: Users can submit their first name via a form.
- **User List**: Displays registered names in a styled table using a clean frontend.

## Technology Stack
- **Backend**: Django Framework
- **Frontend**: HTML, CSS
- **Database**: SQLite (default Django database)

## How to Run Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/partha-09/django-mini-app_1.git
   cd django-mini-app_1
2. Set up a virtual environment.
3. Install dependencies (pip install django).
4. Run migrations:
    python manage.py makemigrations  
    python manage.py migrate  
5. Start the development server:
    python manage.py runserver  
6. Open http://127.0.0.1:8000/ to register a name.

## Files Overview:

1. home.html: Form for entering a first name.
2. Inquiry.html: Displays registered names in a styled table.
3. models.py: Defines the Details model for storing first names.
4. views.py: Handles form submissions and data rendering.

## MVT Architecture:

1. Model: Details model to store user names.
2. View: Logic to process form input and fetch database records.
3. Template: HTML files to render the user interface.


## 📸 Screenshots

- Input View:  
![image alt](https://github.com/partha-09/django-mini-app_1/blob/c86573ca3df412d77ab0326f408e9ce4cbbebaf3/input.jpg)

- Output View:  
![image alt](https://github.com/partha-09/django-mini-app_1/blob/c86573ca3df412d77ab0326f408e9ce4cbbebaf3/output.jpg)
### 📬 Contact:

For any queries:

- **Name**: Siddappa Godi
- **Email**: [siddapp2godi@gmail.com](mailto:siddapp2godi@gmail.com)
- **Phone**: +91 6363504679
- **LinkedIn**: [https://www.linkedin.com/in/siddappagodi/](https://www.linkedin.com/in/siddappagodi/)


## ⭐ Contribute

I welcome contributions to improve this project! If you find this project helpful or see any areas for enhancement, feel free to:

- **Fork** this repository.
- **Submit a Pull Request** with improvements or new features.
- **Open an Issue** if you encounter any bugs or have suggestions for better functionality.

Your contributions are greatly appreciated and will help make this project even better. Don't hesitate to reach out for any queries or collaboration ideas!


### What's Updated:
1. Repository URL: `https://github.com/partha-09/django-mini-app_1.git`.
2. Name: **Siddappa Godi**.
3. Email: **siddapp2godi@gmail.com**.
4. Phone: **+91 6363504679**.
5. LinkedIn: [https://www.linkedin.com/in/siddappagodi/](https://www.linkedin.com/in/siddappagodi/).
