import fs from 'fs/promises';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const rootDir = path.join(__dirname, '..');

// Helper to determine category from directory name
function getCategory(dirName) {
    const name = dirName.toLowerCase();
    
    if (name.includes('onboarding') || name.includes('tutorial')) {
        return 'Onboarding';
    }
    if (name.includes('installation') || name.includes('setup_implementation')) {
        return 'Installation & Setup';
    }
    if (name.includes('mfa') || name.includes('totp') || name.includes('verification') || name.includes('audit_logs') || name.includes('security_audit') || name.includes('authgate')) {
        return 'Security & MFA';
    }
    if (name.includes('checkout') || name.includes('payout') || name.includes('billing') || name.includes('subscription') || name.includes('affiliate') || name.includes('revenue') || name.includes('payment')) {
        return 'Billing & Affiliates';
    }
    if (name.includes('license') || name.includes('ea_marketplace') || name.includes('secure_hub') || name.includes('gating')) {
        return 'Licensing & Security Hub';
    }
    if (name.includes('desktop') || name.includes('elite_dashboard') || name.includes('pro_terminal') || name.includes('execution_terminal') || name.includes('live_terminal')) {
        return 'Desktop Terminals';
    }
    if (name.includes('mobile') || name.includes('hq_dashboard') || name.includes('android_simulator') || name.includes('distribution_hub') || name.includes('play_store_focus') || name.includes('store_listing')) {
        return 'Mobile HQ & Simulators';
    }
    if (name.includes('bridge') || name.includes('sync')) {
        return 'MT4/MT5 Bridge Sync';
    }
    if (name.includes('neural') || name.includes('volatility') || name.includes('predictive') || name.includes('stress_test') || name.includes('backtester') || name.includes('correlation') || name.includes('sentiment') || name.includes('agent') || name.includes('automation') || name.includes('backtest')) {
        return 'Neural Engines & Algos';
    }
    if (name.includes('journal') || name.includes('analytics') || name.includes('performance') || name.includes('recap') || name.includes('audit')) {
        return 'Trade Journal & Analytics';
    }
    if (name.includes('chart') || name.includes('heatmap') || name.includes('liquidity') || name.includes('movers') || name.includes('feed') || name.includes('sentiment')) {
        return 'Live Charts & Market Feeds';
    }
    if (name.includes('consensus')) {
        return 'Consensus Matrix';
    }
    return 'General UI Modules';
}

// Helper to determine style theme based on code content
function getTheme(htmlContent) {
    if (htmlContent.includes('Geist') || htmlContent.includes('#00ffa3') || htmlContent.includes('#00e290')) {
        return {
            name: 'Obsidian Aegis',
            badgeClass: 'bg-emerald-500/10 text-emerald-400 border border-emerald-500/20'
        };
    }
    if (htmlContent.includes('Space Grotesk') || htmlContent.includes('#0e141a') || htmlContent.includes('#dee3ec')) {
        return {
            name: 'Obsidian Abyss',
            badgeClass: 'bg-blue-500/10 text-blue-400 border border-blue-500/20'
        };
    }
    return {
        name: 'Precision Sniper ICT',
        badgeClass: 'bg-lime-500/10 text-lime-400 border border-lime-500/20'
    };
}

async function main() {
    console.log("Scanning workspace for code.html files...");
    const entries = await fs.readdir(rootDir, { withFileTypes: true });
    const screens = [];

    for (const entry of entries) {
        if (!entry.isDirectory()) continue;
        if (['node_modules', '.git', 'backend', 'scripts', '.agents', 'shader', 'three.js'].includes(entry.name)) continue;

        const folderPath = path.join(rootDir, entry.name);
        const codeHtmlPath = path.join(folderPath, 'code.html');

        try {
            // Check if code.html exists
            await fs.access(codeHtmlPath);
            
            const htmlContent = await fs.readFile(codeHtmlPath, 'utf-8');
            
            // Extract title
            const titleMatch = htmlContent.match(/<title>([^<]+)<\/title>/i);
            const title = titleMatch ? titleMatch[1].trim() : entry.name.replace(/_/g, ' ').toUpperCase();
            
            // Check if screen.png exists
            const screenPngPath = path.join(folderPath, 'screen.png');
            let hasScreenshot = false;
            try {
                await fs.access(screenPngPath);
                hasScreenshot = true;
            } catch (e) {}

            const theme = getTheme(htmlContent);
            const category = getCategory(entry.name);

            screens.push({
                folderName: entry.name,
                title: title,
                path: `${entry.name}/code.html`,
                screenshot: hasScreenshot ? `${entry.name}/screen.png` : null,
                category: category,
                theme: theme
            });
        } catch (error) {
            // Skip folders that don't have code.html
        }
    }

    // Sort screens alphabetically by category then by title
    screens.sort((a, b) => {
        if (a.category !== b.category) {
            return a.category.localeCompare(b.category);
        }
        return a.title.localeCompare(b.title);
    });

    const outputPath = path.join(rootDir, 'screens.json');
    await fs.writeFile(outputPath, JSON.stringify(screens, null, 2), 'utf-8');
    console.log(`Successfully indexed ${screens.length} screens. Output saved to: ${outputPath}`);
}

main().catch(console.error);
