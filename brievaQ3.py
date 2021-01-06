# Arianna Brieva
from plotly.graph_objs import Line, Layout
from plotly import offline
import json

with open('numbers.json', 'r') as f:
    roll_value = json.load(f)
# Maximum and minimum numbers
max_num = 6 * 3
min_num = 3 * 1
frequencies = []

# while f == open:
for value in range(min_num, max_num + 1):
    freq = roll_value.count(value)
    frequencies.append(freq)

x_values = list(range(min_num, max_num + 1))
graph = [Line(x=x_values, y=frequencies)]

# inline objects when not necessary
a_layout = Layout(title=f'Results of rolling one D6 {len(roll_value)} times',
                  xaxis={'title': 'Result'},
                  yaxis={'title': 'Frequency of Result'})
offline.plot({'data': graph, 'layout': a_layout}, filename='d6.html')
