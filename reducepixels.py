from PIL import Image

# Open large template file and calculate reduced size
canvas_expanded = Image.open('template.png')
reduced_size = (canvas_expanded.size[0]//3, canvas_expanded.size[1]//3)
# Get palette colors
canvaspalette = canvas_expanded.getpalette('RGBA')
canvaspalette[3] = 0 # Hacky, but I really don't know why it doesn't give 0. Especially when it's transparent in my editor.
# Create reduced image, blank
canvas = Image.new('P', reduced_size, 0)
canvas.putpalette(canvaspalette, 'RGBA')

# Loop through every 3rd pixel starting on the 2nd of each axis
print("Reducing pixels...")
for x in range(1, canvas_expanded.size[0], 3):
    for y in range(1, canvas_expanded.size[1], 3):
        color = canvas_expanded.getpixel((x, y))
        new_x, new_y = (x-1)//3, (y-1)//3
        # Put pixel on reduced image
        canvas.putpixel((new_x, new_y), color)

canvas.save('canvas.png') # For some reason, when it saves, it adds an extra 11 black colors to the palette. It doesn't appear in the palette until saving.
print("Complete!")