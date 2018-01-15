from xboxapi import Client

client = Client(api_key="1eb21143c5fe1b7be233c69116771538bebd847d")

#presence = gamer.get('presence')
#profile = gamer.get('profile')


def _am_i_behind():
    def _get_gamerscore(gamer):
        profile = gamer.get('profile') 
        return profile['Gamerscore']

    def _print_activity(gamer):
        presence = gamer.get('presence')
        log = dict()
        log['status'] = presence.get('status', '')
        log['game'] = presence.get('titles', {})[1].get('name', '')
        print(log)

    g_Josh = client.gamer('Joshmoo2012')
    presence = g_Josh.get('presence')
    log = dict()
    log['status'] = presence.get('status', '')
    log['game'] = presence.get('titles', {})[1].get('name', '')
    print(log)
    g_Jack = client.gamer('xXxSausageShark')
    
    _print_activity(g_Jack)
    
    _diff = _get_gamerscore(g_Josh) - _get_gamerscore(g_Jack)
    if _diff > 0:
        return True
    return False

_am_i_behind()