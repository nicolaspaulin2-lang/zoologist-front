import streamlit as st

"""
# Penguin Guessr
"""

st.markdown(
    """
#### Fill in the following fields with your penguin details in order to predict its' species:
"""
)

title = st.text_input('Island', 'Biscoe, Dream or Torgersen')
number = st.number_input('Bill length (in mm)')
number = st.number_input('Bill depth (in mm)')
number = st.number_input('flipper length (in mm)')
number = st.number_input('body mass (in g)')
title = st.text_input('Sex', 'Male or Female')


"""

## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Of course... The `requests` package 💡

What are the steps to follow in order to call an API ?

1. Which url will you use? Save it in a variable so you can easily change it later...

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
"""
