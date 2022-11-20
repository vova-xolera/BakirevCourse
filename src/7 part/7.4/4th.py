def verify(lst_in):

  for i in range(len(lst_in) - 1):
       for j in range(len(lst_in) - 1):
            if lst_in[i][j] + lst_in[i + 1][j] + lst_in[i][j + 1] + lst_in[i + 1][j + 1] > 1:
                 return False
  return True





