from PIL import Image, ImageDraw

# Open an existing PNG/JPG image as a blank canvas for SVG output
img_path = input("Enter the absolute path of the png or jpg image: ")
image  = Image.open(img_path)   # Replace img_path with your specific image path
draw = ImageDraw.Draw(image)      
# Create font and size for text in the SVG output
font_file  = "arial-black.ttf"
font_size = 18

# Save the content of the opened PNG/JPG image as an SVG with no additional formatting or texts
svg_output_path = '/mnt/Shared/Library/'   # Replace this line with your specific svg output path
image.save(svg_output_path, 'SVG', font_file=font_file, font_size=font_size) 