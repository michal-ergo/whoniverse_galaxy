"""Stellaris Localisation Copier by Ergotoxin"""

import shutil
import os

# File paths
original_files = {
    'localisation/english/whoniverse_l_english.yml': 'whoniverse_l_',
    'localisation/english/whoniverse_concepts_l_english.yml': 'whoniverse_concepts_l_',
    'localisation/english/name_lists/whoniverse_countries_names_l_english.yml': 'whoniverse_countries_names_l_',
    'localisation/english/name_lists/whoniverse_name_list_l_english.yml': 'whoniverse_name_list_l_'
}

# Language mutations and prefixes
languages = {
    'braz_por': 'l_braz_por',
    'french': 'l_french',
    'german': 'l_german',
    'japanese': 'l_japanese',
    'korean': 'l_korean',
    'polish': 'l_polish',
    'russian': 'l_russian',
    'simp_chinese': 'l_simp_chinese',
    'spanish': 'l_spanish'
}

# Copy files to language folders, rename them, modify first line
for original_file, base_name in original_files.items():
    for lang, lang_prefix in languages.items():
        # Directory path by language (with 'name_lists' folder if applicable)
        if 'name_lists' in original_file:
            folder = f"localisation/{lang}/name_lists"
        else:
            folder = f"localisation/{lang}"
        
        # New file name
        new_file_name = f"{base_name}{lang}.yml"
        # Create new folder if it doesn't exist
        os.makedirs(folder, exist_ok=True)
        # Target file path
        target_file_path = os.path.join(folder, new_file_name)
        try:
            # Copy the file
            shutil.copyfile(original_file, target_file_path)
            # Open the file for editing
            with open(target_file_path, 'r+', encoding='utf-8-sig') as file:
                content = file.read()
                # Replace 'l_english:' with the new prefix
                content = content.replace('l_english:', f'{lang_prefix}:')
                # Move the file pointer to the beginning of the file
                file.seek(0)
                file.write(content)
                file.truncate()
            print(f"File '{target_file_path}' succesfully created.")
        except FileNotFoundError:
            print(f"Error: File '{original_file}' not found.")

print("Process finished.")
