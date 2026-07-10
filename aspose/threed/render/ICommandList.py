class ICommandList:
    """Interface for command list."""
    
    def __init__(self):
        raise NotImplementedError("ICommandList is not implemented")
    
    def set_vertex_buffer(self, buffer, offset):
        raise NotImplementedError("ICommandList.set_vertex_buffer is not implemented")
    
    def set_index_buffer(self, buffer, offset, index_type):
        raise NotImplementedError("ICommandList.set_index_buffer is not implemented")
    
    def draw(self, vertex_count, instance_count, start_vertex, start_instance):
        raise NotImplementedError("ICommandList.draw is not implemented")
    
    def draw_indexed(self, index_count, instance_count, start_index, base_vertex, start_instance):
        raise NotImplementedError("ICommandList.draw_indexed is not implemented")
