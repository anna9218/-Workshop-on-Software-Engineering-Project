from enum import Enum


class ManagerPermission(Enum):
    EDIT_INV = 1
    EDIT_POLICIES = 2
    APPOINT_OWNER = 3
    DEL_OWNER = 4  # you can delete only the one's you appoint
    APPOINT_MANAGER = 5
    EDIT_MANAGER_PER = 6
    DEL_MANAGER = 7
    CLOSE_STORE = 8
    USERS_QUESTIONS = 9
    WATCH_PURCHASE_HISTORY = 10
