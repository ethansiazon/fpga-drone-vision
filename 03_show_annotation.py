from pathlib import Path
from PIL import Image, ImageDraw

project_folder = Path(__file__).resolve().parent
archive_folder = project_folder.parent / "archive"

image_path = archive_folder / "Anti-UAV-Tracking-V0" / "video01" / "00001.jpg"
annotation_path = archive_folder / "Anti-UAV-Tracking-V0GT" / "video01_gt.txt"

# The first annotation row belongs to the first frame.
first_line = annotation_path.read_text().splitlines()[0]
x, y, width, height = [int(number) for number in first_line.split()]

print("Annotation row:", first_line.strip())
print("Left:", x, "Top:", y)
print("Width:", width, "Height:", height)

original = Image.open(image_path).convert("RGB")

# Draw on a separate copy so the original pixels stay clean.
preview = original.copy()
draw = ImageDraw.Draw(preview)
draw.rectangle((x, y, x + width, y + height), outline="red", width=4)
preview.show()
