# For check attendance
# 0 = False / 1 = True 

import pandas as pd
import os
import tkinter as tk
from tkinter import ttk

# set file path here
# xls_path for raw data
xls_path = "raw_data"
# attendance_path for xlsx file to check class attendance
attendance_path = "data_attendance"

# check filename list
data_checkfile = []

# for dataframe
column_header = ['เลขที่', 'รหัสประจำตัว', 'ชื่อ', 'Week1', 'Week2', 'Week3', 'Week4', 'Week5', 'Week6', 'Week7', 'Week8', 'Week9', 'Week10', 'Week11', 'Week12', 'Week13', 'Week14', 'Week15', 'Week16']
student_list = []
have2section = False


# collect filename in to data_checkfile
def checkfile(path=attendance_path):
    for file in os.listdir(path):
        file, _ = os.path.splitext(file)
        data_checkfile.append(file)


# this function it's use for cleansing data repclasslist.xls in Burapha university
def cleansing_data():

    checkfile()

    global student_list, data_checkfile, have2section

    for filename in os.listdir(xls_path):
        df = pd.read_excel(os.path.join(xls_path, filename), engine="xlrd")
        get_subject = df.iloc[2,1]
        subject_id = get_subject.split(' ')[2]

        # check data is already cleansing?
        if subject_id not in data_checkfile: 
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

            # add subject_id to check file if data was cleansing
            data_checkfile.append(subject_id)

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



# check attendance class from knowface
def attendance(class_file,section="section1",week="",knowface=""):
    class_file = f"{class_file}.xlsx"
    df_attendance = pd.read_excel(os.path.join(attendance_path, class_file),sheet_name=section)
    df_student = df_attendance.iloc[:,1]
    index = df_student.values.tolist()
    
    for key, val in enumerate(index):
        if knowface == str(val):
            df_attendance.at[key,week] = 1
            print(df_attendance)
 
# attendance(class_file="24537164",section="section1",week="Week1",knowface="65020876")

# gui

# set up ui
def setup_ui():

    main_ui = tk.Tk()
    main_ui.title("Attendance Program")
    main_ui.geometry("500x500")

    # Menu
    menu_bar = tk.Menu(main_ui, tearoff=0)
    # menu_bar.add_command(label="How to use", command=)

    # title
    title = tk.Label(main_ui, text="Class Attendance with Face Recognition")
    title.config(font=("Arial", 18, "bold"))
    title.pack(pady=10)

    # dropdown class
    dropdown_class = ttk.Combobox(main_ui, values=data_checkfile)
    dropdown_class.pack(pady=10)
    dropdown_class.set("Select a Class")
 
    # dropdown week
    dropdown_week = ttk.Combobox(main_ui, values=column_header[3:])
    dropdown_week.pack(pady=10)
    dropdown_week.set("Select a Week")

    # submit
    def onclick_confirm():
        file_name = dropdown_class.get()
        week = dropdown_week.get()
        if file_name == "Select a Class" or week == "Select a Week":
            file_name = ""
            week = ""
        else:
            main_ui.destroy()
            start_record = True

    # confirm button
    bt_confirm = tk.Button(main_ui, text="Confirm & Start Attendance", command=onclick_confirm)
    bt_confirm.config(font=("Arial", 16))
    bt_confirm.pack(pady=10)

    main_ui.config(menu=menu_bar)
    main_ui.mainloop()

cleansing_data()
setup_ui()