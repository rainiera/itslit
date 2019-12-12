from io import BytesIO
from PIL import Image

import requests
import streamlit as st

st.title('Rainier Ababao')

r = st.sidebar.radio(
    'Navigation',
    (
        'About & Work',
        'Travels',
        'Blog',
        'Limitations of this site'
    )
)

st.sidebar.text('You\'re on: {}'.format(r))

def colored_block_write(caption, color):
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
        colored_block_write(caption, color)

if r == 'About & Work':
    with st.spinner('loading the about page'):
        st.balloons()
        st.markdown("""
        ### Currently

        - Work at [Looker](https://looker.com/)
          - Software Engineer on the **Data Delivery and Integrations** team
            - Delivering data to people they spend their time (like Slack!!!)
            - Mostly Kotlin, Ruby, some TypeScript
            - Lmk if you want to know more about working here, I love it!!!
        
        ### Previously

        - Domino Data Lab
          - Software Engineer on the Compute Grid team
            - Helped get Domino on Kubernetes!
            - And a lot of other stuff! Mostly Scala, Kubernetes, TypeScript, React
        - Undergrad CS at the University of Texas
        - Interned (and had some fun projects) at: [Medallia](https://www.medallia.com/), Desktop Genetics, Clover, Bold Metrics
        - Basically a bunch of 1/10/100/1000-person companies!
        """)
        from PIL import Image
        response = requests.get('https://s3-us-west-2.amazonaws.com/rainier.io/hardergrat.jpg')
        image = Image.open(BytesIO(response.content))
        st.image(
            image,
            caption='My favorite hike so far has been the Hardergrat',
            use_column_width=True
        )
elif r == 'Travels':
    with st.spinner('loading the travels page'):
        photo_with_spinner('https://s3-us-west-2.amazonaws.com/rainier.io/eur-jul-2018.png', 'Europe as of July 2018', 'blue')
        photo_with_spinner('https://s3-us-west-2.amazonaws.com/rainier.io/asia-june-2018.png', 'Asia as of June 2018', 'yellow')
        photo_with_spinner('https://s3-us-west-2.amazonaws.com/rainier.io/usa-aug-2018.png', 'USA as of Aug 2018', 'red')
elif r == 'Limitations of this site':
    st.title('Limitations of this site') 
    st.markdown("""
    As much as I like building this on Streamlit, there are a few limitations (that obviously necessitate
    feature requests outside of the ML engineer usecase):

    - Can't use path or other URL query params to pass state into sidebar
    """)
elif r == 'Blog':
    with st.spinner('loading the blog'):
        st.title('Blog?')
        st.markdown("I mostly write on [Medium](https://medium.com/@rainier).")

def router(
    key,
    render_func
):
    # todo finish this try to find an elegant way to implement lambda-based routing
    with st.spinner('loading this function! {}'.format(str(render_func))):
        render_func()
