# A10. Discover privacy technique used offline.

**Overview:** I identified three offline privacy techniques, document shredding, privacy screens, and the MacBook hardware camera indicator and microphone disconnect.

1. **Document Shredding**
    - Physical documents containing sensitive information like bank statements and medical records remain readable long after they are discarded. Just throwing it away however would create a risk from dumpster diving, where an attacker retrieves discarded documents to extract personal information.
        
        To mitigate this risk, a paper shredder can be used to destroy sensitive documents before throwing them away. The paper shredder shreds the paper into small confetti-like pieces that makes it extremely hard to piece together, making the original content virtually unrecoverable. This is a physical data destruction technique, where privacy comes from making the information physically irretrievable rather than encrypting it.
        
2. **Privacy Screen**
    - A privacy screen is a physical filter applied to a phone (or any) display that narrows the viewing angle. When applied, the screen appears normal when viewed directly from the front but will appear dark from the sides. This prevents “shoulder surfing”, which is when someone nearby tries to see contents on your screen without permission. This is especially relevant in public areas like dining area, libraries and public transport.
        
        This privacy filter works by embedding thousands of microscopic vertical slats on the filer. These slats are small enough to not be noticed by the naked eye. These slats make it so that when you look straight to the screen, light passes through the slats allowing you to see the screen normally, but looking at it from an angle, the slats block the light at that angle, making the screen appear dark or black from the side.
        
        Below are images I took showcasing how the privacy screen affects what you can see from different angles.

        (refer to `2_angle_1`,`2_angle_2` and `2_angle_3`)

3. **MacBook hardware Camera Indicator and Microphone Disconnect**
    - MacBooks have hardware-level privacy protections built into many of the physical design of the device. Two notable privacy measures are for the camera and the microphone.
    - Camera Indicator: Apple redesigned the camera module so that the sensor and the green indicator light share the same physical circuit. This means that it is physically impossible for the camera to receive power unless the LED does too. This would mean no malicious software, no matter what privileges they have, can turn on the webcam without triggering the indicator.
    - Microphone Disconnect: All Apple silicon MacBooks also feature a hardware disconnect that disables the microphone whenever the lid is closed. Similar to the camera indicator, this feature is implemented in hardware alone, this means any software even with root or kernel privileges in macOS will not be able to engage with the microphone when the lid is closed. This is done using a hinge angle sensor (or hall effect sensor) emitting a direct hardware signal through non-reprogrammable logic to physically cut the microphone connection.
        
        These privacy measures prevent any attackers or malwares to covertly recording me without my knowledge.