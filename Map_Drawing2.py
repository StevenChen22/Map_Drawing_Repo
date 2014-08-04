# Copyrigt 2014 (c) Steven Chen
# Draw a map from a CSV using stdin with turtle.

import turtle
import csv
import sys

# Create empty lists
cities = []
roads = []
city_coords = []

# Initialize the turtle and make invisible
turtle.hideturtle()

# Open the file and make it a list of lists
def main(argv):
    user_file = ""
    for opt, arg in opts:
        if opt in ("-i", "--ifile"):
            user_file = arg
    if user_file == "":
        print("No file entered. Program terminating.")
        sys.exit()

map_csv = csv.reader(open(user_file))
for row in map_csv:
    map_data = [[row[0], row[1], row[2], row[3], row[4]] for row in map_csv]

# Split into lists of cities and lists of roads
for i in map_data:
    if i[0] == "c":
        cities.extend([i])
    elif i[0] == "r":
        roads.extend([i])

# Draw the cities
for i in cities:
    name = i[1]
    x_coord = float(i[2])
    y_coord = float(i[3])
    pop = int(i[4])
    city_coords += [[name, x_coord, y_coord]]
    turtle.penup()
    turtle.goto(x_coord + 10, y_coord + 10)
    turtle.write(name)
    turtle.goto(x_coord, y_coord)
    if pop == 0:
        turtle.pendown()
        turtle.circle(0)
        turtle.penup()
    elif pop > 90000:
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(8)
        turtle.end_fill()
        turtle.penup()
    elif pop <= 90000 and pop > 0:
        turtle.pendown()
        turtle.circle(5)
        turtle.penup()

# Draw the roads
for i in roads:
    city_start = i[1]
    city_end = i[2]
    for city_list in city_coords:
        if city_start == city_list[0]:
            road_start_x = float(city_list[1])
            road_start_y = float(city_list[2])
    for city_list in city_coords:
        if city_end == city_list[0]:
            road_end_x = float(city_list[1])
            road_end_y = float(city_list[2])
    turtle.goto(road_start_x, road_start_y)
    turtle.pendown()
    turtle.goto(road_end_x, road_end_y)
    turtle.penup()

# Keeps Screen open until user initiates close
turtle.exitonclick()
