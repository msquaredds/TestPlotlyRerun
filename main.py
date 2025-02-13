import streamlit as st
import plotly.express as px

if "var" not in st.session_state:
    st.session_state["var"] = 0

col3, col4 = st.columns(2)


def _update_session_state():
    event = st.session_state.iris
    if len(event.selection.points) != 0:
        st.session_state["var"] = event.selection.points[0]["x"]


def plot():
    df = px.data.iris()
    fig = px.scatter(
        df,
        x="sepal_width",
        y="sepal_length",
        color="species",
        size="petal_length",
        hover_data=["petal_width"],
    )

    st.plotly_chart(fig, key="iris", on_select=_update_session_state)
    # event.selection
    # if len(event.selection.points) != 0:
    #     st.session_state["var"] = event.selection.points[0]["x"]
    #  st.rerun()


with col3:
    st.write(st.session_state["var"])

with col4:
    plot()