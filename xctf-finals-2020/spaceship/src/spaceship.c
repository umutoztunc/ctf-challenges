#include "spaceship.h"

#include <stdbool.h>
#include <stdio.h>
#include <string.h>

#define COUNT_OF(x) (sizeof(x) / sizeof(x[0]))

// Check if the flag satisfies the equations.
bool check(const char *flag) {
  if (strlen(flag) < FLAG_LENGTH)
    return false;

  for (int i = 0; i < COUNT_OF(equations); ++i) {
    int n = COUNT_OF(equations[i]);
    int result = 0;
    for (int j = 0; j < n - 1; j += 2) {
      int coeff = equations[i][j];
      int index = equations[i][j + 1];
      result += coeff * flag[index];
      result %= PRIME_MODULUS;
    }
    if (result < 0)
      result += PRIME_MODULUS;
    if (result != equations[i][n - 1])
      return false;
  }
  return true;
}

int main() {
  char flag[128]; 
  fgets(flag, sizeof(flag), stdin);
  flag[strcspn(flag, "\r\n")] = '\0';

  if (check(flag))
    puts("You are indeed a crewmember.");
  else
    puts("Imposter!");
  return 0;
}
