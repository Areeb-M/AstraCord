from core import *


class Submodule:
    def __init__(self, name, structure, archived):
        self.name = name
        self.structure = structure
        self.archived = archived


'''
@Bot.initialization_sequence
def initialize_manager(bot):
    try:
        data_file_path = bot.data_path + '\\submodules.txt'
        with open(data_file_path) as data_file:
            pass
    except IOError:
        log("[Bot] Submodules datafile corrupted or ")'''


@Bot.register_command
@level_user
async def module(bot, message, argument):
    args = argument.split(' ', 1)
    subcommand = args.pop(0)
    if subcommand == "create":
        try:
            name = args[0]
            guild = message.guild

            category = await guild.create_category_channel(name)
            await guild.create_text_channel(f"{name}-general", category=category)
            await guild.create_text_channel(f"{name}-resources", category=category)
            await guild.create_voice_channel(f"{name.replace(' ', '-').lower()}-voice", category=category)
            # For some reason, voice channels do not have the same naming restriction as text channels,
            # which is the reason for the string manipulation in that last command.
        except KeyError:
            log("[Bot] Not enough arguments for module create command!")
            # TODO: error relaying to users

        except discord.Forbidden:
            log("[Bot] Insufficient permissions to create submodule channels.")
            # TODO: error relaying to users
