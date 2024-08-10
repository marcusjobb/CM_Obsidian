
import os
from pathlib import Path

# Definiera sökvägar
input_folder = Path('C:/Users/CampusMölndal/IdeaProjects')
output_folder = Path('C:\Git\JINH23\Assignments\Livekod')

# Filtyper att inkludera
file_extensions = ['.md', '.properties', '.env', '.java', '.xml', '.txt']

# Lista för att hålla de relevanta mapparna
relevant_folders = []

# Sök igenom input_folder för att hitta relevanta mappar
for root, dirs, files in os.walk(input_folder):
    if 'demo' in root or 'live' in root:
        relevant_folders.append(root)

print(f"Hittade relevanta mappar: {relevant_folders}")
