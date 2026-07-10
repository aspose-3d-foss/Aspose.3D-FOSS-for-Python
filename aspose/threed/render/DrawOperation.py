class DrawOperation:
    """Draw operation type."""
    
    POINT_LIST = None
    LINE_LIST = None
    LINE_STRIP = None
    TRIANGLE_LIST = None
    TRIANGLE_STRIP = None
    TRIANGLE_FAN = None


# Initialize enum values
DrawOperation.POINT_LIST = DrawOperation()
DrawOperation.LINE_LIST = DrawOperation()
DrawOperation.LINE_STRIP = DrawOperation()
DrawOperation.TRIANGLE_LIST = DrawOperation()
DrawOperation.TRIANGLE_STRIP = DrawOperation()
DrawOperation.TRIANGLE_FAN = DrawOperation()
