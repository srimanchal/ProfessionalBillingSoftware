DARK_THEME = """
QWidget {
    background-color: #1e1f22;
    color: #e8e8e8;
    font-size: 13px;
    font-family: "Segoe UI";
}

QMainWindow {
    background-color: #1e1f22;
}

QFrame {
    background: transparent;
    border: none;
}

QLabel {
    color: #e8e8e8;
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
    background-color: #252526;
    color: white;
    border: 1px solid #3c3f41;
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
    border: 2px solid #3B82F6;
}

QTableWidget {
    background-color: #252526;
    alternate-background-color: #2b2d31;
    border: 1px solid #3c3f41;
    border-radius: 14px;
    padding: 6px;
    gridline-color: #3c3f41;
    selection-background-color: #2563EB;
}

QHeaderView::section {
    background-color: #2563EB;
    color: white;
    border: none;
    padding: 8px;
    font-weight: bold;
}

#Sidebar {
    background-color: #202124;
    border-right: 1px solid #374151;
}

#DashboardHeader {
    background-color: #2b2d31;
    border: 1px solid #3c3f41;
    border-radius: 22px;
    padding: 20px;
}

#DashboardCard {
    background-color: #2b2d31;
    border: 1px solid #3c3f41;
    border-radius: 20px;
    padding: 12px;
}

#DashboardCardTitle {
    color: #94A3B8;
    font-size: 14px;
    font-weight: 600;
}

#DashboardCardValue {
    color: white;
    font-size: 38px;
    font-weight: 700;
}

#DashboardSectionTitle {
    font-size: 18px;
    font-weight: bold;
    color: white;
}

/* Login Screen */

#LoginHero {
    background: qlineargradient(
        x1:0,
        y1:0,
        x2:1,
        y2:1,
        stop:0 #1E3A8A,
        stop:1 #111827
    );
}

#LoginTitle {
    color: white;
    font-size: 34px;
    font-weight: bold;
}

#LoginTagline {
    color: #BFDBFE;
    font-size: 18px;
}

#LoginFeatures {
    color: white;
    font-size: 16px;
    line-height: 30px;
}

#LoginBackground {
    background: #111827;
}

#LoginCard {
    background: #1F2937;
    border: 1px solid #374151;
    border-radius: 24px;
}

#LoginCardTitle {
    color: white;
    font-size: 30px;
    font-weight: bold;
}

#LoginSubtitle {
    color: #D1D5DB;
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