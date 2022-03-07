class Sample:
    
    #def __init__(self,name):
    #    self.name=name

    #def __init__(slf,name):
    #    slf.name=name

    def __init__(Vaishnavi,name):
        Vaishnavi.name=name 

        # that means slf and name itself(which I'm passing )are doing the same job as self     

vm=Sample("Vaishnavi")

print(vm.name)