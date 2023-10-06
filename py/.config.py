
from IPython.terminal.prompts import Prompts, Token

class MyPrompt(Prompts):
    def in_prompt_tokens(self, cli=None):
        return [
                 (Token.Prompt, '🥛 ['),
                 (Token.PromptNum, str(self.shell.execution_count)),
                 (Token.Prompt, ']: ')]

    def out_prompt_tokens(self):
        return [
                (Token.OutPrompt, '🫗 ['),
                (Token.OutPromptNum, str(self.shell.execution_count)),
                (Token.OutPrompt, ']: ')]


c.TerminalInteractiveShell.prompts_class = MyPrompt

c.InteractiveShellApp.exec_lines = [
    'import builtins',
    'from rich import inspect',
    'builtins.help = inspect',
]

c.InteractiveShell.confirm_exit=False
c.TerminalInteractiveShell.autosuggestions_provider=None
