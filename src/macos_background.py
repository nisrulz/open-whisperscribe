"""
macOS-specific configuration to prevent the app icon from appearing in the Dock.
This must be called before any GUI-related imports.
"""
import os
import sys


def configure_background_app():
    """
    Configure the application to run as a background-only app on macOS.
    This prevents the bouncing icon from appearing in the Dock.
    """
    if sys.platform == 'darwin':  # macOS
        os.environ['PYTHONHIDEICON'] = '1'
        # Set the app as a background-only app
        try:
            import AppKit
            info = AppKit.NSBundle.mainBundle().infoDictionary()
            info['LSUIElement'] = '1'
        except ImportError:
            pass  # AppKit not available, skip
