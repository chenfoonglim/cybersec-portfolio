# A15. Discover 5 recent security incidents.

**Overview:** I have picked out 5 security incidents based on recentness (2024 onwards), its impact (scale of disruption), and the overall quality of documentation on the incident. Together they cover a diverse range of incidents, from supply chain software failure, nation-state espionage, ransomware to simultaneous multi vector attacks.

1. **CrowdStrike Global IT Outage (July 2024)**
    - On July 19, 2024, a cybersecurity firm called CrowdStrike pushed a faulty sensor configuration update. The update was designed to detect new malicious behaviour patterns. However, the configuration had a logic error causing an invalid memory access, which resulted in an operating system crash, which caused a BSOD and endless reboot loop. Microsoft estimated 8.5 million Windows devices were affected.
        
        Healthcare and banking were the sectors that were hit the hardest, with an estimated loss of 1.94 billion and 1.15 billion respectively, with the total cost to Fortune 500 companies reaching 5.4 billion. The faulty update was withdrawn within 78 minutes, however the recovery required users to manually reboot in safe mode and deleting the bad file, with an automated fix only releasing 3 days later.
        
    
    Sources:
    
    - https://www.crowdstrike.com/en-us/blog/falcon-update-for-windows-hosts-technical-details/
    - https://www.techtarget.com/whatis/feature/Explaining-the-largest-IT-outage-in-history-and-whats-next
    - https://www.cisa.gov/news-events/alerts/2024/07/19/widespread-it-outage-due-crowdstrike-update
    - https://www.cio.com/article/3853689/case-in-point-taking-stock-of-the-crowdstrike-outages.html
2. **Salt Typhoon, US Telecom Hack (2024)**
    - Discovered throughout 2024, Salt Typhoon is a Chinese state-sponsored APT (Advanced Persistent Threat) group linked to China’s Ministry of State Security that infiltrated nine major US telecommunications companies. They gained initial access by exploited known vulnerabilities in edge devices, which includes routers and firewalls, then used “living-off-the-land” techniques (running commands inside Linux containers on Cisco networking devices via Guest Shell, creating GRE tunnels and modifying access control lists, which allows them to move laterally while remaining undetected by standard network networking). The attackers specifically targeted systems that are mandated for court-authorised wiretapping, effectively turning law enforcement surveillance tools into their espionage instruments.
        
        They accessed metadata of calls and texts from over a million users, including high-profile political targets. It was considered as one of the “worst telecom hack in history”.
        
    
    **Sources:**
    
    - https://www.cybersecuritydive.com/news/att-verizon-salt-typhoon/736680/
    - https://en.wikipedia.org/wiki/Salt_Typhoon
    
3. **NHS Synnovis Ransomware Attack**
    - On June 3, 2024, the Russian-speaking Qilin ransomware gang attacked Synnovis, a pathology service provider for the National Health Service. Prior to encrypting files, the attackers first exfiltrated data from the network, which increased their leverage. Almost all their IT system were affected. The attackers then demanded a 50 million ransom which was refused, after which the stolen data was reportedly published online by the attackers.
        
        The attacked caused delays to over 11,000 outpatients In South-East London, with at least one death that was potentially linked to the disruption. More than 900,000 individuals’ personal data was reportedly compromised. The NHS activated emergency protocols, launched a blood donation appeal due to blood shortages caused by the inability to perform blood matching, and services were fully restored by December 2024.
        
    
    **Sources:**
    
    - https://www.england.nhs.uk/synnovis-cyber-incident/
    - https://www.infosecurity-magazine.com/news/synnovis-breach-notification-2024/
    - [https://therecord.media/synnovis-health-data-breach-investigation-onging](https://therecord.media/synnovis-health-data-breach-investigation-onging?utm_source=chatgpt.com)
    
4. **Internet Archive Breach and DDoS (October 2024)**
    - On October 9, 2024, the Internet Archive (non-profit digital library preserving billions of web pages), was hit by a data breach and a DDoS attack that happened around the same time, though it was not confirmed if both were attributed to the same actor. 33 million users had their data exposed from the breach, which included bcrypt-hashed passwords, email address and usernames. Though the passwords are hashed and therefore protected, the emails and usernames can still be used for malicious means like phishing.
        
        Personal data of 33 million users was exposed, and then concurrent DDoS attack took the site offline, hindering the response. The Internet Archive reset all user session keys, and the breach was later indexed on Have I Been Pwned.
        
    
    **Sources:**
    
    - https://www.bleepingcomputer.com/news/security/the-biggest-cybersecurity-and-cyberattack-stories-of-2024/
    
5. **Change Healthcare Ransomware Attack (February 2024)**
    - In February 2024 the ALPHV/BlackCat ransomware group gained access to Change Healthcare, which is a subsidiary of the UnitedHealth Group, by using compromised credentials on a Citrix remote access portal. The credentials were all it needed to access the portal as the it lacked two-factor authentication. The attackers spent several days moving through the network, exfiltrating data before deploying the ransomware on the 21. As the leaders did not initially know where the attackers point of entry was, they cut off connectivity with the data centre to prevent the malware from spreading over to other UnitedHealth Group systems.
        
        A large portion of the US healthcare providers were impacted by this attack, with 74% reporting direct patient care impact and 94% reported financial impact. The company estimated this breach could cost around 1.5 billion, with tens of millions of individuals potentially compromised. The UnitedHealth Group paid the 22 million ransoms but did not recover the stolen data.  They conducted an exit scam, with a second group called RansomHub subsequently demanding additional payment using the same stolen data.
        
    
    **Sources:**
    
    - https://www.aha.org/change-healthcare-cyberattack-underscores-urgent-need-strengthen-cyber-preparedness-individual-health-care-organizations-and
    - https://www.blackfog.com/change-healthcare-landmark-cybersecurity-breach/
    - https://www.ibm.com/think/news/change-healthcare-22-million-ransomware-payment
    - https://www.hipaajournal.com/change-healthcare-responding-to-cyberattack/