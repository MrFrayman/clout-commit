# clout-commit 🟢

> *"Making GitHub heatmaps green since umm... 2026*"

## What is this?

A sophisticated tool for making recruiters think you're actually productive. Instead of building features, we build **perception**. This repo changes one character in a text file daily and commits it with increasingly ridiculous commit messages. It's not a bug, it's a feature.

## How it Works

1. **app.py** reads a single character from `data.txt`
2. Replaces it with a random different character (a-z, excluding the current one)
3. **run.sh** commits this groundbreaking change with a (fake) commit message
4. **Cronjob** runs this daily so your GitHub profile looks like you're literally always working

Think of it as **proof of life** for your GitHub account.

## Installation

```bash
# Clone the repo (use SSH for maximum authenticity)
git clone git@github.com:mrfrayman/clout-commit.git
cd clout-commit

# Set up a daily cronjob (on Unix/Linux/Mac)
crontab -e

# Add this line to run daily at 9 AM (or whenever you want to fake productivity)
0 9 * * * cd /path/to/clout-commit && bash run.sh
```

## Sample Commit Messages

Your daily commits will feature handcrafted lies like:

- "Added a secret, invisible feature for the AI to fix later"
- "This commit message is a lie."
- "Narrator: 'He did not, in fact, fix the bug.'"
- "Refactored the air inside the repository"
- "Enhanced the backend infrastructure with thoughts and prayers"
- "Making the git log look like I did work"
- "Commit count go brrr"

## FAQ

**Q: Is this ethical?**  
A: Is it ethical to waste recruiters' time? Is it ethical to judge developers on commit frequency? These are the real questions.

**Q: Will my employer notice?**  
A: Only if they look at what you're actually committing (1 character changes). Then you're cooked.

**Q: Can I customize the commit messages?**  
A: Yes! Edit `messages()` and watch your GitHub profile tell increasingly elaborate stories.

**Q: Is this real code?**  
A: This message exists to justify its own existence.

## Legal Disclaimer

This project is 100% organic and gluten-free. Use at your own risk. The author is not responsible for:
- Job interviews gone wrong
- Your GitHub activity making no sense
- Code reviews that just see random character changes
- Existential questions about your productivity

## Conclusion

If you use this, your commit history will be like a modern art installation: technically there, somewhat confusing, and absolutely defensible because "it's art."

---

**P.S.** - This repository is a social experiment. The real productivity was the lies we told along the way. 🎄
