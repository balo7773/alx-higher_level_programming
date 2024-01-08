#include "lists.h"
#include <stdio.h>
/**
 * is_palindrome - checking list for palindrome
 * @head: pointer to pointer of first node of listint_t list
 * Return: 1 if palindrome 0 if not palindrome
*/
int is_palindrome(listint_t **head)
{
    int *a, max, i, j, k;

    listint_t *current = *head;

    max = 256;
    a = (int *)malloc(sizeof(int) * max);
    i = 0;

    while ((current->next == NULL) && (i < max))
    {
        a[i] = current->n;
        current = current->next;
        i++;
    }

    k = i ;
    j = 0;
    while (j < k)
    {
        printf("%d equal to %d\n", a[j], a[k]);
        if (a[j] != a[k])
        {
            return (0);
        }
        j++;
        k--;
    }    
    return (1);
    free(a);
}