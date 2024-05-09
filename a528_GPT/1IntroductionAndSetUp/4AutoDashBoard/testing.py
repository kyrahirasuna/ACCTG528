# Import required libraries
import dash
from dash import html, dcc
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output

# Load the dataset
df = pd.read_csv("Output.csv")
df