CREATE SCHEMA PodcastProject;

CREATE TABLE PodcastProject.Podcast(
PodcastID int PRIMARY KEY,
PodcastName varchar(255),
LastUpdated datetime);

CREATE TABLE PodcastProject.PodcastEpisode(
PodcastID int,
EpisodeID int,
EpisodeName varchar(255),
EpisodeDate date,
EpisodeLink varchar(255),
EpisodeSummary varchar(255),
EpisodeLength varchar(10),
LastUpdated datetime,
PRIMARY KEY (PodcastID,EpisodeID),
FOREIGN KEY (PodcastID) REFERENCES podcast(PodcastID));