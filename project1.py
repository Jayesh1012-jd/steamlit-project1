import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -------------------------------
# Condition 1 - Basic Text
# -------------------------------
st.title("My First Streamlit App 🚀")
st.write("Hello Jayesh 👋")
st.text("Let's start")

# -------------------------------
# Condition 2 - Charts
# -------------------------------
random_df = pd.DataFrame(
    np.random.randn(10, 2),
    columns=['A', 'B']
)

st.line_chart(random_df)
st.bar_chart(random_df)

# -------------------------------
# Condition 3 - Sidebar
# -------------------------------
st.sidebar.title("Navigation")
st.sidebar.video("https://youtu.be/6l88XYUjNIs?si=y4fA3OlSTVMfCpqV")

# -------------------------------
# Condition 4 - File Upload
# -------------------------------
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

if uploaded_file is not None:
    uploaded_df = pd.read_csv(uploaded_file)
    st.success("File uploaded successfully!")
    st.dataframe(uploaded_df)

# -------------------------------
# User Input Section
# -------------------------------
name = st.text_input("Enter name:")

if st.button("Welcome"):
    if name:
        st.success(f"Hello, {name} 🎉")
    else:
        st.warning("Please enter your name!")

st.header("This is a header")
st.subheader("This is a subheader")

st.markdown("**Bold**, *Italic*, `code`, [Streamlit](https://streamlit.io)")
st.code("for i in range(5): print(i)", language="python")

st.text_input("What is your name?")
st.text_area("Write something ....")
st.number_input("Pick a number", min_value=0, max_value=100)
st.slider("Choose a range", 0, 100)
st.selectbox("Select a fruit", ["Apple", "Banana", "Mango"])
st.multiselect("Choose Topping", ["Cheese", "Tomato", "Olives"])
st.radio("Pick one", ["Option A", "Option B"])
st.checkbox("I agree to the terms")

# -------------------------------
# Matplotlib Graph
# -------------------------------
fig, ax = plt.subplots()
ax.plot([1, 2, 3], [1, 4, 9])
ax.set_title("Simple Line Plot")
st.pyplot(fig)