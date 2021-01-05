#Arianna Brieva
from plotly.graph_objs import Line, Layout
from plotly import offline
import json
rollval = []
with open('numbers.json', 'w') as f:
    json.dump(rollval, f)
#Maximum and minimum numbers 
max_num = 18
min_num = 3
frqncies = []

while f==open:
    for value in range(min_num, max_num):
        freq = rollval.count(str(value))
        frqncies.append(freq)

x_values = list(range(min_num, max_num))
graph = [Line(x=x_values, y = frqncies)]

x_axis_config ={'title':'Result'}
y_axis_config = {'title':'Frequency of Result'}
a_layout = Layout(title='Results of rolling one D6 10000 times', xaxis=x_axis_config, yaxis = y_axis_config)
offline.plot({'data':graph, 'layout': a_layout}, filename = 'd6.html')