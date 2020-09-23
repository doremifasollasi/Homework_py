def correct_tail(body, tail):
  """Function to make sure that the second argument (tail), 
  is the same as the last letter of the first argument (body) - otherwise the tail wouldn't fit!
  If the tail is right return true, else return false.
  The arguments will always be strings, and normal letters."""
  if body[-1] == tail:
    return True
  else:
    return False

  # return body.endswith(tail)

  # return body[-1] == tail

  # sub = body[len(body)-len(tail)]
  #   if sub == tail:
  #       return True
  #   else:
  #       return False


