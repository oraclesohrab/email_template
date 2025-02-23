# Affirm Email Template - README

## Overview
This project is an email template designed according to the specifications provided by the client. The email is fully responsive, ensuring a smooth experience on both desktop and mobile devices. It has been tested using **Litmus** and **Email on Acid** to verify rendering accuracy across multiple email clients.

## Assets and Image Handling
- The task description provided only **four image assets**, but the layout required additional images. 
- **Solution:**
  - `top_image_D.png` and `top_image_M.png` were used as per the task description for desktop and mobile versions of the header image.
  - `image1.png` was repurposed for the **middle section**.
  - `image2.png` was used as the **bottom section** image.
- **Hosting:**
  - All images are hosted on an **Amazon S3 bucket** for reliable email delivery.
  - The original `<img>` tags for internal image usage have been retained but commented out. Developers can switch between hosted and internal images as needed.

## Layout Implementation
- **Top Section:**
  - The header contains a title, subheading, and a bulletproof button with a green background and rounded corners.
  - Mobile and desktop images are swapped using media queries.
- **Middle Section:**
  - The layout strictly follows the provided order.
  - **Mobile Order:** Images and text alternate as specified: **2-1-4-3-6-5**.
  - Only **Text 1** and **Text 2** are used in mobile as per the description.
- **Bottom Section:**
  - Desktop: `BottomImage` and `BottomText` appear side by side.
  - Mobile: `BottomImage` stacks above `BottomText`.
  - The bottom text has **three lines** on desktop but dynamically adjusts on mobile to wrap correctly.

## Outlook & Microsoft 365 Compatibility Fixes
To handle Outlook and Microsoft 365 rendering issues:
- Specific `<!--[if mso]>` comments were added to hide mobile images in Microsoft-based email clients that do not support media queries.

## Email Testing Results
### **Litmus Results** ✅
- Passed **all tests**, including accessibility and mobile responsiveness checks.
- Fixed errors related to **meta content-type**, **table accessibility**, and **header structure**.
- Hidden preview text of **at least 90 characters** was added to prevent email clients from pulling unwanted content.
- Litmus flagged a recommendation regarding **text alignment**. To comply, I adjusted the body text to be **left-aligned**, ensuring it met accessibility and readability standards while maintaining the intended design.
- [Test Results on Litmus](https://litmus.com/pub/culYwQIsUh4Ew0zm)

### **Email on Acid Results** ✅
- Verified on multiple email clients, including Gmail, Outlook, Apple Mail, and Yahoo.
- **Outlook-specific issues resolved**:
  - Corrected mobile view rendering issues.
- [Test Results on Email on Acid](https://app.emailonacid.com/app/acidtest/osl35nh8gtO2xo558Rzi5SBx1YlKejXWZ1mwvQwnOxumo/list)

## How to Send the Email (Python Script)
A **Python script** (`main.py`) is provided to send test emails.

### **Requirements**
Ensure you have the following installed:
```sh
pip install smtplib ssl email
```

### **Usage**
1. Open `main.py` and update the sender email credentials.
2. Ensure your SMTP provider supports HTML emails.
3. Run the script:
```sh
python main.py
```

## Final Notes
- The template is **fully responsive** and **optimized for major email clients**.
- If further customizations are needed, refer to the **Litmus and Email on Acid results**.
- This template is built with **email accessibility best practices** in mind.

**Final Thoughts:**
- This was a fun challenge! I enjoyed optimizing the email for responsiveness and cross-client compatibility. Looking forward to what’s next!