import colorgram

rgb_color = []
colors = colorgram.extract('OIP.jpeg', 30)

for color in colors:
  r = color.rgb.r
  g = color.rgb.g
  b = color.rgb.b
  rgb_color.append((r, g, b))

print(rgb_color)