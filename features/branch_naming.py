import subprocess
import re
from llama_cpp_python import LlamaModel

class BranchNamer:
    def __init__(self):
        self.model = LlamaModel()

    def suggest_branch_name(self, changes):
        suggestion = self.model.generate_text(changes)
        # Clean up suggestion to fit branch naming conventions
        branch_name = re.sub(r'\W+', '_', suggestion).lower()
        return branch_name

    def get_git_changes(self):
        # Get changes from git diff
        diff_output = subprocess.check_output(['git', 'diff'], text=True)
        return diff_output

    def create_branch(self, branch_name):
        subprocess.run(['git', 'checkout', '-b', branch_name])

    def integrate_with_git(self):
        changes = self.get_git_changes()
        suggested_branch_name = self.suggest_branch_name(changes)
        print(f"Suggested branch name based on changes: {suggested_branch_name}")
        # Here, further integration to automatically create the branch could be implemented

if __name__ == "__main__":
    branch_namer = BranchNamer()
    branch_namer.integrate_with_git()
