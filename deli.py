sandwich_order = ['Cuban', 'BLT', 'Banh', 'Grilled Cheese', 'Meatball', 'Philly Cheese Steak', 'Roast Beef', 'Pastrami', 'Pastrami', 'Pastrami']
finished_sandwiches = []

# Verify each sandwich until there are no more sandwich orders.
# Move each verified sandwich into the list of finished sandwiches.

while 'Pastrami' in sandwich_order:
    sandwich_order.remove('Pastrami')

while sandwich_order:
    completed_orders = sandwich_order.pop()

    print('Completing sandwich order:' + completed_orders.title())
    finished_sandwiches.append(completed_orders)

print('The following sandwiches have been completed')
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())
