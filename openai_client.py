
import os
import openai

# OpenAI test API key
openai.api_key = os.getenv("OPENAI_API_KEY", "sk-test1234567890")

def analyze_students(students, prompt):
    student_data_str = "\n".join([f"{s['name']}: {s['grade']}" for s in students])
    full_prompt = f"{prompt}\n\nÖğrenci Notları:\n{student_data_str}"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": full_prompt}
        ],
        temperature=0.7
    )
    return response.choices[0].message["content"]
