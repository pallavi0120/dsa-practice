class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        l,r=0,0
        while l<len(trainers) and r<len(players):
            if trainers[l]>=players[r]:
                r+=1
            l+=1
        return r
