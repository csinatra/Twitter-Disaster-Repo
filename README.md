# Locate Disasters with Twitter
- What keywords help us classify a tweet as relevant to a disaster?
- How can we best determine where to direct resources towards using the geo coordinates of relevant tweets? 

## Problem Statement
    
### Background

Twitter is a social media platform where users can post and interact with messages known as tweets. We searched tweets using a custom list of search terms relevant to disasters.
    
Keywords are words or phrases which will be used to determine the relevance of a tweet and classify it. There are two classes:

- **On topic:** Tweets that contain keywords relevant to the current disaster.
- **Off topic:** Tweets that contain our search terms but are not referring to the disaster.


### Data Dictionary
| Feature        | Data Type | Description                                                                                                           |
|----------------|-----------|-----------------------------------------------------------------------------------------------------------------------|
| id             | str       | Unique Tweet id returned by the Twitter API                                                                           |
| text           | str       | Text from the Tweet                                                                                                   |
| label_on-topic | bool      | Label based on relatedness to the disaster. Classes are ‘false’ for off-topic or ‘true’ for on-topic                  |
| disaster_type  | str       | Disaster type. Classes are ‘flood’, ‘hurricane’, and ‘tornado’                                                        |
| processed      | str       | Regex cleaned text mapping to lowercase, removing excess whitespace characters, removing links, and removing symbols. |
| tokenized      | str       | List of words from the original Tweet split into single and 2-word tokens                                             |
| lemmatized     | str       | List of tokens converted into their root lemmatized form
    
### Approach
    
**1. Data Collection**

**Train**: From an external source, we gathered a labeled dataset to explore if we could correctly classify a natural disaster based on the contents of a tweet. <br>
    (Source: [CrisisLex Disaster](http://crisislex.org/data-collections.html#CrisisLexT6
))
   
**Test**: Using the Twitter standard tweet search API, we collected tweets using search terms relevant to current disasters and geo coordinates of current disasters. $Xnumber$ tweets were collected from January 6, 2019 - January 16, 2019. We extracted the text and bounding box coordinates. 

**2. Exploratory Data Analysis and Cleaning**

For a better understanding of the data, we performed exploratory data analysis. With the text data, we exercised standard natural language processing techniques such as tokenizing and lemmatizing. Then we split the data into train and test dataset and performed TF-IDF vectorizing.

We want to use TF-IDF to determine which words are most discriminating between tweets. Words that occur frequently are penalized and rare words are given more influence in our model.
- The n-gram range was set with a lower bound of 1 and an upper bound of 2 so that word sequences contain at least one word and up to two words.
- Filter out commonly used words in English.
- Ignore terms that occur in less than 25 documents of the corpus.

**3. Preprocessing and Modeling**
    
**Sandy Hurricane**
- Baseline Model:
    - Accuracy score: 61.33% 
    - If we classify all tweets as being on-topic, we will be predicting correctly 61.33% of the time.
- Random Forest:
    - Accuracy score: 92.49%
    - The accuracy scores are greater than our baseline model of 61.33%.
    - The model is suffering from high variance, with our training score being rougly 4.45% higher than our test score.
- Logistic Regression:
    - Accuracy score: 96.06%
    - The accuracy scores are greater than our baseline model of 61.33% and our Random Forest of 92.49%.
    - The model is still slightly overfitting to the train data because the variance explained from train data is 0.8% higher than the variance explained in the test data.

**Oklahoma Tornado**
- Baseline Model:
    - Accuracy score: 53.84%
    - If we classify all tweets as being on-topic, we will be predicting correctly 53.84% of the time.
- Random Forest:
    - Accuracy score: 93.59%
    - The accuracy scores are greater than our baseline model of 53.83%.
    - The model is still slightly overfitting to the train data because the variance explained from train data is 4.15% higher than the variance explained in the test data.
- Logistic Regression: 
    - Accuracy score: 97.28%
    - The accuracy scores are greater than our baseline model of 53.83%.
    - The model is still slightly overfitting to the train data because the variance explained from train data is 1% higher than the variance explained in the test data.
    
**Alberta Floods and Queensland Flood**
- Baseline Model:
    - Accuracy score: 52.85%
    - If we classify all tweets as being on-topic, we will be predicting correctly 53.84% of the time.
- Random Forest:
    - Accuracy score: 95.95%
    - The accuracy scores are greater than our baseline model of 53.83%.
    - The model is still slightly overfitting to the train data because the variance explained from train data is 2.61% higher than the variance explained in the test data.
- Logistic Regression: 
    - Accuracy score: 97.28%
    - The accuracy scores are greater than our baseline model of 53.83%.
    - The model is still slightly overfitting to the train data because the variance explained from train data is 1% higher than the variance explained in the test data.
    
**All Disasters**
- Baseline Model:
    - Accuracy score: 53.84%
    - If we classify all tweets as being on-topic, we will be predicting correctly 53.84% of the time.
- Random Forest:
    - Accuracy score: 94.42%
    - The accuracy scores are greater than our baseline model of 53.83%.
    - The model is still slightly overfitting to the train data because the variance explained from train data is 4.41% higher than the variance explained in the test data.
- Logistic Regression: 
    - Accuracy score: 98.03%
    - - The accuracy scores are greater than our baseline model of 53.84%.
    - The model is still slightly overfitting to the train data because the variance explained from train data is 0.31% higher than the variance explained in the test data.

**4. Mapping Simulation**

Geo-coordinates are randomly generated for tweets. These tweets are then mapped, with red representing `on-topic` and blue representing `off-topic` to better visualize disaster location.

**5. Proof of Concept**

We query tweets in Malibu, CA and Riverside, CA with flood-related search terms. We cleaned, preprocessed and modeled these raw tweets using the pipeline outlined in previous notebooks.
    
### Model Comparison
    
**Advantages with Random Forest**: The model is more sophisticated and may perform better on less obvious data which can may mean less data preprocessing.
    
**Advantages with Logisitic Regression**:
We can easily determine how likely a tweet will be classified as `on-topic` by taking the exponential of the log odds of words. Even though Random Forest informs us about feature importance, we cannot quickly determine the information gained to classify a tweet as `on-topic`.
    
### Conclusions and Recommendations
Given a training set, we were able to classify disasters with high confidence based on the context of an individual tweet. This is important as given an unseen set of tweets, we are able to identify if a disaster is occuring. We randomly assigned geo coordinates to the training set to simulate a real-life scenario in which first responders would benefit from knowing the specific locations on a map to contain the disaster at hand. 
    
We simulated such process when we gathered real-life flood related tweets. Applying the previously built pipeline for our training data, we classified with high accuracy that a real tweet can be classified into its respective disaster category.
    
### Next Steps
    
There were three areas that we wanted to improve on:

**Lack of recent real world tweet data**: We were unable to find sufficient recent real world disaster tweets from which to test our trained models on. The raw data we were able to collect were not labeled as relevant or not which limited the models we wanted to use.

**Lack of real geo coordinates**: We were unable to gather real geo coordinates. Instead we had generated hypothetical geo coordinates of different weets to mimic a natural disaster. Had we had acccess to the actual geo-coordinates, we could have accurately simulated a disaster through our plot.

**Lack of compute**: With more computing power, we could have scaled our analysis to gather more tweets and run our models handle more tweets and provide a more confident model.
