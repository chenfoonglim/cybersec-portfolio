# B14. Teach your friends about cybersecurity topic of your choice.
Overview: I created a short presentation to teach my friend about safely using AI from a cybersecurity perspective. I chose this topic as LLMs are commonly used now for studies, coding, and also writing, but many of them do not understand the new security risks that comes with using them.
The slideshow is called “Safety Using AI: A Cybersecurity Perspective”. In there, I explained that AI systems behave differently from traditional software as their outputs are probabilistic and context sensitive. This makes them useful, but also new attack methods.
I covered prompt injection, data leakage, adversarial inputs, model inversion, membership inference, supply chain attacks, and jailbreaking.
- For prompt injection, I explained how a user or a hidden document text can override the intended instructions of the AI system
- For jailbreaking, I explained how roleplaying or indirect prompting can sometimes bypass the model guardrails.
- I also explained that models that are trained on private data should be treated as sensitive assets, as they may leak or even real information about their training data.
Overall, I tried keeping it practical by including simple examples. I explained that AI should not be treated as the last line of defence, and that there should also be output filtering and strong application logic too. The main message was that AI can be useful, but it should not be trusted blindly.
My friend was particularly intrigued by prompt injection as she did not realise how easy it was to trick an AI model to doing something it shouldn’t using hidden instructions, especially for weaker models.
![1.png](images/1.png)

The slides are included in my `GitHub` as evidence.
