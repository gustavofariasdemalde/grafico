from pygal import Bar

# Create a chart
chart = Bar(title='Olympic medals')

with open('data/medals.csv') as f:
    for line in f:
        pais, medallas = line.split(",")
        chart.add(pais, int(medallas))

# Display the chart
chart.render_to_file('bar_chart.svg')
