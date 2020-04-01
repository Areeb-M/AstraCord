from core import *
import re

def create_submodule(args, message):
    try:
        # names being lowercase should help with manipulating submodules later
        name = args[0].lower()
        guild = message.guild

        category = await guild.create_category_channel(name)
        await guild.create_text_channel(f"{name}-general", category=category)
        await guild.create_text_channel(f"{name}-resources", category=category)
        await guild.create_voice_channel(f"{name.replace(' ', '-')}-voice", category=category)
        # For some reason, voice channels do not have the same naming restriction as text channels,
        # which is the reason for the string manipulation in that last command.
    except KeyError:
        log("[Bot] Not enough arguments for module create command!")
        # TODO: error relaying to users
        return 1

    except discord.Forbidden:
        log("[Bot] Insufficient permissions to create submodule channels.")
        # TODO: error relaying to users
        return 1

def archive_submodule(args, message):
    try:
        name = args[0].lower()
        guild = message.guild

        category = None
        for c in guild.categories:
            if c.name == name:
                category = c
                break
        if category is None:
            log("[Bot] No submodule with that name found.")
        else:
            archive = None
            for c in guild.categories:
                if c.name == 'archive':
                    archive = c
                    break
            if archive is None:
                archive = await guild.create_category_channel('archive')

            for channel in category.channels:
                if channel.type != discord.ChannelType.voice:
                    await channel.edit(category=archive)
                else:
                    await channel.delete()
            await category.delete()
    except KeyError:
        log("[Bot] Insufficient arguments to archive submodule channels.")
        # TODO: error relaying to users            

def unarchive_submodule(args, message):
    try:
        name = args[0].lower()
        guild = message.guild

        category = None
        for c in guild.categories:
            if c.name == name:
                category = c
                break

            archive = None
            for c in guild.categories:
                if c.name == 'archive':
                    archive = c
                    break
            if archive is None:
                log("[Bot] Nothing is archived.")

        category = await guild.create_category_channel(name)
        #Turn the name into regex to find all channels of that type
        replaced_name = name.lower().replace(' ', '')
        for channel in archive.channels:
            if replaced_name in channel.name.replace('-',''):
                await channel.edit(category=category)
        await guild.create_voice_channel(f"{name.replace(' ', '-')}-voice", category=category)

    except KeyError:
        log("[Bot] Insufficient arguments to unarchive submodule channels.")
        # TODO: error relaying to users