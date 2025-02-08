# Python बेस इमेज
FROM python:3.9

# वर्किंग डायरेक्टरी सेट करें
WORKDIR /app

# ज़रूरी फाइलें कॉपी करें
COPY requirements.txt .
COPY quiz_bot.py .

# Dependencies इंस्टॉल करें
RUN pip install --no-cache-dir -r requirements.txt

# बॉट को स्टार्ट करने के लिए कमांड
CMD ["python", "quiz_bot.py"]
