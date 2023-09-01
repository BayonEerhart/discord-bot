import time
from discord_rpc import Client, Presence

def update_presence():
    client_id = 'your_client_id'  # Replace this with your actual client ID
    rpc = Client(client_id)

    rpc.connect()
    
    presence = Presence(client_id)
    presence.state = "Playing Solo"
    presence.details = "Competitive"
    presence.start = 1507665886
    presence.end = 1507665886
    presence.large_image_text = "Numbani"
    presence.small_image_text = "Rogue - Level 100"
    presence.party_id = "ae488379-351d-4a4f-ad32-2b9b01c91657"
    presence.party_size = 1
    presence.party_max = 5
    presence.join_secret = "MTI4NzM0OjFpMmhuZToxMjMxMjM="
    
    rpc.update(presence)

    rpc.close()

update_presence()