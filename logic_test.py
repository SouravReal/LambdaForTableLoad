
def list_to_string(list_elements):
  """Converts a list to a string without comma and square brackets.

  Args:
    list_elements: The list to be converted.

  Returns:
    A string representation of the list.
  """

  string_representation = "\""
  for element in list_elements:
    string_representation += element+"\" string, \n\""

  return string_representation

if __name__ == "__main__":
  list_elements = ["a", "b", "c"]
  print(list_elements)

  string_representation = list_to_string(list_elements)
#   string = "This is a string."
  new_string = string_representation[:-4]

  print(string_representation)
  print(new_string)