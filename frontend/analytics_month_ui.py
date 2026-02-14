import streamlit as st
from datetime import datetime
import requests
import pandas as pd
API_URL = "http://127.0.0.1:8000"
def analytics_month_tab():
    col1, col2 = st.columns(2)

    with col1:
        start_date = st.date_input(
            "Start date",
            datetime(2024, 8, 1),
            key="month_analytics_start_date"
        )

    with col2:
        end_date = st.date_input(
            "End date",
            datetime(2024, 8, 5),
            key="month_analytics_end_date"
        )

    if st.button("Get analytics", key="month_analytics_button"):
        payload = {
            "start_date": start_date.strftime("%Y-%m-%d"),
            "end_date": end_date.strftime("%Y-%m-%d")
        }

        try:
            response = requests.post(
                f"{API_URL}/analytics-by-month/",
                json=payload
            )
            res = response.json()

            data = {
                "Month name": list(res.keys()),
                "Total": [res[m]['total'] for m in res]
            }

            df = pd.DataFrame(data)

            df_sorted = df.sort_values(by=["Total"], ascending=False)

            st.title("Expense Breakdown by Month")

            st.bar_chart(
                data=df_sorted.set_index("Month name")['Total'],
                use_container_width=True
            )

            df_sorted["Total"] = df_sorted["Total"].map("{:.2f}".format)
            st.dataframe(df_sorted)


            if response.status_code == 200:
                st.write(response.json())
            else:
                st.error(response.text)

        except requests.exceptions.ConnectionError:
            st.error("Backend server is not running on port 8000")
