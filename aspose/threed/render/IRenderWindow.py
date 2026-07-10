class IRenderWindow:
    """Interface for render window."""
    
    def __init__(self):
        raise NotImplementedError("IRenderWindow is not implemented")
    
    def show(self):
        raise NotImplementedError("IRenderWindow.show is not implemented")
    
    def close(self):
        raise NotImplementedError("IRenderWindow.close is not implemented")
