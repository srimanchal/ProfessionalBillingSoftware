from services.auth_service import AuthService

auth = AuthService()

auth.create_default_admin()

user = auth.authenticate(
    "admin",
    "admin123"
)

if user:
    print("Login Successful")
    print(user.username)
else:
    print("Login Failed")