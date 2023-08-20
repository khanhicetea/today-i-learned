#!/usr/bin/env python3

import os
import argparse
import re
import subprocess
from datetime import datetime

def slugify(s):
    s = s.lower().strip()
    s = re.sub(r'[^\w\s-]', '', s)
    s = re.sub(r'[\s_-]+', '-', s)
    s = re.sub(r'^-+|-+$', '', s)
    return s

def create_note(category, title):
    # Create the directory if it doesn't exist
    if not os.path.exists(category):
        os.makedirs(category)
    
    # Create the markdown file with the slug of the title as the filename
    slug = slugify(title)
    filename = os.path.join(category, f"{slug}.md")
    
    # Get the current date
    current_date = datetime.now().strftime("%Y-%m-%d")
    
    # Create and write the content to the markdown file
    content = f"- Date : {current_date}\n- Tags :\n\n## {title}"
    with open(filename, "w") as f:
        f.write(content)
    
    print(f"Note '{title}' created in category '{category}'.")
    
    # Open the created file in the default text editor
    subprocess.run(["/usr/bin/vim", filename], check=True)

def commit():
    subprocess.run(["git", "add", "-A"], check=True)
    current_date = datetime.now().strftime("%Y-%m-%d")
    subprocess.run(["git", "commit", "-m", current_date], check=True)
    subprocess.run(["git", "push"], check=True)
    return print("Changes committed and pushed.")

def main():
    parser = argparse.ArgumentParser(description="Manage your notes")
    parser.add_argument("category", help="Name of the category for the note")
    parser.add_argument("title", help="Title of the note", nargs='?', default="")
    
    args = parser.parse_args()
    
    if args.category == "commit":
        return commit()
    
    create_note(args.category, args.title)

if __name__ == "__main__":
    main()
