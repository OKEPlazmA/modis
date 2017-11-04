import logging
import os
import tkinter as tk
import tkinter.ttk as ttk

from .._tools import helptools

logger = logging.getLogger(__name__)


class ModuleUIFrame(ttk.Frame):
    """The UI for the gamedeals module"""

    def __init__(self, parent):
        """
        Create a new UI for the module

        Args:
            parent: A tk or ttk object
        """

        super(ModuleUIFrame, self).__init__(parent, padding=8)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        # API Frame
        api_frame = ttk.LabelFrame(self, padding=8, text="Google API")
        api_frame.grid(row=0, column=0, sticky="W E N S")
        api_frame.columnconfigure(0, weight=1)
        # Add key field
        self.reddit_api_user_agent = tk.StringVar()
        ttk.Label(api_frame, text="Reddit API User Agent").grid(column=0, row=0, sticky="W E N S")
        ttk.Entry(api_frame, textvariable=self.reddit_api_user_agent).grid(
            column=0, row=1, padx=4, pady=4, sticky="W E N S")
        self.reddit_api_client_id = tk.StringVar()
        ttk.Label(api_frame, text="Reddit API Client ID").grid(column=0, row=2, sticky="W E N S")
        ttk.Entry(api_frame, textvariable=self.reddit_api_client_id).grid(
            column=0, row=3, padx=4, pady=4, sticky="W E N S")
        self.reddit_api_client_secret = tk.StringVar()
        ttk.Label(api_frame, text="Reddit API Client Secret").grid(column=0, row=4, sticky="W E N S")
        ttk.Entry(api_frame, textvariable=self.reddit_api_client_secret).grid(
            column=0, row=5, padx=4, pady=4, sticky="W E N S")
        # Update keys button
        ttk.Button(api_frame, command=lambda: self.update_google_key(), text="Update API Data").grid(
            column=0, row=6, padx=4, pady=4, sticky="W E N S")

        # Set default values
        from ....datatools import get_data
        data = get_data()

        if "reddit_api_user_agent" in data["discord"]["keys"]:
            self.reddit_api_user_agent.set(data["discord"]["keys"]["reddit_api_user_agent"])
        if "reddit_api_client_id" in data["discord"]["keys"]:
            self.reddit_api_client_id.set(data["discord"]["keys"]["reddit_api_client_id"])
        if "reddit_api_client_secret" in data["discord"]["keys"]:
            self.reddit_api_client_secret.set(data["discord"]["keys"]["reddit_api_client_secret"])

        # Help frame
        help_frame = ttk.LabelFrame(self, padding=8, text="Help")
        help_frame.grid(row=1, column=0, sticky="W E N S")
        help_frame.columnconfigure(0, weight=1)
        help_frame.rowconfigure(0, weight=1)
        # Find the help path
        _dir = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__)))
        help_path = "{}/{}".format(_dir, "_help.json")
        # Load the text
        helptools.add_help_text(help_frame, help_path)

    def update_google_key(self):
        """Updates the Google API key with the text value"""
        from ...main import add_api_key
        add_api_key("reddit_api_user_agent", self.reddit_api_user_agent.get())
        add_api_key("reddit_api_client_id", self.reddit_api_client_id.get())
        add_api_key("reddit_api_client_secret", self.reddit_api_client_secret.get())