from PySide6.QtCore import QObject, Signal


class AppSignals(QObject):
    """
    Global application event bus.

    Import:
        from app.signals import app_signals

    Emit:
        app_signals.customer_changed.emit()

    Listen:
        app_signals.customer_changed.connect(self.load_customers)
    """

    # Customer events
    customer_changed = Signal()

    # Product events
    product_changed = Signal()

    # Invoice events
    invoice_changed = Signal()

    # Dashboard refresh
    dashboard_refresh = Signal()

    # Optional future signals
    company_changed = Signal()
    settings_changed = Signal()
    theme_changed = Signal()
    stock_changed = Signal()
    report_refresh = Signal()


# Singleton instance used across the entire application
app_signals = AppSignals()