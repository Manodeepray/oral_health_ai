import re

# Your input string
input_string = ("answer :   what is the grade and stage from the follwoing:1. The grade is 1. 2. The stage is 3. "
                "Helpful_Answer: 1. The grade is 1. 2. The stage is 3. Helpful_Answer: 1. The grade is 1. 2. "
                "The stage is 3. Helpful_Answer: 1. The grade is 1. 2. The stage is 3. Helpful_Answer: 1. "
                "The grade is 1. 2. The stage is 3. Helpful_Answer: 1. The grade is 1. 2. The stage is 3. "
                "Helpful_Answer: 1. The grade is 1. 2. The stage is 3. Helpful_Answer: 1. The grade is 1. 2. "
                "The stage is 3")


def extract_grade(input_string):
    # Regular expression to match the first occurrence of "The grade is <number>" and "The stage is <number>"
    grade_pattern = re.compile(r" Grade (\d+)")

    # Find the first match in the string
    grade_match = grade_pattern.search(input_string)

    # Extract the matched values if found
    if grade_match :
        grade = int(grade_match.group(1))

        print(f"The grade is: {grade}")
        
        return grade 
    else:
        
        print("Grade not found in the input string")
        return None
     
def extract_stage(input_string):
    # Regular expression to match the first occurrence of "The grade is <number>" and "The stage is <number>"
    stage_pattern = re.compile(r" Stage (\d+)")

    # Find the first match in the string
    stage_match = stage_pattern.search(input_string)

    # Extract the matched values if found
    if stage_match:
        stage = int(stage_match.group(1))

        print( f"The stage is: {stage}")
        if stage == 4:
            stage = 3
        return  stage
    else:
        
        print(" stage not found in the input string")
        return None