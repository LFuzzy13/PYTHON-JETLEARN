import pygal

chart = pygal.Pie()

chart.title = 'yippie'

chart.add ('A', 30)
chart.add ('B', 35)

chart.render()
