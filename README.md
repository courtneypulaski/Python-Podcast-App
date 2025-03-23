# Python Podcast App

## Overview
This app takes the RSS feed of a podcast, and outputs the necessary MySQL statements to insert them into two preexisting tables. The SQL to create the tables is also within the app.

## Usage
In order to use this,
1. Run the SQL script of InsertPodcastTables.sql to create the schema and the two tables.
2. Run the app with the URL of a podcast RSS feed as the only command line argument
> <pre>Example: python PodcastApp.py https://rss.art19.com/cat-in-the-hat-cast </pre>
3. The app will ouput into the termal an insert script for the podcast, and an insert script for each episode.
4. Copy the entirety of the SQL scripts, and run them in one go in the MS SQL database that the schema and tables were created in.

## Future Updates
* Write the SQL scripts to a file instead of the terminal
* Have the RSS feed, as well as podcast number, as prompts instead of arguments
* Inserts the podcast data direct to the MySQL databases
* Data can be used to make visualizations
* Hook it up to a webpage?
