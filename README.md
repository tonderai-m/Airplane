# Plane Crash Analysis (1920-2024)


## Team Members:

Nichol 
Tonderai Madamba

## Project Overview

This project aims to analyze plane crash data from 1920 to 2024 to identify trends and insights. We will use the aviation accident database from https://www.planecrashinfo.com/database.htm, which includes information on all major civil, commercial, and military aviation accidents resulting in fatalities.

## Data Set

The database includes the following types of accidents:

* Scheduled and non-scheduled passenger airliner accidents
* Cargo, positioning, ferry, and test flight accidents
* Military transport accidents with 10 or more fatalities
* Helicopter accidents with more than 10 fatalities
* Airship accidents involving fatalities
* Accidents involving famous people
* Accidents of noteworthy interest
* Variables of Interest

We will focus on the following variables:

Year/Date: To analyze trends over time.
Location: To identify high-risk areas.
Aircraft Type: To determine if certain aircraft are more prone to accidents.
Fatalities: To assess the severity of accidents and calculate survival rates.
Research Questions

What are the trends in plane crashes by location?
Is there a relationship between fatalities and aircraft type?
How has the volume of crashes changed over time?
What is the overall survival rate, and how does it vary by year and season?
Project Structure

The project is organized into the following parts:

Part 1: ETL (Extract, Transform, Load)

* part_01.ETL: This directory contains all files related to the ETL process.
* part_01.creating_web_scrapper.ipynb: Jupyter notebook to scrape data from the website.
* part_02.preliminary_clean_and_join.ipynb: Notebook for initial data cleaning and joining.
* part_03.Geolocation_Geopy.Pull_Data.ipynb to part_09.Geolocation_Geopy.USA_state.ipynb: Notebooks for geocoding locations and enriching data with country/state information.
* Part 2: EDA (Exploratory Data Analysis)

part_02.EDA: This directory will contain notebooks and files for exploratory data analysis to answer the research questions.
Final Report

Our final report will include:

Descriptive statistics and visualizations of the data.
Analysis of plane crash trends by location, aircraft type, and time period.
Examination of the relationship between fatalities and aircraft type.
Calculation of survival rates and analysis of how they vary by year and season.
Discussion of any noteworthy findings or insights.
We believe that this project will provide valuable insights into the causes and consequences of aviation accidents, and potentially contribute to improving aviation safety in the future.

Getting Started

Clone this repository.
Download the dataset from https://www.planecrashinfo.com/database.htm.
Follow the instructions in the Jupyter notebooks in the respective directories to perform the ETL and EDA processes.
License

This project is licensed under the MIT License. See the LICENSE file for details.
