from flask import Flask, render_template, request, Response, redirect
import ast

app = Flask(__name__)

history = []


# ==========================================
# Python Code Generator
# ==========================================

def generate_code(question):

    question = question.lower()

    if "even" in question and "odd" in question:
        return '''number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")'''

    elif "sum" in question and ("1 to 20" in question or "1 and 20" in question):
        return '''total = 0

for number in range(1, 21):
    total += number

print("Sum =", total)'''

    elif "hello" in question:
        return '''print("Hello, World!")'''

    elif "factorial" in question:
        return '''number = int(input("Enter a number: "))

factorial = 1

for i in range(1, number + 1):
    factorial *= i

print("Factorial =", factorial)'''

    elif "prime" in question:
        return '''number = int(input("Enter a number: "))

if number < 2:
    print("Not Prime")
else:
    is_prime = True

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime")
    else:
        print("Not Prime")'''

    elif "palindrome" in question:
        return '''text = input("Enter a string: ")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")'''

    elif "reverse" in question and "string" in question:
        return '''text = input("Enter a string: ")

reversed_text = text[::-1]

print("Reversed =", reversed_text)'''

    elif "fibonacci" in question:
        return '''n = int(input("Enter number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b'''

    elif "sum of digits" in question:
        return '''number = int(input("Enter a number: "))

total = 0

while number > 0:
    digit = number % 10
    total += digit
    number //= 10

print("Sum of digits =", total)'''

    elif "reverse number" in question:
        return '''number = int(input("Enter a number: "))

reverse = 0

while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number //= 10

print("Reversed number =", reverse)'''

    elif "vowel" in question:
        return '''text = input("Enter a string: ")

count = 0

for character in text:
    if character.lower() in "aeiou":
        count += 1

print("Number of vowels =", count)'''

    elif "leap year" in question:
        return '''year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")'''

    elif "multiplication table" in question:
        return '''number = int(input("Enter a number: "))

for i in range(1, 11):
    print(number, "x", i, "=", number * i)'''

    else:
        return '''# Example Python program

number = int(input("Enter a number: "))

print("You entered:", number)'''


# ==========================================
# Java Code Generator
# ==========================================

def generate_java_code(question):

    question = question.lower()

    if "even" in question and "odd" in question:
        return '''import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter a number: ");
        int number = sc.nextInt();

        if (number % 2 == 0) {
            System.out.println("Even number");
        } else {
            System.out.println("Odd number");
        }

        sc.close();
    }
}'''

    elif "factorial" in question:
        return '''import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter a number: ");
        int number = sc.nextInt();

        long factorial = 1;

        for (int i = 1; i <= number; i++) {
            factorial *= i;
        }

        System.out.println("Factorial = " + factorial);

        sc.close();
    }
}'''

    elif "prime" in question:
        return '''import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter a number: ");
        int number = sc.nextInt();

        boolean prime = true;

        if (number < 2) {
            prime = false;
        }

        for (int i = 2; i <= Math.sqrt(number); i++) {

            if (number % i == 0) {
                prime = false;
                break;
            }
        }

        if (prime) {
            System.out.println("Prime");
        } else {
            System.out.println("Not Prime");
        }

        sc.close();
    }
}'''

    elif "palindrome" in question:
        return '''import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter a string: ");
        String text = sc.nextLine();

        String reverse = new StringBuilder(text).reverse().toString();

        if (text.equals(reverse)) {
            System.out.println("Palindrome");
        } else {
            System.out.println("Not Palindrome");
        }

        sc.close();
    }
}'''

    elif "hello" in question:
        return '''public class Main {

    public static void main(String[] args) {

        System.out.println("Hello, World!");
    }
}'''

    else:
        return '''import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter a number: ");
        int number = sc.nextInt();

        System.out.println("You entered: " + number);

        sc.close();
    }
}'''


# ==========================================
# C++ Code Generator
# ==========================================

def generate_cpp_code(question):

    question = question.lower()

    if "even" in question and "odd" in question:
        return '''#include <iostream>
using namespace std;

int main() {

    int number;

    cout << "Enter a number: ";
    cin >> number;

    if (number % 2 == 0) {
        cout << "Even number";
    } else {
        cout << "Odd number";
    }

    return 0;
}'''

    elif "factorial" in question:
        return '''#include <iostream>
using namespace std;

int main() {

    int number;
    long long factorial = 1;

    cout << "Enter a number: ";
    cin >> number;

    for (int i = 1; i <= number; i++) {
        factorial *= i;
    }

    cout << "Factorial = " << factorial;

    return 0;
}'''

    elif "prime" in question:
        return '''#include <iostream>
using namespace std;

int main() {

    int number;
    bool prime = true;

    cout << "Enter a number: ";
    cin >> number;

    if (number < 2) {
        prime = false;
    }

    for (int i = 2; i * i <= number; i++) {

        if (number % i == 0) {
            prime = false;
            break;
        }
    }

    if (prime) {
        cout << "Prime";
    } else {
        cout << "Not Prime";
    }

    return 0;
}'''

    elif "hello" in question:
        return '''#include <iostream>
using namespace std;

int main() {

    cout << "Hello, World!";

    return 0;
}'''

    else:
        return '''#include <iostream>
using namespace std;

int main() {

    int number;

    cout << "Enter a number: ";
    cin >> number;

    cout << "You entered: " << number;

    return 0;
}'''


# ==========================================
# Generate Code
# ==========================================

def ask_ai(question, language):

    if language == "python":
        return generate_code(question)

    elif language == "java":
        return generate_java_code(question)

    elif language == "cpp":
        return generate_cpp_code(question)

    return generate_code(question)


# ==========================================
# Explain Code
# ==========================================

def explain_code(code):

    if not code:
        return ""

    explanation = []

    if "import " in code or "#include" in code:
        explanation.append("• The program imports the required libraries.")

    if "def " in code:
        explanation.append("• A function is defined to organize the program.")

    if "input(" in code or "cin >>" in code or "Scanner" in code:
        explanation.append("• The program receives input from the user.")

    if "if " in code:
        explanation.append("• An if statement is used to make a decision.")

    if "else" in code:
        explanation.append("• The else block handles the alternative condition.")

    if "for " in code:
        explanation.append("• A for loop is used to repeat instructions.")

    if "while " in code:
        explanation.append("• A while loop repeats instructions while a condition is true.")

    if "%" in code:
        explanation.append("• The modulus operator (%) is used to find a remainder.")

    if "print(" in code or "System.out" in code or "cout" in code:
        explanation.append("• The program displays the result.")

    if "return" in code:
        explanation.append("• The return statement sends a value back from a function.")

    if not explanation:
        explanation.append("• This program performs the requested programming task.")

    return "\n".join(explanation)


# ==========================================
# Debug Python Code
# ==========================================

def debug_code(code):

    if not code:
        return "⚠️ Please enter Python code to debug."

    try:

        ast.parse(code)

        return "✅ No Python syntax errors found."

    except SyntaxError as error:

        line_number = error.lineno
        message = error.msg

        return f"❌ Syntax Error on line {line_number}: {message}"


# ==========================================
# Generate Test Cases
# ==========================================

def generate_test_cases(question):

    question = question.lower()

    if "even" in question and "odd" in question:

        return """Test Case 1:
Input: 10
Expected Output: Even number

Test Case 2:
Input: 7
Expected Output: Odd number

Test Case 3:
Input: 0
Expected Output: Even number"""

    elif "factorial" in question:

        return """Test Case 1:
Input: 5
Expected Output: 120

Test Case 2:
Input: 0
Expected Output: 1

Test Case 3:
Input: 3
Expected Output: 6"""

    elif "palindrome" in question:

        return """Test Case 1:
Input: madam
Expected Output: Palindrome

Test Case 2:
Input: hello
Expected Output: Not Palindrome

Test Case 3:
Input: level
Expected Output: Palindrome"""

    elif "prime" in question:

        return """Test Case 1:
Input: 7
Expected Output: Prime

Test Case 2:
Input: 10
Expected Output: Not Prime

Test Case 3:
Input: 2
Expected Output: Prime"""

    else:

        return """Test Case 1:
Input: Normal valid input
Expected Output: Correct result

Test Case 2:
Input: Boundary value
Expected Output: Correct result

Test Case 3:
Input: Invalid input
Expected Output: Appropriate error message"""


# ==========================================
# Download Code
# ==========================================

@app.route("/download", methods=["POST"])
def download_code():

    code = request.form.get("code", "")
    language = request.form.get("language", "python")

    if language == "python":
        filename = "generated_code.py"

    elif language == "java":
        filename = "Main.java"

    elif language == "cpp":
        filename = "main.cpp"

    else:
        filename = "generated_code.txt"

    return Response(
        code,
        mimetype="text/plain",
        headers={
            "Content-Disposition": f"attachment; filename={filename}"
        }
    )


# ==========================================
# Clear History
# ==========================================

@app.route("/clear-history", methods=["POST"])
def clear_history():

    history.clear()

    return redirect("/")


# ==========================================
# Home
# ==========================================

@app.route("/", methods=["GET", "POST"])
def home():

    question = ""
    language = "python"

    answer = ""
    explanation = ""

    code_explanation = ""
    debug_result = ""
    test_cases = ""

    if request.method == "POST":

        question = request.form.get("question", "").strip()

        language = request.form.get(
            "language",
            "python"
        )

        # Generate Code
        if question:

            answer = ask_ai(
                question,
                language
            )

            explanation = explain_code(
                answer
            )

            history.append(question)

            if len(history) > 5:
                history.pop(0)

        else:

            answer = "⚠️ Please enter a programming question."

        # Explain Code
        code = request.form.get(
            "code_to_explain",
            ""
        ).strip()

        if code:

            code_explanation = explain_code(
                code
            )

        # Debug Code
        debug_code_input = request.form.get(
            "code_to_debug",
            ""
        ).strip()

        if debug_code_input:

            debug_result = debug_code(
                debug_code_input
            )

        # Test Cases
        test_question = request.form.get(
            "test_question",
            ""
        ).strip()

        if test_question:

            test_cases = generate_test_cases(
                test_question
            )

    return render_template(
        "index.html",
        question=question,
        language=language,
        answer=answer,
        explanation=explanation,
        code_explanation=code_explanation,
        debug_result=debug_result,
        test_cases=test_cases,
        history=history
    )


# ==========================================
# Run Application
# ==========================================

if __name__ == "__main__":

    app.run(
        debug=True
    )