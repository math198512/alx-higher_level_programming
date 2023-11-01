#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: pointer to the head of the list
 * Return: 0 in case of no cycle and 1 otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *templis;
	listint_t *prev;

	templis = list;
	prev = list;
	while (list && templis && templis->next)
	{
		list = list->next;
		templis = templis->next->next;

		if (list == templis)
		{
			list = prev;
			prev = templis;
			while (1)
			{
				templis = prev;
				while (templis->next != list && templis->next != prev)
				{
					templis = templis->next;
				}
				if (templis->next == list)
					break;

				list = list->next;
			}
			return (1);
		}
	}

	return (0);
}
