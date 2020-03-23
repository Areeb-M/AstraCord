from enum import Enum


#####################
#   Permissions
#####################


class Permission(Enum):
    USER = 1
    MOD = 2
    ADMIN = 3


def level_user(func):
    func.permission = Permission.USER
    return func


def level_mod(func):
    func.permission = Permission.MOD
    return func


def level_admin(func):
    func.permission = Permission.ADMIN
    return func
