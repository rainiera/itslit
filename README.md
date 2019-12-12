# itslit


```
rainier@makinitrain$ pip install streamlit
rainier@makinitrain$ streamlit main.py
```

Interesting notes:

---

Initializing a `BytesIO` object in the cached function, e.g.,

```python
@st.cache
def cached_request_bytes_holder_1(url):
    c = requests.get(url).content
    return c
```

yielded this message on-screen:

![Image of warning message]("./img/cached_val_mutation_warning.png")

Whereas

```python
@st.cache
def cached_request_bytes_holder_1(url):
    c = requests.get(url).content
    return c
```

did not.
