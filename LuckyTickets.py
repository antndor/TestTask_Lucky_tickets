def lucky_tickets():

    half_of_number_of_digits = 3
    number_of_tickets = 0
    sum_of_all_digits = 0
    number_of_lucky_tickets = 0

    with open('input.txt', 'r') as file:

        for ticket in file:
            
            ticket = ticket.strip()
            number_of_tickets += 1
            sum_first_three_digits = 0
            sum_last_three_digits = 0

            if len(ticket) != half_of_number_of_digits + half_of_number_of_digits:
                raise Exception('The ticket number must consist of six digits')
                
            for j in range(half_of_number_of_digits):
                try:
                    sum_first_three_digits += int(ticket[j])
                    sum_last_three_digits += int(ticket[j + half_of_number_of_digits])

                except ValueError:
                    raise Exception('The ticket number must consist only of digits')

            sum_of_all_digits += sum_first_three_digits + sum_last_three_digits

            if sum_first_three_digits == sum_last_three_digits:
                number_of_lucky_tickets += 1

    mean_of_all_digits = sum_of_all_digits / number_of_tickets / half_of_number_of_digits / 2

    with open('output.txt', 'w') as file:
        file.write(str(number_of_lucky_tickets) + '\n')
        file.write(str('{:.2f}'.format(mean_of_all_digits)))
