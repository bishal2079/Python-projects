# from turtle import Turtle,Screen
from prettytable import PrettyTable
# tur=Turtle()
# print(tur)
# tur.shape("turtle")

# tur.color("red")
# tur.forward(100)
# tur.backward(50)
# my_screen=Screen()
# print(my_screen.canvheight )
# my_screen.exitonclick()
table=PrettyTable()
table.field_names = ["City name", "Area", "Population", "Annual Rainfall"]

# Add rows of data
table.add_rows([
    ["Adelaide", 1295, 1158259, 600.5],
    ["Brisbane", 5905, 1857594, 1146.4],
    ["Darwin", 112, 120900, 1714.7],
    ["Hobart", 1357, 205556, 619.5],
    ["Sydney", 2058, 4336374, 1214.8],
    ["Melbourne", 1566, 3806092, 646.9],
    ["Perth", 5386, 1554769, 869.4],
])
table2=PrettyTable()
table2.add_column("Pokenon Name",["a","b","c"])
table2.add_column("type",["a","b","c"])
# Print the table
table.align="l"
print(table)
table2.align="r"
print(table2)