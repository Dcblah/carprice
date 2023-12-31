import numpy as np
import pandas as pd
import streamlit as st


def app(car_df):
    # Displaying orginal dataset
    st.header("View Data")
    # Add an expander and display the dataset as a static table within the expander.
    st.write(car_df)

    # Display descriptive statistics.
    st.subheader("Columns Description:")
    st.write(car_df.describe())

    # ADD NEW CODE FROM HERE
    # Add a subheader and create three columns. Store the columns in two separate variables.
    beta_col1, beta_col2, beta_col3 = st.beta_columns(3)

    # Add a checkbox in the first column. Display the column names of 'car_df' on the click of checkbox.
    with beta_col1:
        st.write(list(car_df.columns))

    # Add a checkbox in the second column. Display the column data-types of 'car_df' on the click of checkbox.
    with beta_col2:
        st.write(car_df.dtypes)

    # Add a checkbox in the third column followed by a selectbox which accepts the column name whose data needs to be displayed.
    with beta_col3:
        column_data = st.selectbox('Select column', tuple(car_df.columns))
        st.write(car_df[column_data])
