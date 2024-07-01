class CommitTemplateGenerator:
    def __init__(self):
        self.templates = {
            "feature": "Feature: {description}\n\n- {details}",
            "bug_fix": "Bug Fix: {issue}\n\n- {resolution}",
            "refactor": "Refactor: {scope}\n\n- {reasoning}",
        }

    def get_template(self, commit_type):
        return self.templates.get(commit_type, "No template found.")

    def generate_commit_message(self, commit_type, **kwargs):
        template = self.get_template(commit_type)
        return template.format(**kwargs)

if __name__ == "__main__":
    generator = CommitTemplateGenerator()
    print(generator.generate_commit_message("feature", description="Add login functionality", details="Implemented login with email and password."))
    print(generator.generate_commit_message("bug_fix", issue="Login button crash", resolution="Fixed null pointer exception on login."))
    print(generator.generate_commit_message("refactor", scope="Login flow", reasoning="Improved code readability and performance."))
