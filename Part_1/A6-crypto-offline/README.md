# A6. Discover cryptographic implementation used offline.

**Overview:** I identified three offline cryptographic implementations used offline on my own devices, namely macOS FireVault disk encryption, an APFS encrypted SSD and an AES encrypted ZIP file I created myself. All of them use encryption offline and do not need an internet connection.

1. **MacOS FireVault and Hardware UID**
    - FireVault is Apple’s built in disk encryption feature. On my Apple silicon MacBook, the internal SSD is always hardware-encrypted by default, this is a feature on Apple Silicon MacBooks that cannot be turned off. This encryption is tied to the Hardware UID, which is a unique cryptographic key that is permanently burned into the chip at the factory, and never leaves the Secure Enclave (an isolated hardware-based security coprocessor) and cannot be copied or transferred.
        
        This means even with FireVault turned off, if someone removes the SSD and connects it to another computer, the data is completely unreadable. The drive can only be decrypted by the specific chip it belongs to. Below is a diagram from Apple support visualising the process with FireVault turned off:
        
    - FireVault provides an extra layer of protection by requiring a login password to access the data even with the right chip. Without FireVault, the MacBook will automatically unlock upon startup just using the Hardware UID, so someone who steals the MacBook can turn it on and access everything. FireVault prevents this by adding the login password as a second requirement to unlock the encryption key. Below is an image from Apple Support visualising the process with FireVault turned on:
    - FireVault uses AES-XTS encryption, and on Apple silicon, all key handling occurs in the Secure Enclave so that encryption keys are never exposed to the CPU.
    - To summarise, Hardware UID protect against drive theft, and FireVault prevents someone using the whole laptop without the password.
2. **APFS Encrypted External SSD (Samsung T7)**
    - I recently reformatted my Samsung T7 external SSD, named “Brain”, to APFS (Encrypted) using macOS Disk Utility to make it more compatible with my Mac. APFS (Apple File System) is Apple’s own file system which has native encryption built in. When formatted as APFS encrypted, every file that is written to the drive will be automatically encrypted before being stored.
        
        APFS uses AES-XTS encryption scheme, so the data stored in my APFS encrypted volume cannot be read by anyone who does not know the correct password.
        
    - One distinction from the internal drive is that external drives does not use Secure Enclave as it lacks the dedicated hardware to use it. Instead, encryption is entirely dependent on software.
    - The image below shows evidence that the APFS volume on the SSD drive is encrypted.