# face recognition for class attendance

This project is face recognition for class attendance, developed from Python, use libraries such as [face_recognition](https://github.com/ageitgey/face_recognition), [NumPy](https://numpy.org/), [Scikit-learn](https://scikit-learn.org/), [mediapipe](https://pypi.org/project/mediapipe/), [Pandas](https://pandas.pydata.org/), [OpenCV](https://pypi.org/project/opencv-python/) and developed codebase from [face_recog_tutorial](https://github.com/jsammarco/face_recog_tutorial).

## Documentation

Thai Documentation click [here](https://github.com/A5hisa/face-recognition-beta/blob/main/documentation/README-TH.md)


## Features

- Check class attendance with face recognition
- Data cleansing for Burapha University [reg.buu](https://reg.buu.ac.th/) 
- Log file (for example click [here](https://github.com/A5hisa/face-recognition-beta/blob/main/documentation/log_example.png))
- Save class attendance data with Excel files using Pandas
- Support on windows 11


## Installation

1. Clone repositories

```shell
    $ git clone https://github.com/A5hisa/face-recognition-beta
```

2. Install the required

```shell
    $ pip install -r requirements.txt
```

## Directory Structure & Setup

```bash
    .
    ├── data                    # Directory for storage face images (only .jpg and .png images are supported)
    ├── data_attendance         # Storage cleansing data .xlsx file, log file, list_subject file
    ├── documentation           # Directory for documentation 
    ├── raw_data                # Storage base file before cleansing data (only .xls files)
```

### General User

1. Directory **data**, face image file should be name with student_id or student_number


2. Directory **data_attendance**, name the .xlsx file should be name with subject name or subject id

- for .xlsx file format, you can use in directory **documentation**\format_data_attendance.xlsx
- Example file is in directory **data_attendance** file name 12345678.xlsx


### Burapha University User

1. Directory **data**, face image file should be name with student_id or student_number


2. Directory **raw_data**, you can download repclasslist.xls in [reg.buu](https://reg.buu.ac.th/) and it's will be cleansing data into **data_attendance** when you run program.


**Notice : File name image and Student No in data_attendance file should be the same because it's key for check class attendance.**


## Issues

### Mediapipe DDL Load failed

- You can download [Microsoft Visual C++](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170) 

## Authors

- Aussawin Saksawaddikul [(A5hisa)](https://www.github.com/A5hisa)

## Feedback

If you have any feedback, please reach out to us at saksawaddikul@gmail.com


## License

[MIT](https://choosealicense.com/licenses/mit/)
