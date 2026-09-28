import streamlit as st
import  pandas as pd
import plotly.express as px
import pickle
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title='Plotting Demo')

st.title('Analytics')

new_df = pd.read_csv('data_viz1.csv')
feature_text = pickle.load(open('feature_text.pkl', 'rb'))

group_df = new_df.groupby("sector").mean(numeric_only=True)[["price", "price_per_sqft", "built_up_area", "latitude", "longitude"]]

# wordcloud
st.title('Features WordCloud')
wordcloud = WordCloud(
    width=800,
    height=800,
    background_color="white",
    stopwords=set(['s']),
    min_font_size=10,
).generate(feature_text)

fig = plt.figure(figsize=(9, 9), facecolor=None)
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.tight_layout(pad=0)

st.pyplot(fig)

#areavsprice
st.title('Area vs Price')

property_type = st.selectbox('Select Property Type', ['flat','house'])

if property_type == 'house':
    fig1 = px.scatter(new_df[new_df['property_type'] =='house'], x="built_up_area", y="price", color="bedRoom")
    st.plotly_chart(fig1, use_container_width=True)

else:
    fig1 = px.scatter(new_df[new_df['property_type'] == 'flat'], x="built_up_area", y="price", color="bedRoom",
                      title="Area Vs Price")
    st.plotly_chart(fig1, use_container_width=True)

#map
st.title('Sector Price per sqft Geomap')
fig = px.scatter_map(
    group_df,
    lat="latitude",
    lon="longitude",
    color="price_per_sqft",
    size="built_up_area",
    color_continuous_scale=px.colors.cyclical.IceFire,
    zoom=10,
    map_style="open-street-map",
    width= 1200,
    height= 700,
    hover_name= group_df.index)

st.plotly_chart(fig, use_container_width=True)

plt.rcParams["font.family"] = "Arial"

#piechart
st.title('BHK Pie Chart')
sector_options = new_df['sector'].unique().tolist()
sector_options.insert(0, 'overall')

selected_sector = st.selectbox('Select Sector', sector_options)
if selected_sector == 'overall':
    fig2 = px.pie(new_df, names = 'bedRoom')
    st.plotly_chart(fig2, use_container_width=True)
else:
    fig2 = px.pie(new_df[new_df['sector'] == selected_sector], names='bedRoom')
    st.plotly_chart(fig2, use_container_width=True)

#sidebyside_Comparison
st.title('Side by Side BHK Comparison')
fig3 = px.box(new_df[new_df["bedRoom"] <= 4], x="bedRoom", y="price")
st.plotly_chart(fig3, use_container_width=True)

#distribution_plot
st.title('Side by Side distplot for property type')

fig3, ax = plt.subplots(1, 2, figsize=(14, 5))

sns.histplot(
    new_df[new_df['property_type'] == 'house']['price'],
    kde=True, ax=ax[0], color='skyblue'
)
ax[0].set_title('House')
ax[0].set_xlabel('Price')

sns.histplot(
    new_df[new_df['property_type'] == 'flat']['price'],
    kde=True, ax=ax[1], color='salmon'
)
ax[1].set_title('Flat')
ax[1].set_xlabel('Price')

plt.tight_layout()
st.pyplot(fig3)
