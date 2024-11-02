from .. import linecharts as lc

y1 = [1,1,4,5,1,4,1,9,1,9]
x1 = [1,2,3,4,5,6,7,8,9,10]

y2 = [1,9,1,9,8,1,0,8,9,3]
x2 = [1,2,3,4,5,6,7,8,9,10]

LineChartsExample = lc.LineCharts("x", "y")
LineChartsExample.add(x1, y1, label="homo1")
LineChartsExample.add(x2, y2, label="homo2", style="go--")
LineChartsExample.show()