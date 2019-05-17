######### Import your libraries #######
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import os


####### Set up your app #####
app = dash.Dash(__name__)
server = app.server

app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

###### Import a dataframe #######
df = pd.read_csv("https://raw.githubusercontent.com/austinlasseter/plotly_dash_tutorial/master/00%20resources/titanic.csv")
# variables_list=list(df.columns)
variables_list=['Survived', 'Sex', 'Pclass', 'Embarked']


####### Layout of the app ########
app.layout = html.Div([
    html.H2('Choose a variable to see its value counts'),
    dcc.Dropdown(
        id='dropdown',
        options=[{'label': i, 'value': i} for i in variables_list],
        value=variables_list[0]
    ),
    html.Div(id='display-value')
])


######### Interactive callbacks go here #########
@app.callback(dash.dependencies.Output('display-value', 'children'),
              [dash.dependencies.Input('dropdown', 'value')])
def display_value(value):
    index = list(df[value].value_counts().index)
    values = list(df[value].value_counts().values)
    return 'Categories: {}, Values: {}'.format(index, values)


######### Run the app #########
if __name__ == '__main__':
    app.run_server(debug=True)
