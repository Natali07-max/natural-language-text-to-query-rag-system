import plotly.express as px
import streamlit as st
import pandas as pd
import main

print("MAIN FILE:", main.__file__)
print("GET_ANSWER RETURNS:", main.get_answer.__code__.co_argcount)

# ----------------------------
# Automatic Chart Generator
# ----------------------------

def create_chart(df, user_query):

    if df.empty:
        return

    question = user_query.lower()

    try:

        # Single numeric value
        if len(df.columns) == 1:

            st.metric(
                label=df.columns[0],
                value=df.iloc[0, 0]
            )
            return

        # Two-column results
        elif len(df.columns) == 2:

            x = df.columns[0]
            y = df.columns[1]

            if (
                "month" in question
                or "trend" in question
                or "date" in question
            ):

                fig = px.line(
                    df,
                    x=x,
                    y=y,
                    markers=True,
                    title="Trend Analysis"
                )

            elif (
                "gender" in question
                or "customer" in question
                or "product" in question
                or "company" in question
                or "top" in question
            ):

                fig = px.bar(
                    df,
                    x=x,
                    y=y,
                    title="Analysis"
                )

            else:

                fig = px.bar(
                    df,
                    x=x,
                    y=y,
                    title="Analysis"
                )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

    except Exception as e:

        st.warning(f"Chart Error: {e}")

# ----------------------------
# Page Config
# ----------------------------

st.set_page_config(
    page_title="Enterprise Data Copilot",
    page_icon="🤖",
    layout="wide"
)

# ----------------------------
# Session State
# ----------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# ----------------------------
# Title
# ----------------------------

st.title("🤖 Enterprise Data Copilot")

st.caption(
    "AI-powered natural language analytics for enterprise databases"
)

# ----------------------------
# Company Selection
# ----------------------------

company = st.selectbox(
    "Select Company",
    ["IOCL", "BPCL", "HPCL"]
)

# ----------------------------
# Dashboard Metrics
# ----------------------------

revenue, quantity, customers = main.get_dashboard_metrics(company)

c1, c2, c3 = st.columns(3)

c1.metric(
    "💰 Total Revenue",
    f"₹{revenue:,.0f}"
)

c2.metric(
    "📦 Total Quantity",
    f"{quantity:,}"
)

c3.metric(
    "👥 Customers",
    f"{customers:,}"
)

st.divider()

# ----------------------------
# Chat History
# ----------------------------

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# ----------------------------
# User Input
# ----------------------------

user_query = st.chat_input(
    "Ask anything about your enterprise data..."
)

# ----------------------------
# Process Query
# ----------------------------

if user_query:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_query
        }
    )

    answer, sql, result, columns = main.get_answer(
        user_query,
        company
    )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    with st.chat_message("user"):
        st.write(user_query)

    with st.chat_message("assistant"):

        st.success(answer)

        # ----------------------------
        # Query Result
        # ----------------------------

        if result:

            df = pd.DataFrame(
                result,
                columns=columns
            )

            st.subheader("📊 Query Result")

            st.dataframe(
                df,
                use_container_width=True
            )

            # ----------------------------
            # Download CSV
            # ----------------------------

            csv = df.to_csv(index=False).encode("utf-8")

            st.download_button(
                label="📥 Download CSV",
                data=csv,
                file_name="query_results.csv",
                mime="text/csv"
            )

            # ----------------------------
            # Automatic Chart
            # ----------------------------

            create_chart(
                df,
                user_query
            )

        # ----------------------------
        # Generated SQL
        # ----------------------------

        with st.expander("Generated SQL"):

            st.code(
                sql,
                language="sql"
            )
# ----------------------------
# Footer
# ----------------------------

st.divider()

st.markdown(
    """
### Features

- Natural Language Queries
- SQL Generation
- MySQL Integration
- Automatic Charts
- Enterprise Analytics
- Streamlit UI
"""
)