# Blooket Creator
Speed up creating Blooket question sets using AI.
## Features
- Generate distactors for multiple-choice questions using AI
- Easily create Blooket question sets with minimal input
- Supports HackclubAPI and OpenAI API for AI functionalities

## Setup
1. Download and unzip the repository.
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the root directory and add one of the following API keys:
   ```
   HACKCLUB_API_KEY=your-hackclub-api-key-here
   OPENAI_API_KEY=your-openai-api-key-here
   ```
4. Fill in questions and answers in `questions.txt` following the format:
   ```
   Question 1?
   Correct Answer 1
   Question 2?
   Correct Answer 2
   ```
5. Run the application:
   ```bash
   python main.py
   ```
6. Upload the generated `output.csv` to Blooket using the spreadsheet import feature.