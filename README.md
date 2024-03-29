# Edge Detection API :rocket: :tada: 

The purpose of this README.md file is to explain the steps required to setup this project in your local environment for testing.

<div align='center'>
  <img src='./Images/response.png' width="500px">
</div>


<div align='center'>
  <img src='./Images/response2.png'>
</div>

### How do I get set up? :pushpin:

* Summary of set up
* Dependencies
* How to run tests

### Requirements ###
* Python


### Setting up ### 

* Create a Virtual environment
```
$ python -m venv env
```
* Clone the project in that directory

* Install dependencies
```
$ pip install -r requirements.txt
```

### Test Locally ###

* On your terminal run

```
$ python app.py
```
Copy the URL http://127.0.0.1:5000/ on Postman or any other API testing tool

### API Parameter ###

* Supply API parameter below
```
file ==> Image you want to detect edges, Image size must not be greater than 2MB
```

#### Example of Edge Detected ####

<img src="Images/2.png" width="1000px"/>
<img src="Images/1.png" width="1000px"/>