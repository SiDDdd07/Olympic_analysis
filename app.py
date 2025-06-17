import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import helper
import preprocessor
import plotly.figure_factory as ff

# Load data
url = "https://drive.google.com/uc?id=1dCuvRZVTiq4RbvtGB--Hsluw4Q_zy2Yc"
df = pd.read_csv(url)
region_df = pd.read_csv('noc_regions.csv')

# Preprocess
df = preprocessor.preprocess(df, region_df)

# Sidebar menu
st.sidebar.title("Olympics Analysis")
st.sidebar.image('data:image/png;base64,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')

user_menu = st.sidebar.radio(
    'Select an Option',
    ('Medal Tally', 'Overall Analysis', 'Country-wise Analysis', 'Athlete wise Analysis')
)

# Medal Tally Section
if user_menu == 'Medal Tally':
    st.sidebar.header("Medal Tally")
    years, country = helper.country_year_list(df)
    selected_year = st.sidebar.selectbox("Select Year", years)
    selected_country = st.sidebar.selectbox("Select Country", country)

    medal_tally = helper.fetch_medal_tally(df, selected_year, selected_country)

    if selected_year == 'Overall' and selected_country == 'Overall':
        st.title("Overall Tally")
    elif selected_year != 'Overall' and selected_country == 'Overall':
        st.title(f"Medal Tally in {selected_year} Olympics")
    elif selected_year == 'Overall' and selected_country != 'Overall':
        st.title(f"{selected_country} overall performance")
    else:
        st.title(f"{selected_country} performance in {selected_year} Olympics")

    st.table(medal_tally)

# Overall Analysis Section
if user_menu == 'Overall Analysis':
    # Basic stats
    editions = df['Year'].nunique() - 1
    cities = df['City'].nunique()
    sports = df['Sport'].nunique()
    events = df['Event'].nunique()
    athletes = df['Name'].nunique()
    nations = df['region'].nunique()

    st.title("Top Statistics")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Editions")
        st.title(editions)
    with col2:
        st.header("Hosts")
        st.title(cities)
    with col3:
        st.header("Sports")
        st.title(sports)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Events")
        st.title(events)
    with col2:
        st.header("Nations")
        st.title(nations)
    with col3:
        st.header("Athletes")
        st.title(athletes)

    # Line charts over time
    nations_over_time = helper.data_over_time(df, 'region')
    fig = px.line(nations_over_time, x="Edition", y="region")
    st.title("Participating Nations over the years")
    st.plotly_chart(fig)

    events_over_time = helper.data_over_time(df, 'Event')
    fig = px.line(events_over_time, x="Edition", y="Event")
    st.title("Events over the years")
    st.plotly_chart(fig)

    athlete_over_time = helper.data_over_time(df, 'Name')
    fig = px.line(athlete_over_time, x="Edition", y="Name")
    st.title("Athletes over the years")
    st.plotly_chart(fig)

    # Heatmap of events
    st.title("No. of Events over time (Every Sport)")
    fig, ax = plt.subplots(figsize=(20, 20))
    temp_df = df.drop_duplicates(['Year', 'Sport', 'Event'])
    heatmap_data = temp_df.pivot_table(index='Sport', columns='Year', values='Event', aggfunc='count')
    sns.heatmap(heatmap_data.fillna(0).astype(int), annot=True, ax=ax)
    st.pyplot(fig)
    # Most successful athletes
    st.title("Most Successful Athletes")
    sport_list = df['Sport'].dropna().unique().tolist()
    sport_list.sort()
    sport_list.insert(0, 'Overall')
    selected_sport = st.selectbox('Select a Sport', sport_list)

    top_athletes = helper.most_successful(df, selected_sport)
    st.table(top_athletes)



if user_menu == 'Country-wise Analysis':

    st.sidebar.title('Country-wise Analysis')

    country_list = df['region'].dropna().unique().tolist()
    country_list.sort()

    selected_country = st.sidebar.selectbox('Select a Country',country_list)

    country_df = helper.yearwise_medal_tally(df,selected_country)
    fig = px.line(country_df, x="Year", y="Medal")
    st.title(selected_country + " Medal Tally over the years")
    st.plotly_chart(fig)

    st.title(selected_country + " excels in the following sports")
    pt = helper.country_event_heatmap(df, selected_country)
    fig, ax = plt.subplots(figsize=(20, 20))
    ax = sns.heatmap(pt, annot=True)
    st.pyplot(fig)

    st.title("Top 10 athletes of " + selected_country)
    top10_df = helper.most_successful_countrywise(df, selected_country)
    st.table(top10_df)



if user_menu == 'Athlete wise Analysis':
    athlete_df = df.drop_duplicates(subset=['Name', 'region'])

    x1 = athlete_df['Age'].dropna()
    x2 = athlete_df[athlete_df['Medal'] == 'Gold']['Age'].dropna()
    x3 = athlete_df[athlete_df['Medal'] == 'Silver']['Age'].dropna()
    x4 = athlete_df[athlete_df['Medal'] == 'Bronze']['Age'].dropna()

    fig = ff.create_distplot([x1, x2, x3, x4], ['Overall Age', 'Gold Medalist', 'Silver Medalist', 'Bronze Medalist'],show_hist=False, show_rug=False)
    fig.update_layout(autosize=False,width=1000,height=600)
    st.title("Distribution of Age")
    st.plotly_chart(fig)

    x = []
    name = []
    famous_sports = ['Basketball', 'Judo', 'Football', 'Tug-Of-War', 'Athletics',
                     'Swimming', 'Badminton', 'Sailing', 'Gymnastics',
                     'Art Competitions', 'Handball', 'Weightlifting', 'Wrestling',
                     'Water Polo', 'Hockey', 'Rowing', 'Fencing',
                     'Shooting', 'Boxing', 'Taekwondo', 'Cycling', 'Diving', 'Canoeing',
                     'Tennis', 'Golf', 'Softball', 'Archery',
                     'Volleyball', 'Synchronized Swimming', 'Table Tennis', 'Baseball',
                     'Rhythmic Gymnastics', 'Rugby Sevens',
                     'Beach Volleyball', 'Triathlon', 'Rugby', 'Polo', 'Ice Hockey']
    for sport in famous_sports:
        temp_df = athlete_df[athlete_df['Sport'] == sport]
        x.append(temp_df[temp_df['Medal'] == 'Gold']['Age'].dropna())
        name.append(sport)

    fig = ff.create_distplot(x, name, show_hist=False, show_rug=False)
    fig.update_layout(autosize=False, width=1000, height=600)
    st.title("Distribution of Age wrt Sports(Gold Medalist)")
    st.plotly_chart(fig)

    sport_list = df['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0, 'Overall')

    st.title('Height Vs Weight')
    selected_sport = st.selectbox('Select a Sport', sport_list)
    temp_df = helper.weight_v_height(df,selected_sport)
    fig, ax = plt.subplots()
    ax = sns.scatterplot(x=temp_df['Weight'], y=temp_df['Height'], hue=temp_df['Medal'], style=temp_df['Sex'], s=60)
    st.pyplot(fig)

    st.title("Men Vs Women Participation Over the Years")
    final = helper.men_vs_women(df)
    fig = px.line(final, x="Year", y=["Male", "Female"])
    fig.update_layout(autosize=False, width=1000, height=600)
    st.plotly_chart(fig)


