
# Decryption Engine for STM32 Microcontroller

## Overview
The Decryption Engine is a firmware designed for STM32 microcontrollers to facilitate the decryption of incoming data based on various encryption protocols. It provides a versatile solution for secure communication by supporting different encryption algorithms such as XOR, DES, and AES-128.


## Key Features
- **Support for Multiple Encryption Protocols:**   
The engine supports various encryption protocols including no encryption, XOR encryption, DES encryption, and AES-128 encryption, providing flexibility for different use cases.

- **Secure Key Storage:**  
Decryption keys are securely stored within the firmware, ensuring protection against unauthorized access and tampering.

- **UART Communication:**  Communication with external devices is established via UART interface, allowing seamless integration with other systems.

- **Error Handling:** The engine includes robust error handling mechanisms to detect and handle decryption failures, ensuring the integrity of decrypted data.

- **Efficient Resource Utilization:** Optimized for STM32 microcontrollers, the firmware utilizes system resources efficiently, minimizing memory footprint and processing overhead.

## Specifications
- **Microcontroller Platform:**  STM32F042K6

- **Encryption Algorithms:**
  1. No Encryption 
  2. XOR Encryption
  3. DES Encryption
  4. AES-128 Encryption

- **UART Interface:**  
Configurable baud rate and communication mode

- **Decryption Key Size:**  
128 bits (16 bytes) for AES-128 encryption, variable for other algorithms

- **Input Data Size:**  
8 or 16 bytes, depending on the selected encryption protocol

- **Error Handling:**   Success/failure indication for each decryption attempt

- **Development Environment:**     Developed using STM32CubeIDE

- **Output format:**  
   1. binary blob
   2. Intel HEX
   3. elf
