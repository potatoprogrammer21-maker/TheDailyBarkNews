from app import app
from flask import url_for
import os

OUTPUT_DIR = "dist"

# Make sure dist/ exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

with app.test_request_context():
    # List all the routes you want exported
    routes = [
        "/",           # homepage
        "/about",      # example
        "/news",       # example
    ]

    for route in routes:
        rendered = app.test_client().get(route).data.decode("utf-8")

        # Convert route to filename
        if route == "/":
            filename = "index.html"
        else:
            filename = route.strip("/") + ".html"

        path = os.path.join(OUTPUT_DIR, filename)

        with open(path, "w") as f:
            f.write(rendered)

        print("Exported:", path)
