import pandas as pd
import os
import tkinter as tk
import webbrowser
from tkinter import ttk, messagebox
import logging

# set file path here
# xls_path for cleansing_data (repclasslist.xls in Burapha university)
# attendance_path for .xlsx file to check class attendance
xls_path = "raw_data"
attendance_path = "data_attendance"

#log file & log config
log = "student_check.log"
logging.basicConfig(filename=os.path.join(attendance_path, log),
                    format='%(asctime)s %(message)s',
                    datefmt="%d-%m-%Y %H:%M:%S",
                    level=logging.INFO)

# check filename list
data_checkfile = []
list_subject = "list_subject.txt"

# dataframe
column_header = ['เลขที่', 'รหัสประจำตัว', 'ชื่อ', 
                 'Week1', 'Week2', 'Week3', 'Week4', 'Week5', 'Week6', 'Week7', 'Week8', 
                 'Week9', 'Week10', 'Week11', 'Week12', 'Week13', 'Week14', 'Week15', 'Week16']
# EN version use this list below
# column_header = ['No', 'Student_No', 'Name', 
#                  'Week1', 'Week2', 'Week3', 'Week4', 'Week5', 'Week6', 'Week7', 'Week8', 
#                  'Week9', 'Week10', 'Week11', 'Week12', 'Week13', 'Week14', 'Week15', 'Week16']
student_list = []
have2section = False


# collect filename in to data_checkfile
def checkfile(path=attendance_path):
    for file in os.listdir(path):
        if file == "list_subject.txt" or file == "student_check.log" :
            pass
        else :
            file, _ = os.path.splitext(file)
            data_checkfile.append(file)


# this function it's use for cleansing data repclasslist.xls in Burapha university
# notice : Files with more than 2 classroom sections are not supported.
def cleansing_data():

    checkfile()

    global student_list, data_checkfile, have2section

    for filename in os.listdir(xls_path):
        df = pd.read_excel(os.path.join(xls_path, filename), engine="xlrd")
        get_subject = df.iloc[2,1]
        subject_id = get_subject.split(' ')[2]
        subject_name = get_subject.split(' ')[4]
        
        # check data is already cleansing?
        if subject_id not in data_checkfile:

            # add to list_subject.txt file 
            with open(os.path.join(attendance_path, list_subject), encoding="utf-8", mode="a") as w_file:
                w_file.write(f"\n{subject_id}, {subject_name}")
            print(f"Cleansing data {filename}, subject: {subject_id}, subject name: {subject_name}")
            logging.info(f"Cleansing data : {filename}")

            # get student data from sheet
            student_data = df.iloc[8:,1:4] # start row8 column B:D
            df_student_list = student_data.values.tolist()
            for number, student_id, student_name in df_student_list :  
                if number == "เลขที่":
                    df_section1 = pd.DataFrame(student_list, columns=column_header)
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
                logging.info(f"Create File! : {attendance_path}\{namefile}")

        # set default
        student_list = []
        have2section = False


# create dataframe by file(subject_id) and section
def read_attendance(class_file,section,week):

    # global for use to another function (attendance, save_attendance)
    global list_check_student, df_attendance, week_read, file_name, sect
    file_name = f"{class_file}.xlsx"
    week_read = week
    sect = section
    try :
        df_attendance = pd.read_excel(os.path.join(attendance_path, file_name),sheet_name=sect)
        df_student = df_attendance.iloc[:,1]
        list_check_student = df_student.values.tolist()
        logging.info(f"File Open! : {file_name}, {sect}")
        return True
    except ValueError as e :
        messagebox.showerror(title="Error", message=e)
        return False


# attendance check with knowface from face_recognition in main
def attendance(knowface="") :
    for index, student_id in enumerate(list_check_student):
        if knowface == str(student_id):
            if df_attendance.at[index,week_read] == 0:
                df_attendance.at[index,week_read] = 1
                print(f"{knowface} check")
                logging.info(f"{knowface}, {week_read}")


# save file from dataframe (use attendance_path, file_name from function read_attendance)
def save_attendance():
    with pd.ExcelWriter(os.path.join(attendance_path, file_name)) as writer:
        df_attendance.to_excel(writer, sheet_name=sect, index=False)
        logging.info(f"File Save! : {file_name}, {sect}")


# Menu function 1
def how_to_use():
    webbrowser.open("https://github.com/A5hisa/face-recognition-beta/blob/main/README.md")

    
# Menu fuction 2 
def open_subject_list():
    ui_subject = tk.Tk()
    ui_subject.title("subject list")

    text = tk.Text(ui_subject, width=40, height=10)
    text.pack(pady=10)

    with open(os.path.join(attendance_path, list_subject), encoding="utf-8", mode="r") as file:
        for line in file:
            text.insert(tk.END, line)

    ui_subject.mainloop()


# ui
def setup_ui():

    cleansing_data()

    main_ui = tk.Tk()
    main_ui.title("Attendance Program")
    main_ui.geometry("500x500")

    # Menu
    menu_bar = tk.Menu(main_ui, tearoff=0)
    menu_bar.add_command(label="How to use", command=how_to_use)
    menu_bar.add_command(label="Subject List", command=open_subject_list)

    # title
    title = tk.Label(main_ui, text="Class Attendance \nWith \nFace Recognition")
    title.config(font=("Arial", 18, "bold"))
    title.pack(pady=20)

    # dropdown class
    dropdown_class = ttk.Combobox(main_ui, values=data_checkfile)
    dropdown_class.pack(pady=20)
    dropdown_class.set("Select a Class")
 
    # dropdown week
    dropdown_week = ttk.Combobox(main_ui, values=column_header[3:])
    dropdown_week.pack(pady=20)
    dropdown_week.set("Select a Week")

    dropdown_sect = ttk.Combobox(main_ui, values=["section1", "section2"])
    dropdown_sect.pack(pady=20)
    dropdown_sect.set("Select a Section")

    # submit
    def onclick_confirm():
        file_get = dropdown_class.get()
        week_get = dropdown_week.get()
        sect_get = dropdown_sect.get()
        if file_get == "Select a Class" or week_get == "Select a Week" or sect_get == "Select a Section":
            file_get = ""
            week_get = ""
            sect_get = ""
        else:
            if read_attendance(class_file=file_get, section=sect_get, week=week_get):
                main_ui.destroy()


    # confirm button
    bt_confirm = tk.Button(main_ui, text="Confirm & Start Attendance", command=onclick_confirm)
    bt_confirm.config(font=("Arial", 16))
    bt_confirm.pack(pady=10)

    main_ui.config(menu=menu_bar)
    main_ui.mainloop()