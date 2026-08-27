def analyze_results():
    print("=== CI/CD AI Analysis ===")
    print("OpenAI API disabled.")
    print("Using local rule-based analysis.")

    try:
        with open("automation-results.txt", "r") as f:
            results = f.read()

        print("\n=== Local Analysis Result ===")

        if "error" in results.lower() or "failed" in results.lower():
            print("Status: Issues detected in automation.")
            print("Recommendation: Check automation-results.txt for errors.")
        else:
            print("Status: Automation completed successfully.")
            print("Recommendation: CI/CD pipeline can proceed.")

    except FileNotFoundError:
        print("automation-results.txt not found.")
        print("Status: Unable to analyze automation results.")
        return

    print("\n=== Analysis Completed ===")


if __name__ == "__main__":
    analyze_results()
