from flask import Flask, render_template, request, jsonify
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayFairCipher
from cipher.transposition import TranspositionCipher

app = Flask(__name__)

# Khởi tạo các đối tượng mã hóa
caesar_cipher = CaesarCipher()
vigenere_cipher = VigenereCipher()
railfence_cipher = RailFenceCipher()
playfair_cipher = PlayFairCipher()
transposition_cipher = TranspositionCipher()

# Trang chủ
@app.route('/')
def home():
    return render_template('index.html')

# ------------------- Caesar Cipher -------------------
@app.route('/caesar')
def caesar():
    return render_template('caesar.html')

@app.route('/caesar/encrypt', methods=['POST'])
def caesar_encrypt():
    try:
        text = request.form.get('inputPlainText', '').strip()
        if not text:
            raise ValueError("Plain text is required.")
        key = request.form.get('inputKeyPlain', '')
        if not key:
            raise ValueError("Key is required.")
        key = int(key)
        encrypted_text = caesar_cipher.encrypt(text, key)
        return render_template('caesar.html', encrypted_text=encrypted_text, key=key, error=None)
    except ValueError as ve:
        return render_template('caesar.html', error=str(ve), key=None)
    except Exception as e:
        return render_template('caesar.html', error=f"An error occurred: {str(e)}", key=None)

@app.route('/caesar/decrypt', methods=['POST'])
def caesar_decrypt():
    try:
        text = request.form.get('inputCipherText', '').strip()
        if not text:
            raise ValueError("Cipher text is required.")
        key = request.form.get('inputKeyCipher', '')
        if not key:
            raise ValueError("Key is required.")
        key = int(key)
        decrypted_text = caesar_cipher.decrypt(text, key)
        return render_template('caesar.html', decrypted_text=decrypted_text, key=key, error=None)
    except ValueError as ve:
        return render_template('caesar.html', error=str(ve), key=None)
    except Exception as e:
        return render_template('caesar.html', error=f"An error occurred: {str(e)}", key=None)

# ------------------- Vigenère Cipher -------------------
@app.route('/vigenere')
def vigenere():
    return render_template('vigenere.html')

@app.route('/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    try:
        text = request.form.get('inputPlainText', '').strip()
        if not text:
            raise ValueError("Plain text is required.")
        key = request.form.get('inputKeyPlain', '').strip()
        if not key:
            raise ValueError("Key is required.")
        encrypted_text = vigenere_cipher.vigenere_encrypt(text, key)
        return render_template('vigenere.html', encrypted_text=encrypted_text, key=key, error=None)
    except ValueError as ve:
        return render_template('vigenere.html', error=str(ve), key=None)
    except Exception as e:
        return render_template('vigenere.html', error=f"An error occurred: {str(e)}", key=None)

@app.route('/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    try:
        text = request.form.get('inputCipherText', '').strip()
        if not text:
            raise ValueError("Cipher text is required.")
        key = request.form.get('inputKeyCipher', '').strip()
        if not key:
            raise ValueError("Key is required.")
        decrypted_text = vigenere_cipher.vigenere_decrypt(text, key)
        return render_template('vigenere.html', decrypted_text=decrypted_text, key=key, error=None)
    except ValueError as ve:
        return render_template('vigenere.html', error=str(ve), key=None)
    except Exception as e:
        return render_template('vigenere.html', error=f"An error occurred: {str(e)}", key=None)

# ------------------- Rail Fence Cipher -------------------
@app.route('/railfence')
def railfence():
    return render_template('railfence.html')

@app.route('/railfence/encrypt', methods=['POST'])
def railfence_encrypt():
    try:
        text = request.form.get('inputPlainText', '').strip()
        if not text:
            raise ValueError("Plain text is required.")
        key = request.form.get('inputKeyPlain', '')
        if not key:
            raise ValueError("Key is required.")
        key = int(key)
        if key <= 0:
            raise ValueError("Key must be a positive integer.")
        encrypted_text = railfence_cipher.rail_fence_encrypt(text, key)
        return render_template('railfence.html', encrypted_text=encrypted_text, key=key, error=None)
    except ValueError as ve:
        return render_template('railfence.html', error=str(ve), key=None)
    except Exception as e:
        return render_template('railfence.html', error=f"An error occurred: {str(e)}", key=None)

@app.route('/railfence/decrypt', methods=['POST'])
def railfence_decrypt():
    try:
        text = request.form.get('inputCipherText', '').strip()
        if not text:
            raise ValueError("Cipher text is required.")
        key = request.form.get('inputKeyCipher', '')
        if not key:
            raise ValueError("Key is required.")
        key = int(key)
        if key <= 0:
            raise ValueError("Key must be a positive integer.")
        decrypted_text = railfence_cipher.rail_fence_decrypt(text, key)
        return render_template('railfence.html', decrypted_text=decrypted_text, key=key, error=None)
    except ValueError as ve:
        return render_template('railfence.html', error=str(ve), key=None)
    except Exception as e:
        return render_template('railfence.html', error=f"An error occurred: {str(e)}", key=None)

# ------------------- Playfair Cipher -------------------
@app.route('/playfair')
def playfair():
    return render_template('playfair.html')

@app.route('/playfair/encrypt', methods=['POST'])
def playfair_encrypt():
    try:
        text = request.form.get('inputPlainText', '').strip()
        if not text:
            raise ValueError("Plain text is required.")
        key = request.form.get('inputKeyPlain', '').strip()
        if not key:
            raise ValueError("Key is required.")
        matrix = playfair_cipher.create_playfair_matrix(key)
        encrypted_text = playfair_cipher.playfair_encrypt(text, matrix)
        return render_template('playfair.html', encrypted_text=encrypted_text, key=key, error=None)
    except ValueError as ve:
        return render_template('playfair.html', error=str(ve), key=None)
    except Exception as e:
        return render_template('playfair.html', error=f"An error occurred: {str(e)}", key=None)

@app.route('/playfair/decrypt', methods=['POST'])
def playfair_decrypt():
    try:
        text = request.form.get('inputCipherText', '').strip()
        if not text:
            raise ValueError("Cipher text is required.")
        key = request.form.get('inputKeyCipher', '').strip()
        if not key:
            raise ValueError("Key is required.")
        matrix = playfair_cipher.create_playfair_matrix(key)
        decrypted_text = playfair_cipher.playfair_decrypt(text, matrix)
        return render_template('playfair.html', decrypted_text=decrypted_text, key=key, error=None)
    except ValueError as ve:
        return render_template('playfair.html', error=str(ve), key=None)
    except Exception as e:
        return render_template('playfair.html', error=f"An error occurred: {str(e)}", key=None)

# ------------------- Transposition Cipher -------------------
@app.route('/transposition')
def transposition():
    return render_template('transposition.html')

@app.route('/transposition/encrypt', methods=['POST'])
def transposition_encrypt():
    try:
        text = request.form.get('inputPlainText', '').strip()
        if not text:
            raise ValueError("Plain text is required.")
        key = request.form.get('inputKeyPlain', '')
        if not key:
            raise ValueError("Key is required.")
        key = int(key)
        if key <= 0:
            raise ValueError("Key must be a positive integer.")
        encrypted_text = transposition_cipher.encrypt(text, key)
        return render_template('transposition.html', encrypted_text=encrypted_text, key=key, error=None)
    except ValueError as ve:
        return render_template('transposition.html', error=str(ve), key=None)
    except Exception as e:
        return render_template('transposition.html', error=f"An error occurred: {str(e)}", key=None)

@app.route('/transposition/decrypt', methods=['POST'])
def transposition_decrypt():
    try:
        text = request.form.get('inputCipherText', '').strip()
        if not text:
            raise ValueError("Cipher text is required.")
        key = request.form.get('inputKeyCipher', '')
        if not key:
            raise ValueError("Key is required.")
        key = int(key)
        if key <= 0:
            raise ValueError("Key must be a positive integer.")
        decrypted_text = transposition_cipher.decrypt(text, key)
        return render_template('transposition.html', decrypted_text=decrypted_text, key=key, error=None)
    except ValueError as ve:
        return render_template('transposition.html', error=str(ve), key=None)
    except Exception as e:
        return render_template('transposition.html', error=f"An error occurred: {str(e)}", key=None)

# ------------------- Run Flask App -------------------
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)