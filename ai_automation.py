import os
from datetime import datetime
from openai import OpenAI

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise RuntimeError("OPENAI_API_KEY is not configured")

client = OpenAI(api_key=api_key)

prompt = """
You are a CI/CD automation assistant.

Analyze the following task:
Create a short CI/CD automation status report for a GitHub repository.

The repository already has:
1. Initial CI/CD Prompt Automation Pipeline
2. Automated Dashboard Deployment
3. GitHub Pages Deployment Workflow

All three workflows completed successfully.

Generate:
- Current CI/CD status
- Completed tasks
- Recommended next automation step
- A short deployment summary

Return clean Markdown.
"""

response = client.responses.create(
    model="gpt-5",
    input=prompt
)

output = response.output_text

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("AI_CICD_STATUS.md", "w") as file:
    file.write("# AI Generated CI/CD Status\n\n")
    file.write(f"Generated: {timestamp}\n\n")
    file.write(output)

print(output)
print("\nAI automation completed successfully.")
