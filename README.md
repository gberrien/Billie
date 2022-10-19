# Billie
Billie Eilish Sentiment Analysis

## Contents

## Hypothesis

## SRC Folder
### Installing/Building Code:

### Using Code:

## DATA Folder
### Data Collection Process:

The transcripts of the 2018 and 2021 Vanity Fair interviews were retrieved using a simple Python program. The program utilized the YoutubeTranscriptApi which is a python API that allows you to get the transcript/subtitles for a given YouTube video. All that is needed to retrieve a transcript for a specific video is the video ID which can be found in the URL for that video. Once the transcripts were retrieved, they were written to text files. This tutorial was utilized as guidance: https://www.youtube.com/watch?v=Z6nkEZyS9nA

See the Python program used to retrieve the transcripts here: https://github.com/gberrien/Billie/blob/main/SRC/FetchTranscript.py

The songs from both albums were downloaded from a python command run by the command prompt, following the instructions given on this site (https://github.com/johnwmillr/LyricsGenius). Song titles were manually entered into the command prompt program, as our computers kept timing out on full album requests. A Genius API CLient ID is necessary to run this code. Once downloaded, a separate python file was used to move the Genius song data to Excel to manually clean it more easily. Once cleaed, the data was moved to txt files to be uploaded onto Github. 

### Data File:
<a href="https://github.com/gberrien/Billie/blob/main/DATA/">DATA folder</a>



### Data Dictionary:

### Data Context Narrative:

## Figures Folder
### 1. wordCloud2018VF
This is a WordCloud made from Billie Eilish's 2018 Vanity Fair Interview. Some words that lack sentiment (names, pronouns, conjunctions, etc.) were discluded. This figure gives a broad overview of the commonly used words spoken by Billie as an initial sentiment analysis. 

### 2. wordCloud2021VF
This is a WordCloud made from Billie Eilish's 2021 Vanity Fair Interview. Some words that lack sentiment (names, pronouns, conjunctions, etc.) were discluded. This figure gives a broad overview of the commonly used words spoken by Billie as an initial sentiment analysis. 

## References

### Prepatory Assignments: 

### Acknowledgements: 

### References: 

