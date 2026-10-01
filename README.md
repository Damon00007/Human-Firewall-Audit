# The Human Firewall Audit

### Cybersecurity Project – Social Engineering Awareness & Defense

A defensive cybersecurity mini-project that demonstrates how **social engineering, publicly available information, and weak verification practices** can increase an organization's attack surface.

The project uses a **fictional organization** and a safe, educational simulation. It does not target real organizations, collect real credentials, or conduct real-world phishing.

---

## Project Overview

**The Human Firewall Audit** combines:

* OSINT-style reconnaissance
* Multi-vector social-engineering simulation
* Phishing awareness
* Password security
* Login-attempt monitoring
* Social-engineering red flags
* Layered cybersecurity defenses
* Activity logging

A **Streamlit-based web application** demonstrates the defensive concepts interactively.

---

## Target Organization

**StreamZone Studios Pvt. Ltd.**

* **Industry:** Online Entertainment / Streaming
* **Employees:** Approximately 85
* **Location:** Mumbai
* **Sensitive Information:** Sponsorship contracts, upcoming content, and unreleased media

> StreamZone Studios is completely fictional and is used only for educational simulation.

---

## Key Objectives

1. Understand how public information can expose an organization's attack surface.
2. Demonstrate a safe multi-vector social-engineering scenario.
3. Identify behavioral and technical warning signs.
4. Create practical employee-awareness guidance.
5. Design layered technical and organizational defenses.
6. Demonstrate defensive concepts through a working application.

---

## Application Modules

### 1. Dashboard

Provides an overview of the project, threat model, security posture, and application activity.

### 2. Phishing Analysis

Analyzes a sample message using simple defensive heuristics such as:

* Suspicious keywords
* URLs
* Urgency indicators
* Login-related language

The detector is intended for educational awareness and is **not an enterprise email-security replacement**.

### 3. Password Security

Checks basic password characteristics including:

* Length
* Uppercase characters
* Lowercase characters
* Digits
* Special characters

The application does not store the user's raw password.

### 4. Login Security

Demonstrates:

* Limited login attempts
* Failed-login monitoring
* Account lockout
* Successful authentication events

The demonstration uses a three-attempt limit to illustrate rate limiting and account protection.

### 5. Awareness Center

Provides practical social-engineering warning signs and defensive guidance.

### 6. Activity Log

Records defensive events generated during the application demonstration.

---

## Social-Engineering Scenario

The fictional simulation demonstrates two coordinated vectors:

### Vector 1 – Phishing

A fictional talent-scout style opportunity attempts to create urgency and direct the recipient toward a simulated login/upload flow.

### Vector 2 – Fake Collaboration Account

A fictional influencer-style account contacts the PR function to reinforce the credibility of the same opportunity through a second communication channel.

### Key Lesson

One communication channel can create an opportunity while another appears to confirm it. **Independent verification is therefore essential.**

No real credentials are collected and no real organization is targeted.

---

## OSINT / Reconnaissance Findings

The simulated reconnaissance identifies potential exposure through:

* Public social-media content
* Job postings
* Technology and workflow references
* Behind-the-scenes content
* Personal/company cloud-storage references
* Public travel or availability information

These details can potentially make social-engineering pretexts appear more believable.

---

## Social-Engineering Red Flags

* Unexpected partnership or collaboration requests
* Urgency or pressure to act immediately
* Requests for secrecy
* Sender/domain mismatch
* Unexpected redirects or login pages
* Requests for passwords or authentication codes
* Requests for sensitive files or unreleased content
* Verification through unrelated social-media accounts

---

## Defense Strategy

### People

* Security-awareness training
* Verification drills
* Reporting culture

### Identity & Access

* Zero-Trust access control
* Least privilege
* Controlled OAuth/application permissions

### Email Security

* DMARC
* Suspicious-link filtering
* Email authentication controls

### Content Protection

* Digital watermarking
* Monitoring of sensitive/unreleased media

### Detection & Response

* Phish-reporting mechanism
* Activity monitoring
* Periodic awareness simulations
* Documented incident-escalation process

---

## Technology Stack

* **Python**
* **Streamlit**
* **Regular Expressions**
* **SHA-256 hashing for demo password fingerprinting**
* **Git / GitHub**

---

## Project Structure

```text
Human_Firewall_Audit_V3/
│
├── app/
│   └── app.py
│
├── docs/
│   └── project_structure.txt
│
├── README.md
└── requirements.txt
```

---

## Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/Damon00007/Human-Firewall-Audit.git
```

### 2. Open the project directory

```bash
cd Human-Firewall-Audit
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python -m streamlit run app/app.py
```

The Streamlit application will open in the browser.

---

## Ethical Statement

This project is **fictional, educational, and defensive**.

* No real organization is targeted.
* No real person is impersonated.
* No real credentials are collected.
* No real phishing campaign is conducted.
* Safe sample inputs are used for demonstrations.

The project follows the principle:

> **Think like an attacker, but defend like a strategist.**

---

## Future Scope

Possible future improvements include:

* Database-backed activity logging
* Role-based access control
* Configurable awareness-training scenarios
* Advanced phishing classification
* Security analytics dashboards
* Controlled enterprise security-awareness campaigns
* Integration with safe security-training environments

---

## Author

**Pawan Tiwari**
B.Tech CSE
Ambalika Institute of Management & Technology

---

## Disclaimer

This project is created strictly for **educational cybersecurity awareness and defensive demonstration purposes**.
