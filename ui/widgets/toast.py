from __future__ import annotations

from PySide6.QtCore import (
    Qt,
    QTimer,
    QPropertyAnimation,
    QEasingCurve,
    Signal,
)
from PySide6.QtGui import QColor, QPainter, QPainterPath
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QHBoxLayout,
    QGraphicsOpacityEffect,
    QSizePolicy,
)


class Toast(QWidget):
    """
    Professional toast notification widget.

    Usage:
        toast = Toast(parent, "Customer saved.", "success")
        toast.show_toast()
    """

    closed = Signal(object)

    SUCCESS = "success"
    ERROR = "error"
    WARNING = "warning"
    INFO = "info"

    COLORS = {
        SUCCESS: "#16a34a",
        ERROR: "#dc2626",
        WARNING: "#f59e0b",
        INFO: "#2563eb",
    }

    ICONS = {
        SUCCESS: "✓",
        ERROR: "✕",
        WARNING: "⚠",
        INFO: "ℹ",
    }

    def __init__(
        self,
        parent=None,
        message: str = "",
        toast_type: str = INFO,
        duration: int = 3000,
    ):
        super().__init__(parent)

        self.message = message
        self.toast_type = toast_type
        self.duration = duration

        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint
            | Qt.WindowType.Tool
            | Qt.WindowType.WindowStaysOnTopHint
        )

        self.setFixedWidth(360)
        self.setSizePolicy(
            QSizePolicy.Policy.Fixed,
            QSizePolicy.Policy.Minimum
        )

        self._build_ui()
        self._setup_animation()

    # ---------------------------------------------------------
    # UI
    # ---------------------------------------------------------

    def _build_ui(self):
        self.container = QWidget(self)
        self.container.setObjectName("toastContainer")

        color = self.COLORS.get(
            self.toast_type,
            self.COLORS[self.INFO]
        )

        self.container.setStyleSheet(
            f"""
            QWidget#toastContainer {{
                background-color: #ffffff;
                border-left: 6px solid {color};
                border-radius: 12px;
                border: 1px solid #e5e7eb;
            }}
            """
        )

        layout = QHBoxLayout(self.container)
        layout.setContentsMargins(14, 12, 14, 12)
        layout.setSpacing(12)

        self.icon_label = QLabel(
            self.ICONS.get(self.toast_type, "ℹ")
        )
        self.icon_label.setStyleSheet(
            f"""
            QLabel {{
                color: {color};
                font-size: 18px;
                font-weight: 700;
            }}
            """
        )
        self.icon_label.setFixedWidth(24)

        self.message_label = QLabel(self.message)
        self.message_label.setWordWrap(True)
        self.message_label.setStyleSheet(
            """
            QLabel {
                color: #111827;
                font-size: 13px;
                font-weight: 500;
                background: transparent;
                border: none;
            }
            """
        )

        layout.addWidget(self.icon_label)
        layout.addWidget(self.message_label)

        outer = QHBoxLayout(self)
        outer.setContentsMargins(0, 0, 0, 0)
        outer.addWidget(self.container)

        self.adjustSize()

    # ---------------------------------------------------------
    # Animation
    # ---------------------------------------------------------

    def _setup_animation(self):
        self.opacity_effect = QGraphicsOpacityEffect(self)
        self.setGraphicsEffect(self.opacity_effect)

        self.fade_in = QPropertyAnimation(
            self.opacity_effect,
            b"opacity",
            self,
        )
        self.fade_in.setDuration(250)
        self.fade_in.setStartValue(0.0)
        self.fade_in.setEndValue(1.0)
        self.fade_in.setEasingCurve(
            QEasingCurve.Type.OutCubic
        )

        self.fade_out = QPropertyAnimation(
            self.opacity_effect,
            b"opacity",
            self,
        )
        self.fade_out.setDuration(250)
        self.fade_out.setStartValue(1.0)
        self.fade_out.setEndValue(0.0)
        self.fade_out.setEasingCurve(
            QEasingCurve.Type.InCubic
        )

        self.fade_out.finished.connect(self._finish_close)

    # ---------------------------------------------------------
    # Public API
    # ---------------------------------------------------------

    def show_toast(self):
        self.opacity_effect.setOpacity(0)
        self.show()
        self.raise_()
        self.fade_in.start()

        QTimer.singleShot(
            self.duration,
            self.close_toast
        )

    def close_toast(self):
        if self.fade_out.state():
            return
        self.fade_out.start()

    # ---------------------------------------------------------
    # Internal
    # ---------------------------------------------------------

    def _finish_close(self):
        self.hide()
        self.closed.emit(self)
        self.deleteLater()

    # ---------------------------------------------------------
    # Rounded edges
    # ---------------------------------------------------------

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(
            QPainter.RenderHint.Antialiasing
        )

        path = QPainterPath()
        path.addRoundedRect(
            self.rect(),
            12,
            12,
        )

        painter.fillPath(
            path,
            QColor(0, 0, 0, 0)
        )

        super().paintEvent(event)