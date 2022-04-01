# rocks_not_dead

## Contents
0. [Introduction](#introduction)
1. [Installation](#installation) 
2. [Usage](#usage)
3. [Project Architecture](#projectarchitecture)
4. [Platform Imrpovements](#platformimprovements)
5. [Code Quality Improvements](#codequalityimprovements)

<a name="introduction"></a>
## Introduction 

This was made as a PoC for using Python, Terraform, AWS Lambda and AWS S3. 
This takes 12 rock playlists and 12 rap playlists and gathers the data on the albums - year released, name and artist. 
The idea is to gather data weekly to perform BI analytics to see the trend if rock is really dead.

The script can be modified for different use, like seeing patterns in new music being released, by pulling the playlist weekly.

<a name="installation"></a>
## Installation 

#### Pre-Requisites
[Python](https://www.python.org/downloads/), [Terraform](https://www.terraform.io/downloads.html) and [Spotipy](https://spotipy.readthedocs.io/en/2.13.0/).

<a name="usage"></a>
## Usage 
To set up Terraform, run the aws_architecture_plan.sh script, and create the S3 bucket on AWS. 

Run the albums_released_by_year script to save the data as csv and upload it to S3 bucket.

<a name="projectarchitecture"></a>
## Project Architecture 
The Terraform scripts build:
- A lambda function with the analysis code
- A cloudwatch alarm to run that function weekly
- All relevant IAM policies / roles

This will generate a datalake of Spotify data locally and in S3.

<a name="platformimprovements"></a>
## Platform Improvements
- Connect to Airtable

<a name="codequalityimprovements"></a>
## Code Quality Imrpovements