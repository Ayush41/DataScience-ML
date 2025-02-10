# import Machine_Learning.autotyper as at
import pyautogui as pg
import Machine_Learning.autocode as autocode
import time

time.sleep(10)

autocode.type(
    """
#include <stdio.h>
int main() {
    int num1, num2, sum;
    // Ask the user for the first number
    printf("Enter the first number: ");
    scanf("%d", &num1);
    // Ask the user for the second number
    printf("Enter the second number: ");
    scanf("%d", &num2);
    // Calculate the sum
    sum = num1 + num2;
    // Print the result
    printf("The sum of %d and %d is: %d\n", num1, num2, sum);
    return 0;
}
"""
)



# pg.typewrite("#include <stdio.h>\n")
# pg.typewrite("int main() {\n")
# pg.typewrite("    int num1, num2, sum;\n")
# pg.typewrite("    // Ask the user for the first number\n")
# pg.typewrite("    printf(\"Enter the first number: \");\n")
# pg.typewrite("    scanf(\"%d\", &num1);\n")
# pg.typewrite("    // Ask the user for the second number\n")
# pg.typewrite("    printf(\"Enter the second number: \");\n")
# pg.typewrite("    scanf(\"%d\", &num2);\n")
# pg.typewrite("    // Calculate the sum\n")
# pg.typewrite("    sum = num1 + num2;\n")
# pg.typewrite("    // Print the result\n")
# pg.typewrite("    printf(\"The sum of %d and %d is: %d\\n\", num1, num2, sum);\n")
# pg.typewrite("    return 0;\n")
# pg.typewrite("}")

# #include <stdio.h>
# int main() {
#         int num1, num2, sum;
#             // Ask the user for the first number
#                 printf("Enter the first number: ");
#                     scanf("%d", &num1);
#                         // Ask the user for the second number
#                             printf("Enter the second number: ");
#                                 scanf("%d", &num2);
#                                     // Calculate the sum
#                                         sum = num1 + num2;
#                                             // Print the result
#                                                 printf("The sum of %d and %d is: %d\n", num1, num2, sum);
#                                                     return 0;
#                                                     }
# }


# pg.write("#include <stdio.h>
# int main() {
#     int num1, num2, sum;

#     // Ask the user for the first number
#     printf("Enter the first number: ");
#     scanf("%d", &num1);

#     // Ask the user for the second number
#     printf("Enter the second number: ");
#     scanf("%d", &num2);

#     // Calculate the sum
#     sum = num1 + num2;

#     // Print the result
#     printf("The sum of %d and %d is: %d\n", num1, num2, sum);

#     return 0;
# }")