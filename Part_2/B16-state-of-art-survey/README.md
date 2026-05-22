# B16. Survey the current state-of-the-art solutions in cybersecurity.
Overview: I researched and surveyed the current state-of-the-art defensive cybersecurity solutions and focused on new technologies and approaches that are currently used to reduce modern attack risks.
## 1. Zero Trust Architecture
Zero trust is a type of security model where no user, device or network location is trusted by default. Instead of assuming that anything inside the network is considered safe, every access is checked based on their identity, device state, context and also policy.

This is state of the art as organisations now use cloud services, remote work, SaaS applications and also personal devices, these makes having a single trusted internal network boundary to be unrealistic. Zero trust reduces “over-trust” by using the least privilege and continuous verification, this makes it so that devices only get the access they need.

One example of its application is BeyondCorp by Google. According to Google Cloud, BeyondCorp is Google’s security model and product approach for letting employees access internal applications without relying on using traditional VPN. Instead of trusting someone just because they are on the corporate network, BeyondCorp checks other factors like user identify, the device, and access context before allowing access.

Sources:
https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-207.pdf
https://cloud.google.com/beyondcorp

## 2. Confidential Computing
Confidential computing protects data while it is being processed, not only when it is stored or transmitted. This normally uses a hardware-based trusted execution environment, or secure enclaves (isolated area inside a processor that runs sensitive code and keep data protected from the rest of the system).

This is important as cloud systems often involve the handling of sensitive data, which is processed on infrastructures that the organisation does not physically control.

The goal of this is to reduce the amount of trust placed in a cloud provider, system administrator, and also the surrounding infrastructure by protecting the confidentiality and integrity of the data that is in use

One example is Signal using server-side secure enclaves for secure value recovery. Signal explains that the enclave runs on the server and can store recovery values in a hardware-encrypted memory, while clients use remote attestation to check that they are communicating with the correct enclave code over an encrypted channel.

https://confidentialcomputing.io/about/
https://signal.org/blog/secure-value-recovery/

## 3. Post Quantum Cryptography Migration
This focuses on cryptographic algorithms that are designed to resist attacks from future (potential) quantum computers. This is considered state-of-the-art as NIST released its cryptographic standards in 2024, and organisations now need to start planning migrations from existing quantum-vulnerable algorithms.

The main risk is that attackers may collect encrypted data and decrypt it later when quantum technology improves, this makes mitigation planning important even before large quantum computers even exist.

One example of this implemented is Apples usage of post-quantum cryptography in iMessage through its PQ3 protocol Apple described it as a major cryptographic upgrade for iMessage, which will protect conversations against future quantum attacks and any “harvest now, decrypt later” risks.

Source:
https://www.nist.gov/cybersecurity-and-privacy/what-post-quantum-cryptography
https://security.apple.com/blog/imessage-pq3/

## 4. Deception Technology
Deception technology uses decoy systems, fake credentials, honeytokens or fake data to detect and to study attackers. This is different from only blocking attacks. Instead, this approach gives attackers something fake to interact with, which can create high-confidence alerts when the decoy is touched.

This can be considered state-of-the-art as a lot of modern defensive approaches use adversary engagement and deception to not only waste attackers time, but to also learn the attacker’s behaviour and detect activity that may bypass normal controls.

One instance of this deceptive technology being implemented is `Cloudflare`’s, AI labyrinth. When suspicious crawlers are detected, `Cloudflare` can send them into generated decoy pages instead of the real website. This wastes the crawlers resource and acts like a honeypot as interaction with the decoy pages will give `Cloudflare` a stronger signal that the visitor is a bot.

https://www.mitre.org/news-insights/impact-story/active-defense-using-deception-and-trickery-defeat-cyber-adversaries
https://blog.cloudflare.com/ai-labyrinth/
