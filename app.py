import pandas as pd
import dash
from dash import dcc, html, Input, Output
import plotly.express as px

# =======================
# Load and prepare data
# =======================
df = pd.read_csv("formatted_sales.csv")
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

# =======================
# Create Dash app
# =======================
app = dash.Dash(__name__)

# =======================
# Layout
# =======================
app.layout = html.Div(
    style={
        "fontFamily": "Segoe UI, Arial",
        "backgroundColor": "#eef2f7",
        "minHeight": "100vh",
        "padding": "30px"
    },
    children=[

        # Header section
        html.Div(
            style={
                "backgroundColor": "#1f3c88",
                "padding": "20px",
                "borderRadius": "12px",
                "marginBottom": "30px",
                "textAlign": "center",
                "color": "white"
            },
            children=[
                html.H1("Pink Morsel Sales Dashboard", style={"margin": "0"}),
                html.P(
                    "Explore regional sales trends before and after the January 2021 price increase",
                    style={"marginTop": "8px", "opacity": "0.9"}
                )
            ]
        ),

        # Main card container
        html.Div(
            style={
                "maxWidth": "1000px",
                "margin": "auto",
                "backgroundColor": "white",
                "borderRadius": "12px",
                "padding": "25px",
                "boxShadow": "0 10px 25px rgba(0,0,0,0.08)"
            },
            children=[

                # Region selector
                html.Div(
                    style={
                        "marginBottom": "20px",
                        "padding": "15px",
                        "backgroundColor": "#f8f9fb",
                        "borderRadius": "8px"
                    },
                    children=[
                        html.Label(
                            "Select Region",
                            style={
                                "fontWeight": "600",
                                "fontSize": "16px",
                                "display": "block",
                                "marginBottom": "10px"
                            }
                        ),
                        dcc.RadioItems(
                            id="region-selector",
                            options=[
                                {"label": " All", "value": "all"},
                                {"label": " North", "value": "north"},
                                {"label": " East", "value": "east"},
                                {"label": " South", "value": "south"},
                                {"label": " West", "value": "west"},
                            ],
                            value="all",
                            inline=True,
                            style={"fontSize": "15px"},
                        ),
                    ]
                ),

                # Graph
                dcc.Graph(id="sales-line-chart")
            ]
        )
    ]
)

# =======================
# Callback
# =======================
@app.callback(
    Output("sales-line-chart", "figure"),
    Input("region-selector", "value")
)
def update_chart(selected_region):
    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["Region"] == selected_region]

    fig = px.line(
        filtered_df,
        x="Date",
        y="Sales",
        labels={
            "Date": "Date",
            "Sales": "Total Sales"
        }
    )

    fig.update_traces(
        line=dict(width=3, color="#1f77b4")
    )

    fig.update_layout(
        title={
            "text": "Pink Morsel Sales Over Time",
            "x": 0.5,
            "font": {"size": 18}
        },
        plot_bgcolor="#ffffff",
        paper_bgcolor="#ffffff",
        margin=dict(l=40, r=40, t=60, b=40),
        xaxis=dict(showgrid=True, gridcolor="#e5e5e5"),
        yaxis=dict(showgrid=True, gridcolor="#e5e5e5"),
    )

    return fig


# =======================
# Run server (CRITICAL)
# =======================
if __name__ == "__main__":
    app.run(debug=True)
