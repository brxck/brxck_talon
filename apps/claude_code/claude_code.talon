app: claude_code
-
tag(): user.readline

# Slash commands
clode clear:
    key(ctrl-u)
    insert("/clear")
clode compact:
    key(ctrl-u)
    insert("/compact ")
clode config:
    key(ctrl-u)
    insert("/config")
clode context:
    key(ctrl-u)
    insert("/context")
clode copy:
    key(ctrl-u)
    insert("/copy")
clode cost:
    key(ctrl-u)
    insert("/cost")
clode debug:
    key(ctrl-u)
    insert("/debug ")
clode desktop:
    key(ctrl-u)
    insert("/desktop")
clode doctor:
    key(ctrl-u)
    insert("/doctor")
clode exit:
    key(ctrl-u)
    insert("/exit")
clode export:
    key(ctrl-u)
    insert("/export ")
clode help:
    key(ctrl-u)
    insert("/help")
clode init:
    key(ctrl-u)
    insert("/init")
clode M C P:
    key(ctrl-u)
    insert("/mcp")
clode memory:
    key(ctrl-u)
    insert("/memory")
clode model:
    key(ctrl-u)
    insert("/model")
clode permissions:
    key(ctrl-u)
    insert("/permissions")
clode plan:
    key(ctrl-u)
    insert("/plan")
clode rename:
    key(ctrl-u)
    insert("/rename ")
clode resume:
    key(ctrl-u)
    insert("/resume")
clode rewind:
    key(ctrl-u)
    insert("/rewind")
clode stats:
    key(ctrl-u)
    insert("/stats")
clode status:
    key(ctrl-u)
    insert("/status")
clode status line:
    key(ctrl-u)
    insert("/statusline")
clode tasks:
    key(ctrl-u)
    insert("/tasks")
clode teleport:
    key(ctrl-u)
    insert("/teleport")
clode theme:
    key(ctrl-u)
    insert("/theme")
clode to dos:
    key(ctrl-u)
    insert("/todos")
clode usage:
    key(ctrl-u)
    insert("/usage")
clode vim:
    key(ctrl-u)
    insert("/vim")

# Keyboard shortcuts
clode cancel: key(ctrl-c)
clode verbose: key(ctrl-o)
clode background: key(ctrl-b)
clode task list: key(ctrl-t)
clode editor: key(ctrl-g)
clode search: key(ctrl-r)
clode (mode | toggle mode): key(shift-tab)
clode thinking: key(alt-t)
clode paste image: key(ctrl-v)

# Custom slash commands
clode slash <user.text>:
    key(ctrl-u)
    insert("/{user.formatted_text(text, 'DASH_SEPARATED')}")

# Quick prefixes
clode bash:
    key(ctrl-u)
    insert("! ")
