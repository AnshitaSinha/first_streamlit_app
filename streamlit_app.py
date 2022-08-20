import streamlit

streamlit.title('Hello Have a Good Day')
streamlit.header('Gratitude')
streamlit.text('Reading is good')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('fruit')
streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])

streamlit.dataframe(my_fruit_list)
