import streamlit

streamlit.title('My Parents New Healthy Dinner')

streamlit.header('Breakfast Favroites')
streamlit.text('🥣Omega 3 and Blueberry Oatmeal')
streamlit.text('🥗Kale, Spinach and Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")

#New section to display fruityvice api responce
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json()) # it's just write the data

# Take the json data and normalize it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# Shows the normalize version of data
streamlit.dataframe(fruityvice_normalized)
