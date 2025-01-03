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

def attendance(class_file,section="section1",week="",knowface=""):

    df_attendance = pd.read_excel(os.path.join(attendance_path, class_file),sheet_name=section)
    df_student = df_attendance.iloc[:,1]
    index = df_student.values.tolist()
    
    for key, val in enumerate(index):
        if knowface == str(val):
            df_attendance.at[key,week] = 1

attendance(class_file="24537164.xlsx",section="section1",week="Week1",knowface="65020876")