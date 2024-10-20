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
   {
       "questions": [
           {
               "question": "What is your greatest strength?",
               "responses": [
                   "I believe my greatest strength is my ability to learn quickly.",
                   "I am a team player who can effectively collaborate with others."
               ]
           },
           {
               "question": "Where do you see yourself in five years?",
               "responses": [
                   "In five years, I see myself growing within this company and taking on new challenges.",
                   "I hope to be in a position where I can lead projects and contribute significantly."
               ]
           }
        .....
        .....
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
