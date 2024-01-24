#include "lists.h"

/**
 * is_palindrome - A function in c that checks if a singly linked list
 * is a palindrome
 * @head: the pointer to the first node
 *
 * Return: 0 if it is not a palindrome, 1 if is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow_ptr, *fast_ptr, *sec_half, *fir_half;
	slow_ptr = *head;
	fast_ptr = *head;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (fast_ptr && fast_ptr->next)
	{
		slow_ptr = slow_ptr->next;
		fast_ptr = fast_ptr->next->next;
	}

	sec_half = rev_list(slow_ptr);
	fir_half = *head;

	while (sec_half)
	{
		if (fir_half->n != sec_half->n)
			return (0);

		fir_half = fir_half->next;
		sec_half = sec_half->next;
	}

	return (1);
}

/**
 * rev_list - Reverses a linked list
 * @head: the pointer to the first node
 *
 * Return: the reversed list
 */

listint_t *rev_list(listint_t *head)
{
	listint_t *prev = NULL, *next = NULL;
	listint_t *current = head;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	return (prev);
}
