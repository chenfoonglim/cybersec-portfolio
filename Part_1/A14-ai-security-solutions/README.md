# A14. Discover 5 AI-enabled security solutions.

**Overview:** AI-enabled security solutions are tools that use Artificial Intelligence or Machine Learning to enhance security. AI based solutions can learn patterns from large datasets and predict and identify previously unseen threats, and power security features like biometric authentication and fraud prevention that would not have been possible with traditional rule-based approaches. I have identified 5 AI enabled security solutions that I use or encounter in my daily life.

1. **Google reCAPTCHA v3**
    - Google reCAPTCHA v3 is an AI-powered bot detecting system used on websites to distinguish human users from bots without requiring the user to solve a puzzle. Previous versions of CAPTCHA’s shows distorted test or image grid puzzles, whereas v3 runs invisibly in the background, assigning a risk score from 0 to 1 based on behavioural signals. These signals include mouse movements, typing patterns, browsing history, and interaction timing. A score that is close to 1 indicates human interaction, while close to 0 indicates a bot. This model is trained on billions of interactions across Googles network and is still improving to detect more sophisticated bots that tries to mimic human behaviour.
        
        This is verified by going to Discord’s website and inspecting their Content Security Policy, which shows `google.com/recaptcha`, `recaptcha.net/recaptcha`, and `gstatic.com/reCAPTCHA`. This shows Discord permits and uses reCAPTCHA on their site. When logging into Discord normally, no CAPTCHA challenge appears, which is the intended behaviour of v3, which runs invisibly in the background and only triggers when the score is low enough to suspect a bot.
        
        This protects websites from automated attacks like credential stuffing and fake account creation.
        
2. **Face ID**
    - Face ID is an AI-powered biometric authentication system built into iPhones and iPads. When set-up, the TrueDepth camera project over 30,000 infrared dots onto the face to create a depth map, which is processed by the Secure Neural Engine to generate a mathematical representation of facial geometry. Each attempt to unlock compares the live scan against the stored model using the neural network. Face ID learns and adapts to gradual changes like growing beard or ageing without having to “renew” the original face scan. The entire process happens inside the Secure Enclave, and the data never leaves the device nor reaches Apple’s servers.
        
        Users can set Face ID so that it requires attention and only authenticate when you are looking at your phone. Face ID can be used for unlocking the phone, installing apps, payments, password autofill, and unlocking apps. This provides a secure and convenient way to authenticate a user that is harder to bypass than a regular PIN or password.
        
3. **Apple Mail Spam Filter**
    - Apple Mail uses on-device machine learning to automatically classify incoming emails as spam or legitimate. It analyses senders’ reputation, email headers, content patterns, links and past behaviour of the user to assign each email a spam probability score. Emails above the threshold are moved to the “Junk” folder automatically. When a user marks certain email as junk, the model updates its classification weights for that user. This is considered a form of personalised supervised learning where the user corrections become training data. The screenshot below shows a spam email correctly classified by the AI filter.
    - This feature protects users from phishing attacks and malicious links from emails.
4. **CCTV with AI (Eufy).**
    - Modern CCTVs increasingly use AI-powered video analytics rather than just plain recording. AI CCTV can perform real-time object detection, which can be used to detect human movement. When connected to the internet, it allows homeowners to get notified when there are suspicious movement without the need for them to constantly watch the live feed. This transforms CCTV from a passive recording tool into an active security system.
5. **Cloudflare Bot Fight Mode and AI Labyrinth**
    - I use Cloudflare on my personal domain `chenfoong.com` with two AI-powered bot protections enabled.
    - Bot Fight Mode uses machine learning to detect and challenge bot traffic. The ML engine analyses request features including headers, session characteristics and browser signals to produce a bot likelihood score from 1 to 99. A low score will trigger challenges or automatic blocks.
    - AI Labyrinth takes a deception-based approach. Instead of blocking bots, it adds AI generated links invisible to humans but visible to bots, leading scrapers into fake AI-generated content, wasting their resources.