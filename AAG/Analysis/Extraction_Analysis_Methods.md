# Methods for Data Collection 
## Twitter 
1. [Twitter API](https://developer.twitter.com) is the best source for collection of data from twitter. 
2. Python Package to use to access twitter API – TweePy (install using ‘pip install tweepy’) - [Tweepy Documentation](http://docs.tweepy.org/en/v3.5.0/)
3. Once we setup/develop models using the REST API we are going to want to stream data from twitter. We can use [this](https://developer.twitter.com/en/docs/tutorials/consuming-streaming-data.html) to get live updates. 

## Facebook
1. Reference: [Medium Article](https://towardsdatascience.com/how-to-use-facebook-graph-api-and-extract-data-using-python-1839e19d6999) to connect to facebook's Graph API. 
2. Make an account [here](https://developers.facebook.com/)
3. [Facebook Developer tools](https://developers.facebook.com/tools/explorer/)
4. Facebook API is becoming very difficult to access especially for public profiles and will require that we register and that apps have capability of protecting the user's extracted information - [Click here for more info](https://developers.facebook.com/docs/public_feed/)


## Instagram 
1.	We can analyse data where there are mentions of certain keywords in captions/comments of publicly available posts 
2.	Hashtags 
3.	Extract location of important posts (to see which post is associated with which location)
4. Instagram Graph API uses is similar to that of Facebook but is again for better suited for business pages. Personal posts are going to be difficult to access according to [this change log](https://www.instagram.com/developer/changelog/) 

## Method for analysing data:
1. TextBlob: Extremely easy to use for NLP. Tokenization, sentiment analysis, n-gram model, POS-Tagging can all be done in less than 3 lines of code. [Documentation here](https://textblob.readthedocs.io/en/dev/)

2. nltk - has everything for nlp  
