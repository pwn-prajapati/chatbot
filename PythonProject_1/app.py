from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

def load_data():
    df = pd.read_csv("chatbot_data.csv")  # Updated to use only chatbot data
    return df

def generate_topic_chart(df):
    topic_counts = df['Topic'].value_counts()
    plt.figure(figsize=(6, 4))
    topic_counts.plot(kind='bar', color='skyblue')
    plt.xlabel("Topics")
    plt.ylabel("Frequency")
    plt.title("Chatbot Topic Distribution")
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    return base64.b64encode(img.read()).decode('utf8')

@app.route('/')
def dashboard():
    df = load_data()
    topic_chart = generate_topic_chart(df)
    analytics_data = {
        "total_queries": len(df),
        "average_rating": df['Rating'].mean(),
        "common_topics": df['Topic'].value_counts().items()
    }
    return render_template("dashboard.html", analytics_data=analytics_data, topic_chart=topic_chart)

if __name__ == "__main__":
    app.run(debug=True)
