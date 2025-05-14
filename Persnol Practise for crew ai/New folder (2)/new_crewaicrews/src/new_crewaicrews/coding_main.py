#!/usr/bin/env python
import sys
import warnings
from datetime import datetime
from new_crewaicrews.coding_crew import CodingCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the coding crew.
    """
    inputs = {
        'task_description': 'implement a binary search algorithm in Python and their output with example',
        'code_review_focus': 'performance and readability',
        'test_requirements': 'include edge cases and performance tests'
    }
    
    try:
        CodingCrew().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the coding crew: {e}")

def train():
    """
    Train the coding crew for a given number of iterations.
    """
    inputs = {
        'task_description': 'implement a binary search algorithm in Python and their output with example',
        'code_review_focus': 'performance and readability',
        'test_requirements': 'include edge cases and performance tests'
    }
    try:
        CodingCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while training the coding crew: {e}")

def replay():
    """
    Replay the coding crew execution from a specific task.
    """
    try:
        CodingCrew().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"An error occurred while replaying the coding crew: {e}")

def test():
    """
    Test the coding crew execution and returns the results.
    """
    inputs = {
        'task_description': 'implement a binary search algorithm in Python and their output with example',
        'code_review_focus': 'performance and readability',
        'test_requirements': 'include edge cases and performance tests'
    }
    
    try:
        CodingCrew().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while testing the coding crew: {e}")