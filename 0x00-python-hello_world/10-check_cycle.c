#include "lists.h"

/**
 * check_cycle - A function that checks if a singly linked list
 * has a cycle in it
 * @list: the linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *ptr_slow = list, *ptr_fast = list;

	while (ptr_fast && ptr_fast->next)
	{
		ptr_slow = ptr_slow->next;
		ptr_fast = ptr_fast->next->next;

		if (ptr_slow == ptr_fast)
			return (1);
	}

	return (0);
}
