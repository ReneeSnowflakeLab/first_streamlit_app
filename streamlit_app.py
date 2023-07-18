import streamlit
import pandas

my_fruit_list=pandas.read.csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe = (my_fruit_list)

#Let's put a pick list here
streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index))

#Display table on page
streamlit.dataframe(my_fruit_list)


streamlist.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text('🥣  Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale , Spinach & Rocket Smoothy')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
