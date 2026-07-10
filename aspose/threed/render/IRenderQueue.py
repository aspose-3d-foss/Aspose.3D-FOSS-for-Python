class IRenderQueue:
    """Interface for render queue."""
    
    def __init__(self):
        raise NotImplementedError("IRenderQueue is not implemented")
    
    def add_draw_call(self, command_list):
        raise NotImplementedError("IRenderQueue.add_draw_call is not implemented")
    
    def submit(self):
        raise NotImplementedError("IRenderQueue.submit is not implemented")
