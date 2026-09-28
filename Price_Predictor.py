import  streamlit as st
import  pickle
import pandas as pd
import numpy as np

st.set_page_config(page_title='Viz Demo')

with open('df.pkl', 'rb') as file:
    df = pickle.load(file)

with open('pipeline.pkl', 'rb') as file:
    pipeline = pickle.load(file)

def show():
    st.header('Enter your inputs')


    # property_type
    property_type = st.selectbox('Property Type', ['flat', 'house'])

    # sector
    sector = st.selectbox('Sector', sorted(df['sector'].unique().tolist()))

    #bedroom
    bedroom = st.selectbox(' Number of BedRooms', sorted(df['bedRoom'].unique().tolist()))

    #bathroom
    bathroom = st.selectbox('Number of Bathrooms', sorted(df['bathroom'].unique().tolist()))

    # balcony
    balcony = st.selectbox('Number of Balconies', sorted(df['balcony'].unique().tolist()))

    #agePossession
    agePossession = st.selectbox('Age of property', sorted(df['agePossession'].unique().tolist()))

    #builtuparea
    built_up_area = st.number_input('Built up Area')

    #servantroom
    servant_room = st.selectbox('Servant Room', [0.0, 1.0])

    #storeroom
    store_room = st.selectbox('Store Room', [0.0, 1.0])

    #furnishingType
    furnishing_type = st.selectbox('Furnishing Type', sorted(df['furnishing_type'].unique().tolist()))

    #luxury_categories
    luxury_category = st.selectbox('Luxury Category', sorted(df['luxury_category'].unique().tolist()))

    #floor_category
    floor_Category = st.selectbox('Floor Category', sorted(df['floor_category'].unique().tolist()))


    if st.button('Predict'):
        # form a dataframe
        data = [
            [
                property_type,
                sector,
                bedroom,
                bathroom,
                balcony,
                agePossession,
                built_up_area,
                servant_room,
                store_room,
                furnishing_type,
                luxury_category,
                floor_Category
            ]
        ]
        columns = [
            "property_type",
            "sector",
            "bedRoom",
            "bathroom",
            "balcony",
            "agePossession",
            "built_up_area",
            "servant room",
            "store room",
            "furnishing_type",
            "luxury_category",
            "floor_category"
        ]

        # converting to dataframe
        one_df = pd.DataFrame(data, columns=columns)


        # predict
        base_price = np.expm1(pipeline.predict(one_df))[0]
        low = base_price - 0.22
        high = base_price + 0.22

    # display
        st.text('The price of the flat is between {} Cr and {} Cr'.format(round(low,2), round(high,2)))