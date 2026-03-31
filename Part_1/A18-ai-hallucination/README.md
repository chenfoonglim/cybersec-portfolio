# A18. Discover two hallucination cases when using a generative AI system.

**Overview:** An AI hallucination occurs when a generative AI system produces information that are factually incorrect, logically flawed, or completely made up, whilst presenting the information with the confidence as though the information is correct. This happens as large language models at its core only predict the next statistically likely text rather than reasoning through problems. The following two cases demonstrate hallucinations in a documented real-world incident, and a personal practical test.

1. **Mata v. Avianca**
    - In May 2023, lawyer Steven Schwartz used ChatGPT to assist with legal research for the case Roberto Mata v. Avianca Inc (personal injury lawsuit). ChatGPT provided legal case citations, which was submitted in the court brief. However, it was found that 6 of the submitted cases seems to be entirely made up, with fabricated judicial decisions, quotes, and internal citations.
        
        When it was pointed out that the cited cases cannot be located, the attorney asked ChatGPT to confirm if the cases were real, which ChatGPT confirmed. When asked to produce a copy of one of the cases. ChatGPT fabricated the entire case from scratch. The lawyers were sanctioned by the court and some federal judges issued standing orders requiring attorneys to disclose the use of AI in filings and to verity all their generated content independently.
        
    
    Sources:
    
    - https://www.legaldive.com/news/chatgpt-fake-legal-cases-generative-ai-hallucinations/651557/
    - https://www.bitlaw.com/ai/hallucinations-and-AI.html
    
2. **Local AI Microsoft Teams Release Date Hallucination**
    - I asked my local AI Model (`qwen3.5:35b-a3b`) “What happened on 14 January 2018 at Microsoft?”. The model confidently stated that January 14, 2018, was the date that Microsoft Teams became available to the public, generating a detailed response with functionality descriptions and strategic context.
        
        This is a hallucination as Microsoft Teams was released on March 14, 2017, which was almost a year earlier. The model identified a real event but attached it to the wrong date but still built a confident detailed explanation around it.