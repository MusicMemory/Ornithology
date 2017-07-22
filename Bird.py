class Bird:
    def __init__(self,filename,name,order,difficulty):
        #in python gint es keine expliziten konstruktoren
        #__name meint private, _name protected, name public 
        self.__filename=filename 
        self.__name=name
        self.__order=order
        self.__difficulty=difficulty

    def get_filename(self):
        return self.__filename

    def get_name(self):
        return self.__name

    def get_order(self):
        return self.__order

    def get_difficulty(self):
        return self.__difficulty
