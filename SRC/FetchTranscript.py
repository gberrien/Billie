## Source: https://www.youtube.com/watch?v=Z6nkEZyS9nA

## import
from youtube_transcript_api import YouTubeTranscriptApi

## Get youtube video IDs
ID2021 = '_wNsZEqpKUA'
ID2018 = 'Cm0MGnuRnH0'

## Get transcripts and write them to txt files
outls = []
outls2 = []

tx = YouTubeTranscriptApi.get_transcript(ID2021)
for i in tx:
    outtxt = (i['text'])
    outls.append(outtxt)

    with open("VanityFair2021.txt", "a") as opf:
        opf.write(outtxt + "\n")

tx2 = YouTubeTranscriptApi.get_transcript(ID2018)
for i in tx2:
    outtxt = (i['text'])
    outls2.append(outtxt)

    with open("VanityFair2018.txt", "a") as opf:
        opf.write(outtxt + "\n")
