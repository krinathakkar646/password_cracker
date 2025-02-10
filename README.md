# 🔐 Password Hasher & Cracker

## 🚀 Project Overview
This project is a **password hashing and cracking tool** built in Python. It allows users to:
- Securely hash passwords using **MD5, SHA-256, and other algorithms**.
- Attempt to crack passwords using a **wordlist attack** with `rockyou.txt`.

🔎 **Purpose:** This tool helps understand **how password security works** and why using strong, unique passwords is essential.

---

## ⚙️ Features
✅ Hashes passwords using MD5, SHA-256, SHA-1, etc.  
✅ Stores hashed passwords securely  
✅ Performs wordlist-based password cracking  
✅ Uses `rockyou.txt` or any custom wordlist for brute-force attacks  
✅ Shows why weak passwords are easily crackable  

---

## 🛠️ Installation & Setup
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/yourusername/password-cracker.git
cd password-cracker
```

### **2️⃣ Install Dependencies**
Python is required. If not installed, download it from [python.org](https://www.python.org/downloads/).

```bash
pip install hashlib
```

### **3️⃣ Download RockYou Wordlist (If Needed)**
You can download the `rockyou.txt` wordlist (commonly used for password cracking) from [SecLists](https://github.com/danielmiessler/SecLists/tree/master/Passwords/Common-Credentials).

---

## 📌 How to Use
### **🔑 1. Hash a Password**
Run the **password hasher** script:
```bash
python password_hasher.py
```
💡 **Enter a password**, and it will be hashed using the selected algorithm.

### **🔓 2. Crack a Hashed Password**
Run the **password cracker** script:
```bash
python password_cracker.py
```
💡 The script will compare the hashed password against the wordlist and reveal if a match is found.

---

## 📝 Example Output
### **Password Hasher**
```
Enter hash type (md5, sha256, sha1, etc.): md5
Enter a password to hash: mypassword
✅ The password is hashed and stored securely.
🔐 Hashed (md5): 34819d7beeabb9260a5c854bc85b3e44
```

### **Password Cracker**
```
✅ Password Found in Wordlist!
🔓 Original Password: mypassword
```

---

## 🔥 Key Learnings
- **The importance of strong, unique passwords** 🔑
- **How real-world password attacks work** 💻
- **Why companies use salted hashes to improve security** 🔒

---

## 🤝 Contributing
Want to improve this project? Feel free to fork it and submit a pull request! 😊

---

## 📜 Disclaimer
⚠️ **This tool is for educational purposes only.** Do not use it for illegal activities. Ethical hacking should always be done with permission!

---

## 📩 Connect With Me
**LinkedIn:** [Your LinkedIn Profile](https://www.linkedin.com/in/yourprofile/)  
**GitHub:** [Your GitHub](https://github.com/yourusername/)  

📌 *If you found this project useful, drop a ⭐ on the repo!* 🚀
