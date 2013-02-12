#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int i,j;
int n;

void quicksort(int *arr, int first, int last)
{
  if(first == last || first+1 == last)
    {
      
      return;
    }
  
  int pivot = (first+last)/2;
  printf("Pivot: %d\n", pivot);
  while(first < last)
    {
      while(arr[first] < arr[pivot])
	first++;
      while(arr[last] > arr[pivot])
	last--;
      if(arr[first] > arr[last])
	{
	  int temp; temp = arr[first];
	  arr[first] = arr[last];
	  arr[last] = temp;
	}
      
    }
  
  //quicksort(arr,first,pivot-1);
  //quicksort(arr,pivot,last);
}

int main()
{
  int arr[] = {2,9,8,4,6,5,3,7};
  
  int size; size = sizeof(arr)/sizeof(int);
  n = size;
  
  for(i=0;i<n;i++)
    printf("%d ", arr[i]);
  printf("\n");
  
  quicksort(arr,0,size-1);
  quicksort(arr,0,3);
  quicksort(arr,4,7);
  quicksort(arr,0,1);
  quicksort(arr,2,3);
  quicksort(arr,4,5);
  quicksort(arr,6,7);
  
  for(i=0;i<n;i++)
    printf("%d ", arr[i]);
  printf("\n");
  
  return 0;
}
