LIGHT_THEME = """
QWidget {
    background-color: #f5f7fa;
    color: #222222;
    font-size: 13px;
    font-family: "Segoe UI";
}

QMainWindow {
    background-color: #f5f7fa;
}

QFrame {
    background: transparent;
    border: none;
}

QLabel {
    color: #222222;
    background: transparent;
    border: none;
}

QPushButton {
    background-color: #2563EB;
    color: white;
    border: none;
    border-radius: 12px;
    padding: 10px;
    font-weight: bold;
    min-height: 20px;
}

QPushButton:hover {
    background-color: #1D4ED8;
}

QPushButton:pressed {
    background-color: #1E40AF;
}

QLineEdit,
QComboBox,
QTextEdit,
QDateEdit,
QSpinBox,
QDoubleSpinBox {
    background-color: white;
    color: #222222;
    border: 1px solid #d0d7de;
    border-radius: 10px;
    padding: 8px;
    min-height: 24px;
}

QLineEdit:focus,
QComboBox:focus,
QTextEdit:focus,
QDateEdit:focus,
QSpinBox:focus,
QDoubleSpinBox:focus {
    border: 2px solid #2563EB;
}

QTableWidget {
    background-color: white;
    alternate-background-color: #f5f7fa;
    border: 1px solid #d0d7de;
    border-radius: 14px;
    padding: 6px;
    gridline-color: #d0d7de;
    selection-background-color: #2563EB;
}

QTableCornerButton::section {
    background-color: #2563EB;
    border: none;
}

QHeaderView::section {
    background-color: #2563EB;
    color: white;
    border: none;
    padding: 8px;
    font-weight: bold;
}

QTabWidget::pane {
    border: 1px solid #d0d7de;
    border-radius: 12px;
    background-color: white;
    margin-top: 10px;
}

QTabBar::tab {
    background-color: #edf2f7;
    color: #222222;
    border-top-left-radius: 10px;
    border-top-right-radius: 10px;
    padding: 10px 25px;
    min-width: 160px;
    min-height: 36px;
    margin-right: 4px;
}

QTabBar::tab:selected {
    background-color: #2563EB;
    color: white;
    font-weight: bold;
}

QTabBar::tab:hover {
    background-color: #1D4ED8;
    color: white;
}

/* Sidebar */

#Sidebar {
    background-color: white;
    border-right: 1px solid #E5E7EB;
}

/* Dashboard */

#DashboardHeader {
    background-color: white;
    border: 1px solid #E5E7EB;
    border-radius: 22px;
    padding: 20px;
}

#DashboardCompanyName {
    font-size: 28px;
    font-weight: bold;
}

#DashboardText {
    color: #555555;
}

#DashboardCard {
    background-color: white;
    border: 1px solid #E5E7EB;
    border-radius: 20px;
    padding: 12px;
}

#DashboardCardTitle {
    color: #64748B;
    font-size: 14px;
    font-weight: 600;
}

#DashboardCardValue {
    color: #111827;
    font-size: 38px;
    font-weight: 700;
}

#DashboardSectionTitle {
    font-size: 18px;
    font-weight: bold;
}

/* Login Screen */

#LoginHero {
    background: qlineargradient(
        x1:0,
        y1:0,
        x2:1,
        y2:1,
        stop:0 #2563EB,
        stop:1 #1E40AF
    );
}

#LoginTitle {
    color: white;
    font-size: 34px;
    font-weight: bold;
}

#LoginTagline {
    color: #DBEAFE;
    font-size: 18px;
}

#LoginFeatures {
    color: white;
    font-size: 16px;
    line-height: 30px;
}

#LoginBackground {
    background: #F8FAFC;
}

#LoginCard {
    background: white;
    border: 1px solid #E2E8F0;
    border-radius: 24px;
}

#LoginCardTitle {
    color: #111827;
    font-size: 30px;
    font-weight: bold;
}

#LoginSubtitle {
    color: #6B7280;
    font-size: 14px;
}

#LoginVersion {
    color: #9CA3AF;
    font-size: 12px;
}

QPushButton[active="true"] {
    background-color: #1D4ED8;
}

#Sidebar QPushButton {
    text-align: left;
    padding-left: 20px;
    font-size: 14px;
}
"""