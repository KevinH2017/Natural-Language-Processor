import glob
import streamlit as st
import plotly.express as px
from nltk.sentiment import SentimentIntensityAnalyzer

filepaths = sorted(glob.glob("diary/*.txt"))

analyzer = SentimentIntensityAnalyzer()

pos_value = []
neg_value = []
for filepath in filepaths:
    with open(filepath) as diary:
        entry = diary.read()

    scores = analyzer.polarity_scores(entry)
    pos_value.append(scores["pos"])
    neg_value.append(scores["neg"])

dates = [name.strip(".txt").strip("diary/") for name in filepaths]

st.title("Diary Tone")
st.subheader("Positivity")
fig_1 = px.line(x=dates, y=pos_value, labels={"x": "Date", "y": "Positivity"})
st.plotly_chart(fig_1)

st.subheader("Negativity")
fig_2 = px.line(x=dates, y=neg_value, labels={"x": "Date", "y": "Negativity"})
st.plotly_chart(fig_2)