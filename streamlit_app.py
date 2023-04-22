
import streamlit

import pandas



streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')


streamlit.text('Build your own smoothie')
my_fruit=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit = my_fruit.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit.index),['Avocado','Strawberries'])
fruits_to_show=my_fruit.loc[fruits_selected]

# Display the table on the page
streamlit.dataframe(fruits_to_show)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)

streamlit.header("Fruityvice Fruit Advice!")

streamlit.text(fruityvice_response.json())


# normalize the json format? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# displays data in table format?
streamlit.dataframe(fruityvice_normalized)
