import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import xlrd
from dash.dependencies import Input, Output

# https://dash.plotly.com/


app = dash.Dash()

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

markdown_text = "40% prósent af kolefnisspori Íslands, utan landnotkunar og skógarræktar, má rekja til Orkunotknar. Vegasamgöngur eru megin uppspretta losunar í orkuflokknum, eða um helmingur af kolefnisfótsporinu!"
# https://ust.is/loft/losun-grodurhusalofttegunda/losun-islands/

# TOdo
# plotta upp Heildar Orku og sýna myndrænt hvað fer mikið í vegasamgöngur
# Segja hvað það þarf mörg tré til að binda kolefnið

val_km = [5, 10, 15, 20, 25, 30, 35, 40, 50]

app.layout = html.Div([
    html.H2("""Hvernig þú hefur áhrif með því að taka þátt í áskoruninni "Hjólum í vinnuna" """),
    dcc.Markdown(children=markdown_text),
    html.Div(
        [
            html.Label(
                "Meðal maðurinn keyrir 25km á dag. Hvað keyrir þú mikið?"),

            dcc.Dropdown(
                id="km",
                options=[{
                    'label': i,
                    'value': i
                } for i in val_km],
                value=25),  # value-ið sem við tökum inn á eftir
        ],
        style={'width': '25%',
               'display': 'inline-block'}),
    dcc.Graph(id='funnel-graph'),
])


@app.callback(
    Output('funnel-graph', 'figure'),
    [Input('km', 'value')])
def update_graph(km):

    # hér gætuð þið þá tengt útreikningana ykkar, ég gerði bara ráð fyrir bíll mengi 160g/km frá orkusetrinu.
    losun = 160
    # Þetta er bara demo fyrir ef áskorunin er að hjóla 3svar í viku, getið svo haft vikurnar og hjóladagana sem input breytu
    vikur = 1
    hjoladagar = 3
    # hvað þú mengar mikið ef þú keyrir alla daga
    mengun_bilar = km*losun*vikur*7
    # Hvað það mengar mikið ef þú hjólar 3 daga í staðinn
    mengun_hjol = km*losun*(vikur*7-hjoladagar)

    trace1 = go.Bar(
        x=["ef þú hjólar", "Ef þú hjólar ekki"], y=[mengun_hjol, mengun_bilar])

    figure = {
        'data': [trace1],
        'layout':
        go.Layout(barmode='stack')
    }

    return figure


if __name__ == '__main__':
    app.run_server(debug=True)
