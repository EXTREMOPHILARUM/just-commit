import subprocess
import re
from datetime import datetime
from llama_cpp_python import LlamaModel

class ChangelogGenerator:
    def __init__(self):
        self.model = LlamaModel()

    def generate_changelog_entry(self, commit_message):
        # Use LLM to enhance the commit message for the changelog
        enhanced_message = self.model.generate_text(commit_message)
        return enhanced_message

    def get_last_commit_message(self):
        # Get the last commit message from git
        commit_message = subprocess.check_output(['git', 'log', '-1', '--pretty=%B'], text=True).strip()
        return commit_message

    def update_changelog(self, changelog_entry):
        # Prepend the changelog entry to the CHANGELOG.md file with a timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d")
        formatted_entry = f"## {timestamp}\n\n{changelog_entry}\n\n"
        with open("CHANGELOG.md", "r+") as file:
            content = file.read()
            file.seek(0, 0)
            file.write(formatted_entry + content)

    def integrate_with_git(self):
        last_commit_message = self.get_last_commit_message()
        changelog_entry = self.generate_changelog_entry(last_commit_message)
        self.update_changelog(changelog_entry)
        print("Changelog updated with the latest commit.")

if __name__ == "__main__":
    changelog_generator = ChangelogGenerator()
    changelog_generator.integrate_with_git()
