'''
DATASET ONE & TWO [Frances Lai]
Bar graph visualizations of top 100 most influential Marvel characters and all characters in terms of gender (male vs. female) and character alignment (good, bad, neutral). Two bargraphs.
'''

###
#TOP 100 MOST INFLUENTIAL MARVEL CHARACTERS: ALIGNMENT (GOOD VS. BAD VS. NEUTRAL) VS. GENDER (MALE VS. FEMALE)
###
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as ff
import csv
import pandas 

py.sign_in('franceslai', 'f39Jr2qU4zUdh2jpB0WX') 

data = pandas.read_csv('dataset_one.csv')

#splitting up the data by gender and character alignment
good_male = data.loc[(data['ALIGN'] == 'Good Characters') & (data['SEX'] == 'Male Characters')]
good_female = data.loc[(data['ALIGN'] == 'Good Characters') & (data['SEX'] == 'Female Characters')] 
bad_male = data.loc[(data['ALIGN'] == 'Bad Characters') & (data['SEX'] == 'Male Characters')] 
bad_female = data.loc[(data['ALIGN'] == 'Bad Characters') & (data['SEX'] == 'Female Characters')] 
neutral_male = data.loc[(data['ALIGN'] == 'Neutral Characters') & (data['SEX'] == 'Male Characters')]
neutral_female = data.loc[(data['ALIGN'] == 'Neutral Characters') & (data['SEX'] == 'Female Characters')]

male_total = data.loc[(data['SEX'] == 'Male Characters')]
female_total = data.loc[(data['SEX'] == 'Female Characters')]

#sheer numbers graph
trace_good = go.Bar(x=['Male', 'Female'],
                  y=[len(good_male), len(good_female)],
                  name='Good Characters',
                  marker=dict(color='#8fbc8f'))

trace_bad = go.Bar(x=['Male', 'Female'],
                  y=[len(bad_male), len(bad_female)],
                  name='Bad Characters',
                  marker=dict(color='#556b2f'))

trace_neutral = go.Bar(x=['Male', 'Female'],
                  y=[len(neutral_male), len(neutral_female)],
                  name='Neutral Characters',
                  marker=dict(color='gray'))

data = [trace_good, trace_bad, trace_neutral]
layout = {
    'barmode':'group',
    'xaxis': {'title': 'Gender'},
    'yaxis': {'title': 'Number of Characters'},
    'title':'Top 100 Most Influential Characters: Gender vs. Alignment',
    'font': dict(family='Courier New, monospace', size=14, color='#7f7f7f')
}

fig = go.Figure(data=data, layout=layout)
py.iplot({'data': data, 'layout': layout})


###
#ALL MARVEL CHARACTERS: ALIGNMENT (GOOD VS. BAD VS. NEUTRAL) VS. GENDER (MALE VS. FEMALE)
###
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as ff
import csv
import pandas 

py.sign_in('franceslai', 'f39Jr2qU4zUdh2jpB0WX')

data = pandas.read_csv('dataset_two.csv')

#splitting up the data by gender and character alignment
good_male = data.loc[(data['ALIGN'] == 'Good Characters') & (data['SEX'] == 'Male Characters')]
good_female = data.loc[(data['ALIGN'] == 'Good Characters') & (data['SEX'] == 'Female Characters')] 
bad_male = data.loc[(data['ALIGN'] == 'Bad Characters') & (data['SEX'] == 'Male Characters')] 
bad_female = data.loc[(data['ALIGN'] == 'Bad Characters') & (data['SEX'] == 'Female Characters')] 
neutral_male = data.loc[(data['ALIGN'] == 'Neutral Characters') & (data['SEX'] == 'Male Characters')]
neutral_female = data.loc[(data['ALIGN'] == 'Neutral Characters') & (data['SEX'] == 'Female Characters')]

male_total = data.loc[(data['SEX'] == 'Male Characters')]
female_total = data.loc[(data['SEX'] == 'Female Characters')]

#creating the bars 
trace_good = go.Bar(x=['Male', 'Female'],
                  y=[len(good_male), len(good_female)],
                  name='Good Characters',
                  marker=dict(color='#8fbc8f'))

trace_bad = go.Bar(x=['Male', 'Female'],
                  y=[len(bad_male), len(bad_female)],
                  name='Bad Characters',
                  marker=dict(color='#556b2f'))

trace_neutral = go.Bar(x=['Male', 'Female'],
                  y=[len(neutral_male), len(neutral_female)],
                  name='Neutral Characters',
                  marker=dict(color='gray'))

data = [trace_good, trace_bad, trace_neutral]
layout = {
    'barmode':'group',
    'xaxis': {'title': 'Gender'},
    'yaxis': {'title': 'Number of Characters'},
    'title':'All Characters: Gender vs. Alignment',
    'font': dict(family='Courier New, monospace', size=14, color='#7f7f7f')
}

fig = go.Figure(data=data, layout=layout)
py.iplot({'data': data, 'layout': layout})


'''
DATASET ONE & TWO [Joanne Kwon]
Bar graph visualizations of all Marvel characters as well as top 100 influential characters in correlation to gender (male vs. female) and creation over time (from 1939-2013). Four bar graphs. Two relevant bar graph visualizations and two alternative/extra bar graph visualizations.
'''

###
#TOP 100 INFLUENTIAL MARVEL CHARACTERS: GENDER (MALE VS. FEMALE) VS. YEAR CREATED (1939-2013)
###
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as ff
import csv
import pandas 

py.sign_in('joannekwon','ZuInvWFxVlvtE2Qd3Z2q')

metadata=pandas.read_csv('dataset_one.csv')

#split data by year created and gender
year=metadata['Year']
male_year=year.loc[(metadata['SEX']=='Male Characters')]
female_year=year.loc[(metadata['SEX']=='Female Characters')]

#graphing histogram
trace0=go.Histogram(
    x=male_year,
    opacity=0.75,
    xbins=dict(
        start=1935,
        end=1995,
        size=5),
    name='Male Characters',
    marker=dict(color='#99CCFF')
)
trace1=go.Histogram(
    x=female_year,
    opacity=0.75,
    xbins=dict(
        start=1935,
        end=1995,
        size=5),
    name='Female Characters',
    marker=dict(color='#FFCCCC')
)

data=[trace0,trace1]
layout = {
    'barmode':'overlay',
    'xaxis':{'title':'Year Created'},
    'yaxis':{'title':'Number of Characters'},
    'title':'Top 100 Most Influential Characters: Gender vs. Year Created',
    'font':dict(family='Courier New, monospace',size=14,color='#7f7f7f')
}

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='hist1')


###
#ALL MARVEL CHARACTERS: GENDER (MALE VS. FEMALE) VS. YEAR CREATED (1939-2013)
###
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as ff
import csv
import pandas 

py.sign_in('joannekwon','ZuInvWFxVlvtE2Qd3Z2q')

metadata=pandas.read_csv('dataset_two.csv')

#split data by year created and gender
year=metadata['Year']
male_year=year.loc[(metadata['SEX']=='Male Characters')]
female_year=year.loc[(metadata['SEX']=='Female Characters')]

#graphing histogram
trace0=go.Histogram(
    x=male_year,
    opacity=0.75,
    xbins=dict(
        start=1935,
        end=2015,
        size=5),
    name='Male Characters',
    marker=dict(color='#99CCFF')
)
trace1=go.Histogram(
    x=female_year,
    opacity=0.75,
    xbins=dict(
        start=1935,
        end=2015,
        size=5),
    name='Female Characters',
    marker=dict(color='#FFCCCC')
)

data=[trace0,trace1]
layout = {
    'barmode':'overlay',
    'xaxis':{'title':'Year Created'},
    'yaxis':{'title':'Number of Characters'},
    'title':'All Characters: Gender vs. Year Created',
    'font':dict(family='Courier New, monospace',size=14,color='#7f7f7f')
}

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='hist2')


###
#ALL FEMALE MARVEL CHARACTERS: ALIGNMENT (GOOD VS. BAD VS. NEUTRAL) VS. YEAR CREATED (1939-2013)
###
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as ff
import csv
import pandas 

py.sign_in('joannekwon','ZuInvWFxVlvtE2Qd3Z2q')

metadata=pandas.read_csv('dataset_two.csv')

#split data by year created and alignment for female characters
year=metadata['Year']
good_female = year.loc[(metadata['ALIGN']=='Good Characters')&(metadata['SEX']=='Female Characters')] 
bad_female = year.loc[(metadata['ALIGN'] == 'Bad Characters') & (metadata['SEX']=='Female Characters')] 
neutral_female = year.loc[(metadata['ALIGN']=='Neutral Characters')&(metadata['SEX']=='Female Characters')]

#graphing histogram
trace0=go.Histogram(
    x=good_female,
    opacity=0.75,
    xbins=dict(
        start=1935,
        end=2015,
        size=5),
    name='Good Characters',
    marker=dict(color='#FFFF00')
)
trace1=go.Histogram(
    x=bad_female,
    opacity=0.75,
    xbins=dict(
        start=1935,
        end=2015,
        size=5),
    name='Bad Characters',
    marker=dict(color='#7F00FF')
)
trace2=go.Histogram(
    x=neutral_female,
    opacity=0.75,
    xbins=dict(
        start=1935,
        end=2015,
        size=5),
    name='Neutral Characters',
    marker=dict(color='#606060')
)

data=[trace0,trace1,trace2]
layout = {
    'barmode':'overlay',
    'xaxis':{'title':'Year Created'},
    'yaxis':{'title':'Number of Female Characters'},
    'title':'Female Marvel Characters: Alignment vs. Year Created',
    'font':dict(family='Courier New, monospace',size=14,color='#7f7f7f')
}

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='hist3')

###
#ALL MALE MARVEL CHARACTERS: ALIGNMENT (GOOD VS. BAD VS. NEUTRAL) VS. YEAR CREATED (1939-2013)
###
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as ff
import csv
import pandas 

py.sign_in('joannekwon','ZuInvWFxVlvtE2Qd3Z2q')

metadata=pandas.read_csv('dataset_two.csv')

#split data by year and alignment for male characters
year=metadata['Year']
good_male = year.loc[(metadata['ALIGN']=='Good Characters')&(metadata['SEX']=='Male Characters')] 
bad_male = year.loc[(metadata['ALIGN']=='Bad Characters')&(metadata['SEX']=='Male Characters')] 
neutral_male = year.loc[(metadata['ALIGN']=='Neutral Characters')&(metadata['SEX']=='Male Characters')]

#graphing histogram
trace0=go.Histogram(
    x=good_male,
    opacity=0.75,
    xbins=dict(
        start=1935,
        end=2015,
        size=5),
    name='Good Characters',
    marker=dict(color='#FFFF00')
)
trace1=go.Histogram(
    x=bad_male,
    opacity=0.75,
    xbins=dict(
        start=1935,
        end=2015,
        size=5),
    name='Bad Characters',
    marker=dict(color='#7F00FF')
)
trace2=go.Histogram(
    x=neutral_male,
    opacity=0.75,
    xbins=dict(
        start=1935,
        end=2015,
        size=5),
    name='Neutral Characters',
    marker=dict(color='#606060')
)

data=[trace0,trace1,trace2]
layout = {
    'barmode':'overlay',
    'xaxis':{'title':'Year Created'},
    'yaxis':{'title':'Number of Male Characters'},
    'title':'Male Marvel Characters: Alignment vs. Year Created',
    'font':dict(family='Courier New, monospace',size=14,color='#7f7f7f')
}

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='hist4')
