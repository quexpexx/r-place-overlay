from PIL import Image

# Open large template file and calculate reduced size
canvas_expanded = Image.open('template.png')
reduced_size = (canvas_expanded.size[0]//3, canvas_expanded.size[1]//3)
# Create reduced image, blank
canvas = Image.new('RGBA', reduced_size, (0, 0, 0, 0))

# Loop through every 3rd pixel starting on the 2nd of each axis
for x in range(1, canvas_expanded.size[0], 3):
    for y in range(1, canvas_expanded.size[1], 3):
        color = canvas_expanded.getpixel((x, y))
        new_x, new_y = (x-1)//3, (y-1)//3
        # Put pixel on reduced image
        canvas.putpixel((new_x, new_y), color)

canvas.save('canvas.png')