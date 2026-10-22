# Elevator Gate

Elevator Gate is a full-stack corporate website built for a Saudi elevator company specializing in elevator installation, maintenance, and modernization.

The project was developed as a portfolio project to demonstrate practical full-stack web development using **Python, Django, and PostgreSQL**, from planning and database design through implementation, testing, and production deployment.

## Live Demo

**Live Website:**  
https://elevator-gate.onrender.com

> The project is currently hosted on Render's free tier, so the first request after a period of inactivity may take a few seconds to load.

## Key Features

- Responsive Arabic RTL interface.
- Mobile and desktop layouts.
- Dynamic homepage content.
- Services listing and individual service pages.
- Service features managed dynamically.
- Projects listing and project detail pages.
- Project category filtering.
- Project pagination.
- Blog listing and article detail pages.
- Blog search, categories, and pagination.
- Related blog articles.
- Testimonials.
- Frequently Asked Questions.
- Contact form with privacy consent validation.
- Contact message storage through PostgreSQL.
- Django Admin for content management.
- Custom 404 and 500 error pages.
- SEO-friendly slugs.
- Dynamic meta descriptions.
- XML sitemap.
- `robots.txt`.
- Production static file handling with WhiteNoise.

## Technology Stack

### Backend

- Python
- Django
- PostgreSQL
- Gunicorn

### Frontend

- HTML5
- CSS3
- JavaScript
- Django Templates
- Responsive Design
- Arabic RTL Layout

### Production & Development

- Git
- GitHub
- Render
- WhiteNoise
- python-dotenv

## Project Architecture

The Django project is divided into focused applications:

```text
apps/
├── core/
├── pages/
├── services/
├── projects/
├── blog/
└── contact/
```

### Main Responsibilities

- `core` — shared functionality and site-wide configuration.
- `pages` — homepage, about, FAQ, privacy policy, terms, and testimonials.
- `services` — elevator services and service features.
- `projects` — completed projects and project categories.
- `blog` — articles and blog categories.
- `contact` — contact form and customer messages.

## Main Data Models

The project uses relational PostgreSQL models including:

- Service
- ServiceFeature
- Project
- ProjectCategory
- BlogPost
- BlogCategory
- Testimonial
- FAQ
- ContactMessage

## Local Setup

Clone the repository:

```bash
git clone <repository-url>
cd elevator-gate
```

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file and configure the required environment variables:

```env
DJANGO_SECRET_KEY=your-secret-key
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost

DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=5432
```

Run database migrations:

```bash
python manage.py migrate
```

Start the development server:

```bash
python manage.py runserver
```

## Testing

The project includes automated Django tests covering important application behavior, including:

- Contact form validation.
- Privacy consent validation.
- Service models and detail pages.
- Project filtering and detail pages.
- Blog pages.
- Custom 404 handling.

Run the test suite with:

```bash
python manage.py test
```

## Production

The application is deployed using:

- **Render Web Service** for the Django application.
- **Render PostgreSQL** for the production database.
- **Gunicorn** as the production WSGI server.
- **WhiteNoise** for serving static files.
- Environment variables for production secrets and configuration.

Production runs with:

```env
DJANGO_DEBUG=False
```

## Project Status

**Production deployment completed.**

The main application, database, static files, responsive interface, SEO configuration, automated tests, and production deployment are operational.

Further production improvements may include persistent media storage, production admin setup, and custom domain configuration.

## Documentation

Project planning and design documentation is available in the `docs/` directory.

The project was developed through structured stages covering requirements, UI/UX design, database design, Django implementation, testing, production preparation, and deployment.

## Author

**Eng. Maram Zuaiter**

Computer Engineering graduate focused on Python/Django web development.