def main():
    """
    ########################################
    Code Your Program here
    ########################################
    """
    number=0
    while True:
        try:
            number= int(input('Enter number:'))
            if 1 <= number <= 100: 
                break 
            else: 
                print('retry with appropriate number')
        except ValueError:
            print('Must enter number')
    print(number)

        
        
                

        

    ########################################
    # Do not delete the return statement
    ########################################
    return number


if __name__ == '__main__':
    main()
