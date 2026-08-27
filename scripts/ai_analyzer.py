import os

def analyze_results():
    print("=== CI/CD AI Analysis ===")

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        print("OpenAI API key not available.")
        print("Using local analysis instead.")

        try:
            with open("automation-results.txt", "r") as f:
                results = f.read()

            print("\n=== Local Analysis Result ===")

            if "error" in results.lower() or "failed" in results.lower():
                print("Status: Issues detected in automation.")
                print("Recommendation: Check the automation output for errors.")
            else:
                print("Status: Automation completed successfully.")
                print("Recommendation: CI/CD pipeline can proceed.")

        except FileNotFoundError:
            print("automation-results.txt not found.")
            print("Status: Unable to analyze automation results.")

        return

    print("OpenAI API key detected.")
    print("Running OpenAI analysis...")

    from openai import OpenAI

    client = OpenAI(api_key=api_key)

    with open("automation-results.txt", "r") as f:
        results = f.read()

    response = client.responses.create(
        model=os.getenv("OPENAI_MODEL", "gpt-5"),
        input=f"Analyze this CI/CD automation result:\n\n{results}"
    )

    print("\n=== OpenAI Analysis ===")
    print(response.output_text)


if __name__ == "__main__":
    analyze_results()
