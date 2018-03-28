from xboxapi import Client

client = Client(api_key="ff54cea91a150f202ff7951cad47ff5b027f46b9")

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
    return _diff > 0, _diff

result = _am_i_behind()

print("You are %s behind" % ("not" if result[0] else ""))
print("There is %s Gamerscore between you and Jack" % (result[1]))
