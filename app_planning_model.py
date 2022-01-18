# 2022-01-18 Kofi Manful
# An app to help DrSmile estimate future events and revenue

import dash as d
import dash_core_components as dcc
import dash_html_components as dhc
import dash_bootstrap_components as dbc

app=d.Dash(__name__)

pageTitle='Dr Smile Planning Model'
layout_button1=dbc.NavItem(
    children=[
        dbc.NavLink("TopDown",href="#")
    ]
)
layout_button2=dbc.NavItem(
    children=[
        dbc.NavLink("LeftRight",href="#")
    ]
)
navbar=dbc.NavbarSimple(
    children=[layout_button1,layout_button2]
    ,brand=pageTitle
    ,brand_href="#"
    ,fluid=True
    ,color="primary"
    ,dark=True
)
app.layout=dbc.Container(
    children=[navbar]
    ,id="container"
   ,class_name="dash-bootstrap"
)


if __name__ == '__main__':
    app.run_server(debug=True,port="8051")