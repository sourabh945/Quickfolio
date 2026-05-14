# Quickfolio

A lightweight, data-driven portfolio web application built with Flask. The entire portfolio is driven by a single JSON file hosted remotely, meaning you can update your content without touching any code or redeploying the application.

---

## Overview

This project is designed to let developers launch a fully functional, professional portfolio with minimal setup. All personal data including your name, experience, skills, projects, education, and contact information is loaded dynamically from a remote JSON file at runtime. The frontend is rendered with Jinja2 templates, styled using Tailwind CSS, and powered by Alpine.js for reactive UI behaviour.

---

## Features

- Data-driven architecture: all portfolio content is sourced from a single remote JSON file
- No frontend build step required; Tailwind CSS is loaded via CDN
- Terminal-themed UI with a dark aesthetic using JetBrains Mono
- Sections for About, Experience, Skills, Projects, Education, and Achievements
- Project detail modal with full description and technical implementation notes
- Contact modal with support for email, phone, and social links
- Resume download route
- Custom error pages for 400, 404, and 500 responses
- SEO support via structured JSON-LD injection and sitemap
- Production-ready server configuration using Gunicorn with Gevent workers and SSL support

---

## Project Structure

```
.
├── app.py                  # Flask application and route definitions
├── server.py               # Gunicorn production server configuration
├── data/
│   └── data.json           # Local config pointing to remote JSON data source
├── modules/
│   └── load_data.py        # Utility to load data.json at startup
├── templates/
│   ├── index.html          # Main portfolio page
│   └── error_pages/
│       ├── 400.html
│       ├── 404.html
│       └── 500.html
└── static/
    ├── robots.txt
    ├── sitemap.xml
    ├── favicon.ico
    └── media/
        └── resume.pdf      # Your resume file
```

---

## Configuration

All content configuration is handled through `data/data.json`:

```json
{
  "data_file_location": "https://raw.githubusercontent.com/your-username/your-repo/main/info.json",
  "title": "Your Name | Your Role",
  "description": "A short meta description for SEO."
}
```

- `data_file_location`: URL to the raw JSON file containing your portfolio data. This is fetched by the client browser at page load.
- `title`: The HTML page title shown in the browser tab and search results.
- `description`: The meta description used by search engines.

---

## Remote Data File (info.json)

The `info.json` file hosted on GitHub (or any public URL) must follow a specific schema. The portfolio reads the following top-level keys:

| Key            | Type    | Description                                      |
|----------------|---------|--------------------------------------------------|
| `name`         | string  | Your full name                                   |
| `title`        | string  | Your professional title                          |
| `about`        | string  | A short bio displayed in the About section       |
| `experience`   | array   | List of work experience objects                  |
| `skills`       | array   | List of skill category objects                   |
| `projects`     | array   | List of project objects                          |
| `education`    | array   | List of education objects                        |
| `achievements` | array   | List of achievement objects                      |
| `contacts`     | array   | List of contact link objects                     |
| `nav-bar`      | object  | Navigation links for GitHub, LinkedIn, and resume|
| `sections`     | object  | Optional map to control which sections are shown |

---

## Getting Started

### Prerequisites

- Python 3.10 or higher
- pip

### Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/your-portfolio.git
cd your-portfolio
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install flask gunicorn gevent
```

4. Update `data/data.json` with your remote JSON URL, page title, and description.

5. Place your resume at `static/media/resume.pdf`.

### Running in Development

```bash
python app.py
```

The application will be available at `http://localhost:5000`.

---

## Production Deployment

The `server.py` file configures a Gunicorn server with Gevent workers, SSL support, and sensible defaults for production use.

### SSL Certificates

Place your certificate files in a `certificates/` directory at the project root:

```
certificates/
├── cert.pem
└── key.pem
```

### Starting the Production Server

```bash
python server.py
```

The server will bind to `0.0.0.0:5000` and spawn workers based on the number of available CPU cores (`cpu_count * 2 + 1`).

### HTTP to HTTPS Redirect

The application includes a `before_request` hook that automatically redirects all HTTP traffic to HTTPS via a 304 redirect.

---

## SEO

The following SEO features are included out of the box:

- `<meta name="description">` populated from `data.json`
- `robots.txt` served at `/robots.txt`
- `sitemap.xml` served at `/sitemap.xml`
- JSON-LD structured data (`schema.org/Person`) injected dynamically from your portfolio data

Update `static/sitemap.xml` and `static/robots.txt` with your actual deployment URL before going live.

---

## Customisation

To adapt the portfolio to a different person or brand:

1. Host a new `info.json` file at any public URL and update `data_file_location` in `data/data.json`.
2. Replace `static/media/resume.pdf` with the new resume.
3. Replace `static/favicon.ico` with a custom icon.
4. Update `static/sitemap.xml` and `static/robots.txt` with the correct domain.

No changes to application code are required.

---

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for details.
