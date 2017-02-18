/* sample.c -- a sample cgi program for web programming students
 *
 * by Darren Provine, 14 September 2002
 */

#include <stdio.h>
#include <stdlib.h>

int main()
{
  char *query_string;
  char *content_length;
  char item;

  printf("Content-type: text/plain\n\n");

  content_length = getenv("CONTENT_LENGTH");

  if (content_length != NULL) {
      printf("You used a POST.\n");
      printf("Here is your CONTENT_LENGTH: %d\n", atoi(content_length));
      printf("Here is your data:\n");
      while ( (item = getchar()) != EOF ) {
        putchar(item);
      }
  } else {
      printf("You used a GET.\n");
      query_string = getenv("QUERY_STRING");
      printf("Here is your QUERY_STRING:\n\n");
      printf("%s\n", query_string);
  }
  return 0;
}
