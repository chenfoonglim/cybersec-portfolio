# A23. Enhance the cybersecurity at your home.

**Overview:** As a student living at Trinity College, I share a residential Wi-Fi network with all new residents, with everyone using the same credentials to access the network. This means any device on the network could potentially monitor traffic or discover other devices that are connected to the network. As I already use a VPN and DNS to HTTPS, the following three measures were implemented as additional layers of protection specifically against shared network threats

1. **iCloud Private Relay**
    - Private Relay is an iCloud+ feature that routes Safari traffic through 2 separate relay servers. The first (operated by Apple), can see the user’s IP address but cannot see the destination website as DNS records are encrypted. The second relay (operated by a third party) generates a temporary IP address and decrypts the destination to connect to the site but cannot see the original IP.
    - This means no single party can see both who you are and what you are browsing. This is different from DNS over HTTPS, as that only encrypt DNS queries but still exposes the destination IP to the network. Private relay, hence, provides a stronger protection against traffic monitoring on the shared network.
2. **HTTPS-Only Mode (Firefox) and Safari Fraudulent Site Warning**
    - Firefox by default does not have HTTPS only mode enabled. Having this enabled is especially important for shared networks, as unencrypted HTTP traffic can be read by other users through a man-in-the-middle attack. Enforcing HTTPS ensures all web traffic is encrypted in transit, so even if the traffic is intercepted by an attacker, the contents would still be unreadable.
        
        Safari does not have this feature, however, we can still ensure that it will warn us before we connect to a website over HTTP and simply manually refusing the connection.