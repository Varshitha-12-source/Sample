#!/usr/bin/env python
# coding: utf-8

# In[5]:


get_ipython().system('python -m pip install dash')



# In[8]:


import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import datetime

# Sample data
data = {
    'Date': pd.date_range(start='2025-01-01', periods=100),
    'Destination': ['Paris', 'London', 'Tokyo', 'New York', 'Sydney'] * 20,
    'Revenue': [500 + i * 5 for i in range(100)],
    'Bookings': [10 + i % 5 for i in range(100)],
    'Mode': ['Flight', 'Train', 'Flight', 'Bus', 'Flight'] * 20,
    'Rating': [4, 5, 3, 4, 5] * 20
}
df = pd.DataFrame(data)

# Initialize Dash app
app = dash.Dash(__name__)
app.title = "Realistic Travel Dashboard"

# Layout
app.layout = html.Div(style={'padding': '20px'}, children=[
    html.H1("Travel Agency Dashboard", style={'textAlign': 'center', 'color': '#2c3e50'}),

    dcc.DatePickerRange(
        id='date-range',
        start_date=df['Date'].min(),
        end_date=df['Date'].max(),
        display_format='YYYY-MM-DD',
        style={'margin': '20px'}
    ),

    html.Div([
        html.Div(id='total-revenue', style={'width': '24%', 'display': 'inline-block', 'padding': '10px'}),
        html.Div(id='total-bookings', style={'width': '24%', 'display': 'inline-block', 'padding': '10px'}),
        html.Div(id='avg-rating', style={'width': '24%', 'display': 'inline-block', 'padding': '10px'}),
        html.Div(id='top-destination', style={'width': '24%', 'display': 'inline-block', 'padding': '10px'}),
    ], style={'display': 'flex'}),

    html.Div([
        dcc.Graph(id='revenue-chart', style={'width': '60%', 'display': 'inline-block'}),
        dcc.Graph(id='mode-pie', style={'width': '40%', 'display': 'inline-block'}),
    ]),

    html.H3("Customer Feedback Summary", style={'marginTop': '30px'}),
    html.Div(id='feedback-text', style={'backgroundColor': '#f9f9f9', 'padding': '10px', 'borderRadius': '8px'})
])

# Callbacks
@app.callback(
    [
        Output('total-revenue', 'children'),
        Output('total-bookings', 'children'),
        Output('avg-rating', 'children'),
        Output('top-destination', 'children'),
        Output('revenue-chart', 'figure'),
        Output('mode-pie', 'figure'),
        Output('feedback-text', 'children')
    ],
    Input('date-range', 'start_date'),
    Input('date-range', 'end_date')
)
def update_dashboard(start_date, end_date):
    dff = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]

    total_rev = dff['Revenue'].sum()
    total_bk = dff['Bookings'].sum()
    avg_rt = round(dff['Rating'].mean(), 2)
    top_dest = dff['Destination'].value_counts().idxmax()

    rev_fig = px.line(dff, x='Date', y='Revenue', title='Revenue Over Time')
    pie_fig = px.pie(dff, names='Mode', title='Travel Mode Distribution')

    feedback = f"Customers gave an average rating of {avg_rt}/5 between {start_date} and {end_date}. \
Top destination: {top_dest}."

    return (
        html.Div([html.H4("Total Revenue"), html.P(f"${total_rev:,}")]),
        html.Div([html.H4("Total Bookings"), html.P(f"{total_bk}")]),
        html.Div([html.H4("Avg. Rating"), html.P(f"{avg_rt}")]),
        html.Div([html.H4("Top Destination"), html.P(f"{top_dest}")]),
        rev_fig,
        pie_fig,
        feedback
    )

# Run
if __name__ == '__main__':
    app.run(debug=True)


# In[ ]:




