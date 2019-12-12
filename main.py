from io import BytesIO
from PIL import Image

import requests
import streamlit as st

st.title('Rainier Ababao')

st.subheader('engineer, hiker, reader, etc.')

r = st.sidebar.radio(
    'Navigation',
    ('About', 'Travels', 'Blog', 'What\'s next')
)

st.sidebar.text('You\'re on: {}'.format(r))

def colored_block_write(color, caption):
    if color == 'blue':
        st.info(caption)
    elif color == 'red':
        st.error(caption)
    elif color == 'yellow':
        st.warning(caption)
    elif color == 'green':
        st.success(caption)
    else:
        st.info(caption)

@st.cache
def cached_request_bytes(url):
    c = requests.get(url).content
    return c

def photo_with_spinner(
    url,
    caption,
    color='blue',
    loading_msg='loading 😜 why don\'t u just check ur 📱 or grab a cuppa ☕️, will ya ⏳'
):
    with st.spinner(loading_msg):
        content = cached_request_bytes(url)
        img = Image.open(BytesIO(content))
        st.image(img, use_column_width=True)
        colored_block_write(color, caption)

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
        photo_with_spinner('https://s3-us-west-2.amazonaws.com/rainier.io/eur-jul-2018.png', 'Europe July 2018', 'blue')
        photo_with_spinner('https://s3-us-west-2.amazonaws.com/rainier.io/asia-june-2018.png', 'Asia June 2018', 'yellow')
        photo_with_spinner('https://s3-us-west-2.amazonaws.com/rainier.io/usa-aug-2018.png', 'USA as of Aug 2018', 'red')
elif r == 'What\'s next':
    with st.spinner('loading the What\'s next page'):
        st.title('helly hansen makes me hella handsome while i lend a helping hand son. because honesty and integrity are a part of their corporate policy')
elif r == 'Blog':
    with st.spinner('loading the What\'s next page'):
        st.title('blohg')

def router(
    key,
    render_func
):
    # todo finish this try to find an elegant way to implement lambda-based routing
    with st.spinner('loading this function! {}'.format(str(render_func))):
        render_func()
