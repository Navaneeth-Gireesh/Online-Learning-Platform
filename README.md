
## EduSphere: An Online Learning Platform

EduSphere is a robust online learning platform that leverages Python, Django, and MySQL for backend operations, combined with HTML, CSS, and JavaScript for a responsive frontend. It offers a secure, scalable, and user-friendly experience for both administrators and students.



[Live Demo Link](https://navaneethgireesh.pythonanywhere.com/)

![Projet Landing Page](https://github.com/user-attachments/assets/250ff3d8-525e-4bbb-9b72-d6ade2589006)


## Table of Contents

- [Introduction](#introduction)
- [Key Features](#key-features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Database Configuration (MySQL)](#database-configuration-mysql)
- [Email Configuration (Gmail SMTP)](#email-configuration-gmail-smtp)
- [Running the Application](#running-the-application)
- [API Key Configuration](#api-key-configuration)
- [Live Demo](#live-demo)
- [License](#license)

## Introduction


EduSphere is a feature-rich online learning platform that enables users to enroll in courses, access study materials, and engage with quizzes, videos, and documents. It offers seamless coupon code functionality for course purchases and integrates automated email notifications using Celery to enhance communication with users. Additionally, the platform employs Django AllAuth for secure and efficient social authentication via Google and GitHub. Administrators have full control over managing courses, users, and coupon codes, making EduSphere a powerful tool for educational purposes.
## Key Features

- **Authentication and Security:** Integrated OTP-based authentication and OAuth, allowing secure login and recovery processes using social logins (Google, GitHub).
  
- **Automated Notifications:** Set up automated email notifications for login attempts, account status changes, and course purchases using Django Celery.

- **Role-Based Access Control:** Implemented dynamic coupon generation and role-based access control to enhance the user experience with customized access and discounts.

- **Efficient Management:** Developed CRUD operations for managing courses, users, and coupons, streamlining administrative tasks.

- **Enhanced Search Functionality:** Enabled intuitive search options, allowing admins to locate users by email, username, or name, and students to search for courses by name.

## Prerequisites

Ensure you have the following installed:
- Python 3.12  [python.org](https://www.python.org/downloads/).
- MySQL
- Virtualenv (optional but recommended)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Navaneeth-Gireesh/Online_Learning_Platform.git

   cd Online_Learning_Platform
   ```

2. Set up a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Mac
   venv\Scripts\Activate # On Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Database Configuration (MySQL)

1. **Configure `settings.py`:**

   In your `settings.py`, change the following configuration with yours under `DATABASES`:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': '<your-database-name>',  # Replace with your MySQL database name
           'USER': 'root',                  # Replace with your MySQL username
           'PASSWORD': '<your-password>',   # Replace with your MySQL password
           'HOST': '127.0.0.1',             # Or your database host
           'PORT': '3306',                  # The default MySQL port
           'OPTIONS': {
               'init_command': 'SET sql_mode="STRICT_TRANS_TABLES"',
           }
       }
   }
   ```

2. **Create Database:**
   
   Create the MySQL database if it hasn't been created yet :
   ```sql
   CREATE DATABASE <your-database-name>;
   ```
   Make sure to replace 'your-database-name' with your chosen database name.

3. **Run Make Migrations:**

   ```bash
   python manage.py makemigrations 
   ```

4. **Run Migrate:**

   ```bash
   python manage.py migrate
   ```

## Email Configuration (Gmail SMTP)

1. **Configure `settings.py`:**

   ```python
   EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
   EMAIL_HOST = 'smtp.gmail.com'
   EMAIL_HOST_USER = '<your-email@gmail.com>' # Replace with your email
   EMAIL_HOST_PASSWORD = '<your-app-password>' # Replace with your email app password
   EMAIL_PORT = 587
   EMAIL_USE_TLS = True
   ```

2. **Generate App Password:**
   - Enable two-factor authentication in your Google account.
   - Generate an app password and use it in `EMAIL_HOST_PASSWORD`.
   - 
## Running the Application

Start the server with:

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/`.

## API Key Configuration

To enable social login functionality, users need to configure API keys from Google and GitHub. Follow these steps:

1. **Google OAuth Setup:**
   - Go to the [Google Cloud Console](https://console.cloud.google.com/).
   - Create a new project and enable the "Google+ API" and "Google OAuth 2.0" services.
   - Navigate to the **Credentials** section and create OAuth 2.0 credentials.
   - Copy the **Client ID** and **Client Secret**.

2. **GitHub OAuth Setup:**
   - Visit the [GitHub Developer Settings](https://github.com/settings/developers).
   - Create a new OAuth application.
   - Set the authorization callback URL to `http://127.0.0.1:8000/accounts/github/login/callback/` or your production domain.
   - Copy the **Client ID** and **Client Secret**.

3. **Admin Configuration:**
   - Log in to the Django admin page.
   - Navigate to `Sites` under the **Sites** section and create or update the site with the appropriate domain and `site_id`.
   - Go to **Social Applications** under the **Social Accounts** section and add the Google and GitHub applications.
   - Paste the **Client ID** and **Client Secret** in the corresponding fields.
   - Set the `site_id` for the social account to match the one created under `Sites`.
4. **Settings Configuration:**

    - Go to the settings.py file and set the correct SITE_ID to the site_id number created in the Django admin under Sites.

## Live Demo

You can access the live version of the application at:
[Live Demo Link](https://navaneethgireesh.pythonanywhere.com/)

## License

This project is for educational purposes only. Users may use the code for study and learning purposes but not for commercial use or redistribution.
