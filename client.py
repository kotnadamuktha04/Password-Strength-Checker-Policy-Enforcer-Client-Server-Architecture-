import socket
import json

# Print client header
print("🔐 Strong Password Client")

# Get password requirements from user
# Prompt for password length and convert to integer
length = int(input("Enter password length (e.g., 12): "))
# Ask if uppercase letters should be included and convert answer to boolean
use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
# Ask if digits should be included and convert answer to boolean
use_digits = input("Include digits? (y/n): ").lower() == 'y'
# Ask if special characters should be included and convert answer to boolean
use_special = input("Include special characters? (y/n): ").lower() == 'y'

# Create a dictionary with the password settings
settings = {
    'length': length,             # Store password length
    'use_uppercase': use_uppercase,  # Store uppercase preference
    'use_digits': use_digits,        # Store digits preference
    'use_special': use_special       # Store special characters preference
}

# Network connection settings
host = 'localhost'  # Server host (local machine)
port = 12345       # Server port number

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect to the server at the specified host and port
client_socket.connect((host, port))

# Convert settings to JSON string and encode to bytes, then send to server
client_socket.send(json.dumps(settings).encode())

# Receive the generated password from server (max 1024 bytes) and decode it
password = client_socket.recv(1024).decode()
# Display the generated password to the user
print("\n✅ Your secure password is:", password)

# Close the connection with the server
client_socket.close()