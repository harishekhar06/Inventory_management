#code for generating a secret key
import secrets
secret_key = secrets.token_hex(16)
print(secret_key)
