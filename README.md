# Interview-Response-Chatbot

# NLP Interview Chatbot

## Overview
This is an NLP-based chatbot designed to help users practice interview questions and receive simulated responses. The chatbot utilizes text preprocessing techniques and Jaccard similarity to match user questions with predefined interview questions.

# NLP Interview Chatbot Documentation

## Model Architecture
The NLP Interview Chatbot is designed to simulate interview scenarios by providing responses to user questions. Below is an overview of its architecture:

### Components:
1. **Data Loading**: 
   - The chatbot loads interview data from a JSON file (`interview_data.json`).
   - The data contains a structured list of questions and corresponding responses.

2. **NLP Preprocessing**:
   - **Stop Words**: A predefined list of common stop words is used to filter out non-informative words from the user's input.
   - **Text Processing**:
     - Converts input text to lowercase.
     - Removes punctuation.
     - Tokenizes the text into individual words.

3. **Similarity Calculation**:
   - The chatbot uses the **Jaccard similarity** index to measure the similarity between the processed user input and predefined questions.
   - It calculates the intersection and union of token sets to derive a similarity score.

4. **Response Generation**:
   - Based on the highest similarity score, the chatbot selects an appropriate response from the matched category or provides a default response if no match is found.

## Training Process
The training of the chatbot involves no traditional machine learning but instead focuses on a rule-based approach using the following steps:

1. **Dataset Preparation**:
   - The dataset is in JSON format, structured to contain an array of questions, each associated with a list of possible responses.
   - An example of the dataset format is shown below:

   ```json
  ## Dataset Preparation
The dataset used for the chatbot is stored in a JSON file (`interview_data.json`) and is structured to include an array of questions, each associated with a list of possible responses. Here’s an example of the dataset format:

```json
{
  "questions": [
    {
      "question": "Tell me about yourself.",
      "responses": [
        "I am a recent graduate with a degree in Computer Science. During my studies, I developed a passion for problem-solving and building software solutions.",
        "I have a background in mechanical engineering and have worked on various team projects that have helped me develop strong leadership and technical skills.",
        "I am a self-motivated professional with experience in marketing. I enjoy helping brands grow and improve their presence in competitive markets.",
        "I have always been curious about technology, and my work experience in IT has helped me hone my skills in networking and cloud technologies.",
        "I recently graduated with a B.Tech in Electronics, and I’m eager to start applying my skills in a challenging environment."
      ]
    },
    {
      "question": "What are your strengths?",
      "responses": [
        "I have strong problem-solving skills, which help me approach challenges with a creative mindset.",
        "I am an excellent communicator, which allows me to collaborate well with different teams and stakeholders.",
        "I am adaptable and quick to learn, making it easy for me to pick up new skills and software in a short amount of time.",
        "I am detail-oriented, ensuring that I always deliver quality work while maintaining high productivity.",
        "I have a strong work ethic, and I always strive to exceed expectations in my responsibilities."
      ]
    },
    {
      "question": "What are your weaknesses?",
      "responses": [
        "I sometimes take on too much work because I find it hard to say no, but I’m learning to manage my workload more effectively.",
        "I used to struggle with delegating tasks, but I’ve been working on building trust with my team and letting them take ownership of tasks.",
        "I can be overly detail-oriented, which sometimes slows down my work, but I’m learning to balance quality and efficiency.",
        "I tend to be a bit quiet in group settings, but I’ve been actively working on improving my public speaking skills.",
        "I used to struggle with time management, but I now use tools like Trello and Asana to keep myself organized and on track."
      ]
    }
  ]
}

2. ## Preprocessing Techniques:

The preprocessing methods include converting text to lowercase, punctuation removal, and tokenization.
Stop words are removed from the input to focus on meaningful terms.

3. ## Response Logic:

The chatbot matches user queries against the dataset and provides a relevant response based on the calculated similarity.
How to Run the Chatbot
To run the NLP Interview Chatbot, follow these steps:

4. ## Create the Dataset:

Ensure the interview_data.json file is present in the project directory, containing the structured interview questions and responses.

5. ## Output and Interaction:

Type your interview questions in the terminal.
Type quit to exit the chatbot.
## Dependencies
Python 3.x
No external libraries required (standard Python libraries used).
## Contribution
Contributions are welcome! Feel free to fork the repository and submit pull requests for enhancements or bug fixes.

## Acknowledgments
Thank you to all contributors and resources that made this project possible.
