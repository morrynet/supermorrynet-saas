import os
import re
import json

root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Helper to determine category from directory name
def get_category(dir_name):
    name = dir_name.lower()
    if 'onboarding' in name or 'tutorial' in name:
        return 'Onboarding'
    if 'installation' in name or 'setup_implementation' in name:
        return 'Installation & Setup'
    if any(k in name for k in ['mfa', 'totp', 'verification', 'audit_logs', 'security_audit', 'authgate']):
        return 'Security & MFA'
    if any(k in name for k in ['checkout', 'payout', 'billing', 'subscription', 'affiliate', 'revenue', 'payment']):
        return 'Billing & Affiliates'
    if any(k in name for k in ['license', 'ea_marketplace', 'secure_hub', 'gating']):
        return 'Licensing & Security Hub'
    if any(k in name for k in ['desktop', 'elite_dashboard', 'pro_terminal', 'execution_terminal', 'live_terminal']):
        return 'Desktop Terminals'
    if any(k in name for k in ['mobile', 'hq_dashboard', 'android_simulator', 'distribution_hub', 'play_store_focus', 'store_listing']):
        return 'Mobile HQ & Simulators'
    if 'bridge' in name or 'sync' in name:
        return 'MT4/MT5 Bridge Sync'
    if any(k in name for k in ['neural', 'volatility', 'predictive', 'stress_test', 'backtester', 'correlation', 'sentiment', 'agent', 'automation', 'backtest']):
        return 'Neural Engines & Algos'
    if any(k in name for k in ['journal', 'analytics', 'performance', 'recap', 'audit']):
        return 'Trade Journal & Analytics'
    if any(k in name for k in ['chart', 'heatmap', 'liquidity', 'movers', 'feed', 'sentiment']):
        return 'Live Charts & Market Feeds'
    if 'consensus' in name:
        return 'Consensus Matrix'
    return 'General UI Modules'

# Helper to determine style theme based on code content
def get_theme(html_content):
    if 'Geist' in html_content or '#00ffa3' in html_content or '#00e290' in html_content:
        return {
            'name': 'Obsidian Aegis',
            'badgeClass': 'bg-emerald-500/10 text-emerald-400 border border-emerald-500/20'
        }
    if 'Space Grotesk' in html_content or '#0e141a' in html_content or '#dee3ec' in html_content:
        return {
            'name': 'Obsidian Abyss',
            'badgeClass': 'bg-blue-500/10 text-blue-400 border border-blue-500/20'
        }
    return {
        'name': 'Precision Sniper ICT',
        'badgeClass': 'bg-lime-500/10 text-lime-400 border border-lime-500/20'
    }

def main():
    print("Scanning workspace for code.html files...")
    screens = []

    for entry in os.listdir(root_dir):
        entry_path = os.path.join(root_dir, entry)
        if not os.path.isdir(entry_path):
            continue
        if entry in ['node_modules', '.git', 'backend', 'scripts', '.agents', 'shader', 'three.js']:
            continue

        code_html_path = os.path.join(entry_path, 'code.html')
        if not os.path.exists(code_html_path):
            continue

        try:
            with open(code_html_path, 'r', encoding='utf-8') as f:
                html_content = f.read()

            # Extract title
            title_match = re.search(r'<title>([^<]+)</title>', html_content, re.IGNORECASE)
            title = title_match.group(1).strip() if title_match else entry.replace('_', ' ').upper()

            # Check if screen.png exists
            screen_png_path = os.path.join(entry_path, 'screen.png')
            has_screenshot = os.path.exists(screen_png_path)

            theme = get_theme(html_content)
            category = get_category(entry)

            screens.append({
                'folderName': entry,
                'title': title,
                'path': f"{entry}/code.html",
                'screenshot': f"{entry}/screen.png" if has_screenshot else None,
                'category': category,
                'theme': theme
            })
        except Exception as e:
            print(f"Error reading {entry}: {e}")

    # Sort screens alphabetically by category then by title
    screens.sort(key=lambda s: (s['category'], s['title']))

    output_path = os.path.join(root_dir, 'screens.json')
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(screens, f, indent=2)

    print(f"Successfully indexed {len(screens)} screens. Output saved to: {output_path}")

if __name__ == '__main__':
    main()
