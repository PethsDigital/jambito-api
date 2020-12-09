# jambito-api

##### A flask api that displays the jamb subject cobination for the course of your choice


[![Programming Language](https://img.shields.io/badge/Language-Python-success?style=flat-square)](https://python.org)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-success.svg?style=flat-square)](https://github.com/olumidayy/jambito-api/pulls)


## Requirements
* Any Operating System (ie. MacOS X, Linux, Windows)
* Any IDE with python installed on your system(ie. Pycharm, VSCode etc)
* Flask

## Getting started

#### 1. Clone the repo

```sh
$ git clone https://github.com/olumidayy/jambito-api.git
$ cd jambito-api
```

#### 2. [Setup and activate a virtual environment](https://programwithus.com/learn-to-code/Pip-and-virtualenv-on-Windows/)

#### 3. Get requirements

```sh
$ pip install -r requirements.txt
```

#### 4. Run the application

```sh
$ python app.py
```
## Endpoints
### Root
Visiting the '/' endpoint returns all the courses and their required subjects
Output: 

```
{
  "results": {
    "ACCOUNTING/ACCOUNTANCY ": {..}
    "ACCOUNTING TECHNOLOGY ": {..},
    "ADULT AND COMMUNITY EDUCATION": {..},
    "ADULT AND NON-FORMAL EDUCATION": {..},
    "ADULT EDUCATION ": {..},
    "ADULT EDUCATION/POLITICAL SCIENCE AND PUBLIC ADMINISTRATION ": {..},
    "ADULT EDUCATION/ECONOMICS AND STATISTICS": {..},
    "ADULT EDUCATION/ENGLISH LITERATURE": {..},
    "ADULT EDUCATION/GEOGRAPHY AND REGIONAL PLANNING": {..},
    ........,
    "WOOD PRODUCTION ENGINEERING": {..},
  }
}
```

### Search by course/field of study
Visiting the '/course/{searchItem}' endpoint, where searchItem is a the name of a course or its substring, returns all the courses containing that search item.

For example, the URL "https://jambito-api.herokuapp.com/course/education", where 'education' is the keyword, gives the output below:

```
{
  "results": {
    "ADULT AND COMMUNITY EDUCATION": {..},
    "ADULT AND NON-FORMAL EDUCATION": {..},
    "ADULT EDUCATION ": {..},
    "ADULT EDUCATION/POLITICAL SCIENCE AND PUBLIC ADMINISTRATION ": {..},
    "ADULT EDUCATION/ECONOMICS AND STATISTICS": {..},
    "ADULT EDUCATION/ENGLISH LITERATURE": {..},
    "ADULT EDUCATION/GEOGRAPHY AND REGIONAL PLANNING": {..},
    "AGRICULTURAL PRODUCTION AND MANAGEMENT SCIENCE AND EDUCATION": {..},
    "AGRICULTURAL SCIENCE AND EDUCATION": {..},
    "AGRICULTURAL TECHNOLOGY AND EDUCATION": {..},
    "AUTO AND MECHANICAL TECHNOLOGY EDUCATION": {..},
    .........,
    "VOCATIONAL INDUSTRIAL EDUCATION": {..},
  }
}
```

### Search by a required subject
Visiting the '/subject/{searchItem}' endpoint returns all the courses that require that particular subject(s) whose code is parsed into the url

For example, the URL "https://jambito-api.herokuapp.com/subjects/1+2", where 1 and 2 are the codes for two subjects, gives the output below:

```
{
  "results" : {
    "ACCOUNTING/ACCOUNTANCY ": {},
    "ACCOUNTING TECHNOLOGY ": {},
    "ACTUARIAL SCIENCE ": {..},
    "AERONAUTIC AND ASTRONAUTIC ENGINEERING": {..},
    "AGRIC BUSINESS": {..},
    "AGRIC COOPERATIVE MANAGEMENT ": {..},
    ...........
    "COMPUTER WITH ELECTRONICS": {..},
    "COMPUTER AND COMMUNICATION ENGINEERING": {..},
    "COMPUTER EDUCATION": {..},
    "COMPUTER ENGINEERING": {..},
    "COMPUTER SCIENCE": {..},
    "COMPUTER SCIENCE AND INFORMATION TECHNOLOGY": {..},
    "COMPUTER SCIENCE AND MATHEMATICS": {..},
    ............,
    "WOOD PRODUCTION ENGINEERING": {..}
  }
}
```

### Get all Subject codes
Visiting the '/codes/subjects' endpoint returns all the subjects and their respective codes
The endpoint gives the output below:

```
{
"1": "Use of English",
"2": "Mathematics",
"3": "Biology",
"4": "Chemistry",
"5": "Commerce",
"6": "Economics",
"7": "Physics",
..........
..........
"22": "Music",
"23": "Yoruba",
"24": "Fine Art",
"25": "Book Keeping",
"26": "Business Methods"
}
```

