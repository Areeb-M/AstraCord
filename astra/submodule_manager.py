from .submodule_commands import *
from core import *
import re

@Bot.register_command
@level_user
async def module(bot, message, argument):
    args = argument.split(' ', 1)
    subcommand = args.pop(0)
    if subcommand == "create":
        create_submodule(args, message)
    elif subcommand == "archive":
        archive_submodule(args, message)
    elif subcommand == "unarchive":
        unarchive_submodule(args,message)
