# Python Podcast App

## Overview
This app takes the RSS feed of a podcast, and outputs the necessary MySQL statements to insert them into two preexisting tables. The SQL to create the tables is also within the app.

## Usage
In order to use this app,
1. Run the SQL script of InsertPodcastTables.sql to create the schema and the two tables.
2. Run the app with a python interpreter
3. Enter an RSS feed of a podcast when prompted.
4. The app will ouput into the termal an insert script for the podcast, and an insert script for each episode, and prompt for another podcast.
5. Enter another RSS feed, or type quit or q to end.
6. Copy the entirety of the SQL scripts, and run them in one go in the MS SQL database that the schema and tables were created in.

## Future Updates
* Write the SQL scripts to a file instead of the terminal
* Inserts the podcast data direct to the MySQL databases
* Data can be used to make visualizations
* Hook it up to a webpage?
