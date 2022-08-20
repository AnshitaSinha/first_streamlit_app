import streamlit

streamlit.title('Hello Have a Good Day')
streamlit.header('Gratitude')
streamlit.text('Reading is good')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")



streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index))

streamlit.dataframe(my_fruit_list)
