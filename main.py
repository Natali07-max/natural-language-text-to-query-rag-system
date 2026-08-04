import mysql.connector
from gemini_helper import ask_gemini

print("MAIN.PY LOADED")


# --------------------------------------------------
# Generate SQL using Gemini
# --------------------------------------------------

def generate_sql(query, table_name):

    prompt = f"""
    You are an expert MySQL assistant.

    Database Table:
    {table_name}

    Columns:
    - Transaction ID
    - Date
    - Customer ID
    - Gender
    - Age
    - Product Category
    - Quantity
    - Price per Unit
    - Total Amount
    - Company_name

    IMPORTANT:
    - Generate ONLY valid MySQL.
    - Do NOT explain.
    - Return ONLY SQL.
    - Use backticks around column names containing spaces.

    Question:
    {query}
    """

    sql = ask_gemini(prompt)

    sql = (
        sql.replace("```sql", "")
        .replace("```", "")
        .strip()
    )

    return sql


# --------------------------------------------------
# Dashboard Metrics
# --------------------------------------------------

def get_dashboard_metrics(company):

    if company == "IOCL":
        database = "ioc_db"
        table_name = "iocl"

    elif company == "BPCL":
        database = "bpcl_db"
        table_name = "bpcl"

    else:
        database = "hpcl_db"
        table_name = "hpcl"

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Nitu@ACE#7",
        database=database
    )

    cursor = connection.cursor()

    cursor.execute(f"""
        SELECT
            SUM(`Total Amount`),
            SUM(`Quantity`),
            COUNT(DISTINCT `Customer ID`)
        FROM {table_name}
    """)

    revenue, quantity, customers = cursor.fetchone()

    cursor.close()
    connection.close()

    return revenue, quantity, customers
# --------------------------------------------------
# Main Query Function
# --------------------------------------------------

def get_answer(user_query, company):

    print("INSIDE GET_ANSWER")

    # --------------------------
    # Database Selection
    # --------------------------

    if company == "IOCL":
        database = "ioc_db"
        table_name = "iocl"

    elif company == "BPCL":
        database = "bpcl_db"
        table_name = "bpcl"

    else:
        database = "hpcl_db"
        table_name = "hpcl"

    # --------------------------
    # Generate SQL
    # --------------------------

    sql = generate_sql(
        user_query,
        table_name
    )

    print("\nGenerated SQL:")
    print(sql)

    # --------------------------
    # Database Connection
    # --------------------------

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Nitu@ACE#7",
        database=database
    )

    cursor = connection.cursor()

    result = []
    columns = []

    try:

        cursor.execute(sql)

        result = cursor.fetchall()

        if cursor.description:
            columns = [col[0] for col in cursor.description]

        if len(result) == 0:

            answer = "No records found."

        else:

            row = result[0]

            # --------------------------
            # Two-column result
            # --------------------------

            if len(row) == 2:

                col1 = row[0]
                col2 = row[1]

                if "revenue" in user_query.lower():

                    answer = (
                        f"{col1} generated the highest revenue "
                        f"with ₹{col2}."
                    )

                elif "gender" in user_query.lower():

                    answer = (
                        f"{col1} customers spend the most "
                        f"with a total spend of ₹{col2}."
                    )

                elif "age" in user_query.lower():

                    answer = (
                        f"Customers aged {col1} spend the most "
                        f"with a total spend of ₹{col2}."
                    )

                elif "company" in user_query.lower():

                    answer = (
                        f"{col1} has the highest sales "
                        f"with ₹{col2}."
                    )

                elif "product" in user_query.lower():

                    answer = (
                        f"{col1} generated revenue of ₹{col2}."
                    )

                else:

                    answer = f"{col1} : {col2}"

            # --------------------------
            # Single value
            # --------------------------

            elif len(row) == 1:

                answer = f"Result: {row[0]}"

            # --------------------------
            # Multiple rows
            # --------------------------

            else:

                answer = f"Found {len(result)} records."

    except Exception as e:

        answer = f"Error: {e}"

    cursor.close()
    connection.close()

    return answer, sql, result, columns