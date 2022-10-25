import sys

# считывание списка из входного потока
lst_in = ["django chto  eto takoe    poryadok ustanovki",
"model mtv   marshrutizaciya funkcii  predstavleniya",
"marshrutizaciya  obrabotka isklyucheniy       zaprosov perenapravleniya"]

for i, row in enumerate(lst_in):
    while row.count("  "):
        row = row.replace("  ", " ")
    print(row.replace(" ", "-"))
