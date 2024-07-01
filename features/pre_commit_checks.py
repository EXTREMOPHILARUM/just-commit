import subprocess
import sys

def run_pre_commit_checks():
    checks = [
        {"name": "Code Standards Check", "command": "flake8"},
        {"name": "Unit Tests", "command": "pytest"},
    ]
    failed_checks = []

    for check in checks:
        print(f"Running {check['name']}...")
        result = subprocess.run(check['command'].split(), capture_output=True)
        if result.returncode != 0:
            failed_checks.append(check['name'])
            print(f"{check['name']} failed:\n{result.stdout.decode('utf-8')}\n{result.stderr.decode('utf-8')}")

    if failed_checks:
        print("Pre-commit checks failed for the following:")
        for check in failed_checks:
            print(f"- {check}")
        sys.exit(1)
    else:
        print("All pre-commit checks passed successfully.")

if __name__ == "__main__":
    run_pre_commit_checks()
