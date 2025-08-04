"""
Template script to initialize a FastAPI web app project structure with HTML, CSS, and Python support.
Run this script to create the necessary folders and starter files.
"""
import os

# Define the folder structure
folders = [
    "app",
    "app/static/css",
    "app/static/js",
    "app/static/images",
    "app/templates",
    "app/routers",
    "app/models",
    "app/auth",
    "app/service",
    "app/schemas",
    "app/utils",
    "tests",
    "tests/workflows",
    ".github/workflows",
]

# Define starter files with optional content
files = {
    "app/main.py": "from fastapi import FastAPI\nfrom fastapi.staticfiles import StaticFiles\nfrom fastapi.templating import Jinja2Templates\n\napp = FastAPI()\n\napp.mount('/static', StaticFiles(directory='static'), name='static')\ntemplates = Jinja2Templates(directory='templates')\n\n# ...add your routes here...\n",
    "app/auth/__init__.py": "",
    "app/service/__init__.py": "",
    "app/routers/__init__.py": "",
    "app/models/__init__.py": "",
    "app/schemas/__init__.py": "",
    "app/utils/__init__.py": "",
    "app/static/css/style.css": "/* Add your CSS here */\n",
    "app/static/js/app.js": "// Add your JavaScript here\n",
    "app/templates/index.html": "<!DOCTYPE html>\n<html>\n<head>\n    <title>FastAPI Web App</title>\n    <link rel='stylesheet' href='/static/css/style.css'>\n</head>\n<body>\n    <h1>Welcome to FastAPI Web App!</h1>\n    <script src='/static/js/app.js'></script>\n</body>\n</html>\n",
    "tests/__init__.py": "",
    "tests/workflows/__init__.py": "",
    ".github/workflows/ci.yml": "name: CI\n\non:\n  push:\n    branches: [main]\n  pull_request:\n    branches: [main]\n\njobs:\n  build:\n    runs-on: ubuntu-latest\n    steps:\n      - uses: actions/checkout@v4\n      - name: Set up Python\n        uses: actions/setup-python@v5\n        with:\n          python-version: '3.11'\n      - name: Install dependencies\n        run: |\n          python -m pip install --upgrade pip\n          pip install fastapi uvicorn jinja2 pytest\n      - name: Run tests\n        run: |\n          pytest\n",
    "README.md": """\n# FastAPI Web App\n\nProject initialized with template.py\n\n## 📁 Folder Structure & Purpose\n\n- **app/** — Main application code\n    - **main.py** — FastAPI application entry point. Initialize the app, mount static files, and include routers here.\n    - **routers/** — Place your API route definitions here. Each file can represent a module or feature (e.g., user.py, items.py).\n    - **models/** — Database models or ORM classes. Define your SQLAlchemy or Tortoise ORM models here.\n    - **schemas/** — Pydantic schemas for request/response validation. Use for data validation and serialization.\n    - **utils/** — Utility/helper functions, reusable logic, or service classes.\n    - **templates/** — Jinja2 HTML templates for server-side rendering. Place your .html files here.\n    - **static/** — Static files for the frontend (served as-is).\n        - **css/** — CSS files for styling your HTML templates.\n        - **js/** — JavaScript files for frontend interactivity.\n        - **images/** — Static image assets (logos, icons, etc).\n\n- **tests/** — Test suite for the project\n    - **__init__.py** — Makes the tests directory a package.\n    - **workflows/** — Place for pytest workflow helpers, fixtures, or test utilities.\n\n- **.github/workflows/** — GitHub Actions workflows for CI/CD\n    - **ci.yml** — Runs tests automatically on push/PR to main. Ensures code quality and reliability.\n\n- **README.md** — Project overview, setup instructions, and folder explanations.\n\n---\n\n## 🚀 Quick Start\n\n1. **Install dependencies:**\n   ```bash\n   pip install fastapi uvicorn jinja2 pytest\n   ```\n2. **Run the app:**\n   ```bash\n   uvicorn app.main:app --reload\n   ```\n3. **Run tests:**\n   ```bash\n   pytest\n   ```\n\n---\n\n## 💡 Tips\n- Add new routers in `app/routers` and include them in `main.py`.\n- Use `app/templates` for your HTML and reference static assets with `/static/...`.\n- Write tests in `tests/` and organize by feature or module.\n- Customize the CI workflow in `.github/workflows/ci.yml` as needed.\n\n---\n\nHappy coding! 🎉\n""",
}

def create_folders():
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        print(f"Created folder: {folder}")

def create_files():
    for path, content in files.items():
        if not os.path.exists(path):
            with open(path, "w") as f:
                f.write(content)
            print(f"Created file: {path}")
        else:
            print(f"File already exists: {path}")

def main():
    create_folders()
    create_files()
    print("\nProject structure created successfully!")
    print("\nNext steps:")
    print("1. Install FastAPI and Uvicorn: pip install fastapi uvicorn jinja2")
    print("2. Run the app: uvicorn app.main:app --reload")

if __name__ == "__main__":
    main()
