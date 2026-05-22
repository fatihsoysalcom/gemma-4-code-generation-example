import google.generativeai as genai
import os

# Configure the API key. It's recommended to use environment variables.
# Replace 'YOUR_GOOGLE_API_KEY' with your actual API key or set the environment variable.
API_KEY = os.environ.get("GOOGLE_API_KEY", "YOUR_GOOGLE_API_KEY")

if API_KEY == "YOUR_GOOGLE_API_KEY":
    print("Warning: GOOGLE_API_KEY environment variable not set. Using placeholder.")
    print("Please set the GOOGLE_API_KEY environment variable or replace 'YOUR_GOOGLE_API_KEY' in the script.")

genai.configure(api_key=API_KEY)

# Initialize the Generative Model
# 'gemini-1.5-flash-latest' is a good choice for speed and cost-effectiveness,
# aligning with Gemma's goal of accessibility.
model = genai.GenerativeModel('gemini-1.5-flash-latest')

# Define a prompt for code generation
# This prompt asks the model to generate a Python function for calculating factorial.
prompt = """
Generate a Python function that calculates the factorial of a non-negative integer.
Include a docstring explaining the function and its parameters.
"""

print("Generating Python code for factorial function...")

try:
    # Generate content using the model
    response = model.generate_content(prompt)

    # Print the generated code
    print("\n--- Generated Code ---")
    print(response.text)
    print("----------------------")

    # Example of how to use the generated code (if it's valid Python)
    # This part is illustrative and assumes the generated code is correct.
    # In a real scenario, you might want to dynamically execute or validate it.
    print("\nAttempting to execute the generated code (for demonstration purposes)...")
    try:
        # Extract the function definition from the generated text
        # This is a simple approach and might need refinement for complex outputs.
        code_lines = response.text.split('\n')
        function_code = "\n".join(code_lines)

        # Execute the code in a local scope
        local_scope = {}
        exec(function_code, globals(), local_scope)

        # Check if the function was defined
        if 'factorial' in local_scope and callable(local_scope['factorial']):
            # Test the function
            number_to_test = 5
            result = local_scope['factorial'](number_to_test)
            print(f"Factorial of {number_to_test} is: {result}")
        else:
            print("Could not find or execute the 'factorial' function from the generated code.")

    except Exception as e:
        print(f"Error executing generated code: {e}")

except Exception as e:
    print(f"An error occurred during API call: {e}")
    print("Please ensure your API key is valid and you have network connectivity.")
