name = input("Please employee's name: ")
hour = input("Please enter number of hours worked in a week: ")
pay_rate = input("Please enter hourly pay rate: ")
f_tax = input("Please enter federal tax withholding rate: ")
s_tax = input("Please enter state tax withholding rate: ")

gross_pay = float(hour) * float(pay_rate)
f_hold = float(f_tax) * gross_pay
s_hold = float(s_tax) * gross_pay
t_deduction = f_hold + s_hold
net = gross_pay - t_deduction

f_tax = format(float(f_tax), '.1%')
s_tax = format(float(s_tax), '.1%')

f_hold = format(f_hold, '.2f')
s_hold = format(s_hold, '.2f')
t_deduction = format(t_deduction, '.2f')
net = format(net, '.2f')

print(f"Employee Name: {name}\nHours Worked: {float(hour)}\nPay Rate: ${pay_rate}\nGross Pay: ${gross_pay}\nDeductions:\n\tFederal Withholding ({f_tax}): ${f_hold}\n\tState Withholding ({s_tax}): ${s_hold}\n\tTotal Deduction: ${t_deduction}\nNet Pay: ${net}")