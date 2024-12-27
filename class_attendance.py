# 0 = False
# 1 = True
import pandas as pd
import os

column_header = ['เลขที่', 'รหัสประจำตัว', 'ชื่อ', 'Week1', 'Week2', 'Week3', 'Week4', 'Week5', 'Week6', 'Week7', 'Week8', 'Week9', 'Week10', 'Week11', 'Week12', 'Week13', 'Week14', 'Week15', 'Week16']
list = ["รหัสประจำตัว", "ชื่อ", "Week1"]
xlspath = "data_attendance"
 
# for filename in os.listdir(xlspath):
#     df = pd.read_excel(os.path.join(xlspath, filename), engine="xlrd", sheet_name="Sheet1")
#     # print(df.columns.values.tolist()) 
#     columns = df[list]
#     dict_student = columns.to_dict(orient="records")
#     for i in range(0 , len(dict_student)):
#         dict_student[i][list[2]] = 0

for filename in os.listdir(xlspath):
    df = pd.read_excel(os.path.join(xlspath, filename), engine="xlrd", sheet_name="Sheet")
    sub_df = df.iloc[8:len(df.index) - 1,1:4]
    df_list = sub_df.values.tolist()
    print(df_list)