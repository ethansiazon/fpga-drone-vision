from pathlib import Path
from PIL import Image

project_folder = Path(__file__).resolve().parent
image_path = project_folder.parent / "archive" / "Anti-UAV-Tracking-V0" / "video01" / "00001.jpg"

image = Image.open(image_path)

print("Width and height:", image.size)
print("Color mode:", image.mode)

image.show()
