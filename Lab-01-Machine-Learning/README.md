# PUSL 3205 – Large Language Models and Generative AI

## Lab 01: Sentiment Analysis Using Traditional Machine Learning (BOW & TF-IDF)

### Objective

To perform sentiment analysis on customer reviews using traditional machine learning techniques. This practical focuses on text preprocessing, feature extraction using Bag of Words (BOW) and TF-IDF, and training machine learning models to classify reviews as positive or negative.

### 1. Dataset Loading and Integration

Used the UCI Sentiment Labelled Sentences Dataset, which contains reviews from three different sources:

- Amazon
- IMDb
- Yelp

Loaded the three text files using Pandas and combined them into a single dataset.

**Dataset details:**
- Total records: 3,000
- Features: Review text and sentiment label
- Positive sentiment: 1
- Negative sentiment: 0

### 2. Text Preprocessing

Applied the following preprocessing steps to clean the review text:

- Converted all text into lowercase.
- Removed numbers, punctuation and special characters using regular expressions.
- Removed extra whitespace.
- Created a new column containing the cleaned text.

Compared the original sentences with the preprocessed sentences to check the changes.

### 3. Exploratory Data Analysis (EDA)

Explored the dataset to understand the differences between positive and negative reviews.

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

Converted the text data into numerical features using two vectorization techniques.

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

Tested the trained Logistic Regression model using four new customer reviews.

Each review was passed through the same preprocessing and BOW transformation steps before making predictions.

**Prediction Results**

| Review | Predicted Sentiment |
|---|---|
| This phone battery lasts forever and the camera is amazing! | Positive |
| Worst restaurant experience ever. The food was cold and tasteless. | Negative |
| The movie was okay, a bit slow in the middle, not great. | Positive |
| Absolutely loved the acting and the storyline! | Positive |

### Conclusion

Successfully completed the sentiment analysis practical using traditional machine learning techniques. Practised text preprocessing, exploratory data analysis, feature extraction using BOW and TF-IDF, and training classification models. The Logistic Regression model achieved an accuracy of 81.17% on the testing dataset.