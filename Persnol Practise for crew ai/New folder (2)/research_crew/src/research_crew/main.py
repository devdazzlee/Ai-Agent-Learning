#!/usr/bin/env python
import sys
import warnings
import time
from datetime import datetime

from research_crew.crew import ResearchCrew
import os
warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

os.environ["GEMINI_API_KEY"] = "AIzaSyCulHojov19SEEIY-VXw4TXcyQhboKhZEQ"
os.environ["MODEL"] = "gemini/gemini-1.5-flash"

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'AI LLMs',
        'current_year': str(datetime.now().year)
    }
    
    try:
        # Add a delay before making API calls to prevent rate limiting
        time.sleep(1)  # 1 second delay
        ResearchCrew().crew().kickoff(inputs=inputs)
    except Exception as e:
        if "RateLimitError" in str(e):
            print("Rate limit exceeded. Waiting 60 seconds before retrying...")
            time.sleep(60)  # Wait 60 seconds before retrying
            try:
                ResearchCrew().crew().kickoff(inputs=inputs)
            except Exception as retry_e:
                raise Exception(f"An error occurred while running the crew after retry: {retry_e}")
        else:
            raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs",
        'current_year': str(datetime.now().year)
    }
    try:
        ResearchCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        ResearchCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year)
    }
    
    try:
        ResearchCrew().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
