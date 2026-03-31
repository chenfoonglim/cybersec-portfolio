# A13. Discover 5 unique online security tools.

**Overview:** Online security tools are any software or service used to protect devices or data while connected to the internet. These tools can actively monitor, detect and respond to threats in real time over a network connection. I identified 5 distinct tools I use regularly, covering network protection, credential monitoring, device security, and DNS level threat blocking.

1. **Norton 360 (Antivirus and Security Suite)**
    - Norton 360 is a comprehensive online security suite that provides real-time protection against malware, viruses, ransomware, spyware and phishing attempts. Their real time antivirus uses multiple detection methods including signature matching, heuristic analysis and machine learning. Signature matching checks files against a database of known malware, while heuristic analysis detects suspicious behaviours from unknown threats. They also have a Safe Web feature which sends notifications to warn against suspicious links before they load. Below are screenshots using Norton to do a device scan, the dashboard, and opening a (suspicious) Instagram advertisement link.
        
        (refer to `1_scan`, `1_dashboard`, `1_sus_link`)
        
2. **Mac Firewall**
    - The macOS built in firewall is an application layer firewall that controls which application and services are allowed to accept incoming network connections. This allows the blocking of unauthorised incoming connections while allowing trusted apps and system services to communicate. It works by allowing or denying specific applications, which indirectly protects the ports they use. This is particularly important on shared networks, where other devices may attempt to scan or connect to the laptop. Users can also further configure the firewall, and to enable stealth mode, which prevents the laptop to respond to probing requests.
3. **Have I Been Pwned (HIBP)**
    - Have I Been Pwned is a free online tool that checks whether an email address or password has appeared in a known data breach. To securely test the password, it is first hashed client side with `SHA-1`, then only the first 5 characters of the hash are sent to their servers using a k-anonymity implementation. The server then returns all hash suffixes matching that 5-character prefix, and the check will happen on device. This ensures HIBP cannot directly know the password that was checked. Below are screenshots of the status of my email address, and a common password `abd12345`
        
        (refer to `3_email` and `3_password`
        
4. **Apple Find My**
    - Apple Find My is an online security tool that uses a crowdsourced network of Apple devices to help locate, lock and remotely wipe lost or stolen Apple devices. The Find My network uses end to end encryption so that Apple cannot see the location of any offline device or reporting device. When a device is marked as lost, Activation Lock activates, which requires an Apple Account password or device passcode before Find My can be turned off, or to erase and reactivate the device. This makes a stolen Mac or iPhone essentially unusable without the owners’ credentials, deterring theft. Screenshots below show evidence that a marked as lost MacBook requires an Apple ID or device password to reactivate.
        
        (refer to `4_apple_lost`)
        
5. **DNS Filtering (Cloudflare 1.1.1.2)**
    - DNS filtering is a security technique that blocks access to malicious domains at the DNS resolution stage, which happens before any connection is made to the dangerous server. I use Cloudflare’s 1.1.1.2 DNS resolver as it includes malware blocking. DNS filtering prevents malware attacks by blocking access to sites known to host malicious software. As no web content can load until the DNS process is complete, the filter stops communication between the device and the malicious server at the earliest possible stage. If the domain in a DNS query is classified as malicious, depending on the configuration, the resolver may return an invalid IP address (0.0.0.0) or indicate that the domain does not exist.
        
        This filtering is demonstrated by running `dig malware.testcategory.com` in terminal and comparing 1.1.1.2 against Google’s 8.8.8.8 DNS. Googles returned a real IP and loaded the site, while 1.1.1.2 returned 0.0.0.0 and blocked it, confirming DNS filtering effectiveness.
        
        **With 1.1.1.2:**
        
        (refer to `5_cloud_1` and `5_cloud_2` 
        
        **With others (8.8.8.8):**
        
        (refer to `5_google_1` and `5_google_2`