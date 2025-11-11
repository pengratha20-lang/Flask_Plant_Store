import os
import re

# Directory to search
template_dir = r"C:\Users\ASUS\PycharmProjects\FlaskProject_Final\templates"

# Mapping of old to new endpoints
replacements = {
    "fronts.home.index": "home.home",
    "fronts.shop.all_products": "shop.shop",
    "fronts.contact.index": "contact.contact",
    "fronts.cart.index": "cart.cart",
    "fronts.service.index": "service.service",
    "fronts.about.index": "about.about"
}

def replace_in_file(file_path, replacements):
    """Replace URL endpoints in a file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Replace each endpoint
        for old_endpoint, new_endpoint in replacements.items():
            pattern = f"url_for\\(['\"]({re.escape(old_endpoint)})['\"]"
            replacement = f"url_for('{new_endpoint}'"
            content = re.sub(pattern, replacement, content)
        
        # Only write if content changed
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated: {file_path}")
            return True
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
    return False

def process_directory(directory):
    """Process all HTML files in directory"""
    updated_files = []
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                if replace_in_file(file_path, replacements):
                    updated_files.append(file_path)
    
    return updated_files

if __name__ == "__main__":
    print("Updating URL endpoints in templates...")
    updated = process_directory(template_dir)
    print(f"\nUpdated {len(updated)} files:")
    for file_path in updated:
        print(f"  - {file_path}")
    print("Done!")