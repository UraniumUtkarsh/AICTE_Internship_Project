# AICTE_Internship_Project

### **🛠 Secure Data Hiding In Images Using Steganography**  

## **📌 Project Overview**  
This project implements **image-based steganography** to hide secret messages within images while maintaining image integrity. It utilizes the **Least Significant Bit (LSB) technique** along with **password protection** to ensure secure data encoding and retrieval.  

## **🚀 Features**  
✅ **Secure Message Hiding** – Uses LSB steganography for imperceptible data embedding.  
✅ **Password-Protected Extraction** – Prevents unauthorized access to hidden messages.  
✅ **Minimal Image Distortion** – Keeps the visual quality of the image intact.  
✅ **Efficient Storage Management** – Dynamically utilizes pixel channels for optimized data embedding.  
✅ **User-Friendly** – Simple command-line interface for encryption and decryption.  

## **🛠 Technologies Used**  
- **Programming Language:** Python  
- **Libraries:** OpenCV, NumPy  
- **Concepts:** Image Processing, Steganography, Data Security  
- **Encoding:** UTF-8 for compatibility across different character sets  

## **🔧 Installation & Setup**  
1️⃣ **Clone the repository:**  
```sh
git clone https://github.com/UraniumUtkarsh/AICTE_Internship_Project
cd AICTE_Internship_Project
```  
2️⃣ **Install dependencies:**  
```sh
pip install opencv-python numpy
```  
3️⃣ **Run the program:**  
- **Encryption:**  
```sh
python stegv2.5.py
```  
- Choose `(E)ncrypt`, enter the image path, message, and password.  
- The encrypted image is saved as `encryptedImage.png`.  

- **Decryption:**  
```sh
python stegv2.5.py
```  
- Choose `(D)ecrypt`, enter the image path and password.  
- The hidden message is revealed if the correct password is provided.  

## **🖥 Usage Example**  
🔹 **Encrypting a Message:**  
```sh
Enter image path: secret.png
Enter secret message: This is confidential!
Enter a passcode: mypassword123
Message encrypted successfully!
```  

🔹 **Decrypting a Message:**  
```sh
Enter image path: encryptedImage.png
Enter passcode for decryption: mypassword123
Decrypted message: This is confidential!
```  

## **🔮 Future Scope**  
🔹 **AES/RSA encryption** for additional security.  
🔹 **Support for video and audio steganography.**  
🔹 **Mobile & web-based integration.**  
🔹 **Blockchain-based tamper-proof steganography.**  

## **📜 License**  
This project is open-source and available under the **MIT License**.  

---

### **💡 Contribute & Support**  
Feel free to **fork, improve, or suggest enhancements** by creating a pull request. For any queries, open an issue in the repository. 🚀  

