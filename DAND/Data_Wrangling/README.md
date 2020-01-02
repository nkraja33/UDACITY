# Data Wrangling

>About
WeRateDogs is a Twitter account that rates people’s dogs with a humorous comment about the
dog. The account was started in 2015 by college student Matt Nelson, and has received
international media attention both for its popularity and for the attention drawn to social media
copyright law when it was suspended by Twitter for breaking these aforementioned laws.
I have wrangled WeRateDogs twitter data and after analysing the data i found the following
insights and I have plotted for easy understanding.


Please View the "**act_report.pdf** to see the outcome of this project.


> I followed the below 3 methods for to completer this project. Which are called as wrangling steps.

 - Gather
 - Assess
 - Clean

1. Gather

I gathered or loaded data from 3 sources, stored in separate files:

    WeRateDogs Twitter Enhanced archive, Manually downloaded from Udacity classroom
    The image predictions file, programmatically downloaded from the Udacity servers.
    Twitter data for WeRateDogs account, Downloaded using tweepy API

2. Assess

In this section i have verified the data and definied the problems under section Quality and Tidiness

    Quality

    Twitter Archive

        There are 23 rows where the denominator of rating != 10. These entries will have to be removed. these may be geniune tweets. However, these cases only account for a small fraction of the data set and can be set aside for now.
        Multiple rows of where the numerator of rating < 10. This needs to be removed.
        Multiple rows where numerator of rating > 10. These entries will be assessed and removed if not authentic.
        columns names needs to be renamed: "timestamp" to "tweet_timestamp", "text" to "tweet_text", "rating_numerator" to "dog_rating_out_of_ten", "name" to "dog_name".
        Since retweets and replies will be removed, the column "retweeted_status_timestamp" will be removed as it will no longer provide any useful information.
        Remove column "rating_denominator" once all the values that != 10 have been removed since this will no longer provide any useful information.
        Create a single column for dog type.

    Image Prediction

        Rows where the first (i.e. most confident prediction) has a False value for "p1_dog" (i.e. does not correspond to a type of dog) will be removed.
        The "p1" and "p1_conf" columns will be renamed with more explanatory titles.
        The column "jpg_url" will be removed since url data is already contained in the twitter archive data
        The "p2" and "p3" related columns will be removed as I am only using the most likely prediction ("p1") in my analysis
        After removal of "False" entries, the "p1_dog" column will be removed as it will no longer add any valuable information.

    Retweet/Favourite count

        There are some non-numeric values for the "tweet_id" which needs to be removed.

    Tidiness

    Twitter Archive

        There are 181 retweets which need to be removed. This will ensure there are not two rows corresponding to the same tweet, i.e. holding to the definition of tidy data which requires each row to represent a unique entry.
        There are 78 tweet replies which need to be removed. This will ensure there are not two rows corresponding to the same tweet, i.e. holding to the definition of tidy data which requires each row to represent a unique entry.

3. Clean

In this section i have fixed all the quality and tidiness issues, which we observed in Assess section.
