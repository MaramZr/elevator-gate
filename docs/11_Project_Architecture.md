# 10 — Django Project Architecture

## Project: Elevator Gate

**Framework:** Django  
**Architecture Style:** Modular Monolith  
**Primary Language:** Arabic — RTL  
**Project Type:** Corporate website with a content-management dashboard  
**Purpose:** Define the project structure and the responsibility of each Django application before implementation.

---

## 1. Architecture Overview

The Elevator Gate website will be developed as a **Modular Monolith** using Django.

The system will be one Django project, divided into independent applications according to business responsibility. Each application will contain the logic, models, URLs, views, templates, forms, and admin configuration related to its domain.

The initial Django applications are:

- `core`
- `pages`
- `services`
- `projects`
- `blog`
- `contact`

This separation improves:

- Code organization
- Maintainability
- Reusability
- Testing
- Future scalability
- Clear ownership of business logic
- Easier content management through Django Admin

---

## 2. High-Level Project Structure

```text
elevator_gate/
│
├── manage.py
├── requirements.txt
├── .env
├── .env.example
├── .gitignore
├── README.md
│
├── config/
│   ├── __init__.py
│   ├── settings/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── development.py
│   │   └── production.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── apps/
│   ├── __init__.py
│   ├── core/
│   ├── pages/
│   ├── services/
│   ├── projects/
│   ├── blog/
│   └── contact/
│
├── templates/
│   ├── base.html
│   ├── includes/
│   ├── errors/
│   └── admin/
│
├── static/
│   ├── css/
│   ├── js/
│   ├── images/
│   ├── icons/
│   └── fonts/
│
├── media/
│   ├── services/
│   ├── projects/
│   ├── blog/
│   └── testimonials/
│
├── locale/
│
└── tests/
```

---

## 3. Configuration Layer — `config`

The `config` package is the central configuration layer of the Django project. It is not a business application and should not contain website content or domain models.

### Responsibilities

- Define project settings.
- Register installed Django applications.
- Configure the database.
- Configure static and media files.
- Configure templates.
- Configure security and middleware.
- Configure localization and time zone.
- Define the root URL configuration.
- Provide WSGI and ASGI entry points.
- Separate development and production settings.

### Settings Structure

#### `base.py`

Contains settings shared between all environments:

- `INSTALLED_APPS`
- `MIDDLEWARE`
- `TEMPLATES`
- Authentication configuration
- Internationalization
- Static and media configuration
- Default primary key type

#### `development.py`

Contains local-development configuration:

- `DEBUG = True`
- Local database credentials
- Console email backend
- Development-only tools
- Local allowed hosts

#### `production.py`

Contains deployment configuration:

- `DEBUG = False`
- Production database
- Secure cookies
- HTTPS settings
- Production email provider
- Logging
- Allowed hosts
- CSRF trusted origins

---

# 4. Django Applications

## 4.1 `core` App

### Purpose

The `core` app contains shared functionality and global content used throughout the entire website. It should not own business-specific content that belongs to services, projects, blog, or contact.

### Main Responsibilities

- Shared site-wide models.
- Global website settings.
- Navigation and footer data.
- Reusable mixins and utilities.
- Common context processors.
- Shared validators.
- Shared template tags.
- Testimonials.
- Frequently asked questions when they are global.
- SEO helper utilities.
- Common abstract models.
- Custom error handlers.
- Health-check endpoint.

### Suggested Models

#### `TimeStampedModel`

An abstract model inherited by other models.

```python
created_at
updated_at
```

#### `PublishableModel`

An optional abstract model for content that may be published or hidden.

```python
is_active
published_at
```

#### `SiteSettings`

Stores editable global website information.

Possible fields:

```text
company_name
logo
favicon
phone
email
whatsapp_number
address
working_hours
facebook_url
instagram_url
linkedin_url
x_url
default_meta_title
default_meta_description
```

Only one active record should normally exist.

#### `Testimonial`

Stores customer testimonials.

Possible fields:

```text
client_name
client_position
company_name
content
client_image
rating
is_featured
is_active
display_order
created_at
updated_at
```

#### `FAQ`

Stores general frequently asked questions.

Possible fields:

```text
question
answer
category
display_order
is_active
created_at
updated_at
```

### Suggested Components

```text
apps/core/
├── admin.py
├── apps.py
├── context_processors.py
├── models.py
├── urls.py
├── views.py
├── validators.py
├── mixins.py
├── utils.py
├── templatetags/
│   ├── __init__.py
│   └── core_tags.py
├── migrations/
└── tests/
```

### URL Examples

```text
/health/
/robots.txt
/sitemap.xml
```

### Notes

- Avoid placing unrelated models in `core`.
- A model belongs in `core` only when it is genuinely shared across multiple domains.
- Site-wide footer and header information should be loaded through a context processor.

---

## 4.2 `pages` App

### Purpose

The `pages` app manages static or semi-static website pages that do not require a separate business domain.

### Main Responsibilities

- Home page.
- About page.
- General FAQ page presentation.
- Privacy policy.
- Terms and conditions.
- Other informational pages.
- Composition of content from other apps for the homepage.

### Pages Managed

- Home
- About
- FAQ
- Privacy Policy
- Terms and Conditions
- Custom informational pages, when required

### Suggested Models

A simple first version may use templates without models. If the content must be editable from Django Admin, the following models can be added.

#### `Page`

```text
title
slug
content
meta_title
meta_description
is_active
created_at
updated_at
```

#### `HomeSection`

Optional model for editable homepage sections.

```text
section_key
title
subtitle
content
image
button_text
button_url
display_order
is_active
```

### Home Page Responsibilities

The home view may read data from other apps:

- Featured services from `services`
- Featured projects from `projects`
- Latest blog posts from `blog`
- Testimonials from `core`
- FAQs from `core`

The `pages` app displays and composes this data but does not own it.

### Suggested Components

```text
apps/pages/
├── admin.py
├── apps.py
├── models.py
├── urls.py
├── views.py
├── migrations/
├── tests/
└── templates/
    └── pages/
        ├── home.html
        ├── about.html
        ├── faq.html
        ├── privacy_policy.html
        └── terms.html
```

### URL Examples

```text
/
/about/
/faq/
/privacy-policy/
/terms/
```

### Notes

- Keep the homepage composition logic readable.
- For complex homepage queries, use service functions or selectors instead of placing all logic inside the view.
- Static pages should not duplicate content owned by another app.

---

## 4.3 `services` App

### Purpose

The `services` app manages all elevator services offered by Elevator Gate.

### Main Responsibilities

- Display the services listing page.
- Display individual service detail pages.
- Manage services through Django Admin.
- Store service descriptions, images, features, and SEO metadata.
- Mark selected services as featured.
- Control service ordering and publication status.

### Main Model

#### `Service`

Suggested fields:

```text
title
slug
short_description
description
icon
featured_image
meta_title
meta_description
is_featured
is_active
display_order
created_at
updated_at
```

### Optional Models

#### `ServiceFeature`

Used when each service contains a structured list of benefits or features.

```text
service
title
description
icon
display_order
```

Relationship:

```text
Service 1 ──── * ServiceFeature
```

### Suggested Components

```text
apps/services/
├── admin.py
├── apps.py
├── models.py
├── urls.py
├── views.py
├── selectors.py
├── migrations/
├── tests/
└── templates/
    └── services/
        ├── service_list.html
        └── service_detail.html
```

### URL Examples

```text
/services/
/services/<slug:slug>/
```

### Public Views

- `ServiceListView`
- `ServiceDetailView`

### Query Rules

Public pages should display only records where:

```python
is_active=True
```

The service detail lookup should use the unique `slug`, not the database ID.

### Notes

- Service-related business logic must remain inside this app.
- The `projects` app may reference a service, but should not duplicate service information.
- Images should be uploaded under `media/services/`.

---

## 4.4 `projects` App

### Purpose

The `projects` app manages completed elevator projects and their categories.

### Main Responsibilities

- Display the projects listing page.
- Filter projects by category.
- Display project detail pages.
- Manage project categories.
- Manage project galleries.
- Mark selected projects as featured.
- Store project SEO metadata.
- Provide portfolio content for the homepage.

### Main Models

#### `ProjectCategory`

Suggested fields:

```text
name
slug
description
display_order
is_active
created_at
updated_at
```

#### `Project`

Suggested fields:

```text
title
slug
category
service
client_name
location
completion_date
short_description
description
cover_image
meta_title
meta_description
is_featured
is_active
display_order
created_at
updated_at
```

Possible relationships:

```text
ProjectCategory 1 ──── * Project
Service         1 ──── * Project
```

The `service` relationship may be optional if one project is associated with one primary service.

#### `ProjectImage`

Stores multiple images for one project.

```text
project
image
alt_text
caption
display_order
is_active
```

Relationship:

```text
Project 1 ──── * ProjectImage
```

### Suggested Components

```text
apps/projects/
├── admin.py
├── apps.py
├── models.py
├── urls.py
├── views.py
├── filters.py
├── selectors.py
├── migrations/
├── tests/
└── templates/
    └── projects/
        ├── project_list.html
        ├── project_detail.html
        └── includes/
            └── project_card.html
```

### URL Examples

```text
/projects/
/projects/category/<slug:category_slug>/
/projects/<slug:slug>/
```

### Public Views

- `ProjectListView`
- `ProjectDetailView`
- Optional category-filtered project view

### Query Optimization

For project listing and detail pages, use:

```python
select_related("category", "service")
prefetch_related("images")
```

This prevents unnecessary database queries.

### Notes

- Project categories belong only to this app.
- Images should be uploaded under `media/projects/`.
- Filtering must use safe ORM queries and validated URL parameters.

---

## 4.5 `blog` App

### Purpose

The `blog` app manages SEO-focused articles, categories, and blog content.

### Main Responsibilities

- Display the blog listing page.
- Display article detail pages.
- Manage blog categories.
- Support article publication workflow.
- Store SEO metadata.
- Display related articles.
- Provide recent articles to the homepage.
- Generate structured article URLs.

### Main Models

#### `BlogCategory`

Suggested fields:

```text
name
slug
description
is_active
created_at
updated_at
```

#### `BlogPost`

Suggested fields:

```text
title
slug
category
excerpt
content
featured_image
author
meta_title
meta_description
published_at
is_featured
is_published
created_at
updated_at
```

Relationships:

```text
BlogCategory 1 ──── * BlogPost
User         1 ──── * BlogPost
```

The author may use Django’s configured user model:

```python
settings.AUTH_USER_MODEL
```

### Optional Models

#### `BlogTag`

Can be added later if tag-based discovery becomes necessary.

#### `BlogPostTag`

Handled through a Django `ManyToManyField`.

### Suggested Components

```text
apps/blog/
├── admin.py
├── apps.py
├── models.py
├── urls.py
├── views.py
├── selectors.py
├── migrations/
├── tests/
└── templates/
    └── blog/
        ├── post_list.html
        ├── post_detail.html
        ├── category_posts.html
        └── includes/
            └── post_card.html
```

### URL Examples

```text
/blog/
/blog/category/<slug:category_slug>/
/blog/<slug:slug>/
```

### Publication Rules

A public article must satisfy:

```python
is_published=True
published_at <= timezone.now()
```

### SEO Responsibilities

Each article should support:

- Unique slug
- Meta title
- Meta description
- Canonical URL
- Social sharing image
- Semantic headings
- Image alternative text
- Article structured data, when implemented

### Notes

- Blog publication logic belongs in the blog app.
- Draft articles must never be exposed publicly.
- Rich text input must be sanitized when HTML content is allowed.

---

## 4.6 `contact` App

### Purpose

The `contact` app manages customer inquiries submitted through the website.

### Main Responsibilities

- Display the contact page.
- Validate contact forms.
- Store customer messages.
- Send email notifications.
- Manage inquiry status from Django Admin.
- Protect forms from spam and abuse.
- Provide success and error responses.

### Main Model

#### `ContactMessage`

Suggested fields:

```text
full_name
phone
email
subject
message
preferred_contact_method
status
admin_notes
ip_address
user_agent
created_at
updated_at
```

Suggested status values:

```text
new
in_progress
contacted
closed
spam
```

### Optional Future Model

#### `MaintenanceRequest`

This should be added only when maintenance requests require structured elevator and fault details instead of a general contact message.

Possible fields:

```text
customer_name
phone
email
building_name
city
elevator_type
fault_type
fault_description
urgency
attachment
status
created_at
updated_at
```

### Suggested Components

```text
apps/contact/
├── admin.py
├── apps.py
├── forms.py
├── models.py
├── urls.py
├── views.py
├── services.py
├── migrations/
├── tests/
└── templates/
    └── contact/
        ├── contact.html
        └── contact_success.html
```

### URL Examples

```text
/contact/
/contact/success/
```

### Form Processing Flow

```text
Visitor
   ↓
Contact Form
   ↓
Server-Side Validation
   ↓
Spam Protection
   ↓
Save ContactMessage
   ↓
Send Notification Email
   ↓
Redirect to Success Page
```

### Security Requirements

- Use Django CSRF protection.
- Validate all submitted values.
- Apply rate limiting where possible.
- Add a honeypot or CAPTCHA if spam becomes a problem.
- Never expose `admin_notes` publicly.
- Avoid logging sensitive message content unnecessarily.
- Escape user content when displayed in admin or templates.

### Notes

- Email sending should be placed in `services.py`, not directly embedded in a large view.
- A failed notification email should not necessarily delete a valid stored inquiry.
- The database record is the primary source of truth.

---

# 5. App Ownership Matrix

| Feature or Data | Owning App |
|---|---|
| Site settings | `core` |
| Header and footer shared data | `core` |
| Testimonials | `core` |
| General FAQs | `core` |
| Home page | `pages` |
| About page | `pages` |
| Privacy and terms pages | `pages` |
| Services | `services` |
| Service features | `services` |
| Projects | `projects` |
| Project categories | `projects` |
| Project gallery | `projects` |
| Blog posts | `blog` |
| Blog categories | `blog` |
| Contact form | `contact` |
| Customer messages | `contact` |
| Root settings and URLs | `config` |

---

# 6. URL Architecture

The root URL configuration should delegate URLs to each application.

## `config/urls.py`

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.pages.urls")),
    path("services/", include("apps.services.urls")),
    path("projects/", include("apps.projects.urls")),
    path("blog/", include("apps.blog.urls")),
    path("contact/", include("apps.contact.urls")),
    path("", include("apps.core.urls")),
]
```

Each app must define:

```python
app_name = "app_name"
```

Example:

```python
app_name = "services"
```

Templates should use named URLs:

```django
{% url "services:detail" service.slug %}
```

Do not hard-code internal URLs in templates.

---

# 7. Template Architecture

## Global Templates

```text
templates/
├── base.html
├── includes/
│   ├── header.html
│   ├── footer.html
│   ├── navbar.html
│   ├── messages.html
│   ├── breadcrumbs.html
│   └── pagination.html
└── errors/
    ├── 400.html
    ├── 403.html
    ├── 404.html
    └── 500.html
```

## App Templates

Each app should own its templates:

```text
apps/<app_name>/templates/<app_name>/
```

Example:

```text
apps/services/templates/services/service_list.html
```

## Base Template Responsibilities

`base.html` should contain:

- HTML document structure
- Arabic language declaration
- RTL direction
- Global metadata blocks
- Header
- Footer
- CSS imports
- JavaScript imports
- Flash messages
- Reusable template blocks

Suggested blocks:

```django
{% block title %}{% endblock %}
{% block meta_description %}{% endblock %}
{% block extra_css %}{% endblock %}
{% block content %}{% endblock %}
{% block extra_js %}{% endblock %}
```

---

# 8. Static and Media Files

## Static Files

Static assets are version-controlled assets shipped with the application.

```text
static/
├── css/
├── js/
├── images/
├── icons/
└── fonts/
```

Examples:

- CSS files
- JavaScript files
- Logo fallback
- Icons
- Decorative images
- Local font files referenced by the project

## Media Files

Media files are uploaded through Django Admin.

```text
media/
├── services/
├── projects/
├── blog/
└── testimonials/
```

Uploaded files must not be committed to Git.

---

# 9. Business Logic Placement

To avoid oversized views and models, the project may use the following modules when needed.

## `selectors.py`

Contains reusable read/query logic.

Examples:

```python
get_featured_services()
get_published_projects()
get_latest_blog_posts()
```

## `services.py`

Contains operations that change state or interact with external systems.

Examples:

```python
create_contact_message()
send_contact_notification()
publish_blog_post()
```

## `forms.py`

Contains form declaration and validation.

## `validators.py`

Contains reusable field or file validators.

## `utils.py`

Contains small generic helper functions that do not own business rules.

### Rule

Do not create these files only for appearance. Add them when the app has enough logic to justify the separation.

---

# 10. Dependency Rules

The applications should follow controlled dependency rules.

## Allowed Examples

- `pages` reads featured services from `services`.
- `pages` reads featured projects from `projects`.
- `pages` reads latest articles from `blog`.
- `pages` reads testimonials and FAQs from `core`.
- `projects.Project` may reference `services.Service`.
- All content models may inherit abstract timestamp models from `core`.

## Avoid

- Circular model imports.
- Services importing page-specific logic.
- Blog importing contact form logic.
- Core depending on every business app.
- Duplicating the same fields or records in different apps.
- Calling one app’s private helper functions from many unrelated apps.

## Recommended Dependency Direction

```text
config
   ↓
pages ─────→ services
   │        projects
   │        blog
   └──────→ core

projects ──→ services

contact ───→ core utilities, only when required
```

`core` should remain as independent as possible.

---

# 11. Django Admin Architecture

Each content-owning application is responsible for its own admin configuration.

## Admin Requirements

- Useful list columns
- Search fields
- Filters
- Slug auto-population
- Logical fieldsets
- Read-only timestamps
- Image previews where practical
- Editable publication status
- Ordering controls
- Inline project images
- Inline service features

## Examples

### Services Admin

```text
list_display:
title, is_featured, is_active, display_order, updated_at

search_fields:
title, short_description

list_filter:
is_featured, is_active
```

### Contact Admin

```text
list_display:
full_name, phone, subject, status, created_at

search_fields:
full_name, phone, email, subject

list_filter:
status, created_at

readonly_fields:
ip_address, user_agent, created_at, updated_at
```

---

# 12. Naming Conventions

## Python

- Files and variables: `snake_case`
- Classes: `PascalCase`
- Constants: `UPPER_SNAKE_CASE`
- Model names: singular
- App names: plural or domain-based lowercase names

## URLs

Use lowercase, readable, hyphen-separated paths:

```text
/privacy-policy/
/project-category/
```

## Slugs

Use unique slugs for public content:

```text
elevator-maintenance
commercial-building-project
elevator-safety-tips
```

## Templates

Use descriptive names:

```text
service_list.html
service_detail.html
project_card.html
```

---

# 13. Testing Architecture

Each app must contain tests for its own behavior.

Suggested structure:

```text
apps/services/tests/
├── __init__.py
├── test_models.py
├── test_views.py
├── test_urls.py
└── test_admin.py
```

## Minimum Test Coverage Areas

### `core`

- Site settings retrieval
- Active FAQ filtering
- Testimonial ordering

### `pages`

- Home page response
- Correct context data
- Static page availability

### `services`

- Active service listing
- Inactive services hidden
- Detail page by slug
- Featured service query

### `projects`

- Project filtering by category
- Gallery retrieval
- Inactive project protection
- Query relationships

### `blog`

- Draft posts hidden
- Future posts hidden
- Published article detail
- Category filtering

### `contact`

- Valid form submission
- Invalid form rejection
- Message saved correctly
- Success redirect
- Email service behavior

---

# 14. Security Architecture

The project must use Django’s built-in protections and secure configuration.

## Required Controls

- CSRF protection
- ORM-based database access
- Escaped template output
- Secure password hashing
- Environment variables for secrets
- File upload validation
- Production HTTPS
- Secure cookies
- Restricted allowed hosts
- Restricted admin access
- No debug mode in production
- Rate limiting for public forms, when supported
- Database and media backups

## Environment Variables

Sensitive configuration belongs in `.env`:

```text
DJANGO_SECRET_KEY
DJANGO_DEBUG
DJANGO_ALLOWED_HOSTS
DATABASE_URL
EMAIL_HOST
EMAIL_PORT
EMAIL_HOST_USER
EMAIL_HOST_PASSWORD
DEFAULT_FROM_EMAIL
```

The `.env` file must be excluded through `.gitignore`.

---

# 15. SEO Architecture

SEO is shared across the project but owned by each content app for its domain.

## Shared SEO Responsibilities — `core`

- Default site title
- Default meta description
- Sitemap configuration
- Robots configuration
- Shared Open Graph defaults
- Canonical URL helpers

## App SEO Responsibilities

### `services`

- Service meta title
- Service meta description
- Service slug
- Service structured content

### `projects`

- Project title and description
- Image alt text
- Project canonical URL

### `blog`

- Article metadata
- Publishing date
- Author
- Article schema
- Social sharing image

### `pages`

- Home and about metadata
- Static page canonical URLs

---

# 16. Internationalization and RTL

The initial website language is Arabic.

Recommended settings:

```python
LANGUAGE_CODE = "ar"
TIME_ZONE = "Asia/Riyadh"
USE_I18N = True
USE_TZ = True
```

Base HTML:

```html
<html lang="ar" dir="rtl">
```

Architecture should not prevent future English support. User-facing text should not be unnecessarily hard-coded in Python code.

Potential future structure:

```text
locale/
├── ar/
└── en/
```

---

# 17. Request Flow Example

## Service Detail Request

```text
Browser requests /services/elevator-maintenance/
                    ↓
config.urls
                    ↓
services.urls
                    ↓
ServiceDetailView
                    ↓
Service query by active slug
                    ↓
services/service_detail.html
                    ↓
HTML response
```

## Contact Submission Request

```text
Browser submits POST /contact/
                    ↓
contact.urls
                    ↓
ContactView
                    ↓
ContactForm validation
                    ↓
ContactMessage saved
                    ↓
Notification service called
                    ↓
Redirect to success page
```

---

# 18. Initial Model Ownership$$$

The database entities defined during the database-design stage map to apps as follows:

| Model | Django App |
|---|---|
| `Service` | `services` |
| `Project` | `projects` |
| `ProjectCategory` | `projects` |
| `BlogPost` | `blog` |
| `BlogCategory` | `blog` |
| `Testimonial` | `core` |
| `FAQ` | `core` |
| `ContactMessage` | `contact` |

This mapping must remain the source of truth unless the system requirements change.

---

# 19. Development Sequence $$$

Recommended implementation order:

1. Create the Django project and settings structure.
2. Create all application packages.
3. Register apps in `INSTALLED_APPS`.
4. Implement shared abstract models in `core`.
5. Implement service models.
6. Implement project models and relationships.
7. Implement blog models.
8. Implement contact model and form.
9. Configure Django Admin.
10. Create and apply migrations.
11. Add app URLs.
12. Build templates.
13. Connect static and media files.
14. Add tests.
15. Add SEO and production security configuration.

---

# 20. Architecture Decisions Summary $$$

- Use one Django project divided into domain-focused applications.
- Use `config` only for project configuration.
- Use `core` for genuinely shared system functionality.
- Use `pages` for static pages and homepage composition.
- Keep each business model inside the app that owns its domain.
- Use named and namespaced URLs.
- Use slugs for public content URLs.
- Keep uploaded content under `media`.
- Keep application assets under `static`.
- Use abstract shared models to reduce duplication.
- Separate complex queries and operations when the codebase requires it.
- Prevent circular dependencies.
- Keep public content controlled by active or publication status.
- Design the structure to support testing, SEO, security, and future localization.

---

## Final Approved Application Structure

```text
apps/
├── core/       # Shared system functionality and global content
├── pages/      # Home and informational pages
├── services/   # Elevator services
├── projects/   # Projects, categories, and galleries
├── blog/       # Articles and blog categories
└── contact/    # Contact forms and customer inquiries
```

This architecture is the approved starting structure for the Elevator Gate Django implementation.
