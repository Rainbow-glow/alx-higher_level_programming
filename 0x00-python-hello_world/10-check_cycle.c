#include <stdlib.h>
#include "lists.h"

/**
* check_cycle - Checks if a singly-linked list has a cycle on it.
* @list: A singly-linked list.
*
* Return: 1 If there is cycle, otherwise 0.
*/
int check_cycle(listint_t *list)
{
	listint_t *checker, *audit;

	if (list == NULL || list->next == NULL)
		return (0);

	checker = list->next;
	audit = list->next->next;

	while (checker && audit && audit->next)
	{
		if (checker == audit)
			return (1);

		checker = checker->next;
		audit = audit->next->next;
	}

	return (0);
}
