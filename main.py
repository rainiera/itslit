from io import BytesIO
import requests
import streamlit as st

st.title('Rainier Ababao')

st.subheader('engineer, hiker, reader, etc.')

r = st.sidebar.radio(
    'Select a page',
    ('About', 'Travels', 'Blog', 'What\'s next')
)

st.sidebar.text('You\'re on the page: {}'.format(r))

# option = st.sidebar.selectbox(
#     'Select a page',
#     ('About', 'Travels', 'Blog', 'What\'s next')
# )

# st.sidebar.text('You\'re on the page: {}'.format(option))

if r == 'About':
    with st.spinner('loading the about page'):
        from PIL import Image
        response = requests.get('https://s3-us-west-2.amazonaws.com/rainier.io/hardergrat.jpg')
        image = Image.open(BytesIO(response.content))
        st.image(
            image,
            use_column_width=True
        )
        st.warning('My favorite hike so far has been the Hardergrat')
elif r == 'Travels':
    with st.spinner('loading the travels page'):
        st.subheader('Wow!')
        from PIL import Image
        response_1 = requests.get('https://s3-us-west-2.amazonaws.com/rainier.io/eur-jul-2018.png')
        response_2 = requests.get('https://s3-us-west-2.amazonaws.com/rainier.io/asia-june-2018.png')
        response_3 = requests.get('https://s3-us-west-2.amazonaws.com/rainier.io/usa-aug-2018.png')
        i = Image.open(BytesIO(response_1.content))
        j = Image.open(BytesIO(response_2.content))
        k = Image.open(BytesIO(response_3.content))
        st.image(
            i,
            use_column_width=True
        )
        st.info('Europe July 2018')
        st.image(
            j,
            use_column_width=True
        )
        st.success('Asia June 2018')
        st.image(
            k,
            use_column_width=True
        )
        st.warning('Usa Aug 2018')
