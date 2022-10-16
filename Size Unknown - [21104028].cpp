#include <iostream>
using namespace std;

// Creating a function for Binary search in an array
int binarySearch(int arr[], int low, int high, int target)
{
    if (high>=low)
    {
        int mid = (high + low)/2;
        if (arr[mid] == target)
            return mid;
        if (arr[mid] > target)
            return binarySearch(arr, low, mid-1, target);
        return binarySearch(arr, mid+1, high, target);
    }
    return -1;
}

// Creating a function to search the target element in array
int searchElement(int arr[], int target)
{
    int low = 0, high = 1;
    int val = arr[0];
 
    
    while (val < target)
    {
        low = high;        
        high = high << 1;      // high = 2*high
        val = arr[high]; 
    }
    // Running Binary search over the array with the updated high index
    return binarySearch(arr, low, high, target);
}

int main()
{
    int n, target;
    cout<<"Enter the number of elements in array: ";
    cin>>n;
    cout<<"Enter the element to be searched: ";
    cin>>target;
    int arr[n];
    cout<<"Enter the array elements separated by a space: ";
    for(int i=0; i<n; i++){
        cin>>arr[i];
    }

    int ans = searchElement(arr, target);
    if (ans == -1)
        cout << "Element not found";
    else
        cout << "Element found at index: " << ans;
    return 0;
}