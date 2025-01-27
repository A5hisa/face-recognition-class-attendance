# face recognition for class attendance

โปรเจคเช็คชื่อนักเรียนหรือนักศึกษาด้วยเทคโนโลยีการจดจำใบหน้า(face recoginition) ถูกพัฒนาด้วย Python และ library ต่าง ๆ ได้แก่ [face_recognition](https://github.com/ageitgey/face_recognition), [NumPy](https://numpy.org/), [Scikit-learn](https://scikit-learn.org/), [mediapipe](https://pypi.org/project/mediapipe/), [Pandas](https://pandas.pydata.org/), [OpenCV](https://pypi.org/project/opencv-python/) และมีโค้ดพื้นฐานมาจาก [face_recog_tutorial](https://github.com/jsammarco/face_recog_tutorial).


## Features

- เช็คชื่อนักเรียนหรือนิสิตผ่านทางกล้องด้วยระบบจดจำใบหน้า
- จัดรูปแบบข้อมูล(Data Cleansing) สำหรับไฟล์ที่ดาวน์โหลดผ่านทางระบบ reg ของมหาวิทยาลัยบูรพา เพื่อให้ง่ายต่อการเช็คชื่อ
- มี Log file สำหรับเช็คข้อมูลย้อนหลัง (ตัวอย่างรูป log file คลิก [ที่นี่](https://github.com/A5hisa/face-recognition-beta/blob/main/documentation/log_example.png))
- บันทึกข้อมูลการเช็คชื่อของนักเรียนหรือนิสิตด้วย Pandas ในรูปแบบของ Excel(.xlsx)


## Installation

1. ทำสำเนา (Clone repositories)

```shell
    $ git clone https://github.com/A5hisa/face-recognition-beta
```

2. ติดตั้ง library ที่จำเป็น (Install the required)

```shell
    $ pip install -r requirements.txt
```

## Directory Structure & Setup

```bash
    .
    ├── data                    # โฟลเดอร์สำหรับเก็บภาพนักเรียนหรือนิสิต(รองรับเฉพาะไฟล์นามสกุล .jpg และ .png เท่านั้น)
    ├── data_attendance         # โฟลเดอร์เก็บไฟล์ข้อมูลของวิชาและรายชื่อนักเรียนหรือนิสิต (.xlsx), log file, และไฟล์รหัสวิชาและรายชื่อวิชาต่าง ๆ(.txt)
    ├── documentation           # โฟลเดอร์สำหรับเก็บเอกสาร 
    ├── raw_data                # โฟลเดอร์สำหรับไฟล์ที่ต้องการจัดรูปแบบข้อมูล(Data Cleansing) ดาวน์โหลดได้ที่ reg ของมหาวิทยาลัยบูรพา(รองรับเฉพาะไฟล์นามสกุล .xls เท่านั้น)
```

### ผู้ใช้ทั่วไป (General User)

1. ในโฟลเดอร์ **data** ให้เก็บภาพนักเรียนหรือนิสิต และตั้งชื่อไฟล์ภาพเป็นรหัสนักเรียนหรือรหัสนิสิต


2. ในโฟลเดอร์ **data_attendance** ให้เก็บไฟล์ข้อมูลรายชื่อนักเรียนหรือนิสิตของแต่ละวิชา(.xlsx)

- สำหรับไฟล์ข้อมูลรายชื่อ(.xlsx) สามารถใช้รูปแบบไฟล์ได้ที่โฟลเดอร์ **documentation** ชื่อไฟล์ format_data_attendance.xlsx
- ตัวอย่างข้อมูลรายชื่อ สามารถดูได้ที่โฟลเดอร์ **data_attendance** ชื่อไฟล์ 12345678.xlsx


### สำหรับมหาวิทยาลัยบูรพา (Burapha University)

1. ในโฟลเดอร์ **data**, ให้เก็บภาพนิสิตและตั้งชื่อไฟล์ภาพเป็นรหัสนิสิต


2. ในโฟลเดอร์ **raw_data**, ผู้ใช้สามารถดาวน์โหลดไฟล์ repclasslist.xls ที่ [reg.buu](https://reg.buu.ac.th/) และเมื่อทำการจัดรูปแบบข้อมูล(Data Cleansing) ข้อมูลของ repclasslist.xls จะถูกย้ายไปอยู่ที่ **data_attendance**


**ข้อควรระวัง : ไฟล์ภาพนิสิตจะต้องเป็นรหัสนิสิต เนื่องจากระบบเช็คชื่อถูกสร้างให้เช็คด้วยรหัสนิสิต หากตั้งชื่อไฟล์ภาพนิสิตด้วยชื่อ ระบบจะไม่สามารถเช็คชื่อได้**

## Authors

- อัศวิน ศักดิ์สวัสดิกุล [(A5hisa)](https://www.github.com/A5hisa)

## Feedback

หากมีข้อเสนอแนะสามารถติดต่อได้ที่ saksawaddikul@gmail.com


## License

[MIT](https://choosealicense.com/licenses/mit/)