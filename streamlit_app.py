import pandas

my_fruit=pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
streamlit.dataframe(my_fruit)
