# Using plotly Library to graph a map.
import plotly.graph_objects as go

# Load data frame.
import pandas as pd

# Connect the sql part.
import mysql.connector

import getpass

# Insert your mysql&connect.
con = mysql.connector.connect(
    host = "localhost",
    user = input("\n\n\n\nEnter username: "), # Fill
    passwd = getpass.getpass("\n\n\n\nEnter your password: "),   # Fill
    database = "animals") #make sure the animals database already exists

frame = pd.read_sql("select * from states", con)

fig = go.Figure(data=go.Choropleth(
    locations=frame['state'], # Spatial coordinates
    z = frame['count'].astype(int), # Data to be color-coded
    locationmode = 'USA-states', # set of locations match entries in `locations`
    colorscale = 'Reds',
    colorbar_title = "Number of Species",
))

fig.update_layout(
    title_text = '2020 US Endangered Species by State',
    geo_scope='usa', # limit map scope to USA
)

con.close() 

with open('index.html', 'w') as f:
    f.write(fig.to_html(include_plotlyjs='cdn'))

