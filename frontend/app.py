# import streamlit as st
# import pandas as pd
# #text element
# st.header("Streamlit core feature")
# st.subheader("Text element")
# st.text("This is asimple element")
#
# #data display
# st.subheader("Data display")
# st.write("Here is a simple element")
# df=pd.DataFrame({
#     "Date":["2024-08-01","2024-08-02","2024-08-03","2024-08-04"],
#     "Amount":[105,204,303,408]
# })
# st.table(df)
#
# #charts
# st.subheader("Charts")
# st.line_chart([1,2,3,4])
# #user input
#
# st.subheader("User input")
# value = st.slider("Select a value", 0, 100)
# st.write(f"Selected value: {value}")
#
# =====================================
#
# import streamlit as st
# #checkbox
# st.header("Interactive widget example")
# if st.checkbox("Show/hide"):
#     st.write("Checkbox is checked !")
# #selectbox
# option=st.selectbox("Category",["rent","food"], label_visibility="collapsed")
# st.write(f"Selected option: {option}")
#
# #multiselect
# option=st.multiselect("Select multiple number",[1,2,3,4])
# st.write(f"Selected option: {option}")

# ===================================================



# import streamlit as st
# from datetime import datetime
# import requests

# API_URL = "http://localhost:8000"
#
# st.title("Expense Tracking System")
#
# tab1, tab2 = st.tabs(["Add/Updates", "Analytics"])
#
# with tab1:
    # selected_date = st.date_input(
    #     "Enter date",
    #     datetime(2024, 8, 1),
    #     label_visibility="collapsed"
    # )
    #
    # response = requests.get(f"{API_URL}/expenses/{selected_date}")
    #
    # if response.status_code == 200:
    #     existing_expenses = response.json()
    #     # st.write(existing_expenses) # This will show table-like output
    # else:
    #     st.error("Failed to retrieve expenses data")
    #     existing_expenses = []
    #
    # categories = ["Rent", "Food", "Shopping", "Entertainment", "Other"]
    #
    # with st.form(key="expense_form"):
    #     col1,col2, col3=st.columns(3)
    #     with col1:
    #         st.subheader("Amount")
    #     with col2:
    #         st.subheader("Category")
    #     with col3:
    #         st.subheader("Notes")
    #     expenses=[]
    #     for i in range(5):
    #         if i<len(existing_expenses):
    #             amount = existing_expenses[i]["amount"]
    #             category = existing_expenses[i]["category"]
    #             notes = existing_expenses[i]["notes"]
    #         else:
    #             amount = 20.0
    #             category = "Shopping"
    #             notes = "daily use"
    #
    #
    #
    #         col1, col2, col3 = st.columns(3)
    #
    #         with col1:
    #             amount_input=st.number_input(
    #                 label="Amount",
    #                 min_value=0.0,
    #                 step=1.0,
    #                 value=amount,
    #                 key=f"amount_{selected_date}_{i}",label_visibility="collapsed"
    #             )
    #
    #         with col2:
    #             category_input=st.selectbox(
    #                 label="Category",
    #                 options=categories,
    #                 index=categories.index(category),
    #                 key=f"category_{selected_date}_{i}",label_visibility="collapsed"
    #             )
    #
    #         with col3:
    #             notes_input=st.text_input(
    #                 label="Notes",
    #                 value=notes,
    #                 key=f"notes_{selected_date}_{i}",label_visibility="collapsed"
    #             )
    #         expenses.append({
    #             "amount":amount_input,
    #             "category":category_input,
    #             "notes":notes_input
    #         })
    #
    #     submit_button = st.form_submit_button("submit")
    #     if submit_button:
    #         st.success("Form Submitted")
    #         filtered_expenses = [expense for expense in expenses if expense['amount']>0]
    #         response=requests.post(f"{API_URL}/expenses/{selected_date}", json=filtered_expenses)
    #         if response.status_code == 200:
    #             st.success("Expense updated successfully")
    #         else:
    #             st.error("Failed to update expense")
# ============================================

import streamlit as st
from add_update_ui import add_update_tab
from analytics_ui import analytics_tab
st.title("Expense Tracking System")

tab1, tab2 = st.tabs(["Add/Updates", "Analytics"])

with tab1:
    add_update_tab()
with tab2:
    analytics_tab()






































































