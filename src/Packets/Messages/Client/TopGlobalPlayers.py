from random import choice
from string import ascii_uppercase
import json

from Logic.Player import Players
from Packets.Messages.Server.TopGlobalPlayersData import TopGlobalPlayersData

from Utils.Reader import BSMessageReader


class TopGlobalPlayers(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.player.LeaderboardType = self.read_Vint()
        self.player.LeaderboardInfo = self.read_Vint()

    def process(self):
        TopGlobalPlayersData(self.client, self.player).send()