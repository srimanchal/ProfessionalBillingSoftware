from __future__ import annotations

from PySide6.QtCore import (
    Qt,
    QTimer,
    QPropertyAnimation,
    QEasingCurve,
)
from PySide6.QtGui import (
    QColor,
    QFont,
    QLinearGradient,
    QPainter,
    QPen,
)
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QProgressBar,
    QGraphicsOpacityEffect,
)


class SplashScreen(QWidget):
    """
    Professional ERP Splash Screen.

    Usage
    -----
    splash = SplashScreen()
    splash.show()

    # During startup
    splash.set_progress(25, "Loading database...")
    splash.set_progress(50, "Loading services...")
    splash.set_progress(100, "Starting application...")
    """

    def __init__(self):
        super().__init__()

        self._current_progress = 0

        self.setFixedSize(700, 420)
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint
            | Qt.WindowType.WindowStaysOnTopHint
        )
        self.setAttribute(
            Qt.WidgetAttribute.WA_TranslucentBackground
        )

        self._build_ui()
        self._setup_animation()

    # ==========================================================
    # UI
    # ==========================================================

    def _build_ui(self):
        self.container = QWidget(self)
        self.container.setGeometry(
            0,
            0,
            self.width(),
            self.height(),
        )

        self.container.setObjectName("container")
        self.container.setStyleSheet(
            """
            QWidget#container {
                background: white;
                border-radius: 20px;
                border: 1px solid #d1d5db;
            }
            """
        )

        layout = QVBoxLayout(self.container)
        layout.setContentsMargins(
            50,
            40,
            50,
            40,
        )
        layout.setSpacing(0)

        layout.addStretch()

        # ------------------------------------------------------
        # App Logo
        # ------------------------------------------------------

        self.logo_label = QLabel("🧾")
        self.logo_label.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )
        self.logo_label.setStyleSheet(
            """
            QLabel {
                font-size: 72px;
                border: none;
                background: transparent;
            }
            """
        )

        layout.addWidget(self.logo_label)

        # ------------------------------------------------------
        # App Name
        # ------------------------------------------------------

        self.title_label = QLabel(
            "Professional Billing Software"
        )
        self.title_label.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        title_font = QFont()
        title_font.setPointSize(20)
        title_font.setBold(True)

        self.title_label.setFont(title_font)
        self.title_label.setStyleSheet(
            """
            QLabel {
                color: #111827;
                background: transparent;
                border: none;
                padding-top: 15px;
            }
            """
        )

        layout.addWidget(self.title_label)

        # ------------------------------------------------------
        # Subtitle
        # ------------------------------------------------------

        self.subtitle_label = QLabel(
            "Smart Invoicing • Inventory • GST • Reports"
        )
        self.subtitle_label.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )
        self.subtitle_label.setStyleSheet(
            """
            QLabel {
                color: #6b7280;
                font-size: 12px;
                background: transparent;
                border: none;
                padding-top: 8px;
            }
            """
        )

        layout.addWidget(self.subtitle_label)

        layout.addStretch()

        # ------------------------------------------------------
        # Status Label
        # ------------------------------------------------------

        self.status_label = QLabel(
            "Initializing..."
        )
        self.status_label.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )
        self.status_label.setStyleSheet(
            """
            QLabel {
                color: #374151;
                font-size: 12px;
                background: transparent;
                border: none;
            }
            """
        )

        layout.addWidget(self.status_label)

        # ------------------------------------------------------
        # Progress Bar
        # ------------------------------------------------------

        self.progress_bar = QProgressBar()
        self.progress_bar.setMinimum(0)
        self.progress_bar.setMaximum(100)
        self.progress_bar.setValue(0)
        self.progress_bar.setTextVisible(False)
        self.progress_bar.setFixedHeight(12)

        self.progress_bar.setStyleSheet(
            """
            QProgressBar {
                background: #e5e7eb;
                border: none;
                border-radius: 6px;
            }

            QProgressBar::chunk {
                background: #2563eb;
                border-radius: 6px;
            }
            """
        )

        layout.addSpacing(20)
        layout.addWidget(self.progress_bar)

        # ------------------------------------------------------
        # Version
        # ------------------------------------------------------

        version_layout = QHBoxLayout()

        self.version_label = QLabel(
            "Version 1.0"
        )
        self.version_label.setStyleSheet(
            """
            QLabel {
                color: #9ca3af;
                font-size: 11px;
                background: transparent;
                border: none;
            }
            """
        )

        version_layout.addWidget(
            self.version_label,
            alignment=Qt.AlignmentFlag.AlignLeft
        )

        version_layout.addStretch()

        self.copyright_label = QLabel(
            "© Professional Billing Software"
        )
        self.copyright_label.setStyleSheet(
            """
            QLabel {
                color: #9ca3af;
                font-size: 11px;
                background: transparent;
                border: none;
            }
            """
        )

        version_layout.addWidget(
            self.copyright_label,
            alignment=Qt.AlignmentFlag.AlignRight
        )

        layout.addSpacing(15)
        layout.addLayout(version_layout)

    # ==========================================================
    # Animations
    # ==========================================================

    def _setup_animation(self):
        self.opacity_effect = (
            QGraphicsOpacityEffect(self)
        )

        self.setGraphicsEffect(
            self.opacity_effect
        )

        self.fade_in = QPropertyAnimation(
            self.opacity_effect,
            b"opacity"
        )
        self.fade_in.setDuration(500)
        self.fade_in.setStartValue(0)
        self.fade_in.setEndValue(1)
        self.fade_in.setEasingCurve(
            QEasingCurve.Type.OutCubic
        )

        self.fade_out = QPropertyAnimation(
            self.opacity_effect,
            b"opacity"
        )
        self.fade_out.setDuration(300)
        self.fade_out.setStartValue(1)
        self.fade_out.setEndValue(0)
        self.fade_out.setEasingCurve(
            QEasingCurve.Type.InCubic
        )
        self.fade_out.finished.connect(
            self.close
        )

    # ==========================================================
    # Public API
    # ==========================================================

    def start(self):
        self.show()
        self.fade_in.start()

    def finish(self):
        self.fade_out.start()

    def set_progress(
        self,
        value: int,
        message: str = "",
    ):
        value = max(
            0,
            min(
                100,
                value,
            ),
        )

        self.progress_bar.setValue(value)

        if message:
            self.status_label.setText(
                message
            )

        self._current_progress = value

    # ==========================================================
    # Paint
    # ==========================================================

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(
            QPainter.RenderHint.Antialiasing
        )

        gradient = QLinearGradient(
            0,
            0,
            self.width(),
            self.height(),
        )

        gradient.setColorAt(
            0,
            QColor("#eff6ff")
        )
        gradient.setColorAt(
            1,
            QColor("#ffffff")
        )

        painter.setBrush(gradient)
        painter.setPen(
            QPen(
                QColor(0, 0, 0, 0)
            )
        )

        painter.drawRoundedRect(
            self.rect(),
            20,
            20,
        )