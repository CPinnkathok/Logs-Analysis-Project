# Logs Analysis Project

This project is an internal reporting tool that will extract data from a newspaper database to find the most popular three articles, the most popular article authors and the day where more than 1% of the requests led to errors.

## Installation
* Download [Virtual Box](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)
* Download [Vagrant](https://www.vagrantup.com/downloads.html)
* Download the VM Configuration:
	- Fork and clone the repository here: https://github.com/udacity/fullstack-nanodegree-vm
* cd into the fullstack-nanodegree-vm folder and then cd into the vagrant folder
* run the command ``` vagrant up ```
* run the command ``` vagrant ssh ```
* run the command ``` cd /vagrant ```
* The files in this folder mirror the files on your local computer
* Any edits to the folder on your computer will be reflected here

## Get the newspaper data
* Download the newsdata.sql data that can be found [here](https://classroom.udacity.com/nanodegrees/nd004/parts/51200cee-6bb3-4b55-b469-7d4dd9ad7765/modules/c57b57d4-29a8-4c5f-9bb8-5d53df3e48f4/lessons/bc938915-0f7e-4550-a48f-82241ab649e3/concepts/a9cf98c8-0325-4c68-b972-58d5957f1a91)
* Copy the newsdata.sql file to the vagrant directory

## Connect to database
* In your vagrant machine cd into the vagrant folder and run the command: 
```
psql -d news -f newsdata.sql
```
* You can explore the data by connecting to the database via the command: ``` psql -d news ```
* Explore the tables by using ``` \dt ``` or ``` \d table ``` and ``` select ``` commands

## Run the Script
* cd into the folder within the vagrant directory in the vagrant machine that contains the projectone.py file
* Run the command: ``` python projectone.py ```

* Sample output can be seen in the SampleOutput.txt file

## Author
Author is Christine Pinnkathok

## Acknowledgements
I would like to thank the Udacity FullStack Nanodegree course as well as my mentor Tim Nelson for working with me throughout the project. 





















