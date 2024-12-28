# For check attendance
# 0 = False / 1 = True 

import pandas as pd
import os

# set file path here
# xls_path for raw data
xls_path = "raw_data"
# attendance_path for xlsx file to check class attendance
attendance_path = "data_attendance"

# check filename list
checkfile = []

# for dataframe
column_header = ['เลขที่', 'รหัสประจำตัว', 'ชื่อ', 'Week1', 'Week2', 'Week3', 'Week4', 'Week5', 'Week6', 'Week7', 'Week8', 'Week9', 'Week10', 'Week11', 'Week12', 'Week13', 'Week14', 'Week15', 'Week16']
student_list = []
have2section = False

# this function it's use for cleansing data repclasslist.xls in Burapha university
def cleansing_data():

    global student_list, checkfile, have2section

    # collect filename in to checkfile
    for file in os.listdir(attendance_path):
        file, _ = os.path.splitext(file)
        checkfile.append(file)

    for filename in os.listdir(xls_path):
        df = pd.read_excel(os.path.join(xls_path, filename), engine="xlrd")
        get_subject = df.iloc[2,1]
        subject_id = get_subject.split(' ')[2]

        # check data is already cleansing?
        if subject_id not in checkfile: 
            print(f"Cleansing data {filename} subject: {subject_id}")
            # get student data from sheet
            student_data = df.iloc[8:,1:4] # start row8 column B:D
            df_student_list = student_data.values.tolist()
            for number, student_id, student_name in df_student_list :  
                if number == "เลขที่":
                    df_section1 = pd.DataFrame(student_list, columns= column_header)
                    have2section = True
                    student_list = []
                # if number is int then add [number, student_id, student_name and 0] 0 for week1-16 in to list for create data frame            
                if type(number) is int:
                    student = [number, student_id, student_name,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    student_list.append(student)    
            if not have2section:
                df_section1 = pd.DataFrame(student_list, columns= column_header)

            # create excelfile in attendance_path
            namefile = f"{subject_id}.xlsx"
            with pd.ExcelWriter(os.path.join(attendance_path, namefile)) as writer:
                df_section1.to_excel(writer, sheet_name="section1", index=False)
                if have2section:
                    df_section2 = pd.DataFrame(student_list, columns= column_header)
                    df_section2.to_excel(writer, sheet_name="section2", index=False)
                print(f"Create file in folder:{attendance_path} filename:{namefile}\n")

        # set default
        student_list = []
        have2section = False


# for filename in os.listdir(xlspath):
#     df = pd.read_excel(os.path.join(xlspath, filename), engine="xlrd", sheet_name="Sheet1")
#     # print(df.columns.values.tolist()) 
#     columns = df[list]
#     dict_student = columns.to_dict(orient="records")
#     for i in range(0 , len(dict_student)):
#         dict_student[i][list[2]] = 0