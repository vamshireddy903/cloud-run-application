from flask import Flask, render_template_string
import os

app = Flask(__name__)

# HTML template embedded in Python (simple!)
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Beautiful Cloud App</title>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=Inter:wght@400;600&display=swap" rel="stylesheet">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Inter', sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
            position: relative;
            overflow: hidden;
        }

        /* Animated background circles */
        .circle {
            position: absolute;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.1);
            animation: float 20s infinite ease-in-out;
        }

        .circle:nth-child(1) {
            width: 300px;
            height: 300px;
            top: -150px;
            left: -150px;
            animation-delay: 0s;
        }

        .circle:nth-child(2) {
            width: 200px;
            height: 200px;
            bottom: -100px;
            right: -100px;
            animation-delay: 7s;
        }

        .circle:nth-child(3) {
            width: 250px;
            height: 250px;
            top: 50%;
            left: 50%;
            animation-delay: 14s;
        }

        @keyframes float {
            0%, 100% {
                transform: translate(0, 0) scale(1);
                opacity: 0.3;
            }
            50% {
                transform: translate(50px, 50px) scale(1.2);
                opacity: 0.6;
            }
        }

        .container {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border-radius: 30px;
            padding: 60px 40px;
            max-width: 600px;
            width: 100%;
            text-align: center;
            box-shadow: 0 30px 60px rgba(0, 0, 0, 0.3);
            position: relative;
            z-index: 10;
            animation: slideUp 0.8s ease-out;
        }

        @keyframes slideUp {
            from {
                opacity: 0;
                transform: translateY(50px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .emoji {
            font-size: 80px;
            margin-bottom: 20px;
            display: inline-block;
            animation: bounce 2s infinite;
        }

        @keyframes bounce {
            0%, 100% {
                transform: translateY(0);
            }
            50% {
                transform: translateY(-20px);
            }
        }

        h1 {
            font-family: 'Playfair Display', serif;
            font-size: 48px;
            font-weight: 900;
            color: #2d3748;
            margin-bottom: 20px;
            line-height: 1.2;
        }

        .gradient-text {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        p {
            font-size: 18px;
            color: #718096;
            margin-bottom: 30px;
            line-height: 1.6;
        }

        .button {
            display: inline-block;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 16px 40px;
            border-radius: 50px;
            text-decoration: none;
            font-weight: 600;
            font-size: 16px;
            transition: all 0.3s ease;
            box-shadow: 0 10px 25px rgba(102, 126, 234, 0.4);
        }

        .button:hover {
            transform: translateY(-3px);
            box-shadow: 0 15px 35px rgba(102, 126, 234, 0.6);
        }

        .stats {
            display: flex;
            justify-content: space-around;
            margin-top: 40px;
            padding-top: 30px;
            border-top: 2px solid #e2e8f0;
        }

        .stat {
            text-align: center;
        }

        .stat-number {
            font-family: 'Playfair Display', serif;
            font-size: 36px;
            font-weight: 900;
            color: #667eea;
            display: block;
            margin-bottom: 5px;
        }

        .stat-label {
            font-size: 14px;
            color: #a0aec0;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        .badge {
            display: inline-block;
            background: #48bb78;
            color: white;
            padding: 8px 16px;
            border-radius: 20px;
            font-size: 14px;
            font-weight: 600;
            margin-bottom: 20px;
        }

        @media (max-width: 600px) {
            .container {
                padding: 40px 30px;
            }

            h1 {
                font-size: 36px;
            }

            .stats {
                flex-direction: column;
                gap: 20px;
            }
        }
    </style>
</head>
<body>
    <div class="circle"></div>
    <div class="circle"></div>
    <div class="circle"></div>

    <div class="container">
        <div class="badge">🚀 Deployed on Cloud Run</div>
        
        <div class="emoji">☁️</div>
        
        <h1>
            Welcome to<br>
            <span class="gradient-text">Cloud Run</span>
        </h1>
        
        <p>
            A simple, awesome Python Flask application running on Google Cloud Run.
            Fast, scalable, and serverless!
        </p>
        
        <a href="#" class="button" onclick="alert('Hello from Cloud Run! 🎉'); return false;">
            Get Started
        </a>

        <div class="stats">
            <div class="stat">
                <span class="stat-number">99.9%</span>
                <span class="stat-label">Uptime</span>
            </div>
            <div class="stat">
                <span class="stat-number">&lt;100ms</span>
                <span class="stat-label">Response</span>
            </div>
            <div class="stat">
                <span class="stat-number">∞</span>
                <span class="stat-label">Scale</span>
            </div>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/health')
def health():
    return {'status': 'healthy'}, 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
