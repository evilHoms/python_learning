import pandas

data = pandas.read_csv("/mnt/c/Dev/python_learning/day25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240428.csv")
col = "Primary Fur Color"
c1 = "Gray"
c2 = "Black"
c3 = "Cinnamon"

res = pandas.DataFrame({
    "Fur Color": [c1, c2, c3],
    "Count": [
        len(data[data[col] == c1]),
        len(data[data[col] == c2]),
        len(data[data[col] == c3])
    ]
})

res.to_csv("/mnt/c/Dev/python_learning/day25/output.csv")