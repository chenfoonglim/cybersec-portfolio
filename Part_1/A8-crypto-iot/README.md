# A8. Discover cryptography used in Internet of Things devices.

**Overview:** Cryptography is used in plenty of IoT devices, for this section I have identified two that I own, namely my Apple Watch and a smart LED strip that is controlled by the Tuya application on my phone.

1. **Apple Watch (Series 8)**
    - The Apple Watch Series 8 is an IoT wearable device that continuously collects sensitive health data including heart rate, ECG readings and sleep patterns. It uses cryptography both to protect stored data and to establish a secure communication with the phone.
        
        When the watch pairs with an iPhone, each device generates a random Ed25519 public and private key pairs, and exchanges public keys. The Apple watch stores the private key to its own Secure Enclave. All communications after that between the phone and watch are encrypted using `AES-256-GCM` (used for confidentiality and integrity). The Bluetooth device address also rotates every 15 minutes to prevent the watch from being tracked by persistent identifiers.
        
        All Apple Watch S-series chip contains a built-in Secure Enclave, which handles all cryptographic operations in hardware, this means keys never leave the chip. This also means that without the password nor the right chip, the data will not be decrypted.
        
2. **Smart LED Strips**
    - I own a smart light that is connected to Trinity College’s Wi-Fi and controlled via the Tuya app. TLS 1.2 is used for the devices connected and the Tuya cloud, so when I control the light from my phone, the command travels from the app to Tuya’s cloud, and down to the device, all encrypted with TLS. Tuya also uses AES encryption on the device itself with a unique dynamic key per device, so even if the device is physically stolen, the data will still not be able to be deciphered.
    - As seen in the device Information screenshot from the app, each device is assigned a unique Virtual ID, a device identifier that is flashed to the hardware at the factory. This is used by Tuya’s cloud to authenticate legitimate devices. This prevents other residents who have access to the same Wi-Fi network to potentially communicate and control the device.