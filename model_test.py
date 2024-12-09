# text generator 
from huggingface_hub import InferenceClient
client = InferenceClient(api_key ="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")

# message input
messages=[
    {
        'role': 'user',
        'content': input("enter you prompt : "),
    }
]
# model request
try:
    completion = client.chat.completions.create(
        model = "Qwen/QwQ-32B-Preview",
        messages= messages,
        max_tokens=1000
    )

    response = completion.choices[0].message['content']
    print(f"response : {response}")
# exception
except Exception as e:
    print(f"An error occurred : {e}")