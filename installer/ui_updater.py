class UIUpdater:
    def __init__(self, panel_manager):
        self.panel_manager = panel_manager

    def update_panel_message(self, panel, message):
        """Updates the message on the given panel."""
        panel.update_message(message)
