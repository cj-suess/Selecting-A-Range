[] This algorithm will extract values within a specified range from a sorted list.
  --> works in time O(k + log n)

[] It takes a sorted list, list_s, and two values, lo and hi, and returns a list of all the values in list_s which are greater than or equal to lo and less than or equal to hi. The list of returned values does not need to be sorted.

[] Special conditions to keep in mind:

  --> If list_s is None then return None.
  --> If lo is greater than hi then return None.
  --> If lo is None then all values are greater than lo and select the return value(s) accordingly.
  --> If hi is None then all values are less than hi and select the return value(s) accordingly.
  --> list_s may contain repeated values. For instance, [2, 2, 3, 4] is a permissible input.
  --> If a list is present, even if it is empty (i.e., []), your routine should return all values in the range, which may be the empty list.
  --> lo and hi do not have to be present in list_s but your routine should still return all values that greater than or equal (if present) to lo and less then or equal (if present) to hi.
  --> Values in list_s can be compared for equality and less than and greater than. But there is no guarantee that adding or subtracting values makes sense. Expressed more concretely, you cannot reliably compute list_s[index] - list_s[index-1].
