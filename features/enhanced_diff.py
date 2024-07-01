import difflib
import pygments
from pygments.lexers import get_lexer_by_name
from pygments.formatters import TerminalFormatter

class EnhancedDiff:
    def __init__(self, file_path, from_lines, to_lines, from_file_name='From', to_file_name='To'):
        self.file_path = file_path
        self.from_lines = from_lines
        self.to_lines = to_lines
        self.from_file_name = from_file_name
        self.to_file_name = to_file_name

    def generate_diff(self):
        diff = difflib.unified_diff(self.from_lines, self.to_lines, fromfile=self.from_file_name, tofile=self.to_file_name)
        return list(diff)

    def highlight_diff(self, diff_lines):
        lexer = get_lexer_by_name('diff', stripall=True)
        formatter = TerminalFormatter()
        highlighted_diff = pygments.highlight('\n'.join(diff_lines), lexer, formatter)
        return highlighted_diff

    def display(self):
        diff_lines = self.generate_diff()
        highlighted_diff = self.highlight_diff(diff_lines)
        print(highlighted_diff)

if __name__ == "__main__":
    # Example usage
    from_lines = ['This is a test.', 'This part of the document has remained unchanged.', 'This is another test.']
    to_lines = ['This is a test.', 'This part has been modified.', 'This is another test.']
    diff = EnhancedDiff('example.txt', from_lines, to_lines)
    diff.display()
