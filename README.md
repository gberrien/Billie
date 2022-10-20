# Billie Eilish Sentiment Analysis

## Contents

This Repository contains three main folders and two additional files. 
- The SRC folder contains the main source code of our analysis
- The DATA folder contains the data used in the analysis as well as documentation about the data
- The FIGURES folder contains all figures produced during our analysis
- The LICENSE.md file explains to a visitor the terms under which they may use and cite this repository
- This README.md file serves as an orientation to this repository. 

## Hypothesis
We expect to observe similar sentiments between Billie Eilish’s 2018 Vanity Fair interview and her debut album as well as between her 2021 Vanity Fair interview and her sophomore album, with the 2021 album and interview displaying more positive sentiments than the 2018 album and interview.

## SRC Folder
### Installing/Building Code:
#### FetchTranscript.py:
This python file can be downloaded and imported into any Python compatible IDE. PyCharm was used for this project. The youtube_transript_api module also has to be installed on your local machine to run this program. 

It is recommended to install this module using pip with the following command: *pip install youtube_transcript_api* 

#### WordCloud_Transcripts.py
This python file can be downloaded and imported into any Python compatible IDE. PyCharm was used for this project. The matplotlib.pyplot, wordcloud, numPy, Pillow modules also have to be installed on your local machine to run this program. It is recommended to install these modules using pip with the following commands:

*pip install wordcloud*</br>
*pip install numpy* </br>
*python -m pip install -U matplotlib* </br>
*pip install Pillow* 

The Vanity Fair transcripts and cloud.png also have to be downloaded. These can be found in the Data Folder of this repository. </br>

#### test_articles.py
This python file can be downloaded and imported into any Python compatible IDE. PyCharm was used for this project. The textblob, SentimentIntensityAnalyzer, nltk, and article modeules also have to be installed on your local machine to run this program.  It is recommended to install these modules using pip with the following commands:

*pip install nltk*</br>
*pip install textblob* </br>
*pip install article* 


#### SongLyrics.py
Grace to add directions

#### Vader Analysis.py
Grace to add directions


### Using Code:

#### FetchTranscript.py:
With the proper modules installed this Python file can be ran all at once. It will result in a txt file being created in the same directory as the Python file. The videos from which the transcript is produced can also be changed by changing the video IDs as seen on lines 7 and 8 of the original Python file.

#### WordCloud_Transcripts.py
With the proper modules installed this Python file can be ran all at once. It will result in a Word Cloud png file being created in the same directory as the Python file. Stop words can be added and deleted. The file from which the WordCloud is built from can also be changed when creating the **dataset** variable as seen on line 29 of the original Python file. 

#### test_articles.py
With proper modules installed this Python file can be ran all at once. Using the url of an online article, the article is downloaded as a text file. The outcome of the code will break down the overall sentiment into three percentages that all equate to 100%, one postive, one negative, and one neutral, and then states whether the overall sentiment of the text is positive or negative. 

#### SongLyrics.py
Grace to add directions.

#### Vader Analysis.py
Grace to add directions. 

## DATA Folder
### Data Collection Process:

The transcripts of the 2018 and 2021 Vanity Fair interviews were retrieved using a simple Python program. The program utilized the YoutubeTranscriptApi which is a python API that allows you to get the transcript/subtitles for a given YouTube video. All that is needed to retrieve a transcript for a specific video is the video ID which can be found in the URL for that video. Once the transcripts were retrieved, they were written to text files. This tutorial was utilized as guidance: https://www.youtube.com/watch?v=Z6nkEZyS9nA

See the Python program used to retrieve the transcripts here: https://github.com/gberrien/Billie/blob/main/SRC/FetchTranscript.py

The songs from both albums were downloaded from a python command run by the command prompt, following the instructions given on this site (https://github.com/johnwmillr/LyricsGenius). Song titles were manually entered into the command prompt program, as our computers kept timing out on full album requests. A Genius API CLient ID is necessary to run this code. Once downloaded, a separate python file was used to move the Genius song data to Excel to manually clean it more easily. Once cleaed, the data was moved to txt files to be uploaded onto Github. 

### Data File:
<a href="https://github.com/gberrien/Billie/blob/main/DATA/">DATA folder</a>



### Data Dictionary:
<b>HappierThanEver?.txt :</b> Lyrics from Billie Eilish's song "Happier Than Ever?"  <br>
<b>WhenWeAllFallAsleepWhereDoWeGo?.txt :</b> Lyrics from Billie Eilish's song "When We All Fall Asleep Where Do We Go?"  <br>
<b>VanityFair2018.txt :</b> Text transcripts of Billie Eilish's answers in her 2018 Vanity Fair Interview  <br>
<b>VanityFair2021.txt :</b> Text transcripts of Billie Eilish's answers in her 2021 Vanity Fair Interview  <br>


## Figures Folder
### 1. wordCloud2018VF
This is a WordCloud made from Billie Eilish's 2018 Vanity Fair Interview. Some words that lack sentiment (names, pronouns, conjunctions, etc.) were discluded. This figure gives a broad overview of the commonly used words spoken by Billie as an initial sentiment analysis. 

### 2. wordCloud2021VF
This is a WordCloud made from Billie Eilish's 2021 Vanity Fair Interview. Some words that lack sentiment (names, pronouns, conjunctions, etc.) were discluded. This figure gives a broad overview of the commonly used words spoken by Billie as an initial sentiment analysis. 

### 3. WhenWeFallAsleepWhereDoWeGo_wordcloud
This is a WordCloud made from Billie Eilish's song When We Fall Asleep Where Do We go from her debut Album. Some words that lack sentiment (names, pronouns, conjunctions, etc.) were discluded. This gives a general impression of the lyric make-up of Billie's early career song as an initial sentiment analysis. 

### 4. HappierThanEver_wordcloud
This is a word cloud made from Billie Eilish's song Happier Than Ever from her sophomore album. Some words that lack sentiment (names, pronouns, conjunctions, etc.) were discluded. This gives a general impression of the lyric make-up of Billie's songs later in her career as an initial sentiment analysis. 

### 5. image.png
This is a histogram displaying the net positive sentiment of each song on Billie's album "When We Fall Asleep, Where Do We Go?" The histogram notes two lines. The dotted line represents the median net positive sentiment, found by measuring the sentiment of each song on the album individually. The solid line represents the total album net positive sentiment, which we found by measuring the sentiment of the entire album's lyrics all at once (i.e. all songs from the album combined into one set and measured).

### 6. image.png
This is a histogram displaying the net positive sentiment of each song on Billie's album "Happier Than Ever?" The histogram notes two lines. The dotted line represents the median net positive sentiment, found by measuring the sentiment of each song on the album individually. The solid line represents the total album net positive sentiment, which we found by measuring the sentiment of the entire album's lyrics all at once (i.e. all songs from the album combined into one set and measured).

## References:

[1] A. Bajaj, “Vader sentiment analysis: NLP sentiment analysis using Vader,” Analytics Vidhya, 23-Aug-2022. [Online]. Available: https://www.analyticsvidhya.com/blog/2021/06/vader-for-sentiment-analysis/. [Accessed: 19-Oct-2022]. <br><br>
[2] A. Gustafson, “Billie Eilish's happier than ever: Bedroom production reaches New Heights,” Headliner Magazine. [Online]. Available: https://headlinermagazine.net/billie-eilish-happier-than-ever-bedroom-production-reaches-new-heights.html. [Accessed: 19-Oct-2022]. <br><br>
[3] B. Spanos, “Billie Eilish and the pursuit of happiness,” Rolling Stone, 27-Jun-2021. [Online]. Available: https://www.rollingstone.com/music/music-features/billie-eilish-new-album-happier-than-ever-tour-1183156/. [Accessed: 19-Oct-2022]. <br><br>
[4] Billie Eilish: Same Interview, One Year Apart | Vanity Fair. YouTube, 2018. <br><br>
[5] Billie Eilish: Same Interview, The Fifth Year | Vanity Fair. YouTube, 2021. <br><br>
[6] How to get the transcript of a YouTube video. YouTube, 2021. <br><br>
[7] J. Miller, “Johnwmillr/Lyricsgenius: Download song lyrics and metadata from genius.com 🎶🎤,” GitHub, 2020. [Online]. Available: https://github.com/johnwmillr/LyricsGenius. [Accessed: 19-Oct-2022]. <br><br>
[8] JJ Beck, “How do I concatenate text files in python?,” Stack Overflow, 01-Mar-1960. [Online]. Available: https://stackoverflow.com/questions/13613336/how-do-i-concatenate-text-files-in-python. [Accessed: 19-Oct-2022]. <br><br>
[9] K. Boyini, “Create word cloud using Python,” Tutorials Point, 30-Jul-2019. [Online]. Available: https://www.tutorialspoint.com/create-word-cloud-using-python. [Accessed: 19-Oct-2022]. <br><br>
[10] Simple Sentiment Text Analysis in Python. YouTube, 2020. 

### Prepatory Assignments: 
<a href="https://docs.google.com/document/d/1bkknP33MFT9XR1ovv4hFG8CekbWAAWRUouEA8Xdc-iU/edit?usp=sharing">M1: Hypothesis</a> <br>
<a href="https://docs.google.com/document/d/1rruddvRWK4BdKiVESKXcHqCWTFNkUCupiCY6W-lsPfM/edit?usp=sharing">M2: Establish Data</a> 


### Acknowledgements: 
Thanks to Professor Alonzi for his guidance, wisdom, and inspiration and thanks to Harsh for his expertise each step of the way. And shoutout Billie Eilish for her wonderful music and interviews. 



