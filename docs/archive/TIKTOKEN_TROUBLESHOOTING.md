# Tiktoken Troubleshooting Guide

## WINDOWS USERS - QUICK FIX

You have a Python 3.13 installation but tiktoken isn't installed to it.

**Run this script now:**

```bash
python fix_tiktoken_windows.py
```

This will automatically:
1. Detect your Python installation
2. Install tiktoken to it
3. Test that it works
4. Tell you if there are any remaining issues

---

## Step 1: Run the Diagnostic Script

First, run the built-in diagnostic:

```bash
python check_tiktoken.py
```

This will tell you exactly what's wrong. If it passes all checks, but camera.py still fails, continue to Step 2.

## Step 2: Verify Which Python You're Using

The issue is usually that you have **multiple Python installations** and they're different:

### Check which Python camera.py is using:

**Option A - Add diagnostic to camera.py temporarily:**

Open `camera.py` and after the tiktoken import section (around line 12-24), add:

```python
print(f"DEBUG: Python = {sys.executable}")
print(f"DEBUG: tiktoken module = {tiktoken if 'tiktoken' in dir() else 'NOT FOUND'}")
```

Then run `python camera.py` and see what it prints.

**Option B - Check Python path directly:**

```bash
python -c "import sys; print(sys.executable)"
```

And separately check where tiktoken is installed:

```bash
pip show tiktoken
```

Note the location. If the Python path from step A and the pip installation path are different, that's your problem.

## Step 3: Solutions

### If you have multiple Python installations:

**Option 1: Use full path to correct Python**
```bash
# If tiktoken is in C:\Python\Scripts\pip, use:
C:\Python\python.exe camera.py
```

**Option 2: Reinstall to correct Python**
```bash
# Find which python has the right location
where python          # Windows
which python          # Mac/Linux

# Then use that exact path to install tiktoken
C:\exact\path\python.exe -m pip install tiktoken

# Verify it worked
C:\exact\path\python.exe -m pip list | find tiktoken
```

**Option 3: Use venv (recommended)**
```bash
# Create virtual environment
python -m venv modelA_env

# Activate it
# Windows:
modelA_env\Scripts\activate
# Mac/Linux:
source modelA_env/bin/activate

# Install tiktoken
pip install tiktoken

# Run camera.py
python camera.py
```

## Step 4: Common Issues on Windows

**Issue: "pip install tiktoken" seems to work but Python can't import**

Solution: You might have Python from Windows Store. Windows Store Python has install restrictions.

Fix:
1. Uninstall Python from Windows Store
2. Install from python.org instead
3. Reinstall tiktoken

**Issue: Still not working after all above steps**

Last resort - use the diagnostic to see exact error:

```python
python -c "
import sys
sys.path.insert(0, '.')
try:
    import tiktoken
    print('SUCCESS: tiktoken imported')
    enc = tiktoken.get_encoding('cl100k_base')
    print('SUCCESS: encoding loaded')
except Exception as e:
    print(f'ERROR: {type(e).__name__}: {e}')
    import traceback
    traceback.print_exc()
"
```

Copy the error and let me know what it says.

## If tiktoken Still Won't Work

The fallback math estimation (`len // 4`) works fine. Accuracy difference:
- **Tiktoken:** Exact token count
- **Math:** Off by ~5-10% but good enough for budgeting

You can continue using camera.py without tiktoken - it will use the fallback automatically.

---

## Quick Verification

After fixing, verify tiktoken works in camera.py by running:

```bash
python camera.py 2>&1 | head -1
```

You should see:
```
✓ Using tiktoken for accurate token counting
```

Instead of:
```
⚠ tiktoken not available - using math estimation (len // 4)
```

