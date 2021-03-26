class ListKeeper:
    
    def __init__(self):
        '''Initalization'''
        self.Keeper = {"example" : [1, 2, 3, 4, 5]}
        
    def show(self):
        '''Show every name of the lists'''
        print("Lists :")
        for i in self.Keeper:
            print("- ", i)

    def add(self, name, list):
        '''Add a new list'''
        self.Keeper[name] = list

    def delete(self, name):
        '''Delete the list'''
        del self.Keeper[name]
        
    def sort(self, name):
        '''Sort the list'''
        sortedList = self.Keeper[name]
        sortedList.sort()
        print(sortedList)
        
    def append(self, name, list):
        '''Appends two lists to have one list at the end'''
        newList = self.Keeper[name]
        newList.extend(list)
