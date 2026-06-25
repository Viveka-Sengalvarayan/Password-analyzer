# 🔐 Password Strength Analyzer

A Python-based cybersecurity tool that evaluates password strength using industry-standard security checks and provides actionable recommendations to improve password security.

## 📌 Overview

Weak passwords are one of the most common causes of security breaches. This project analyzes user passwords based on multiple security parameters and classifies them as **Weak**, **Medium**, **Strong**, or **Very Strong**.

The application also calculates password entropy and suggests improvements to help users create more secure passwords.

---

## ✨ Features

* Password strength evaluation
* Password score calculation (0–6)
* Entropy calculation
* Detection of common password weaknesses
* Security recommendations
* Interactive graphical user interface (GUI)
* Hidden password input field for privacy

---

## 🛠️ Technologies Used

* Python
* Tkinter (GUI Development)
* Regular Expressions (Regex)
* Math Module

---

## 🔍 Password Evaluation Criteria

The password is evaluated based on:

| Criteria                    | Score |
| --------------------------- | ----- |
| Length ≥ 8 characters       | +1    |
| Length ≥ 12 characters      | +1    |
| Contains uppercase letters  | +1    |
| Contains lowercase letters  | +1    |
| Contains numbers            | +1    |
| Contains special characters | +1    |

**Maximum Score: 6**

---

## 📊 Output Information

The application displays:

* Password Strength
* Security Score
* Password Entropy (bits)
* Suggestions for improvement

### Example

Password: Hello123

Output:

* Strength: Medium Password
* Score: 4/6
* Entropy: 45.87 bits

Suggestions:

* Add special characters
* Increase password length

---

## 🚀 How to Run

### Clone the Repository

```bash
git clone https://github.com/Viveka-Sengalvarayan/Password-analyzer.git
```

### Navigate to the Project Directory

```bash
cd Password-analyzer
```

### Run the Application

```bash
python gui_analyzer.py
```

---

## 📸 Sample Outputs

### Weak Password Analysis

<img width="620" height="596" alt="Screenshot 2026-06-25 225605" src="https://github.com/user-attachments/assets/dc2a71d0-0712-46c9-a6ec-e69e0de00599" />


### Medium Password Analysis

<img width="617" height="591" alt="Screenshot 2026-06-25 225624" src="https://github.com/user-attachments/assets/8197eabe-cfac-4b98-bc5a-6d5bf340f5e4" />


### Strong Password Analysis

<img width="622" height="590" alt="Screenshot 2026-06-25 225646" src="https://github.com/user-attachments/assets/59c9499e-1d3c-44e7-8ff9-d3ad7d18f938" />

## 📚 Cybersecurity Concepts Applied

* Password Security
* Authentication Best Practices
* Entropy Analysis
* Secure Password Policies
* Input Validation
* Pattern Matching using Regular Expressions

---

## 🎯 Learning Outcomes

Through this project, I gained practical experience in:

* Python Programming
* GUI Development with Tkinter
* Cybersecurity Fundamentals
* Password Security Analysis
* Git & GitHub Version Control

---

## 👨‍💻 Author

**Viveka Sengalvarayan**

Cybersecurity Enthusiast | Python Learner | Aspiring Security Professional
