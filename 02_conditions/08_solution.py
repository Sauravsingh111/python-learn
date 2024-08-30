# 8) Password Strength Checker
# Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).

password = "password"
password_length = len(password)
print(password_length)

if password_length < 6:
    message = "Weak"
elif password_length >= 6 and password_length <= 10:
    message = "Medium"
else:
    message = "Strong"

print("Your password strength is", message)