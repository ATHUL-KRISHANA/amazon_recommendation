import streamlit as st
import pickle
import pandas as pd

df = pickle.load(open('product.pkl', 'rb'))
similarity = pickle.load(open('product_similarity.pkl', 'rb'))
product_lst = df['product_title'].values

def recommendation(product):
    product_index = df.index[df['product_title'] == product][0]
    similar_product = list(enumerate(similarity[product_index]))
    similar_product.sort(key=lambda x: x[-1], reverse=True)
    top_similar = similar_product[1:6]
    result = [df.iloc[i[0], 0] for i in top_similar]
    img_link = [df.iloc[i[0], 3] for i in top_similar]
    avg_rating = [df.iloc[i[0], 1] for i in top_similar]
    total_rating = [df.iloc[i[0], 2] for i in top_similar]

    return result, img_link, avg_rating, total_rating



st.title('Product Recommendation')
selected_product = st.selectbox('Choose any product', product_lst)

if st.button('Recommend'):
    result, img_links, avg_rating, total_rating = recommendation(selected_product)
    for title, img, avg, total in zip(result, img_links, avg_rating, total_rating):
        col1, col2 = st.columns([1, 2])

        with col1:
            st.image(img, width=100)
        with col2:
            st.write(title)
            st.write('RATING:', avg)
            st.write('TOTAL RATINGS:', total)
