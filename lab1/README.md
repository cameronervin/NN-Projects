# Bias Testing Within Word Embeddings
 
## About this Project

The goal of this project is to explore the age related biases present in both traditional word embeddings such as GloVe but also NLP transformers such as BERT.
 
## Dataset & Dependencies

Our evaluation dataset originates from the Social Security Administration (SSA) website and includes the top 1000 names for each gender for each birth year. Additionally, we used an IMDB Reviews dataset from Kaggle to train our GloVe and BERT models on words that were positive or negative. Additionally, we used the 300 dimension GloVe embedding with 6 Billion parameters.

We use the following Python/JupyterNotebook libraries in our work: 
* TensorFlow and Keras to create our model architecture.
* Hugging Face DistilBERT for our BERT model.
* Scikit-learn for model evaluation and data processing.
* Seaborn and Matplotlib for data visualization.
* Other essential libraries include NumPy, Pandas, and TensorFlow.

 
## Technical Approach

To create our GloVe and BERT models, we performed the following:

GloVe - 
1. Load in the IMDB dataset and the Names dataset
2. Preprocess the IMDB dataset by removing stop words, etc.
3. Load embeddings in with our `load_embeddings(filename)` function
4. Tokenize and pad our IMDB dataset
5. Create the embedding matrix using GloVe and the tokenized corpus text from the IMDB dataset using our `create_embedding_matrix(word_index, embeddings_index, embedding_dim, tokenizer, vocab_size)` function
6. Split the dataset into train and test
7. Build a RNN model including our GloVe embedding as an embedding layer to predict text sentiment
8. Train model

BERT - 
1. Steps 1 & 2 from above
2. Load in the `distil_bert_uncased` Hugging Face DistilBERT model for TensorFlow as well as the AutoTokenizer
3. Tokenize the IMDB dataset separately from before using our `tokenize_text(input, max_len=512)` function
4. Parse the newly created text column into two separate columns of 'input_ids' and 'attention_mask' using our `parsing(text, label)` function
5. Convert our datasets to TensorFlow datasets
6. Define our model architecture using our DistilBERT model as a layer within the model as a whole
7. Train model

Next, we utilized our Names dataset to evaluate the sentiment scores of our respective models by running each Name through the model and calculating a sentiment score using our `add_log_sentiment_scores_to_dataframe(model, dataset, dataframe, col_name)` function. This function calculates the log probability of whether a word is positive or negative. These results are stored in a Pandas DataFrame. Finally, we analyzed if there was a statistical difference between our two models based off the sentiment scores of the two models.
 
## Highlights

* BERT
* Transformers
* NLP
* GloVe pretrained embedding
* Recurrent Neural Network
 
## Conclusion

The generational results of Bert sentiment analysis of names perhaps provides a new window into the feelings between generations: Boomer names (male and female) generally have a negative sentiment, while Greatest Generation male names have a similar negative sentiment, yet Greatest Generation female names have a positive sentiment.


