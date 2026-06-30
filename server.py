import os
import json
import urllib.parse
from http.server import HTTPServer, SimpleHTTPRequestHandler

PORT = 3000
root_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(root_dir, 'backend', 'users.json')
screens_path = os.path.join(root_dir, 'screens.json')

class DashboardServerHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        # Enable CORS for standard web client interactions
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

    def do_OPTIONS(self):
        # Handle preflight requests
        self.send_response(200, "OK")
        self.end_headers()

    def do_GET(self):
        # API Route: Get Screens Index
        if self.path == '/api/screens':
            try:
                if os.path.exists(screens_path):
                    with open(screens_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                    self.send_response(200)
                    self.send_header('Content-Type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps(data).encode('utf-8'))
                else:
                    self.send_response(404)
                    self.send_header('Content-Type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps({"error": "Screens database not generated yet. Run scripts/generate_metadata.py."}).encode('utf-8'))
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"error": str(e)}).encode('utf-8'))
            return

        # Fallback to standard static file serving
        super().do_GET()

    def do_POST(self):
        # API Route: User Signup
        if self.path == '/api/auth/signup':
            try:
                content_length = int(self.headers['Content-Length'])
                post_data = self.rfile.read(content_length)
                req_data = json.loads(post_data.decode('utf-8'))

                email = req_data.get('email', '').strip().lower()
                password = req_data.get('password', '')

                if not email or not password:
                    self.send_response(400)
                    self.send_header('Content-Type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps({"error": "IDENTITY_KEY (Email) and ACCESS_TOKEN (Password) are required."}).encode('utf-8'))
                    return

                # Load existing users
                users = []
                if os.path.exists(db_path):
                    with open(db_path, 'r', encoding='utf-8') as f:
                        users = json.load(f)

                # Check duplicates
                if any(u.get('email') == email for u in users):
                    self.send_response(400)
                    self.send_header('Content-Type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps({"error": "Identity node already registered."}).encode('utf-8'))
                    return

                # Save new user
                new_user = {
                    "email": email,
                    "password": password,
                    "createdAt": "2026-06-27T19:00:00Z"
                }
                users.append(new_user)

                # Ensure backend directory exists
                os.makedirs(os.path.join(root_dir, 'backend'), exist_ok=True)
                with open(db_path, 'w', encoding='utf-8') as f:
                    json.dump(users, f, indent=2)

                self.send_response(201)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"success": True, "message": "Identity key registered successfully.", "email": email}).encode('utf-8'))

            except Exception as e:
                self.send_response(500)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"error": f"Internal security registration error: {str(e)}"}).encode('utf-8'))
            return

        # API Route: User Login
        elif self.path == '/api/auth/login':
            try:
                content_length = int(self.headers['Content-Length'])
                post_data = self.rfile.read(content_length)
                req_data = json.loads(post_data.decode('utf-8'))

                email = req_data.get('email', '').strip().lower()
                password = req_data.get('password', '')

                if not email or not password:
                    self.send_response(400)
                    self.send_header('Content-Type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps({"error": "IDENTITY_KEY and ACCESS_TOKEN are required."}).encode('utf-8'))
                    return

                # Load existing users
                users = []
                if os.path.exists(db_path):
                    with open(db_path, 'r', encoding='utf-8') as f:
                        users = json.load(f)

                # Verify credentials
                matched_user = next((u for u in users if u.get('email') == email and u.get('password') == password), None)
                if matched_user:
                    self.send_response(200)
                    self.send_header('Content-Type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps({
                        "success": True,
                        "message": "Authentication successful.",
                        "token": f"mock-session-py-{email.replace('@', '-')}"
                    }).encode('utf-8'))
                else:
                    self.send_response(401)
                    self.send_header('Content-Type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps({"error": "Invalid system identity credentials."}).encode('utf-8'))

            except Exception as e:
                self.send_response(500)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"error": f"Internal authentication error: {str(e)}"}).encode('utf-8'))
            return

        else:
            self.send_response(404)
            self.end_headers()

def run_server():
    server = HTTPServer(('0.0.0.0', PORT), DashboardServerHandler)
    print(f"================================================================")
    print(f"  PRECISION SNIPER ICT - PYTHON INSTITUTIONAL API SERVER STATUS  ")
    print(f"================================================================")
    print(f"  Local Access: http://localhost:{PORT}")
    print(f"  API Status:   Active (Authentication & Database online)")
    print(f"  Directory:    Serving static folders securely")
    print(f"================================================================")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server...")
        server.server_close()

if __name__ == '__main__':
    run_server()
