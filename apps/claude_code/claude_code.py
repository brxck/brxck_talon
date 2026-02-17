from talon import Context, Module, actions

mod = Module()
mod.apps.claude_code = """
os: mac
and app.bundle: com.superset.desktop
"""
mod.apps.claude_code = """
tag: terminal
and win.title: /claude/i
"""

ctx = Context()
ctx.matches = r"""
app: claude_code
"""


@ctx.action_class("edit")
class EditActions:
    def delete_line():
        actions.key("ctrl-u")
