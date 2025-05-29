import openai

def format_prompt(query: str, context_docs: list) -> str:
    """
    Formats the prompt by combining context and user query.
    """
    context = "\n\n".join([f"- {doc}" for doc in context_docs])
    prompt = (
        "You are a helpful assistant specialized in bioinformatics tools.\n\n"
        f"Context:\n{context}\n\n"
        f"Question: {query}\n"
        "Answer:"
    )
    return prompt


def generate_answer(query: str, context_docs: list) -> str:
    """
    Generates a grounded answer using OpenAI's GPT model.
    """
    prompt = format_prompt(query, context_docs)

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an expert in bioinformatics tools."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=512,
            n=1,
            stop=None
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return f"⚠️ Error generating answer: {str(e)}"
# Answer generation logic module
