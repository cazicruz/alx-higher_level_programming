#include <stdio.h>
#include <stdlib.h>

/**
* check_cycle: this is the start of this function
* @list: function parameter
* Return: returns 1 if list is a cycle and 0 if not
*/

int check_cycle(listint_t *list)
{
	listint_t *temp;
	
	if (list == NULL || list->next == NULL)
	{
		return (0);
	}
	temp = list->next;
	while (temp)
	{
		if(temp == list )
		{
			return (1);
		}else if (temp == NULL)
		{
			return (0);
		}else
			temp = temp->next;
	}
}

