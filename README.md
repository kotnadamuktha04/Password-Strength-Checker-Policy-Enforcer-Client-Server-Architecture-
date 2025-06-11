# Password-Strength-Checker-Policy-Enforcer-Client-Server-Architecture-
🔐 Secure Password Generator & Logger
A client-server application that generates strong, customizable passwords and logs them securely in a local database.

🌟 Features

Custom Password Generation: Create passwords with your preferred:
Length (8-64 characters)
Character types (uppercase, digits, special characters)
Secure Local Storage: All generated passwords are logged in an encrypted SQLite database with:
Generation timestamp
Configuration settings
Password hashes (not plaintext)
Network-Based: Uses socket communication between client and server components
🛠️ Installation

Clone the repository:

bash

git clone https://github.com/yourusername/secure-password-generator.git

cd secure-password-generator

Install dependencies:

bash

pip install -r requirements.txt

🚀 Usage


Start the server (in one terminal):

bash

python server.py

Run the client (in another terminal):

bash

python client.py

View logs (optional):

bash

python view_logs.py

📊 Example Workflow

plaintext

🔐 Strong Password Client

Enter password length (e.g., 12): 16

Include uppercase letters? (y/n): y

Include digits? (y/n): y

Include special characters? (y/n): y


✅ Your secure password is: k7#mQ!4pL@2vN$9b

🔒 Security Notes


Passwords are generated locally and never transmitted over the internet

Database uses SQLite encryption (password protection optional)

Server runs on localhost only by default

