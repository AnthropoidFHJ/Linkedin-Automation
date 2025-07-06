import os
import requests
from dotenv import load_dotenv

load_dotenv()

def generate_groq_reply(text, context="reply_comment"):
    prompts = {
        "post": f"Write a 1000+ character LinkedIn post with strong reasoning, examples, structure, and hashtags on: {text}",
        "reply_comment": f"Reply kindly and professionally to this comment on my LinkedIn post: '{text}'",
        "comment_on_post": f"Write a thoughtful, polite comment based on this LinkedIn post: '{text}'"
    }

    data = {
        "model": "llama3-70b-8192",
        "messages": [
            {"role": "system", "content": "You are a professional LinkedIn user who writes friendly, intelligent replies."},
            {"role": "user", "content": prompts[context]}
        ]
    }

    try:
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {os.getenv('GROQ_API_KEY')}",
                "Content-Type": "application/json"
            },
            json=data
        )
        return response.json()['choices'][0]['message']['content'].strip()
    except Exception as e:
        print("[ERROR] Groq API failed:", e)
        return "Thank you for your comment! 😊"
