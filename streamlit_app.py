import streamlit
import pandas
streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('Pint of bitter')
streamlit.text('4 eggs')
streamlit.text('Scampi Crisps')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('Fruit')
streamlit.multiselect('Pick some Fruits:', list(my_fruit_list.index),['Avocado','Strawberries'])
streamlit.dataframe(my_fruit_list)


