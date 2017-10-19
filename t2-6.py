spam = 2000.0
not_spam = 1000.0

singles = 1500.0/spam
meeting = 550.0/spam
buy = 1000.0/spam

x_singles = 200.0/not_spam
x_meeting = 600.0/not_spam
x_buy = 150.0/not_spam



email = "Hey Bill, you have a meeting at 3 o'clock."
email_2 = "Meet singles in your area, click the link."

keywords = ['singles', 'meeting', 'buy']
for item in keywords:
      if item in email:
          if ((singles)/(singles + x_singles)) >= .8:
                print "This email is spam"
          elif ((meeting)/(meeting + x_meeting)) >= .8:
                print "This email is spam"
          elif ((buy)/(buy + x_buy)) >= .8:
                print "This email is spam"
          else:
              print email

for item in keywords:
     if item in email_2:
         if ((singles)/(singles + x_singles)) >= .8:
               print "This email is spam"
         elif ((meeting)/(meeting + x_meeting)) >= .8:
               print "This email is spam"
         elif ((buy)/(buy + x_buy)) >= .8:
               print "This email is spam"
         else:
             print email_2
