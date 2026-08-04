from google import genai

client = genai.Client(
    api_key="GEMINI_API_KEY"
)


def ask_gemini(prompt):

    print("CALLING GEMINI")

    response = client.models.generate_content(
        model="gemini-flash-lite-latest",
        contents=prompt
    )

    print("GEMINI RESPONSE RECEIVED")

    return response.text
