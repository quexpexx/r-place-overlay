from PIL import Image, ImagePalette

# Open canvas file and calculate expanded size
canvas = Image.open('canvas.png').convert("P", palette=Image.ADAPTIVE)
expanded_size = (canvas.size[0]*3, canvas.size[1]*3)
# Get palette colors
canvaspalette = canvas.getpalette('RGBA')
print(canvaspalette)
canvaspalette[3] = 0 # Hacky, but I really don't know why it doesn't give 0. Especially when it's transparent in my editor.
# Create expanded image, blank
canvas_expanded = Image.new('P', expanded_size, 0)
canvas_expanded.putpalette(canvaspalette, 'RGBA')

# Loop through every pixel
print("Expanding pixels...")
for x in range(canvas.size[0]):
    for y in range(canvas.size[1]):
        color = canvas.getpixel((x, y))
        # Calculate new pixel locations
        new_x, new_y = x*3 + 1, y*3 + 1
        # Put pixel on reduced image
        canvas_expanded.putpixel((new_x, new_y), color)

canvas_expanded.save('template.png') # For some reason, when it saves, it adds an extra 11 black colors to the palette. It doesn't appear in the palette until saving.
print("Complete!")
