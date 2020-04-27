#include "lists.h"
/**
 *check_cycle - verify if there is a cycle in the list
 * @list : head
 * Return 1 if there is a cycle otherwise 0
 */
 
int check_cycle(listint_t *list)
{
	listint_t *auxslow, *auxfast;

	auxslow = list;
	auxfast = list;

	while (auxslow != NULL && auxfast != NULL && auxfast->next != NULL)
	{
		auxslow = auxslow->next;
		auxfast = auxfast->next->next;
		if (auxslow == auxfast)
			return(1);
	}
	return(0);
}
