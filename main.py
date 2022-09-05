import shutil
import pandas as pd
import os

#paths
pdfsPath = (r'')
indexPath = (r"")

df_index = pd.read_csv(indexPath)#, sheet_name='Worksheet')
df_RID_SUBID = pd.DataFrame(df_index, columns = ['Response ID', 'Submission id'])

for file in os.listdir(pdfsPath):
        RIDArray = file.split(".") # splits the filename to isolate the response id
        fileName = RIDArray[0] # sets fileName to the response id
        fileNameArray = fileName.split("-") #further splits the fileName to isolate the number
        RID = fileNameArray[1] #sets RID to the number of the response id
        df_RID_SUBID_find = df_RID_SUBID[df_RID_SUBID['Response ID'] == int(RID)] # finds the response id in the dataframe
        SubIdArray = df_RID_SUBID_find['Submission id'].tolist() #takes the submission id  and puts it into and array
        SubID = SubIdArray[0] # essentially changes the array to a stirng
        os.rename(os.path.join(pdfsPath, file), os.path.join(pdfsPath, str(SubID) + ".pdf")) # renames the pdf from the response id to the submission id
        print("renamed " + str(RID) + " to " + str(SubID))
