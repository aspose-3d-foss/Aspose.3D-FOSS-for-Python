class CompareFunction:
    """Compare function for depth/stencil testing."""
    
    NEVER = None
    LESS = None
    EQUAL = None
    LESS_EQUAL = None
    GREATER = None
    NOT_EQUAL = None
    GREATER_EQUAL = None
    ALWAYS = None


# Initialize enum values
CompareFunction.NEVER = CompareFunction()
CompareFunction.LESS = CompareFunction()
CompareFunction.EQUAL = CompareFunction()
CompareFunction.LESS_EQUAL = CompareFunction()
CompareFunction.GREATER = CompareFunction()
CompareFunction.NOT_EQUAL = CompareFunction()
CompareFunction.GREATER_EQUAL = CompareFunction()
CompareFunction.ALWAYS = CompareFunction()
