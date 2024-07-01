import subprocess
import matplotlib.pyplot as plt
import os

class VisualGitStatus:
    def __init__(self):
        self.status_output = self.get_git_status()

    def get_git_status(self):
        try:
            status_output = subprocess.check_output(['git', 'status', '--porcelain'], text=True)
            return status_output
        except subprocess.CalledProcessError as e:
            print(f"Error getting git status: {e}")
            return ""

    def parse_status(self):
        files_status = {'staged': [], 'unstaged': [], 'untracked': []}
        for line in self.status_output.splitlines():
            if line.startswith('A ') or line.startswith('M ') or line.startswith('R '):
                files_status['staged'].append(line[3:])
            elif line.startswith('?? '):
                files_status['untracked'].append(line[3:])
            else:
                files_status['unstaged'].append(line[3:])
        return files_status

    def visualize_status(self):
        files_status = self.parse_status()
        labels = ['Staged', 'Unstaged', 'Untracked']
        sizes = [len(files_status['staged']), len(files_status['unstaged']), len(files_status['untracked'])]
        colors = ['gold', 'lightcoral', 'lightskyblue']
        explode = (0.1, 0, 0)  # explode 1st slice

        plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.title('Git Status Overview')
        plt.show()

if __name__ == "__main__":
    visual_status = VisualGitStatus()
    visual_status.visualize_status()
