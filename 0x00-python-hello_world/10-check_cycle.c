#include "lists.h"
/**
 *check_cycle - Function in C that checks if a singly linked
 *list has a cycle in it
 *@list: pointer to head of list
 *Return:0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *_single = list;
	listint_t *_double = list;

	if (list == NULL)
		return (0);

	while (_single != NULL && _double != NULL)
	{
		_single = _single->next;
		_double = _double->next->next;
		if (_double == _single)
			return (1);
	}

	return (0);
}
