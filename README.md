# Tjango

This is a collaborative music voting and playing app using Django, React, and the Spotify API.

UI Elements are created using Material UI.

## Project Screenshots
![image](https://user-images.githubusercontent.com/71597829/201571815-70b6e1b4-7b52-423b-8f7e-2acc9bcb2158.png)
![image](https://user-images.githubusercontent.com/71597829/201572915-b7dcd706-4867-4d48-a5f5-41647be37170.png)
![image](https://user-images.githubusercontent.com/71597829/201572990-fdbe5fd0-d80b-4527-9b6e-f3f77f0533cc.png)


## Tech Stack
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff&style=for-the-badge)
![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB)
![React Router](https://img.shields.io/badge/React_Router-CA4245?style=for-the-badge&logo=react-router&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![Material UI](https://img.shields.io/badge/Material%20UI-2196F3?logo=materialdesignicons&logoColor=fff&style=for-the-badge)
![NodeJS](https://img.shields.io/badge/node.js-6DA55F?style=for-the-badge&logo=node.js&logoColor=white)
![Spotify](https://img.shields.io/badge/Spotify-1ED760?style=for-the-badge&logo=spotify&logoColor=white)

## Setup Instructions

### Install Required Python Modules

```bash
pip install -r requirements.txt
```
### Start Web Server

To start the web server you need to run the following sequence of commands.

First cd into your desired tutorial folder (replace x with tutorial number).
```bash 
cd music_controller
```
Next run the django web server.
```bash
python manage.py runserver
```

If you are on Python 3:
```bash
python3 manage.py runserver
```

### [Install Node.js](https://nodejs.org/en/)

### Install Node Modules

First cd into the ```frontend``` folder.
```bash
cd frontend
```
Next install all dependicies.
```bash
npm i
```

### Compile the Front-End

Run the production compile script
```bash
npm run build
```
or for development:
```bash
npm run dev
```
