import pandas as pd
import os
import re
import win32com.client as win32
from markdown import markdown  # Install using `pip install markdown`

# File paths
markdown_file = "Betyg.md"
base_directory = os.path.dirname(os.path.abspath(markdown_file))

# Function to parse Markdown table
def parse_markdown_table(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Find the header line
    header_index = 0
    for i, line in enumerate(lines):
        if line.strip().startswith("|") and line.strip().endswith("|"):
            header_index = i
            break

    # Extract header and data rows
    header_line = [col.strip() for col in lines[header_index].split("|") if col.strip()]
    data_lines = lines[header_index + 2:]  # Skip the header and separator lines

    rows = []
    for line in data_lines:
        if not line.strip().startswith("|") or not line.strip().endswith("|"):
            continue  # Skip non-table lines
        columns = line.split("|")[1:-1]  # Split by '|' and ignore outer boundaries
        if len(columns) != len(header_line):
            print(f"Skipping malformed row: {line.strip()}")
            continue
        rows.append(columns)

    # Build DataFrame
    data = [{header_line[i]: col.strip() for i, col in enumerate(row)} for row in rows]
    return pd.DataFrame(data)

# Function to extract text from linked file and convert Markdown to HTML with custom adjustments
def extract_html_from_link(link):
    file_path = os.path.join(base_directory, link.replace("./", ""))
    with open(file_path, "r", encoding="utf-8") as f:
        markdown_text = f.read()

    # Remove the first header line (e.g., # Title)
    markdown_text = re.sub(r"^# .*?\n", "", markdown_text)

    # Convert Markdown to HTML
    html_content = markdown(markdown_text, extensions=["fenced_code"])

    # Adjust code blocks for better rendering
    html_content = html_content.replace(
        "<code>", "<p><pre style='background-color:#f8f9fa;padding:10px;border-radius:5px;'><code>"
    )
    html_content = html_content.replace("</code>", "</code></pre></p>")

    # Add custom styles for headers and ensure bullets are hidden inside code blocks
    html_content = f"""
    <style>
        h1 {{ font-size: 1.25em; font-weight: bold; }}
        h2 {{ font-size: 1.1em; font-weight: bold; }}
        h3 {{ font-size: 1em; font-weight: bold; }}
        pre {{ font-family: monospace; white-space: pre-wrap; word-wrap: break-word; margin: 10px 0; }}
        pre code {{ display: block; color: #333; }}
        li pre {{ list-style: none; margin: 0; padding-left: 0; }} /* Remove bullets in <li> */
        ul pre {{ list-style: none; margin: 0; padding-left: 0; }}
    </style>
    {html_content}
    """
    return html_content

# Function to format PascalCase name
def format_name(pascal_name):
    separated = re.sub(r'(?<!^)(?=[A-Z])', ' ', pascal_name).strip()
    first_name = separated.split()[0]
    return first_name

# Function to save email as draft or send
def process_email(outlook, recipient, subject, body_html, dry_run):
    mail = outlook.CreateItem(0)
    mail.To = recipient
    mail.Subject = subject
    mail.HTMLBody = body_html  # Set HTML body

    if dry_run:
        mail.Save()  # Save as draft
        print(f"Draft saved for {recipient}: {subject}")
    else:
        mail.Send()

# Main script
def main(dry_run=True):
    # Read and parse the Markdown table
    df = parse_markdown_table(markdown_file)

    # Prepare Outlook instance
    outlook = win32.Dispatch("Outlook.Application")

    # Counter for dry run limit
    dry_run_count = 0
    dry_run_limit = 3

    # Loop through the rows
    for _, row in df.iterrows():
        name_with_link = row["Namn"]
        name = name_with_link.split("[", 1)[1].split("]", 1)[0]  # Extract name from markdown link
        link = name_with_link.split("(", 1)[1].split(")", 1)[0]  # Extract link from markdown link
        name = format_name(name)  # Format PascalCase name
        email = row["email"]
        betyg = row["Betyg"]

        # Adjust grade labels
        if betyg == "G":
            betyg = "Godkänt"
        elif betyg == "IG":
            betyg = "Icke Godkänt"
        elif betyg == "VG":
            betyg = "Väl Godkänt"
        else:
            betyg = "Ej satt"

        # Extract HTML from the linked file
        try:
            presentation_html = extract_html_from_link(link)
        except Exception as e:
            print(f"Error reading linked file for {name}: {e}")
            continue

        # Compose the email
        subject = "Examensarbete"
        body_html = f"""
        <html>
        <body>
            <p>Hej {name},</p>
            {presentation_html}
            <p>Ditt betyg är <strong>{betyg}</strong>.</p>
            <p>God Jul och Gott nytt år,<br>Marcus</p>
        </body>
        </html>
        """
        
        # Send or save the email
        #if dry_run:
        #    if dry_run_count >= dry_run_limit:
        #        print("Dry run limit reached, skipping further emails.")
        #        break
        #    dry_run_count += 1

        process_email(outlook, email, subject, body_html, dry_run)

if __name__ == "__main__":
    main(dry_run=True)  # Set dry_run=False to actually send emails
