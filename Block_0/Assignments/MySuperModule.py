class ListKeeper:
    pass
    
    def __init__(self):
        self.Keeper = {"example" : [1, 2, 3, 4, 5]}
        
    def show(self):
        print("Lists :")
        for i in self.Keeper:
            print("- ", i)

    def add(self, name, list):
        self.Keeper[name] = list

    def delete(self, name):
        del self.Keeper[name]
        
    def sort(self, name):
        sortedList = self.Keeper[name]
        sortedList.sort()
        print(sortedList)
        
    def append(self, name, list):
        newList = self.Keeper[name]
        newList.extend(list)
        print(newList)
