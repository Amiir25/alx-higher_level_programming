#include "lists.h"

/**
 * check_cycle - Checks if a linked list has a cycle init
 * @list: The pointer to the list
 *
 * Return: 1 if the list has cycle, 0 otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *ptr;

	ptr = list;
	while (ptr)
	{
		if (ptr->next == list)
			return (1);

		ptr = ptr->next;
	}

	return (0);
}
