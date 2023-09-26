class time:
    def __init__(self, discord_name, Military_Time, datetime):
        self.discord_name = discord_name
        self.Military_Time = Military_Time
        self.time = datetime.datetime.now().strftime('%H:%M:%S')

    def opject(self):
        return self.