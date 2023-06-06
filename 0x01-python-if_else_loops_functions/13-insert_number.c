#include "lists.h"

/**
* insert_node - Inserts a number into a sorted singly linked list.
* @head: Pointer to head node.
* @number: Value to be inserted.
*
* Return: Address of New Node OR NULL on failure.
*/
listint_t *insert_node(listint_t **head, int num)
{
		listint_t *current = &head;
		listint_t *next = current->next;
		while (current->next != '\0')
		{
				if (next->n > num)
				{
						current->n = num;
						current->next = current->next;
						return (current);
				}
				current = current->next;
		}
		return (NULL);
}
