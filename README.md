# amazon_recommendation
The Amazon Recommendation System is a content-based recommendation system designed to suggest products to users based on their similarity to a selected product. This system leverages product features such as titles, ratings, and other attributes to compute similarities and recommend the most relevant items. The recommendation engine is implemented using Python and Streamlit, making it an interactive and user-friendly web application.
## Dataset
I obtained the dataset from Amazon Reviews 2023. The main challenge I faced was the enormous size of the dataset, which was provided in JSON format. Converting such a large JSON file to CSV was time-consuming. However, I managed to find a solution with a code snippet from ChatGPT that efficiently handled the conversion.

After converting the JSON data to CSV, I extracted a subset containing headphones and related items. To create a comprehensive dataset, I merged the metadata file and the ratings file using a left join. Given the large volume of data, I decided to focus on a sample of 1 million products. Subsequently, I performed data cleaning and exploratory data analysis (EDA) to prepare the dataset for building the recommendation system.

## NLP Implementation
I implemented several NLP steps to enhance the product recommendation system:

* Tokenization: Splitting product descriptions into individual tokens or words to process them effectively.

* Stemming: Reducing words to their root or base form (e.g., "running" to "run") to normalize text and improve matching.

* Vectorization: Converting text data into numerical vectors, such as TF-IDF or word embeddings, to quantify similarity between products.

*Special Word Removal: Removing non-informative or noisy words, such as stopwords or rare terms, to focus on meaningful content.

* Cosine Similarity: Using cosine similarity to compute the similarity between product vectors. This metric measures the cosine of the angle between two vectors in a multidimensional space, indicating their similarity.

These steps collectively enable the system to effectively process and compare product descriptions, allowing it to recommend the most similar products based on textual content.

## Deployment
The deployment of the project is achieved using Streamlit, a powerful Python library for creating interactive web applications. Streamlit simplifies the process of turning data scripts into shareable web apps, making it an ideal choice for deploying machine learning models and data-driven applications.
