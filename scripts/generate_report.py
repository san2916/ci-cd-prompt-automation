from datetime import datetime
from pathlib import Path


def generate_report(status, message):
    report = f"""# CI/CD Automation Report

**Execution Time:** {datetime.now().isoformat()}

**Pipeline Status:** {status}

## Summary

{message}

## Recommended Action

Review the pipeline results and take corrective action if required.
"""

    Path("reports/latest_report.md").write_text(report)
    print("Report generated: reports/latest_report.md")


if __name__ == "__main__":
    generate_report(
        "SUCCESS",
        "The automation pipeline completed successfully."
    )
