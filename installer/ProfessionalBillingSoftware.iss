#define MyAppName "Professional Billing Software"
#define MyAppVersion "1.0.0"
#define MyAppPublisher "Srimanchal Sahoo"
#define MyAppExeName "Professional Billing Software.exe"

[Setup]
AppId={{7B9B5C1A-7F6C-4C7F-9A22-9B7F0D7A0001}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}

DefaultDirName={autopf}\{#MyAppName}
DefaultGroupName={#MyAppName}

OutputDir=Output
OutputBaseFilename=ProfessionalBillingSoftwareSetup

Compression=lzma
SolidCompression=yes
WizardStyle=modern

SetupIconFile=..\assets\icons\app.ico
UninstallDisplayIcon={app}\{#MyAppExeName}

PrivilegesRequired=admin

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "Create Desktop Shortcut"; GroupDescription: "Additional Icons:"; Flags: unchecked

[Files]
Source: "..\dist\Professional Billing Software\*"; DestDir: "{app}"; Flags: recursesubdirs createallsubdirs ignoreversion

[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"

Name: "{autodesktop}\{#MyAppName}";Filename: "{app}\{#MyAppExeName}";Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}";Description: "Launch Professional Billing Software";Flags: nowait postinstall skipifsilent