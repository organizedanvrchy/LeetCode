# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

def long_com_prefix(strs):
  # Check for an empty list and return empty string if true
  if not strs:
    return ""

  # Assume 1st string is the common prefix
  prefix = strs[0]

  # Compare the 1st string as the prefix to each string in the rest of array
  # and if each string doesn't start with the prefix string, reduce the prefix
  # string one character at a time and repeat until it matches the start of the
  # current string
  for s in strs[1:]:
    while string[:len(prefix)] != prefix and prefix:
      prefix = prefix[:-1]

  # Return "" if prefix becomes empty
  if not prefix:
    return ""

return prefix
