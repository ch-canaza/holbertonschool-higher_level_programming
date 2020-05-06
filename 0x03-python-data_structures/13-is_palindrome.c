#include <stdio.h>
#include "lists.h"
/**
 * is_palindrome - verify if a list is a palindrome
 * @head: pointer to first  node
 * Return: 1 if palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
        listint_t *aux = *head;
        int tmp[100], i = 0, j = 0;

        if (!*head || !head || !aux->next)
                return (1);

        while (aux)
        {
            tmp[i] = aux->n;
            i++;
            aux = aux->next;
        }
        i--;
        while (j <= i)
        {
            if(tmp[j] != tmp[i])
                return (0);
            j++;
            i--;
        }
        return (1);
}
