import os
import pandas as pd
import xlsxwriter

print ("Program Starts ........")

filepath = "D:\\Work\\NetApp OneDrive\\OneDrive - NetApp Inc\\294915 - ARCH-Identify the unused objects in the system\\Process Extension Scenario.csv"
path = "C:\\Users\\share\\Documents\\CopernicusIsolatedShell\\Projects\\NETAPP_DEV"

df = pd.read_csv(filepath)
#print(df[['Name']])
termToSearchCollection=[]
ui=[]
tempname=' '

def searchterm(str,fname):
    with open(fname,encoding="mbcs") as f:
        if str in f.read():
            return True
        else:
            return False

for line in df['Name']:
    termToSearch = line.replace(".xs","")
    valid = False  
    for root, dirs, files in os.walk(path):
        for name in files:
            if name.endswith(".bo") or name.endswith(".xbo"):
                print('Searching ',termToSearch, ' in ',name )
                
                result = searchterm(termToSearch,os.path.join(root, name))
                if result == True:
                    valid = True
                    ui.append(name)
                    if (tempname != termToSearch):
                        termToSearchCollection.append(termToSearch)
                        tempname = termToSearch
                    else:
                        termToSearchCollection.append(' ')
    if(not valid):
        termToSearchCollection.append(termToSearch)
        ui.append('x')
    ui.append('.')
    termToSearchCollection.append('.')



d = {'Name':termToSearchCollection,"UI":ui}

df = pd.DataFrame.from_dict(d, orient='index')
df = df.transpose()
writer = pd.ExcelWriter('PES.xlsx', engine='xlsxwriter')  # pylint: disable=abstract-class-instantiated
df.to_excel(writer, sheet_name='Sheet1')
writer.save()

print("gig")