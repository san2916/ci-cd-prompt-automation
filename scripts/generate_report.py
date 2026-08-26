from datetime import datetime
from pathlib import Path


def generate_report(status, message, errors=0):
    reports_dir = Path("reports")
    reports_dir.mkdir(exist_ok=True)

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CI/CD Automation Dashboard</title>
</head>
<body>
    <h1>CI/CD Automation Dashboard</h1>

    <h2>Pipeline Status: {status}</h2>

    <p><strong>Execution Time:</strong> {now}</p>
    <p><strong>Errors:</strong> {errors}</p>

    <h2>Summary</h2>
    <p>{message}</p>

    <h2>Recommended Action</h2>
    <p>
        Review the pipeline results. If the pipeline failed,
        investigate the reported errors and rerun the workflow.
    </p>
</body>
</html>
"""

    Path("reports/index.html").write_text(html)

    markdown = f"""# CI/CD Automation Report

**Execution Time:** {now}

**Pipeline Status:** {status}

**Errors:** {errors}

## Summary

{message}

## Recommended Action

Review the pipeline results and take corrective action if required.
"""

    Path("reports/latest_report.md").write_text(markdown)

    print("HTML dashboard generated: reports/index.html")
    print("Markdown report generated: reports/latest_report.md")


if __name__ == "__main__":
    generate_report(
        "SUCCESS",
        "The automation pipeline completed successfully.",
        0
    )
