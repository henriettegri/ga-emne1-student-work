#Tilgang på et spill

has_username = True
accepted_rules = True
is_blocked = False

can_enter = has_username and accepted_rules and not is_blocked
print(can_enter)


