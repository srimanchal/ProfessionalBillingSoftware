from __future__ import annotations

from PySide6.QtCore import QPoint

from ui.widgets.toast import Toast


class ToastManager:
    """
    Global toast manager.

    Example:
        toast_manager.success(
            self,
            "Customer saved successfully."
        )
    """

    MARGIN_RIGHT = 20
    MARGIN_TOP = 20
    SPACING = 12

    def __init__(self):
        self.active_toasts = []

    # ---------------------------------------------------------
    # Generic
    # ---------------------------------------------------------

    def show(
        self,
        parent,
        message: str,
        toast_type: str = Toast.INFO,
        duration: int = 3000,
    ):
        if parent is None:
            return

        toast = Toast(
            parent=parent,
            message=message,
            toast_type=toast_type,
            duration=duration,
        )

        toast.closed.connect(
            self._remove_toast
        )

        self.active_toasts.append(toast)

        self._reposition(parent)

        toast.show_toast()

    # ---------------------------------------------------------
    # Convenience methods
    # ---------------------------------------------------------

    def success(
        self,
        parent,
        message: str,
        duration: int = 3000,
    ):
        self.show(
            parent,
            message,
            Toast.SUCCESS,
            duration,
        )

    def error(
        self,
        parent,
        message: str,
        duration: int = 4000,
    ):
        self.show(
            parent,
            message,
            Toast.ERROR,
            duration,
        )

    def warning(
        self,
        parent,
        message: str,
        duration: int = 3500,
    ):
        self.show(
            parent,
            message,
            Toast.WARNING,
            duration,
        )

    def info(
        self,
        parent,
        message: str,
        duration: int = 3000,
    ):
        self.show(
            parent,
            message,
            Toast.INFO,
            duration,
        )

    # ---------------------------------------------------------
    # Positioning
    # ---------------------------------------------------------

    def _reposition(self, parent):
        y = self.MARGIN_TOP

        for toast in self.active_toasts:
            toast.adjustSize()

            x = (
                parent.width()
                - toast.width()
                - self.MARGIN_RIGHT
            )

            toast.move(QPoint(x, y))

            y += (
                toast.height()
                + self.SPACING
            )

    # ---------------------------------------------------------
    # Cleanup
    # ---------------------------------------------------------

    def _remove_toast(self, toast):
        if toast in self.active_toasts:
            parent = toast.parent()

            self.active_toasts.remove(toast)

            if parent:
                self._reposition(parent)


toast_manager = ToastManager()