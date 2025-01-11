import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

countries = ['European Union', 'Denmark', 'Norway', 'Austria', 'Estonia',
       'Latvia', 'Portugal', 'Spain', 'United Kingdom (Northern Ireland)',
       'France', 'Lithuania', 'Slovenia', 'Ireland', 'Iceland', 'Sweden',
       'Hungary', 'Italy', 'Romania', 'Germany', 'Netherlands',
       'Slovakia', 'Poland', 'Malta', 'Luxembourg', 'Greece', 'Belgium',
       'Bulgaria', 'Finland', 'Czechia', 'Croatia', 'Liechtenstein',
       'Cyprus']

df1 = pd.read_csv("file.csv")

df = df1.dropna(subset = ["Product Authorisation country"])
df2 = df1.dropna()


data = df["Product Authorisation country"].value_counts().reset_index().rename(columns={"count": "Volume of Product", "Product Authorisation country": "Country"})

# Create the choropleth map
choropleth = px.choropleth(
    data,
    locations='Country',
    locationmode='country names',
    color='Volume of Product',
    hover_name='Country',
    color_continuous_scale=px.colors.sequential.Plasma,
    scope='europe',
    title = "Chloropleth Map of Product Volume by Country"
)

# Create the bar chart
bar_chart = px.bar(data, x='Country', y='Volume of Product', title='Bar Chart of Product Volume by Country')



def  main():
    st.set_page_config(
    page_title="Dashboard",
    layout="wide",
    initial_sidebar_state="expanded")

    # Main Interface
    st.markdown("<h1 style='text-align: center; color: black;'> Dashboard </h1>", unsafe_allow_html=True)
    
    st.markdown(
        """
        <style>
        .main {
            background-color: #f0f2f6;
        }
        .reportview-container .main .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        .css-145kmo2.e1fqkh3o3 {
            background-color: #ffffff;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    

    # Create two columns
    col1, col2 = st.columns(2)

    # Place the choropleth chart in the first column
    with col1:
        st.plotly_chart(choropleth, use_container_width=True)

    # Place the bar chart in the second column
    with col2:
        st.plotly_chart(bar_chart, use_container_width=True)
    
    st.write("\n\n\n\n")

    cols1, cols2, cols3 = st.columns(3)
    with cols1:
        st.markdown ("###### Companies Volume of Product across Countries")
        option = st.selectbox(
        "", countries)

    data=df2[df2["Product Authorisation country"] == option]["MAH organisation name"].value_counts().to_frame().reset_index().rename(columns={"count": "Volume of Product", "MAH organisation name": "Company"})
    # Create the bar plot
    fig = px.bar(data, y = "Volume of Product", x = "Company")

    # Update the layout to increase the size
    title = option +" Volume of Product"
    fig.update_layout(
        width=1200,  # Adjust the width as needed
        height=800,
        title= title  # Adjust the height as needed
    )

    st.plotly_chart(fig, use_container_width=True)

   

        
        
    from streamlit.web import cli as stcli
    from streamlit import runtime

import sys

if __name__ == '__main__':
    main()