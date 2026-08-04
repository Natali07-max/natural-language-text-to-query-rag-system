from gemini_helper import ask_gemini

print("SQL_GENERATOR LOADED")


def generate_sql(question):

    print("\nINSIDE SQL_GENERATOR")
    print("Question:", question)

    prompt = f"""
    You are an expert MySQL assistant.

    Database Table:
    iocl

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

    IMPORTANT RULES:
    1. Return ONLY executable MySQL.
    2. Do NOT explain anything.
    3. Do NOT return English text.
    4. Do NOT use markdown.
    5. Output must always begin with SELECT.
    6. Use backticks (`) around columns that contain spaces.

    Examples:

    Question:
    Which product generated the highest revenue?

    SQL:
    SELECT `Product Category`,
    SUM(`Total Amount`) AS revenue
    FROM iocl
    GROUP BY `Product Category`
    ORDER BY revenue DESC
    LIMIT 1;

    Question:
    Which age group spends the most?

    SQL:
    SELECT FLOOR(`Age`/10)*10 AS age_group,
    SUM(`Total Amount`) AS total_spent
    FROM iocl
    GROUP BY age_group
    ORDER BY total_spent DESC
    LIMIT 1;

    Now generate SQL for:

    {question}
    """

    sql = ask_gemini(prompt)

    print("\nRAW GEMINI OUTPUT:")
    print(sql)

    sql = (
        sql
        .replace("```sql", "")
        .replace("```", "")
        .strip()
    )

    print("\nFINAL SQL:")
    print(sql)

    return sql