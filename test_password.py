from services.password_service import PasswordService

password = "admin123"

hashed = PasswordService.hash_password(password)

print("Hashed Password:")
print(hashed)

print(
    "Password Valid:",
    PasswordService.verify_password(
        password,
        hashed
    )
)