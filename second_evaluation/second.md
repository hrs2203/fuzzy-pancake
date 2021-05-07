# Second Evalutation

##  Content List
- Introduction
- About the Project
- Deliveries till now
    - methods used -> citations
    - metric based comparision
    - server side sample
- Plans Ahead

## Introduction
> Web Interface ( ayush )

> What is semantic similarity?

The  task  of  measuring  sentence  similarity  is defined  as  determining  how  similar  the  meanings  of  two sentences are.

> Why is it important?

Today we have an abboundance of text data, but the utilizing this resource if tricky as Computing sentence similarity is not a trivial task, due to the variability of natural language expressions.
If done correctly, this metric could be used to collect, compare and classify large corpus of raw data, which could be utilized efficiently.

Real World Examples:
1. Medical : when a new case comes to an practicionar, he/she can look for similar case in past and get the most clossely ressembeling case and make better decisions.
2. Law : When a new case comes, law firms look over there database for similar cases in past and then stratergise from those case studies. ( Currently used by some firms )

There above examples are a reality but are still kept as an internal tool by organizations, as it brings them a competetive edge.

We wish to present this technology in the hands of general consumer with this platform where individuals and organizations will be able to
1. Collect
2. Compare
3. Classify
Text data, which will accelerate there processes.

Possible Clinet base:
1. Law Firms
2. Hospitals
3. Schools -> checking google form (text) answers automatically
4. Researchers -> collecting news/information from different sources and classifiy them
5. Others.

## About the Product 
FuzzyPancake is a Web based, REST-full service, providing our clinet base with text processing services. The core of our buisness is our ComparisionEngine, which is tuned to compare text sequences and tell how much Semantically Similar these sequences are.

We provide a Web Interface for consumers build around ReactJs and Django and REST-api services for clients who wish to integrate our services into there product. To monitor consumer usage, we provide customers with digital coins, with a pay as you go system. 

Customer can use our universal text comparator or Domain specific models which provides better results for that domain ( Example, twitter text comparisino ).

APIs that we will be providing around the model
1. Text Sequence similarity comparision
2. Text Sequence ranking based on parent query.
3. Text Sequence classification ( using the above two services )


## Progress till now
> Comparision engine ( ME )

### Word Count Semantic Similarity
1. About
The Jaccard similarity index (sometimes called the Jaccard similarity coefficient) compares members for two sets to see which members are shared and which are distinct. It’s a measure of similarity for the two sets of data, with a range from 0% to 100%. The higher the percentage, the more similar the two populations. 

![Jaccards](./jaccard.png)

2. Result

3. Observations
Although it’s easy to interpret, it is extremely sensitive to small samples sizes and may give erroneous results, especially with very small samples or data sets with missing observation.

### Tf-Idf Semantic Similarity
1. About
TF-IDF stands for “Term Frequency — Inverse Document Frequency”. This is a technique to quantify a word in documents, we generally compute a weight to each word which signifies the importance of the word in the document and corpus. This method is a widely used technique in Information Retrieval and Text Mining.
The computer can understand any data only in the form of numerical value. By vectorizing the documents we can further perform multiple tasks such as finding the relevant documents, ranking, clustering and so on.

TF-IDF = Term Frequency (TF) * Inverse Document Frequency (IDF)

> Term Frequency
This measures the frequency of a word in a document. 
> tf(t,d) = count of t in d / number of words in d


> Document Frequency
This measures the importance of document in whole set of corpus. DF is the number of documents in which the word is present. We consider one occurrence if the term consists in the document at least once, we do not need to know the number of times the term is present.
> df(t) = occurrence of t in documents

> Inverse Document Frequency
IDF is the inverse of the document frequency which measures the informativeness of term t. When we calculate IDF, it will be very low for the most occurring words such as stop words (because stop words such as “is” is present in almost all of the documents, and N/df will give a very low value to that word). This finally gives what we want, a relative weightage.

> idf(t) = N/df

For large datasets ( link corpus size 10,000 ) the idf term will explode. to dampen the effect we take log of IDF.

> idf(t) = log(N/(df + 1))

df+1 to avoid division by zero error

By taking a multiplicative value of TF and IDF, we get the TF-IDF score
> tf-idf(t, d) = tf(t, d) * log(N/(df + 1))

#### How we use above


2. Result

3. Observations



### Word Vector Semantic Similarity
1. About



3. Result

4. Observations


### Comparision



### Future plans
#### for 3rd quarter
On Developement side
1. Creation of routes, db layer, an user interface

On Engine side.
1. Experimenting with transformers, and fine tuninng them for our use case.
2. Creating server side scripts for clients to train on there dataset as to provide better result.

#### for 4th quarter
1. Engine and Server side script integration.

### References
Thanks to the amazing research community for providing us with these research
1. ...
2. ...
3. ...