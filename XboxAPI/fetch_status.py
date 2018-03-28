import requests
from config import XBOX_API_CONFIG, get_session

def _am_i_behind():
    def _get_gamerscore(xuid):
        return session.get(XBOX_API_CONFIG._API_URL +'/'+ str(xuid) +'/'+ 'profile').json()['Gamerscore']

    session = get_session()
    jos_xuid = session.get(XBOX_API_CONFIG._API_URL + '/xuid/' + XBOX_API_CONFIG._JOSH_GAMERTAG).json()
    jac_xuid = session.get(XBOX_API_CONFIG._API_URL + '/xuid/' + XBOX_API_CONFIG._JACK_GAMERTAG).json()
    
    _diff = _get_gamerscore(jos_xuid) - _get_gamerscore(jac_xuid)
    return _diff > 0, _diff

result = _am_i_behind()

print("You are %s behind" % ("not" if result[0] else ""))
print("There is %s Gamerscore between you and Jack" % (result[1]))
