// Name : Ng Chun Ping
// Student ID : CT0383802
// Module Code: ICS50
// Module Name: PTDip2501_IT50_ICS
// Date : 15/1/25
// Desc : Question 3

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char user_name[30];
float salary_performance = 0;
char employee_id[30];
int  bonus = 0;
int found = 0;
char employee_details[100];
char name_in_file[50];
char id_in_file[50];
char salary_string[50];
float salary_float = 0;

void get_user_name()
{
    printf("Enter your Name press Enter\n");
    fgets(user_name, sizeof(user_name), stdin);
    printf("Hello, %s\n", user_name);
}

void calculate_employee_bonus()
{
  FILE *fptr;
  fptr = fopen("filename.txt", "r");
  if (fptr == NULL) 
  {
    printf("Error opening file.\n");
    return;
  }
  printf("Enter Sales Performance Percentage : \n");
  scanf("%f", &salary_performance);
  if (salary_performance > 0)
  {
    printf("Enter Employee ID press enter: \n");
    scanf("%s", employee_id);
    while (fgets(employee_details, 100, fptr) != NULL) 
    {
      // Read the ID, name, and salary from the line
      sscanf(employee_details, "%s %s %s", id_in_file, name_in_file, salary_string);
      // Check if the name in the file matches the input name
      if (strcmp(employee_id, id_in_file) == 0) 
      {
        printf("Found %s: ID = %s, Salary = %s\n", name_in_file, id_in_file, salary_string);
        salary_float = atof(salary_string);
        found = 1;
        break;  // Exit the loop once the name is found
      }
    }
    if (!found) 
    {
      printf("Employee ID not found in the file.\n");
    }
    else
    {
      if (salary_performance < 100)
      {
        bonus = salary_float * 1;
      } 
      else if (salary_performance >= 100 && salary_performance < 200)
      {
        bonus = salary_float * 2;
      }
      else if (salary_performance >= 200)
      {
        bonus = salary_float * 3;
      } 
      printf("bonus for %s = $ %d \n", name_in_file, bonus);
    }
  }
  else 
  {
    printf("Salary performanace must be numeric and greater than 0");
  }
  fclose(fptr);
}

int main() 
{
  printf("Chun Ping bonus Calculator\n");  
  printf("Done By : Chun Ping, SID CT0383802\n");
  get_user_name();
  calculate_employee_bonus();
  return 0;
}