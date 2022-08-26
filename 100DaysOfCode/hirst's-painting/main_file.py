import colorgram

colors = colorgram.extract("image.jpg", 30)

color_list = []
for color in colors:
    rgb = color.rgb
    color_list.append((rgb.r, rgb.g, rgb.b))

print(color_list)