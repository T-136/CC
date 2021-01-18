from PIL import Image
import pypandoc
import pandas as pd


# im = Image.open("borat.png")
# im.save("test.jpg")

keys = ["a","b","c"]
data = {"a":["a"],"b":["b"], "c":["c"]}


with pd.ExcelWriter('mattest.xlsx') as writer:
    for key in keys: 
        print("schlüsel: ", key)
        print("daten: ", data[key])
        pd.DataFrame(data[key]).to_excel(writer, sheet_name=key, header=None, index=False)

