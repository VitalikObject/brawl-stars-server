from Utils.Writer import Writer


class TopGlobalPlayersData(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24403
        self.player = player

    def encode(self):
        self.writeVint(self.player.LeaderboardInfo)
        self.writeVint(0)
        self.writeVint(0)
        if self.player.LeaderboardType == 0:
        	self.writeString()
        else:
        	self.writeString("IL")

        if self.player.LeaderboardInfo == 0:
        	self.writeVint(1)
        
        	self.writeVint(0)
        	self.writeVint(1)
        
        	self.writeVint(1)       
       		self.writeVint(self.player.trophies)
        
        	self.writeVint(1)
        
        	self.writeString()
        	self.writeString("Mr Vitalik")
        
        	self.writeVint(1)
        	self.writeVint(28000000 + self.player.profileIcon)
        	self.writeVint(43000000 + self.player.namecolor)
        	self.writeVint(0)
        elif self.player.LeaderboardInfo == 1:
        	self.writeVint(1)
        
        	self.writeVint(0)
        	self.writeVint(1)
        
        	self.writeVint(1)       
       		self.writeVint(self.player.trophies)
        
        	self.writeVint(1)
        
        	self.writeString()
        	self.writeString("Mr Vitalik")
        
        	self.writeVint(1)
        	self.writeVint(28000000 + self.player.profileIcon)
        	self.writeVint(43000000 + self.player.namecolor)
        	self.writeVint(0)
        elif self.player.LeaderboardInfo == 2:

        	self.writeVint(1)
        
        	self.writeVint(0)
        	self.writeVint(1)
        
        	self.writeVint(1)       
       		self.writeVint(99999)       
        	self.writeVint(2)
        
        	self.writeString("ObjectTeam")
        	self.writeVint(1)
        
        	self.writeVint(8)
        	self.writeVint(5)

        
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        
        self.writeString("IL")
        print("[INFO] Message TopGlobalPlayersData has been sent.")