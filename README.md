# face recognition for class attendance

This project is face recognition for class attendance, developed from Python, use libraries such as [face_recognition](https://github.com/ageitgey/face_recognition), [NumPy](https://numpy.org/), [Scikit-learn](https://scikit-learn.org/), [mediapipe](https://pypi.org/project/mediapipe/), [Pandas](https://pandas.pydata.org/), [OpenCV](https://pypi.org/project/opencv-python/) and developed codebase from [face_recog_tutorial](https://github.com/jsammarco/face_recog_tutorial).


## Authors

- Aussawin Saksawaddikul [(A5hisa)](https://www.github.com/A5hisa)

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
    ├── data                    # Directory for storage face images
    ├── data_attendance         # Storage cleansing data .xlsx file, log file(student_check.log), list_subject.txt 
    ├── raw_data                # Storage base file before cleansing data
```

### General User

1. Directory **data**, face images file should be name with student_id or student_number(It's key for check in class attendace)

2. Directory **data_attendance**, name the xlsx file should be name with subject_id

### Burapha University User

1. Directory **data**, face images file should be name with student_id or student_number(It's key for check in class attendace)

2. Directory **raw_data**, you can download repclasslist.xls in [reg.buu](https://reg.buu.ac.th/) and it's will be cleansing data into **data_attendance** when you run program.


## License

[MIT](https://choosealicense.com/licenses/mit/)