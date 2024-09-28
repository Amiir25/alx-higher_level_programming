#include "lists.h"

/**
 * check_cycle - Checks if a linked list has a cycle init
 * @list: The pointer to the list
 *
 * Return: 1 if the list has cycle, 0 otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *slow;
	liatint_t *fast;

	if (list == NULL || list->next == NULL)
		return (0);

	slow = fast = list;
	while (slow != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	if (slow == fast)
		return (1);

	return (0);
}
