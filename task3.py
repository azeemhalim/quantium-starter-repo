import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc

# the path to the processed_sales file
DATA_PATH = "data/processed_sales.csv"

# load in data
data = pd.read_csv(DATA_PATH)
data = data.sort_values(by="date")

# initialize dash
app = Dash(__name__)

# create the visualization
line_chart = px.line(data, x="date", y="sales", title="Pink Morsel Sales")
visualization = dcc.Graph(
    id="visualization",
    figure=line_chart
)

# create the header
header = html.H1(
    "Pink Morsel Visualizer",
    id="header"
)

# define the app layout
app.layout = html.Div(
    [
        header,
        visualization
    ]
)

# this is only true if the module is executed as the program entrypoint
if __name__ == '__main__':
    app.run(debug=True)
