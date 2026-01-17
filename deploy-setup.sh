#!/bin/bash

echo "🚀 HyperSpace LEO Network - Quick Deploy Setup"
echo "=============================================="
echo ""

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "❌ Git is not installed. Please install git first."
    exit 1
fi

echo "📝 Step 1: Initialize Git Repository"
git init
echo "✅ Git initialized"
echo ""

echo "📝 Step 2: Add all files to git"
git add .
echo "✅ Files staged"
echo ""

echo "📝 Step 3: Create initial commit"
git commit -m "Initial commit - HyperSpace LEO Satellite Network Optimizer"
echo "✅ Initial commit created"
echo ""

echo "=============================================="
echo "🎉 Git setup complete!"
echo ""
echo "Next steps:"
echo "1. Create a new repository on GitHub: https://github.com/new"
echo "2. Run these commands (replace YOUR_USERNAME):"
echo ""
echo "   git remote add origin https://github.com/YOUR_USERNAME/hyperspace-leo-network.git"
echo "   git branch -M main"
echo "   git push -u origin main"
echo ""
echo "3. Then deploy to Render.com:"
echo "   - Go to https://render.com"
echo "   - Sign in with GitHub"
echo "   - Click 'New +' → 'Web Service'"
echo "   - Select your repository"
echo "   - Render will auto-detect settings from Procfile"
echo ""
echo "4. Update globe.html line 96 with your deployed backend URL"
echo ""
echo "📖 See DEPLOYMENT.md for detailed instructions"
echo "=============================================="
