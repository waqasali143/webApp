import streamlit as st
import pandas as pd
import sweetviz as sv

# Page title
st.title("Auto EDA Report Web App")

# Upload a CSV file
st.sidebar.header("Upload CSV File")
uploaded_file = st.sidebar.file_uploader("Upload your CSV file", type=["csv"])

# Sidebar - Data options
if uploaded_file is not None:
    @st.cache_data
    def load_data():
        data = pd.read_csv(uploaded_file)
        return data

    data = load_data()

    st.sidebar.subheader("Preview Data")
    if st.sidebar.checkbox("Show Data Preview"):
        st.write(data.head())

    # Auto EDA Report
    st.header("Auto EDA Report")

    if st.checkbox("Generate EDA Report"):
        st.write("This may take a moment...")
        report = sv.analyze(data)
        report.show_html("report.html")  # save HTML
        
        # Display the report in Streamlit
        with open("report.html", "r", encoding="utf-8") as f:
            html_content = f.read()
        components.html(html_content, height=800, scrolling=True)
else:
    st.info("Please upload a CSV file to get started.")

st.sidebar.markdown(
    """
    **Need help?** Please check the [Streamlit documentation](https://docs.streamlit.io/) for guidance.
    """
)
