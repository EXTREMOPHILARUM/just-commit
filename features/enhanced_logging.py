import subprocess
import re

class EnhancedLogging:
    def __init__(self):
        pass

    def format_log_output(self, log_output):
        # Apply better formatting to the git log output
        formatted_output = re.sub(r'commit (\w+)', r'Commit ID: \1', log_output)
        return formatted_output

    def filter_log(self, keyword):
        # Filter git log by a specific keyword
        log_output = subprocess.check_output(['git', 'log', '--grep', keyword], text=True)
        return self.format_log_output(log_output)

    def search_in_log(self, search_term):
        # Search for a specific term in the git log
        log_output = subprocess.check_output(['git', 'log', '--grep', search_term], text=True)
        return self.format_log_output(log_output)

if __name__ == "__main__":
    enhanced_logging = EnhancedLogging()
    print(enhanced_logging.filter_log("fix"))
    print(enhanced_logging.search_in_log("performance"))
