# A7. Discover cryptography used in modern networks.

**Overview:** I identified two real world examples of cryptography used in modern networks, which are TLS/HTTPS  on YouTube, and an SSH handshake to GitHub observed using the terminal.

1. **TLS Certificate on YouTube:**
    - I inspected YouTube’s TLS certificate using Firefox’s certificate viewer by going to YouTube > clicking the shield icon > clicking “Connection Secure” > clicking “More site information”
    - TLS (Transport Layer Security) is the technology behind HTTPS as it encrypts the connection between the browser and website so nobody can read nor tamper with the data. This certificate is what YouTube shows to prove its identity and to establish encryption during the TLS handshake.
    - We see the subject as `*.google.com` (this is a wildcard and covers YouTube). The Issuer is Google Trust Services (WR2), we also see the public key algorithm to be elliptic curve (256 bit) and its signature algorithm to by SHA-256 with RSA encryption. In the certificate we also see that it is only valid until 25 May 2026.
    - YouTube uses Elliptic Curve Cryptography with 256-bit key rather than just RSA, as ECC (256 bit key) provides equivalent security to RSA with a larger bit key, while being much faster which matters for Google’s scale of operations.
    - SHA-256 signs the certificate to ensure its contents cannot be tampered with.
2. **SSH Handshake to GitHub**
    - SSH (Secure Shell) is a network protocol that uses cryptography to establish a secure connection between two computers over a network. To observe it in action, I ran `ssh -v github.com` in my terminal. The `-v` flag enables verbose mode, which prints every step of the handshake in real time. Running this does not grant access to GitHub, it is just to attempt a connection and is mainly used here to observe the negotiation process.
    - The verbose output revealed the following cryptographic parameters negotiated between my laptop and their server:
        - **Key exchange:** `ecdh-sha2-nistp256` which is Elliptic Curve Diffie-Hellman on the P-256 curve with SHA-256. This establishes a shared session key between my laptop and GitHub without ever transmitting it. Even if the traffic is intercepted, the key cannot be derived.
        - **Host key algorithm:** `ssh-ed25519`. GitHub authenticates its identity using Ed25519, which is a modern elliptic curve signature algorithm
        - **Session Cipher:** [`aes128-gcm@openssh.com`](mailto:aes128-gcm@openssh.com) – All data is encrypted using AES-128 in GCM mode, this provides gives both checking for encryption and integrity.
        - **Host fingerprint**: `SHA256:+DiY3wvvV6TuJJhbpZisF/zLDA0zPMSvHdkr4UvCOqU`. I further verified this against GitHub’s officially published fingerprints at [`https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/githubs-ssh-key-fingerprints`](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/githubs-ssh-key-fingerprints) .The keys matched perfectly (Ed25519), which confirms that I was connecting to the real GitHub and not a site impersonating GitHub.
- This shows multiple cryptographic concepts working together at the network layer, where key exchange authentication and encryption are all handled by different algorithms within a single connection attempt.