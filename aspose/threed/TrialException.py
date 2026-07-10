class TrialException(Exception):
    """This is raised in Scene.Open/Scene.Save when no licenses are applied.
    You can turn off this exception by setting SuppressTrialException to true."""

    _suppress_trial_exception = False

    @staticmethod
    def set_suppress_trial_exception(value: bool):
        """Sets whether to suppress trial exception for unlicensed usage."""
        TrialException._suppress_trial_exception = bool(value)

    @property
    def suppress_trial_exception(self) -> bool:
        """Gets whether trial exception is suppressed."""
        return TrialException._suppress_trial_exception

    def __init__(self, msg: str = None):
        if msg is None:
            super().__init__()
        else:
            super().__init__(msg)
