def lbs_to_kg(weight):
    return weight * 0.45
def kg_to_lbs(weight):
    return weight / 0.45
from openpyxl.chart import BarChart, Reference
values = Reference(sheet,
           min_row=2,
           max_row=sheet.max_row,
           min_col=4,
           max_col=4,)

chart = BarChart()
chart.add_data(values)
sheet.add_chart(chart,'e2')