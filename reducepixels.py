from PIL import Image

canvas_file = Image.open('template.png')
canvas_expanded = canvas_file.load()
contracted_size = (canvas_file.size[0]//3, canvas_file.size[1]//3)
canvas = Image.new('RGBA', contracted_size, (0, 0, 0, 0))

for x in range(1, canvas_file.size[0], 3):
    for y in range(1, canvas_file.size[1], 3):
        color = canvas_expanded[x, y]
        new_x, new_y = (x-1)//3, (y-1)//3
        canvas.putpixel((new_x, new_y), color)

canvas.save('canvas.png')