from xboxapi import Client

client = Client(api_key="963c54c1ade7e21efa9b2ce8c6aaac736d9f284f")
gamer = client.gamer('Joshmoo2012')
print(gamer)

presence = gamer.get('presence')
print(presence)