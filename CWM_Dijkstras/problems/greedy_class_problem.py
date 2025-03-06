from datetime import time

# also called activity selection problem
class Class:
   def __init__(self, subject, start, end):
      self.subject = subject
      self.start = start
      self.end = end


classes = [ 
   Class("Algebra", time(8,0), time(10,0)),
   Class("World History", time(9,0), time(11,30)),
   Class("Art", time(10,0), time(10,30)),
   Class("Study Hall", time(12,0), time(13,0)),
   Class("Intro To Python", time(11,0), time(12,0)),
   Class("Chemistry", time(14,0), time(15,0)),
   Class("Orchestra", time(14,30), time(16,0)),
]

# Want to schedule as many classes as possible for the day
schedule = []

## Solution goes HERE ##

print(f"Fit {len(schedule)}/{len(classes)} classes.")
for _class in schedule:
   print (f"{_class.start} {_class.end} {_class.subject}")

