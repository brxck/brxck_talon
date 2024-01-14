from talon import Context, Module

mod = Module()
ctx = Context()

mod.list("botler_command", desc="Botler commands")
ctx.lists["user.botler_command"] = {
    "diff": "diff",
    "peek": "peek",
    "release": "release",
    "livestage": "livestage",
}

mod.list("solv_repository", desc="Solv repository names")
ctx.lists["user.solv_repository"] = {
    "dappy tasks": "dapi-tasks",
    "dappy": "dapi",
    "jigsaw": "jigsaw",
    "manage": "manage-dev",
    "mapp": "mapp-dev",
    "release": "release",
    "schema": "schema",
    "turbo provider": "turbo-provider",
    "turbo consumer": "turbo-consumer",
}
