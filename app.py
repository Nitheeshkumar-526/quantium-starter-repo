import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

# Load the processed sales data
df = pd.read_csv("formatted_sales.csv")

# Convert Date column to datetime and sort
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

# Create line chart
fig = px.line(
    df,
    x="Date",
    y="Sales",
    title="Pink Morsel Sales Over Time",
    labels={
        "Date": "Date",
        "Sales": "Total Sales"
    }
)

# Initialize Dash app
app = dash.Dash(__name__)

# App layout
app.layout = html.Div(
    children=[
        html.H1("Pink Morsel Sales Visualiser"),
        dcc.Graph(figure=fig)
    ]
)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)

