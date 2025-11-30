from app import app, dogs
from flask import render_template
import os

OUTPUT_DIR = "dist"

os.makedirs(OUTPUT_DIR, exist_ok=True)

with app.app_context():
    # Render homepage
    html = render_template("index.html", dogs=dogs)

    # Write to dist/index.html
    with open(os.path.join(OUTPUT_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)

# Copy static folder
import shutil
if os.path.exists("static"):
    shutil.copytree("static", os.path.join(OUTPUT_DIR, "static"), dirs_exist_ok=True)

print("Export complete!")
