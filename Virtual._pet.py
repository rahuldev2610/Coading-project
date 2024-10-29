class virtualpet:
    def __init__(self,name):
        self.name=name
        self.mood="happy"
    
    def feed(self):
        self.mood="full"
        print(f"{self.name}is full and happy!")
    
    def play(self):
        self.mood="exited"
        print(f"{self.name} is playing and very exited!")

    def sleep(self):
        self.mood="sleepy"
        print(f"{self.name} is now sleepy")


pet= virtualpet("Buddy")
pet.feed()
pet.play()
pet.sleep()
    
    