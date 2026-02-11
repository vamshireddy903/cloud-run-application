from flask import Flask, render_template, jsonify
import os
from datetime import datetime

app = Flask(__name__)

# Sample data for the dashboard
stats = [
    {"label": "Active Users", "value": "12,453", "change": "+12.5%", "trend": "up"},
    {"label": "Revenue", "value": "$45,678", "change": "+8.2%", "trend": "up"},
    {"label": "Projects", "value": "89", "change": "-3.1%", "trend": "down"},
    {"label": "Performance", "value": "94.2%", "change": "+5.7%", "trend": "up"},
]

recent_activity = [
    {"user": "Sarah Chen", "action": "completed project review", "time": "2 minutes ago", "type": "success"},
    {"user": "Marcus Johnson", "action": "uploaded new design files", "time": "15 minutes ago", "type": "info"},
    {"user": "Elena Rodriguez", "action": "commented on feedback", "time": "1 hour ago", "type": "comment"},
    {"user": "David Kim", "action": "started new sprint", "time": "3 hours ago", "type": "milestone"},
]

@app.route('/')
def index():
    return render_template('index.html', 
                         stats=stats, 
                         recent_activity=recent_activity,
                         current_time=datetime.now().strftime("%B %d, %Y"))

@app.route('/api/stats')
def get_stats():
    return jsonify(stats)

@app.route('/health')
def health():
    return jsonify({"status": "healthy", "timestamp": datetime.now().isoformat()})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False)
