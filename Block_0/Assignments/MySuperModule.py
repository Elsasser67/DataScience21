class ListKeeper:
    pass
    
    def __init__(self):
        self.Keeper = {"example" : [1, 2, 3, 4, 5]}
        
    def show(self):
        nb = 0
        for i,j in self.Keeper.items():
            nb+=1
            print("Name of List ", nb, " :")
            print(i)

    def add(self,name, list):
        self.Keeper[name] = list

    def delete(self, name):
        del self.Keeper[name]
        
    def sort(self,name):
        self.Keeper

    def append(self,name, list):
        pass
