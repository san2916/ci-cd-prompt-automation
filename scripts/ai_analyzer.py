import os
from pathlib import Path
from openai import OpenAI


def analyze_results():
    test_output = Path("test-results.txt").read_text(
        errors="replace"
    )

    automation_output = Path("automation-results.txt").read_text(
        errors="replace"
    )

    prompt = f"""
You are a CI/CD automation assistant.

Analyze the following CI/CD execution results.

Determine:

1. Overall pipeline status
2. Test failures or errors
3. Probable cause
4. Recommended corrective actions
5. Agile task status

Use these Agile statuses:
- SUCCESS = Done
- FAILURE = Blocked

Return a concise Markdown report.

TEST RESULTS:
{test_output}

AUTOMATION RESULTS:
{automation_output}
"""

    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

    response = client.responses.create(
        model=os.environ.get("OPENAI_MODEL", "gpt-5"),
        input=prompt,
    )

    report = response.output_text

    Path("reports/ai_report.md").write_text(report)

    print("AI report generated successfully.")
    print(report)


if __name__ == "__main__":
    analyze_results()
