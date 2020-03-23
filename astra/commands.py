from core import *


@Bot.register_command
@level_user
async def echo(bot, message, argument):
    await message.channel.send(argument)


@Bot.register_command
@level_mod
async def purge(bot, message, argument):
    limit = 100
    try:
        if len(argument) > 0:
            limit = int(argument)
    except ValueError:
        log("[Bot] Incorrect argument format.")
        # TODO: proper error messages
    try:
        await message.channel.purge(limit=limit)

    except discord.errors.Forbidden:
        log("[Bot] Insufficient permissions.")
        # TODO: proper error message


@Bot.register_command
@level_admin
async def prefix(bot, message, argument):
    new_prefix = argument.split(" ")[0]  # Filter out any white spaces before and after the prefix
    bot.register_config_variable('prefix', new_prefix, overwrite=True)
    await message.channel.send(f"Prefix changed to `{bot.value('prefix')}`!")
    log(f"[Bot] Prefix changed to {bot.value('prefix')}")
