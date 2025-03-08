// user_name : Ng Chun Ping
// Student ID : CT0383802
// Module Code: ICS50
// Module user_name: property_typeDip2501_IT50_ICS
// Date : 15/1/25
// Desc : Question 2

#include <stdio.h>
char user_name[30];
int property_price = 0;
int property_type = 0;
float buyer_stamp_duty = 0;
int property_price_cat = 0;
//Declare this variable for switch case 

void get_user_name()
{
    printf("Enter your Name press Enter\n");
    fgets(user_name, sizeof(user_name), stdin);
    printf("Hello, %s\n", user_name);
}
//The same function in Question_1 to ask for username

void calculate_buyer_stamp_duty()
    {
        printf("Enter Property Price : \n");
        scanf("%d", &property_price);
        if (property_price <= 0)
        {
            property_price_cat = 1;
        }
        else if (property_price > 0)
        {
            property_price_cat = 2;
        }

        switch (property_price_cat)
        {
            case 1:
                printf("Invalid property price, input must be numeric and greater than 0\n");
                break;
            
            case 2:
                printf("Enter 1 for Residential Property, 2 for Non-Residential Property: \n");
                scanf("%d", &property_type);
                switch (property_type)
                {
                    case 1:
                        if (property_price < 180000)
                        {
                            buyer_stamp_duty = property_price * 0.01;
                        }
                        else if (property_price > 180000 && property_price < 600000)
                        {
                            buyer_stamp_duty = property_price * 0.02;
                        }
                        else if (property_price > 600000)
                        {
                            buyer_stamp_duty = property_price * 0.03;
                        }
                        break;
                    case 2:
                        if (property_price < 180000)
                        {
                            buyer_stamp_duty = property_price * 0.015;
                        }
                        else if (property_price > 180000 && property_price < 600000)
                        {
                            buyer_stamp_duty = property_price * 0.025;
                        }
                        else if (property_price > 600000)
                        {
                            buyer_stamp_duty = property_price * 0.035;
                        }
                        break;
                break;
                    default:
                        printf("Invalid property type, Please enter 1 or 2.\n");
                    //"default" will make sure the programe user only enter 1 or 2 as the property type input
                    break;
                }
        }
        
        
        //Switch Case is used to differentiate 2 property types  separately, 
        //case 1 is for Residential Property,
        //case 2 is for Non-Residential Property.
        

    }
    // There are 6 different conditions listed in this switch and if block

int main() 
{
    printf("Chun Ping Property Buyer's Stamp Duty Calculator\n");  
    printf("Done By : Chun Ping , SID : CT0383802\n");
    get_user_name();
    calculate_buyer_stamp_duty();
    printf("Total buyer_stamp_duty = $ %.2f \n", buyer_stamp_duty);
    return 0;
}