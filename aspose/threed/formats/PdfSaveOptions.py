class PdfSaveOptions:
    """Save options for PDF"""

    def __init__(self):
        self._lighting_scheme = None
        self._render_mode = None

    @property
    def lighting_scheme(self):
        return self._lighting_scheme

    @lighting_scheme.setter
    def lighting_scheme(self, value):
        self._lighting_scheme = value

    @property
    def render_mode(self):
        return self._render_mode

    @render_mode.setter
    def render_mode(self, value):
        self._render_mode = value
