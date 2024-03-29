import os
from pathlib import Path
import shutil

from block_markdown import(
    markdown_to_html_node
)

def extract_title(markdown):
    for line in markdown.split("\n"):
        if line.startswith("# "):
            return line.lstrip("# ")
    raise Exception("No h1 header present")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as f:
        markdown = f.read()
    with open(template_path, "r") as f:
        template = f.read()
    title = extract_title(markdown)
    content = markdown_to_html_node(markdown).to_html()
    template = template.replace("{{ Title }}", title).replace("{{ Content }}", content)

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, 'w') as f:
        print(f"writing template to {dest_path}")
        f.write(template)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path)
        else:
            generate_pages_recursive(from_path, template_path, dest_path)
