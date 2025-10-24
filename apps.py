from flask import Flask, render_template

app = Flask(__name__)

# Static cybersecurity news dataset
news_data = [
    {
        "title": "Critical Cisco ASA Vulnerability Could Allow Remote Code Execution",
        "summary": "Cisco patched a severe ASA firewall vulnerability allowing remote code execution.",
        "url": "https://thehackernews.com/2025/10/cisco-asa-vulnerability.html"
    },
    {
        "title": "Microsoft Patches Zero-Day Exploited in the Wild",
        "summary": "October Patch Tuesday fixed a Windows zero-day exploited in targeted attacks.",
        "url": "https://thehackernews.com/2025/10/microsoft-zero-day.html"
    },
    {
        "title": "AI-Powered Phishing Campaign Targets Banks",
        "summary": "A new phishing wave uses AI to mimic voice and writing patterns to bypass filters.",
        "url": "https://thehackernews.com/2025/10/ai-phishing-attack.html"
    },
    {
        "title": "Linux Kernel Bug Lets Attackers Escalate Privileges",
        "summary": "A privilege escalation flaw affects major Linux distributions, including Ubuntu.",
        "url": "https://thehackernews.com/2025/10/linux-kernel-bug.html"
    },
    {
        "title": "Google Removes 500 Malicious Chrome Extensions",
        "summary": "Extensions were caught stealing user data and browser session cookies.",
        "url": "https://thehackernews.com/2025/10/google-malicious-extensions.html"
    }
]

# Sidebar updates (scrolling / blinking)
system_updates = [
    "⚙️ Microsoft Edge update improves sandbox isolation security.",
    "🐧 Linux Kernel 6.9 introduces memory-hardening enhancements.",
    "🧱 Ubuntu 24.10 includes new AppArmor rules for AI workloads.",
    "🪟 Windows Defender adds AI-driven ransomware shield.",
    "🔧 Debian team releases major patch for OpenSSL vulnerability."
]

@app.route('/')
def home():
    return render_template('index.html', news=news_data, updates=system_updates)

if __name__ == '__main__':
    app.run(debug=True)

