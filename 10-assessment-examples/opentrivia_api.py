import requests
import html

url = 'https://opentdb.com/api.php?amount=5&type=multiple'

response = requests.get(url)
data = response.json()

question_list = data['results']

for item in question_list:
    question = html.unescape(item['question'])
    print("Q:", question)
    print("CA:", item['correct_answer'])
    print("IA:", item['incorrect_answers'])
