# B2. Discover 5 unique strong security implementations.
Overview: I identified five strong security implementations that are used in modern systems. These include areas like authentication, account security, code security, web protection and device security.
## 1. Passkeys
Passkeys can be considered a strong authentication implementation as they replace passwords with key cryptography. The private key remains on the user’s device, while the website only stores the public key. During the login process, the device signs a challenge for the correct domain. This makes passkeys phishing resistant as a fake website cannot use a passkey that is registered to the real website domain.
[1.png](images/1.png)

## 2. Microsoft Authenticator Number Matching
Number matching improves push-based `MFA` by requiring the user to type the number shown on the login screen into the authenticator app. This is much stronger than just using a simple “approve” button as it reduces `MFA` fatigue attacks. This is where attackers repeatedly send push notifications until the user accidentally accepts. Using this number matching method, it forces the user to match the login attempt they are trying to approve
[2.png](images/2.png)

[3.png](images/3.png)

## 3. `GitHub` Secret Scanning Push Protection
`GitHub` push protection is a strong implementation as it can scan the codebase for hardcoded credentials like secrets and tokens, before they reach the repository. If `GitHub` detects a (supported) secret during a push, it will block the push and give the developer immediate feedback so the secret can be removed before it becomes part of the repository history.

For repository:
[4.png](images/4.png)

For User:
[5.png](images/5.png)

Source: https://docs.github.com/en/code-security/concepts/secret-security/about-push-protection

## 4. `Cloudflare` Web Application Firewall
`Cloudflare`’s Web Application Firewall is a strong security implementation as it can inspect incoming web traffic and apply set rules before the traffic reaches the server. This can help block common web attacks such as injection attacks, malicious bots and known exploit patterns. A `WAF` is not a replacement for secure coding, but it is still recommended as it adds an additional layer of security in front of a website.
[6.png](images/6.png)

## 5. Apple Secure Enclave
Apple Secure Enclave is a strong device security implementation as it separate and isolate sensitive cryptographic implementations from the main processor. It is used for security features such as `FaceID` (or `TouchID`), key handling and device protection. This makes sures that the sensitive keys can be protected even if the normal software is compromised, as the keys are handled with separate hardware.
[7.png](images/7.png)

https://support.apple.com/en-au/guide/security/sec59b0b31ff/web
