import matplotlib.pyplot as plt

class LineCharts:
    def __init__(self, xlabel:str, ylabel:str):
        self.lines = []
        self.xlabel,self.ylabel = xlabel,ylabel
        
    def add(self, x:set, y:set, label:str, style:str="bo-", alpha:int=1, width:int=1):
        self.lines.append({
            "x": x,
            "y": y,
            "label": label,
            "style": style,
            "alpha": alpha,
            "width": width
        })
        
    def show(self):
        for i in range(len(self.lines)):
            line = self.lines[i-1]
            data_x = line["x"]
            data_y = line["y"]
            data_label = line["label"]
            data_style = line["style"]
            data_alpha = line["alpha"]
            data_width = line["width"]
            plt.plot(data_x, data_y, data_style, alpha=data_alpha, linewidth=data_width, label=data_label)
            for x, y in zip(data_x, data_y):
                plt.text(x, y+0.3, '%.00f' % y, ha='center', va='bottom', fontsize=7.5)
        plt.title(f"{self.xlabel} - {self.ylabel}")
        plt.legend()
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.show()
        
if __name__ == "__main__":
    print("This is a module of FedpyLib.You should read 'example/linecharts.py' to understand the usage.")