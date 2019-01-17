# <b>Twitter Tweets Emergency Classifying Locator during Disasters
- What keywords help us classify a tweet as relevant to a disaster?
- How can we best determine where to direct resources towards using the geo coordinates of relevant tweets? 

## Problem Statement
    
### Background: 

Twitter is a social media platform where users can post and interact with messages known as tweets. We searched tweets using a custom list of search terms relevant to disasters.
    
Keywords are words or phrases which will be used to determine the relevance of a tweet and classify it. There are two classes:

- <b>On topic: </b>Tweets that contain keywords relevant to the current disaster.
- <b>Off topic: </b>Tweets that contain our search terms but are not referring to the disaster.
    
### Approach:
    
<b>1. Data Collection: <br>

Train:
- From an external source, we gathered a labeled dataset to explore if we could correctly classify a natural disaster based on the contents of a tweet. <br>
    source: (enter URL)
    
Test:    
- Using the Twitter standard tweet search API, we collected tweets using search terms relevant to current disasters and geo coordinates of current disasters. $Xnumber$ tweets were collected from January 6, 2019 - January 16, 2019. We extracted the text and bounding box coordinates. 

<b>2. Exploratory Data Analysis and Cleaning:
- For a better understanding of the data, we performed exploratory data analysis. With the text data, we exercised standard natural language processing techniques such as tokenizing, lemmatizing and count vectorizing.