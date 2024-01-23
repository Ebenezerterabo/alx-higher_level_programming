#include "lists.h"

/**
 * insert_node - A function that insert a node at a specific position
 * @head: the pointer to the first node
 * @number: the number
 *
 * Return: the address of a new node or NULL on failure
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *newNode = malloc(sizeof(listint_t));

	if (newNode == NULL)
		return (NULL);

	newNode->n = number;
	newNode->next = NULL;

	if (*head == NULL || number < (*head)->n)
	{
		newNode->next = *head;
		*head = newNode;
		return (newNode);
	}

	while (current->next && number > current->next->n)
		current = current->next;

	newNode->next = current->next;
	current->next = newNode;

	return (newNode);
}
