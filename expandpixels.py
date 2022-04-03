from PIL import Image

# Open canvas file and calculate expanded size
canvas = Image.open('canvas.png')
expanded_size = (canvas.size[0]*3, canvas.size[1]*3)
# Create expanded image, blank
canvas_expanded = Image.new('RGBA', expanded_size, (0, 0, 0, 0))

# Loop through every pixel
print("Expanding pixels...")
for x in range(canvas.size[0]):
    for y in range(canvas.size[1]):
        color = canvas.getpixel((x, y))
        # Calculate new pixel locations
        new_x, new_y = x*3 + 1, y*3 + 1
        # Put pixel on reduced image
        canvas_expanded.putpixel((new_x, new_y), color)

canvas_expanded.save('template.png')
print("Complete!")