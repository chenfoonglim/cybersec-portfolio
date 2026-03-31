# A4. Discover a vulnerable website.

**Overview:** I identified and analysed the security vulnerabilities of flixmomo.org, an unofficial movie streaming website, using Mozilla Observatory’s HTTP security header scanner and Firefox’s and TLS inspection on mobile 4G connection. No attacks were performed.

**Findings**

1. **Irregular TLS Failure**
    - When first visiting the site, Firefox and Safari returned a “A TLS error caused the secure connection to fail”. The site loaded successfully after a period, suggesting an intermittent TLS misconfiguration. A properly configured sit should have a consistent and reliable TLS, this inconsistent behaviour indicates the certificate or TLS configuration might not be applied uniformly, and as a result some users may be unable to establish an encrypted connection depending on which server they are routed to.
2. **Mozilla Observatory Scan**
    - Mozilla Observatory is a web security scanning tool developed by Mozilla. It analyses a website’s HTTP response headers, which are the instructions that a server send to the browser telling it how to behave. It lists out which security headers are present or missing, and below are the findings:
        
        
        | Missing Header | Risk |
        | --- | --- |
        | Content Security Policy | Vulnerable to XSS and malicious ad injection. This header tells which script are allowed to run |
        | Strict Transport Security | Browser not forced to use HTTPS which means downgrade attacks are possible |
        | X-Frame-Options | Page can be embedded in iframes, increasing risk of clickjacking |
        | Referrer Policy | Leaks browsing URL to third parties |
        | X-Content-Type-Options | Browser may misinterpret file types |
        
        Some of these missing headers (like CSP) are likely deliberately left missing and vulnerable as to support third party advertising and streaming.