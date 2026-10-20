
import os
import shutil
from pathlib import Path

CATEGORIES = {
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Archives": [".zip", ".rar", ".7z", ".tar"],
    "Code": [".py", ".java", ".c", ".cpp", ".html", ".css", ".js"]
}

def get_category(extension):
    for category, extensions in CATEGORIES.items():
        if extension in extensions:
            return category
    return None

def unique_path(path):
    if not path.exists():
        return path

    number = 1
    while True:
        new_path = path.with_name(
            f"{path.stem}_{number}{path.suffix}"
        )
        if not new_path.exists():
            return new_path
        number += 1

def organize_folder(folder):
    folder = Path(folder).expanduser().resolve()

    if not folder.is_dir():
        print("Error: Folder does not exist!")
        return

    moved = 0
    skipped = 0

    for item in folder.iterdir():
        if not item.is_file():
            continue

        if item.resolve() == Path(__file__).resolve():
            continue

        category = get_category(item.suffix.lower())

        if category is None:
            skipped += 1
            continue

        destination_folder = folder / category

        try:
            destination_folder.mkdir(exist_ok=True)
            destination = unique_path(destination_folder / item.name)
            shutil.move(str(item), str(destination))
            print(f"Moved: {item.name} -> {category}/")
            moved += 1

        except (PermissionError, OSError, shutil.Error) as error:
            print(f"Could not move {item.name}: {error}")
            skipped += 1

    print("\n===== ORGANIZER SUMMARY =====")
    print("Files moved:", moved)
    print("Files skipped:", skipped)
    print("Organization completed!")

if __name__ == "__main__":
    print("===== AUTOMATED FILE ORGANIZER =====")
    folder = input("Enter folder path to organize: ").strip().strip('"')
    organize_folder(folder)
