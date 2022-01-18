
class Word(str):
    """The Word class inherits from the str class. Which means it
    gets everything from the str class plus whatever it defines.
    So we will redefine <, >, <=, >= so that a Word is compared
    by length, not alphabetically.
    
    NOTE: Technically, all we need to enable sorting is __lt__, but
    it would be odd to not define the others as we'd have a case where 
    < and > would return the same answer!
    """

    def __lt__(self, other):
        return len(self) < len(other)
    
    
    def __gt__(self, other):
        return len(self) > len(other)
    
    
    def __le__(self, other):
        return len(self) <= len(other)
    
    
    def __ge__(self, other):
        return len(self) >= len(other)
  
    
    def __eq__(self, other):
        return len(self) == len(other)
