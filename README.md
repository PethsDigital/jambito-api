# jambito-api

##### A flask api that displays the jamb subject cobination for the course of your choice


[![Programming Language](https://img.shields.io/badge/Language-Python-success?style=flat-square)](https://python.org)

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-success.svg?style=flat-square)](https://github.com/LordGhostX/animeX-v2/pulls)


## Requirements
* Any Operating System (ie. MacOS X, Linux, Windows)
* Any IDE with python installed on your system(ie. Pycharm, VSCode etc)
* Flask
* [openpyxl](https://openpyxl.readthedocs.io/en/stable/)

## Getting started

#### 1. Clone the repo

```sh
$ git clone https://github.com/LordGhostX/animeX-v2.git
$ cd animeX-v2
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
#### 5. Endpoints

* Visiting the '/' endpoint returns all the courses and their required subjects
* Visiting the '/course/<searchItem>' endpoint, where searchItem is a the name of a course or its substring, returns all the courses containing that search item
* Visiting the '/subject/<searchItem>' endpoint returns all the courses that require that particular subject which is parsed into the url

## :heart: Found this project useful?
If you found this project useful or you like what you see, then please consider giving it a :star: on Github and sharing it with your friends via social media.

## 🐛 Bugs/Request
Encounter any problem(s)? feel free to open an issue. If you feel you could make something better, please raise a ticket on Github and I'll look into it. Pull request are also welcome.

