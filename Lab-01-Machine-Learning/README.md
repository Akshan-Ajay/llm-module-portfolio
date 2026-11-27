# PUSL 3205 – Large Language Models and Generative AI

## Lab 01 – Sentiment Analysis (BOW and TF-IDF)

### Objective

The aim of this lab was to construct a sentiment analysis system using traditional machine learning. Within this, I focussed on text preprocessing, feature creation (Bag of Words and TF-IDF), and construction of models to determine if a customer review was positive or negative.

### 1. Dataset Loading and Integration

I analysed a dataset called the UCI Sentiment Labelled Sentences Dataset comprising of customer reviews from three sources:

- Amazon
- IMDb
- Yelp

I utilised Pandas to load the data and merge it together.

**Dataset details:**
- Total records: 3,000
- Features: Review text and sentiment label
- Positive sentiment: 1
- Negative sentiment: 0

### 2. Text Preprocessing

As part of processing the data, I undertook the following steps to preprocess the customer reviews.

- Converted all text into lowercase.
- Removed numbers, punctuation and special characters using regular expressions.
- Removed extra whitespace.
- Generated a new column containing preprocessed text.

Furthermore, I analysed some original and preprocessed text to observe the effects of text preprocessing.

### 3. Exploratory Data Analysis (EDA)

I analysed my dataset to investigate the customer review data. In particular, I aimed to highlight frequently occurring words within both positive and negative reviews.

- Displayed sample positive and negative reviews.
- Removed common English stop words using NLTK.
- Identified the top 10 most frequent words in each sentiment category.
- Visualised the word frequencies using Seaborn bar charts.

### 4. Dataset Splitting

Separated the cleaned text and sentiment labels into training and testing datasets using `train_test_split()`.

- Training set: 80% (2,400 samples)
- Testing set: 20% (600 samples)
- Used `stratify=y` to maintain the class distribution.
- Set `random_state=42` for reproducibility.

### 5. Feature Extraction

As machine learning systems cannot analyse text directly, I generated numerical features from the customer reviews. Two methods were employed to do this:

**Bag of Words (BOW)**
- Used `CountVectorizer()`.
- Represented text based on word frequency.
- Applied English stop word removal.

**TF-IDF**
- Used `TfidfVectorizer()`.
- Represented words based on their importance in the dataset.
- Applied English stop word removal.

Both vectorizers were fitted using the training data and then used to transform the testing data.

| Representation | Training Matrix Shape |
|---|---|
| BOW | (2400, 4389) |
| TF-IDF | (2400, 4389) |

### 6. Model Training

Trained two machine learning classification models using the BOW features:

- Logistic Regression
- Linear Support Vector Classifier (LinearSVC)

### 7. Model Evaluation

Evaluated the Logistic Regression model using the testing dataset.

**Evaluation Results**

| Metric | Score |
|---|---:|
| Accuracy | 81.17% |
| Precision | 80.86% |
| Recall | 81.67% |
| F1-Score | 81.26% |

Also generated a classification report and confusion matrix to examine the model's predictions.

### 8. Sentiment Prediction on New Reviews

Finally, I analysed four additional customer reviews which had not been included in my original data set. As with my existing data, these were preprocessed and transformed using BOW prior to sentiment prediction.

**Prediction Results**

| Review | Predicted Sentiment |
|---|---|
| This phone battery lasts forever and the camera is amazing! | Positive |
| Worst restaurant experience ever. The food was cold and tasteless. | Negative |
| The movie was okay, a bit slow in the middle, not great. | Positive |
| Absolutely loved the acting and the storyline! | Positive |

### Conclusion

Throughout this lab I developed my knowledge of traditional machine learning based sentiment analysis. I learnt how to preprocess text, undertake exploratory data analysis, and generate features using both BOW and TF-IDF. Furthermore, I constructed models for classifying data.

My Logistic Regression model had an 81.17% test data analysis accuracy. I also learnt how to apply my trained model to analyse the sentiment of new customer reviews.
