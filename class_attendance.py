# 0 = False
# 1 = True
import pandas as pd
import os

# set file path here
xls_path = "data_subject"
attendance_path = "data_attendance"
# for create sheet
column_header = ['เลขที่', 'รหัสประจำตัว', 'ชื่อ', 'Week1', 'Week2', 'Week3', 'Week4', 'Week5', 'Week6', 'Week7', 'Week8', 'Week9', 'Week10', 'Week11', 'Week12', 'Week13', 'Week14', 'Week15', 'Week16']
final_student_list = []
check_sect = 0

def cleansing_data():

    global check_sect, final_student_list

    for filename in os.listdir(xls_path):
        df = pd.read_excel(os.path.join(xls_path, filename), engine="xlrd", sheet_name="Sheet")
        student_data = df.iloc[:,1:4]
        df_student_list = student_data.values.tolist()
        for number, student_id, student_name in df_student_list :  

            # check sect1 and sect2
            if number == 1:
                check_sect += 1
                if check_sect == 2:
                    # create dataframe sect1
                    df_create1 = pd.DataFrame(final_student_list, columns= column_header)
                    # clear list sect1 for sect2
                    final_student_list = []  

            # if number is int then add number, student_id, student_name to list for create data frame            
            if type(number) is int:
                new_list = [number, student_id, student_name,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                final_student_list.append(new_list)       

        # create excelfile
        name, file_format = os.path.splitext(filename)
        name = f"{name}.xlsx"

        with pd.ExcelWriter(os.path.join(attendance_path, name)) as writer:
            df_create1.to_excel(writer, sheet_name="section1", index=False)

            # Have sect2 create dataframe for sect2 and sheet sect2
            if check_sect == 2:
                df_create2 = pd.DataFrame(final_student_list, columns= column_header)
                df_create2.to_excel(writer, sheet_name="section2", index=False)
    check_sect = 0


# for filename in os.listdir(xlspath):
#     df = pd.read_excel(os.path.join(xlspath, filename), engine="xlrd", sheet_name="Sheet1")
#     # print(df.columns.values.tolist()) 
#     columns = df[list]
#     dict_student = columns.to_dict(orient="records")
#     for i in range(0 , len(dict_student)):
#         dict_student[i][list[2]] = 0
