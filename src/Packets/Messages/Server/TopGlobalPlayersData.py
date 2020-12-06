from Utils.Writer import Writer


class TopGlobalPlayersData(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24403
        self.player = player

    def encode(self):
        self.writeVint(1)
        self.writeVint(0)
        self.writeVint(0)
        self.writeString()
        
        self.writeVint(1)
        
        self.writeVint(0)
        self.writeVint(1)
        
        self.writeVint(1)       
        self.writeVint(9999)
        
        self.writeVint(1)
        
        self.writeString()
        self.writeString("Mr Vitalik")
        
        self.writeVint(1)
        self.writeVint(28000000 + self.player.profileIcon)
        self.writeVint(43000000 + self.player.namecolor)
        self.writeVint(0)
        
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        
        self.writeString("IL")
        print("[INFO] Message TopGlobalPlayersData has been sent.")