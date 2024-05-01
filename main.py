import os
import re
import markdown
from datetime import datetime
import click

@click.command()
@click.argument("markdown_file", type=click.Path(exists=True))
@click.argument("daily_notes_folder", type=click.Path())
def main(markdown_file, daily_notes_folder):
    """
    Parse a Markdown file, extract specific blocks of information, and organize them into daily note files.
    """
    # Read the contents of the Markdown file
    with open(markdown_file, "r") as f:
        markdown_content = f.read()

    # Parse the Markdown file and identify blocks of text that start with an h2 headline followed by text
    blocks = re.split(r"\n(?=\s*## )", markdown_content)
    blocks = [block.strip() for block in blocks if block.strip()]

    # Create the daily notes folder if it doesn't exist
    os.makedirs(daily_notes_folder, exist_ok=True)

    for block in blocks:
        # Extract the timestamp from the h2 headline (in the format YYMMDDHHmm)
        match = re.search(r"## (\d{10})", block)
        if match:
            timestamp = match.group(1)
            date = datetime.strptime(timestamp, "%y%m%d%H%M").strftime("%Y-%m-%d")

            # Create a new file in the daily notes folder with the name YYYY-MM-DD.md if it doesn't already exist
            daily_note_file = os.path.join(daily_notes_folder, f"{date}.md")
            if not os.path.exists(daily_note_file):
                with open(daily_note_file, "w") as f:
                    f.write(f"# {date}\n\n")

            # Append the extracted block to the daily note file
            with open(daily_note_file, "a") as f:
                f.write(f"\n{block}\n\n")

if __name__ == "__main__":
    main()
