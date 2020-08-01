from tkinter import *

root = Tk()

for i in range(9999):
    theLabel = Label(root, text = "God is Great "+ str(i))

theLabel.pack()

root.mainloop()























# import pandas as pd
# import xlsxwriter

# # Create a Pandas dataframe from the data.
# df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})

# # Create a Pandas Excel writer using XlsxWriter as the engine.
# writer = pd.ExcelWriter('pandas_simple.xlsx', engine='xlsxwriter')

# # Convert the dataframe to an XlsxWriter Excel object.
# df.to_excel(writer, sheet_name='Sheet1')

# # Close the Pandas Excel writer and output the Excel file.
# writer.save()



# import xml.etree.ElementTree as ET

# tree = ET.parse('ZOpptyEstBooking.webservice')
# root = tree.getroot()
# # print (root[1])

# # print(root.find('SourceAssociationName'))

# for x in root:
#     print(x.tag)
#     if(x.tag == 'BOView'):
#         for y in x:
#             for z in y:
#                 print(z.tag,z.text)

#     # print (x.find('SourceAssociationName').text)