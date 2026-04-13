class Human:
    def __init__(self,height):
        self.height = height
    def __len__(self):
        return self.height+50
    
sj = Human(182)
print(len(sj))
