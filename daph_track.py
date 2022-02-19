import math
class daph_track:
    X = 0
    Y = 0
    dist_trash = 100
    
    neighbors = []


    x_speed = 0
    y_speed = 0

    def __init__(self, x, y, distance_trashold):
        self.X = x
        self.Y = y
        self.dist_trash = distance_trashold

    def get_dist(self, other_daph):
        return math.sqrt((other_daph.X-self.X)*(other_daph.X-self.X)+(other_daph.Y-self.Y)*(other_daph.Y-self.Y))

    def get_speed_diff(self, other_daph):
        return math.sqrt(((other_daph.X-self.X)-self.x_speed)*((other_daph.X-self.X)-self.x_speed)+((other_daph.Y-self.Y)-self.y_speed)*((other_daph.Y-self.Y)-self.y_speed))

    def find_self(self, arr_of_daphny_on_new_frame):
        scoor_list = []

        for i in range(0,len(arr_of_daphny_on_new_frame)) :
            daph = arr_of_daphny_on_new_frame[i]
            if (self.get_dist(daph)<self.dist_trash):
                self.neighbors.append([i,daph])


        

        for i in range(0,len(self.neighbors)):
            daph = self.neighbors[i][1]
            scoor_list.append([self.neighbors[i][0], self.get_dist(daph)+(self.get_speed_diff(daph)/2)])
        scoor_list.sort(key=lambda d: d[1])


        index = scoor_list[0][0]
        return(index)

D=daph_track(0,0,20)
D1=daph_track(0,5,20)
D2=daph_track(0,1,20)
daa = [D1,D2]
print(D.find_self(daa))
