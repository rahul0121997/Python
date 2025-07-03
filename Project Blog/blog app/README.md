# Personal Blog with Django

A simple and elegant personal blog built with Django, perfect for beginners to learn Django web development.

## Features

- User authentication (Register, Login, Logout)
- Create, Read, Update, Delete blog posts
- Rich text editor for blog posts
- Admin panel for content management
- Responsive design
- Static file handling
- Category and tag system

## Setup Instructions

1. Clone the repository:
```bash
git clone <your-repository-url>
cd blog-app
```

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the virtual environment:
- Windows:
```bash
venv\Scripts\activate
```
- Linux/Mac:
```bash
source venv/bin/activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Run migrations:
```bash
python manage.py migrate
```

6. Create a superuser:
```bash
python manage.py createsuperuser
```

7. Run the development server:
```bash
python manage.py runserver
```

8. Visit http://127.0.0.1:8000/ to see your blog!

## Project Structure

```
blog-app/
├── blog/                 # Main blog application
├── static/              # Static files (CSS, JS, images)
├── templates/           # HTML templates
├── media/              # User-uploaded files
├── manage.py           # Django management script
└── requirements.txt    # Project dependencies
```

## Contributing

Feel free to fork this project and make your own changes. Pull requests are welcome!

## License

This project is licensed under the MIT License. 