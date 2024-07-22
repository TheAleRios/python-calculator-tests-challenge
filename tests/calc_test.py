import subprocess
import pytest

dockerCommand = "docker run --rm public.ecr.aws/l4q9w4c5/loanpro-calculator-cli"

def run_calculator(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True, encoding='utf-8')
    return result.stdout.strip()

@pytest.mark.parametrize("operation, firstNumber, secondNumber, expected", [
                           ("add",8,5,"13"),
                           ("add",5,8,"13"),
                           ("add",-8,5,"-3"),
                           ("add",-8,-5,"-13"),
                           ("add",8,-5,"3"),
                           ("add",0,0,"0"),
                           ("add",1.000000001,1.000000001,"2"),
                           ("add",1.0000001,1.0000001,"2.0000002"),
                           ("add","Infinity","Infinity","∞"),
                           ("add","-Infinity","-Infinity","-∞"),
                           ("add","-Infinity","Infinity","NaN"),
                           ("add","Infinity","-Infinity","NaN"),
                           ("subtract",8,5,"3"),
                           ("subtract",5,8,"-3"),
                           ("subtract",8,-5,"13"),
                           ("subtract",-8,5,"-13"),
                           ("subtract","Infinity","Infinity","NaN"),
                           ("subtract","Infinity","1","∞"),
                           ("subtract","1","Infinity","-∞"),
                           ("subtract","Infinity","-Infinity","∞"),
                           ("subtract","-Infinity","Infinity","-∞"),
                           ("subtract","-Infinity","-Infinity","NaN"),
                           ("multiply",8,5,"40"),
                           ("multiply",5,8,"40"),
                           ("multiply",8,-5,"-40"),
                           ("multiply",-8,5,"-40"),
                           ("multiply",-8,-5,"40"),
                           ("multiply",0,0,"0"),
                           ("multiply",1e5,1e-2,"1000"),
                           ("multiply","Infinity","Infinity","∞"),
                           ("multiply","-Infinity","-Infinity","∞"),
                           ("multiply","Infinity","-Infinity","-∞"),
                           ("multiply","-Infinity","Infinity","-∞"),
                           ("multiply","1e308","1e308","∞"),
                           ("multiply","1e308","-1e308","-∞"),
                           ("divide",8,2,"4"),
                           ("divide",8,-2,"-4"),
                           ("divide",-8,2,"-4"),
                           ("divide",-8,-2,"4"),
                           ("divide",2,8,"0.25"),
                           ("divide","Infinity","Infinity","NaN"),
                           ("divide","-Infinity","-Infinity","NaN"),
                           ("divide","Infinity","Infinity","NaN"),
                           ("divide","Infinity","Infinity","NaN"),                          
                              
])

def test_operations(operation, firstNumber, secondNumber, expected):
    result= run_calculator(f"{dockerCommand} {operation} {firstNumber} {secondNumber}").split(": ")[-1]

    assert result == expected, f"App expected '{expected}' but received '{result}'"





    

@pytest.mark.parametrize("operation, firstInput, secondInput, error_message", [
                           ("add","1","b","Invalid argument. Must be a numeric value."),
                           ("subtract","1","b","Invalid argument. Must be a numeric value."),
                           ("divide","1","b","Invalid argument. Must be a numeric value."),
                           ("multiply","1","b","Invalid argument. Must be a numeric value."),
                           ("add","a","1","Invalid argument. Must be a numeric value."),
                           ("subtract","a","1","Invalid argument. Must be a numeric value."),
                           ("divide","a","1","Invalid argument. Must be a numeric value."),
                           ("multiply","a","1","Invalid argument. Must be a numeric value."),
                           ("divide",8,0,"Error: Cannot divide by zero"),
                           ("add","","","Usage: cli-calculator operation operand1 operand2\nSupported operations: add, subtract, multiply, divide"),
                           ("subtract","","","Usage: cli-calculator operation operand1 operand2\nSupported operations: add, subtract, multiply, divide"),
                           ("multiply","","","Usage: cli-calculator operation operand1 operand2\nSupported operations: add, subtract, multiply, divide"),
                           ("divide","","","Usage: cli-calculator operation operand1 operand2\nSupported operations: add, subtract, multiply, divide"),
                           ("add","1","","Usage: cli-calculator operation operand1 operand2\nSupported operations: add, subtract, multiply, divide"),  
                           ("subtract","1","","Usage: cli-calculator operation operand1 operand2\nSupported operations: add, subtract, multiply, divide"),  
                           ("multiply","1","","Usage: cli-calculator operation operand1 operand2\nSupported operations: add, subtract, multiply, divide"),   
                           ("divide","1","","Usage: cli-calculator operation operand1 operand2\nSupported operations: add, subtract, multiply, divide")                                                   
])

def test_errors(operation,firstInput, secondInput, error_message):
    result = run_calculator(f"{dockerCommand} {operation} {firstInput} {secondInput}")
    assert result == error_message, f"App expected '{error_message}' but received '{result}'"






@pytest.mark.parametrize("operation, firstInput, secondInput, thirdInput, error_message", [
     ("add","2","2","2","Error message"),
     ("subtract","6","2","2","Error message"),
     ("multiply","2","2","2","Error message"),
     ("divide","8","2","2","Error message"),

        ])

def test_three_inputs(operation,firstInput, secondInput, thirdInput, error_message):
    result = run_calculator(f"{dockerCommand} {operation} {firstInput} {secondInput} {thirdInput}")
    assert result == error_message, f"App expected '{error_message}' but received '{result}'"