import random

class City:
    def __init__(self,x,y,num):
        self.x = x
        self.y = y
        self.number = num
        
    def display(self):
        fill(0,155,105)
        ellipse(self.x, self.y, 10, 10)
        
        textSize(20)
        text(self.number,self.x-10,self.y-10)
        noFill()

class Route:
    def __init__(self):
        self.distance = 0
        self.cityNums = random.sample(list(range(NO_CITIES)),NO_CITIES)  
        
    def display(self):
        strokeWeight(3)
        stroke(150,10,25)
        beginShape()
        for i in self.cityNums:
            vertex(cities[i].x, cities[i].y)
            cities[i].display()
        endShape(CLOSE)
        
    def calcLength(self):
        self.distance = 0
        for i, num in enumerate(self.cityNums):
            self.distance += dist(cities[num].x, cities[num].y, cities[self.cityNums[i-1]].x, cities[self.cityNums[i-1]].y)
        return self.distance   
    
    def mutateN(self,num):
       indices = random.sample(list(range(NO_CITIES)),num)
       child = Route()
       child.cityNums = self.cityNums[::]
       
       for i in range(num-1):
           child.cityNums[indices[i]], child.cityNums[indices[(i+1)%num]] = child.cityNums[indices[(i+1)%num]], child.cityNums[indices[i]]
       return child 
        
    
    
NO_CITIES = 13
        
cities = []
random_improvements = 0
mutated_improvements = 0

def setup():
    global best, record_distance
    size(600,600)
    for i in range(NO_CITIES):
        cities.append(City(random.randint(50,width-50),random.randint(50,height-50), i))
    
    best = Route()
    record_distance = best.calcLength()
        
def draw():
    global best, record_distance, random_improvements
    global mutated_improvements
    background(0)
    best.display()

    route1= Route()
    length1 = route1.calcLength()
    fill(12,203,100)
    text("random "+str(random_improvements),150,550)
    text("mutation "+str(mutated_improvements),300,550)
    text("distance = "+str(int(record_distance)),150,580)
    
    if length1 < record_distance:
        record_distance = length1
        best = route1
        textSize(25)
        random_improvements += 1
     
    for i in range(2,9):
        mutated = Route()
        mutated.cityNums = best.cityNums[::]
        mutated = mutated.mutateN(i)
        length2 = mutated.calcLength()
        if length2 < record_distance:
            record_distance = length2
            best = mutated
            mutated_improvements += 1
