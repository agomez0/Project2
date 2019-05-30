# Project 2

# Topic: Entertainment & Sports

## Group: Angie, Judy, Dylan

## Introduction

The Staples Center, The Coliseum and Dodgers Stadium, all located within the Downtown Los Angeles vicinity, combined host hundreds of events yearly. Home to some of the most iconic teams in their sports and concerts for Grammy-winning artists, these venues attract thousands of people from all over the world. We believe that these popular arenas would attract lots of crimes, such as petty theft, due to the influx of visitors and tourists.

This is due to multiple factors. Many fans and tourists carry large sums of money or other valuables. Also, especially tourists, are vulnerable because they are more likely to be relaxed and off guard while on vacation*. Other studies show that stadiums can lead to an increase in crimes, not necessarily on days of events, but on days that do not have events, when security and police surveillance is lowered. This is because stadiums bring many new people into a neighborhood, and allow criminals in crowds to spot possible targets, which they can act on at a later time**.

We hypothesized that there are more reported crime events in areas immediately surrounding the three venues when compared to other areas within a 1.5 mile radius of each respective Los Angeles venue. We used reported crime data from the LAPD to conduct our research.

* https://popcenter.asu.edu/content/crimes-against-tourists-0
** http://www.flanderstoday.eu/stadiums-and-crime-go-hand-hand-say-ghent-researchers

## How did we do this?

We used reported crime data from the LAPD to conduct our research. We analyzed all crimes that occurred between June 1st, 2018 and December 31st, 2018. The link to the data source is below:

https://data.lacity.org/A-Safe-City/2018-Crime/cg5b-sjhs

## What are our visualizations?

We created three different visualizations to help us either prove or disprove that all three venues have an impact on crime rates in their surrounding areas.

    1. A heat map of all crime incidents in the last 6 months of 2018 within a 1.5 mile radius of each venue.
    2. A plot with 3 lines, one for each venue, that plots the crime count by distance from each venue.
    3. An interactive table that allows users to filter crimes by date, time, etc.

* NOTE: All distances are measured in miles, and rounded to the nearest tenth.

## mySQL Tables

* venues: contains the venues of interest that are located in Los Angeles and their latitude and longitude
* crimes: contains a division of records number, date reported, date occurred, time, area id, area name, crime description, address, latitude, longitude, distance from Staples Center, distance from Coliseum, and distance from Dodger Stadium

## How to run the app locally:

    1. Sign up for a mapbox token at: https://account.mapbox.com/auth/signup/?route-to=%22/access-tokens/%22
    2. Insert mapbox token into the config.py file: ![1-config file](static/js/config.js)
    3. pip install geopy
    4. Insert sql connection settings in the config.js file: ![2-config file](config.py)
    5. Run the crimes_db.sql file to create the database for the data.
    6. Run the etl.py file.
    7. Run the app.py file.
