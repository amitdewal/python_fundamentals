# set difference in python

# registered vs attended
registered_students = {"Alice", "Bob", "Charlie", "David", "Emma"}
attended_students = {"Alice", "David", "Emma"}

print("RegisteredStudents:", registered_students)
print("AttendedStudents:", attended_students)

# using difference method
absentees = registered_students.difference(attended_students)
print("Absentees:", absentees)

# diffeence using - symbole

difference_symbol = registered_students - attended_students
print("DifferenceSymbol:", difference_symbol)

# real world inventory example
in_stock = {"pen", "pencil", "notebook", "rules", "eraser"}
solid_item ={"notebook","pen","eraser"}

remaining_stck = in_stock.difference(solid_item)
print("Remaining Stock:", remaining_stck)

rem_stock = solid_item.difference(in_stock)
print("Rema", rem_stock)
