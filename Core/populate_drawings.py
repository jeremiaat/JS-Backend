import os
import json
from api.models import Drawings
from django.conf import settings

media_path = os.path.join(settings.MEDIA_ROOT, "drawings")
json_file = os.path.join(settings.BASE_DIR, "data_utf8.json")  # adjust path if needed

with open(json_file, encoding="utf-8") as f:
    data = json.load(f)

added = 0
skipped_existing = 0
skipped_missing = 0

for item in data:
    filename = item.get("filename")
    year = int(item.get("year", 2025))
    commissioned = item.get("Commissioned", False)

    image_path = f"drawings/{filename}"

    # Skip if image does not exist
    if not os.path.exists(os.path.join(media_path, filename)):
        print(f"Image not found: {filename}")
        skipped_missing += 1
        continue

    # Skip if record already exists
    if Drawings.objects.filter(image=image_path).exists():
        print(f"Already exists in DB: {filename}")
        skipped_existing += 1
        continue

    # Create new record
    Drawings.objects.create(
        image=image_path,
        year=year,
        Commissioned=commissioned
    )
    added += 1

print(f"\nMigration finished. Added: {added}, Skipped existing: {skipped_existing}, Missing images: {skipped_missing}")
