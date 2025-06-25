# MITM-DNS-Spoofing-Attack
A man-in-the-middle attack using DNS spoofing with Bettercap, Python server, and Wireshark

# 🛡️ Man-in-the-Middle Attack using DNS Spoofing and Credential Harvesting

This project demonstrates a **Man-in-the-Middle (MITM) attack** using **DNS spoofing** to redirect a victim to a fake login page, where their credentials are captured by the attacker. The attack was executed in a safe, controlled virtual environment using Kali Linux, Bettercap, a custom Python HTTP server, and Wireshark.

---

## 📌 Project Summary

- ✅ Spoofed domain: `veryrealloginpage.com`  
- ✅ Bettercap used for ARP poisoning + DNS spoofing  
- ✅ Fake login page hosted via custom `server.py`  
- ✅ Credentials captured in attacker terminal  
- ✅ Wireshark used to confirm POST data in transit  

---

## 🧰 Tools & Technologies Used

| Tool               | Purpose                                 |
|--------------------|------------------------------------------|
| Kali Linux         | Attacker VM (Bettercap, server, capture) |
| Ubuntu             | Victim system                            |
| Bettercap          | DNS spoofing + ARP poisoning             |
| Python HTTP Server | Hosts fake login and logs credentials    |
| Wireshark          | Network traffic analysis                 |
| UTM (macOS)        | Virtual machine manager                  |

---

## 🎥 Project Demonstration

📎 [Watch Phase 3 Demo](https://drive.google.com/YOUR_SHARE_LINK)

*(or add `Phase3_DNS_Spoofing_Demo.mov` if uploading directly to GitHub under 100MB)*

---

## 🧪 How the Attack Works

1. **Bettercap** poisons the network and spoofs DNS for `veryrealloginpage.com`.  
2. **Victim** visits the spoofed domain and sees a fake login page.  
3. **Python server** receives credentials and logs them.
4. **Wireshark** captures the HTTP POST request and reveals credentials in plain text.

---

## 🧠 Learning Outcomes

- Understood MITM attacks via DNS spoofing  
- Hands-on experience with Bettercap and Wireshark  
- Learned to build and debug a fake credential-capturing HTTP server  
- Realized the importance of HTTPS and DNSSEC

---

## 🚨 Disclaimer

> This project was developed for academic purposes and executed entirely in an isolated virtual environment.  
> **Do NOT** attempt these techniques on real networks or systems without explicit permission.  
> This repository is for educational and ethical research purposes only.

---

## 👩‍💻 Author

**Vanshika Deswal**  
B.Tech Computer Science Engineering  
Summer Project (1 Credit) – 2025  

