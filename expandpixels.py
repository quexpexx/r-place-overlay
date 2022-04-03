from PIL import Image

canvas = Image.open('canvas.png')
expanded_size = (canvas.size[0]*3, canvas.size[1]*3)
canvas_expanded = Image.new('RGBA', expanded_size, (0, 0, 0, 0))

for x in range(canvas.size[0]):
    for y in range(canvas.size[1]):
        color = canvas.getpixel((x, y))
        new_x, new_y = x*3 + 1, y*3 + 1
        canvas_expanded.putpixel((new_x, new_y), color)

canvas_expanded.save('template.png')