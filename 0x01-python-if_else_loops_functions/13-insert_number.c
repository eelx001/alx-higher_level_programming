#include "lists.h"

/**
* insert_node - Inserts a number into a sorted singly linked list.
* @head: Pointer to head node.
* @number: Value to be inserted.
*
* Return: Address of New Node OR NULL on failure.
*/
listint_t *insert_node(listint_t **head, int number)
{
		listint_t *current = *head;
		listint_t *next = current->next;
		while (current->next != NULL)
		{
				if (next->n > number)
				{
						current->n = number;
						current->next = current->next;
						return (current);
				}
				current = current->next;
		}
		return current;
}
