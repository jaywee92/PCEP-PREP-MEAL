#!/usr/bin/env python3
"""
PCEP Question Bank Quiz Tool
Interaktives Quiz-Werkzeug zum Üben mit der Fragenbank
"""

import json
import random
import sys
from pathlib import Path

class PCEPQuizzer:
    def __init__(self, json_file):
        self.json_file = json_file
        self.questions = {}
        self.stats = {
            "total_attempted": 0,
            "correct": 0,
            "incorrect": 0,
            "by_module": {}
        }
        self.load_questions()
        
    def load_questions(self):
        """Load questions from JSON file"""
        try:
            with open(self.json_file, 'r', encoding='utf-8') as f:
                self.questions = json.load(f)
            print(f"✓ Loaded {sum(len(q) for q in self.questions.values())} questions")
        except FileNotFoundError:
            print(f"✗ Error: File not found: {self.json_file}")
            sys.exit(1)
            
    def get_quiz_questions(self, module=None, count=10, difficulty=None):
        """Get random questions for a quiz"""
        if module:
            questions_list = self.questions.get(module, [])
        else:
            questions_list = [q for qs in self.questions.values() for q in qs]
        
        if difficulty:
            questions_list = [q for q in questions_list if q.get('difficulty') == difficulty]
        
        return random.sample(questions_list, min(count, len(questions_list)))
    
    def run_quiz(self, module=None, count=10):
        """Run an interactive quiz"""
        questions = self.get_quiz_questions(module=module, count=count)
        
        print("\n" + "="*70)
        print("PCEP QUIZ".center(70))
        print("="*70)
        print(f"Module: {module or 'All Modules'}")
        print(f"Questions: {len(questions)}")
        print("="*70 + "\n")
        
        correct = 0
        
        for i, q in enumerate(questions, 1):
            print(f"\n[Question {i}/{len(questions)}]")
            print(f"Difficulty: {q.get('difficulty', 'unknown').upper()}")
            print(f"\n{q['prompt']}")
            
            if q['code']:
                print(f"\nCode:")
                for line in q['code'].split('\n'):
                    print(f"  {line}")
            
            print(f"\nOptions:")
            for idx, opt in enumerate(q['options']):
                print(f"  [{idx}] {opt}")
            
            # Get user answer
            while True:
                try:
                    user_answer = int(input("\nYour answer (0-3): ").strip())
                    if 0 <= user_answer <= 3:
                        break
                    print("Invalid input. Please enter 0-3.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
            
            # Check answer
            if user_answer == q['answer']:
                print("✓ CORRECT!")
                correct += 1
            else:
                print(f"✗ INCORRECT. Correct answer: {q['options'][q['answer']]}")
            
            print(f"\nHint: {q['hint']}")
            print(f"Explanation: {q['explanation']}")
            
            # Show progress
            print(f"\nProgress: {correct}/{i} correct ({correct*100//i}%)")
        
        # Final stats
        percentage = (correct * 100) // len(questions)
        print("\n" + "="*70)
        print("QUIZ COMPLETE".center(70))
        print("="*70)
        print(f"Total: {len(questions)} questions")
        print(f"Correct: {correct}")
        print(f"Incorrect: {len(questions) - correct}")
        print(f"Percentage: {percentage}%")
        print("="*70)
        
        return percentage
    
    def show_statistics(self):
        """Show statistics about the question bank"""
        print("\n" + "="*70)
        print("QUESTION BANK STATISTICS".center(70))
        print("="*70)
        
        for module, questions in self.questions.items():
            print(f"\n{module.upper()}:")
            print(f"  Total: {len(questions)}")
            
            difficulties = {}
            for q in questions:
                diff = q.get('difficulty', 'unknown')
                difficulties[diff] = difficulties.get(diff, 0) + 1
            
            for diff, count in sorted(difficulties.items()):
                pct = count * 100 / len(questions)
                print(f"    {diff:10} {count:3} ({pct:5.1f}%)")
        
        total = sum(len(q) for q in self.questions.values())
        print(f"\nTOTAL: {total} questions")
        print("="*70)
    
    def search_questions(self, keyword):
        """Search for questions containing keyword"""
        results = []
        for module, questions in self.questions.items():
            for q in questions:
                if keyword.lower() in q['prompt'].lower() or \
                   keyword.lower() in q['code'].lower() or \
                   keyword.lower() in q['explanation'].lower():
                    results.append((module, q))
        
        print(f"\nFound {len(results)} questions matching '{keyword}':")
        for module, q in results[:5]:  # Show first 5
            print(f"\n{q['id']} - {module}")
            print(f"  {q['prompt']}")
            print(f"  Answer: {q['options'][q['answer']]}")

def main():
    """Main function"""
    json_file = Path(__file__).parent / "questions-bank-1000.json"
    
    if not json_file.exists():
        print(f"Error: {json_file} not found")
        sys.exit(1)
    
    quizzer = PCEPQuizzer(json_file)
    
    # Interactive menu
    while True:
        print("\n" + "="*70)
        print("PCEP QUESTION BANK QUIZ TOOL".center(70))
        print("="*70)
        print("1. Run full quiz (10 random questions)")
        print("2. Run module-specific quiz")
        print("3. Show statistics")
        print("4. Search questions")
        print("5. Exit")
        print("="*70)
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == "1":
            quizzer.run_quiz()
        elif choice == "2":
            print("\nAvailable modules:")
            for i, module in enumerate(quizzer.questions.keys(), 1):
                print(f"{i}. {module}")
            
            mod_choice = input("Select module (1-4): ").strip()
            modules = list(quizzer.questions.keys())
            if mod_choice.isdigit() and 1 <= int(mod_choice) <= len(modules):
                module = modules[int(mod_choice) - 1]
                quizzer.run_quiz(module=module)
        elif choice == "3":
            quizzer.show_statistics()
        elif choice == "4":
            keyword = input("Enter search keyword: ").strip()
            quizzer.search_questions(keyword)
        elif choice == "5":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
