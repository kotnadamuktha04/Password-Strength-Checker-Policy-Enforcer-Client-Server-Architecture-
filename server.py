# Import required modules
import socket  # For network communication
import random  # For generating random passwords
import string  # For string operations and character sets
import json  # For JSON data handling
import sqlite3  # For database operations
from datetime import datetime  # For timestamping

# Function to generate a password
def generate_password(length=12, use_uppercase=True, use_digits=True, use_special=True):
    # Start with lowercase letters as base character set
    characters = string.ascii_lowercase
    
    # Add uppercase letters if requested
    if use_uppercase:
        characters += string.ascii_uppercase
    
    # Add digits if requested
    if use_digits:
        characters += string.digits
    
    # Add special characters if requested
    if use_special:
        characters += string.punctuation
    
    # Generate password by randomly selecting characters
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def init_db():
    # Connect to SQLite database (creates if doesn't exist)
    conn = sqlite3.connect('password_log.db')
    c = conn.cursor()
    
    # Create table if it doesn't exist with required fields
    c.execute('''
        CREATE TABLE IF NOT EXISTS password_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,  -- Auto-incrementing ID
            length INTEGER,                       -- Password length
            use_uppercase BOOLEAN,                -- Uppercase flag
            use_digits BOOLEAN,                   -- Digits flag
            use_special BOOLEAN,                  -- Special chars flag
            password TEXT,                        -- Generated password
            timestamp TEXT                       -- Creation timestamp
        )
    ''')
    # Commit changes and close connection
    conn.commit()
    conn.close()

# Function to log password to database
def log_password(length, use_uppercase, use_digits, use_special, password):
    # Connect to database
    conn = sqlite3.connect('password_log.db')
    c = conn.cursor()
    
    # Insert password record with all parameters
    c.execute('''
        INSERT INTO password_logs (length, use_uppercase, use_digits, use_special, password, timestamp)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (length, use_uppercase, use_digits, use_special, password, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    
    # Commit changes and close connection
    conn.commit()
    conn.close()

# Set up server
init_db()  # Initialize database before starting server
host = 'localhost'  # Server host (local machine)
port = 12345       # Server port number

# Create TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind socket to host and port
server_socket.bind((host, port))
# Start listening for connections (1 queued connection)
server_socket.listen(1)

# Server startup message
print(f"🔐 Server listening on {host}:{port}...")

# Main server loop
while True:
    # Accept incoming connection
    conn, addr = server_socket.accept()
    print(f"✅ Connected by {addr}")

    # Receive data from client (max 1024 bytes) and decode from bytes to string
    data = conn.recv(1024).decode()
    # Parse received JSON data into Python dictionary
    settings = json.loads(data)

    # Generate password using received settings
    password = generate_password(
        length=settings['length'],
        use_uppercase=settings['use_uppercase'],
        use_digits=settings['use_digits'],
        use_special=settings['use_special']
    )

    # Log password to database
    log_password(settings['length'], settings['use_uppercase'], settings['use_digits'], settings['use_special'], password)

    # Send generated password back to client (encoded as bytes)
    conn.send(password.encode())
    # Close the connection
    conn.close()