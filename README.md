# NLP Topic Modelling and Classification of Machine Learning Related Patent Documents
The objective of this repo is to explore which industries are seeing the most mentions of machine learning technology in patent filings in the US, and to analyize historical trends to anticipate the future direction of the field.

## Data Source
The data was acquired from public patent documents via the US Patent Organization's PatentsView API. The features used are text data from patent titles, abstract summaries of the patent documents, classification ids, and year filed.

## Model
The modelling task is multi-class unsupervised classification using the LDA method. Depending on the results, other topic modelling methods may be added in the future.
