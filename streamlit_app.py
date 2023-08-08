import streamlit
streamlit.title('My parents new healthy dinner')
streamlit.header('Breakfast Favourites')
streamlit.text('🥣 Omega 3 and Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Bioled Free-Range egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list = pandas.read_csv(" https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

#let's put a picklist so they can pick the fruit they want to include.
streamlit.multiselect("Pick Some Fruits:",list(my_fruit_list.index))

# display the fruits table on the page
streamlit.dataframe(my_fruit_list)
