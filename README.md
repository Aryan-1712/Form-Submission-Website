# Form-Submission-Website

Overview

This is a simple website project built using Django and Bootstrap. It has a Home Page and a Contact Us page, where users can submit queries or entries. The submitted form data is stored in the database, which the admin can access via the Django admin panel.

Features

Home Page:

Initial landing page with images, albums, and a carousel using Bootstrap.

Contact Us Page:

Users can submit their queries by filling out a form with the following fields:

Name

Email

Phone

Query

On successful submission, an alert notifies the user that the form has been submitted.

Admin Panel:

The superuser can log in to the admin panel to view and manage the submitted queries.

Technologies Used

Backend: Django (Python)

Frontend: HTML, CSS, Bootstrap

Database: SQLite (default Django database)

Installation Instructions

Clone the repository:

git clone https://github.com/Aryan-1712/Form-Submission-Webiste.git

Navigate to the project directory:

cd Aryan-1712

Create a virtual environment:

python -m venv venv

Activate the virtual environment:

On Windows:

venv\Scripts\activate

On macOS/Linux:

source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Run database migrations:

python manage.py migrate

Create a superuser to access the admin panel:

python manage.py createsuperuser

Run the development server:

python manage.py runserver

Open the website in your browser:

http://127.0.0.1:8000

Usage

Visit the home page to see the Bootstrap-styled content.

Navigate to the Contact Us page to submit a query.

Log in to the admin panel at /admin/ to view submitted queries.

Folder Structure

project-root/
│-- manage.py
│-- Website/
│-- example/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│-- db.sqlite3
│-- requirements.txt
│-- README.md

Contributing

Feel free to contribute to this project by creating a pull request or reporting issues.

Contact

For any queries or suggestions, please contact us via the "Contact Us" page on the website.

