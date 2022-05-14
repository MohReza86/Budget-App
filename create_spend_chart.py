''' @uthor: Mohammadreza Baghery'''

from budget import Budget

def create_spend_chart(categories):
    ''' creates a bar chart displaying 
the percentage spent in each category.

    Argument: a list of budget category objects
    Return: a chart of the percentage spent in each category
    '''

    # Init variables
    cat_final = []
    total_withdraw = 0
    chart = ''

    # Iterate lists and calc total withdrawals and total for each category
    for item in categories:
      total_category = 0
      for ledger_item in item.ledger:
        if ledger_item['amount'] < 0:
          total_withdraw += float(ledger_item['amount'])
          total_category += float(ledger_item['amount'])      
      cat_final.append({'category': item.category, 'category_vertical':'', 'total': total_category, 'percentage':0})

    # Calculate category percentage from total
    for item in cat_final:
      item['percentage'] = math.floor((float(item['total']) / total_withdraw) * 100)

    # Start outputting/printing barchart
    chart = 'Percentage spent by category' + '\n'

    # Loop the barchart y value from 100 downto 0
    for x in range(11, 0, -1):
      barchart_yvalue = (x * 10) - 10

      # print y value barchart
      line = str(barchart_yvalue).rjust(3) + "|"

      # iterate over categories and if within barchart y value print the '0' else print ' ' centered(3)
      for item in cat_final:
        if item['percentage'] >= barchart_yvalue:
          line += 'o'.center(3)
        else:
          line += ' '.center(3)
      
      # print barchart line
      chart += line + ' ' + '\n'

    # print dotted line belowe chart before category names
    dots_len = len(cat_final) * 3 + 1;
    dots = '-'.center(dots_len, '-')
    chart += '    ' + dots + '\n'

  # print category names vertical
    len_max = 0
    for cat in cat_final:
      if len(cat['category']) > len_max:
        len_max = len(cat['category'])

    # iterate with counter in for in loop
    for x in range(0, len_max):
      char = ''
      for i, cat in enumerate(cat_final): 
        if x <= len(cat['category']) - 1:
          char += cat['category'][x].center(3)
        else:
          char += ' '.center(3)
          
      # Last vertical cat name must have double spaces 
      if i == len(cat_final) - 1:
        chart += '    ' + char + ' ' + '\n'
      else:
        chart += '    ' + char + '\n'

    # Remove \n at end of string
    chart = chart.rstrip('\n')

    return chart



# instantiating two example objects
Clothing = Budget('Clothing')
Clothing.deposit(500.000, 'initial deposit')
Clothing.withdraw(50, 'shirt')

Food = Budget('Food')
Food.deposit(1000.000, 'initial deposit')
Food.withdraw(10.15, 'groceries')
Food.withdraw(15.89, 'restaurant and more food')
Food.transfer(50.00, Clothing)

