                                        // -> BUBBLE SORT <-

// CODE:

#include <iostream>
using namespace std;

int main(){

    int n;
    cin>>n;

    int arr[n];
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }
    int counter=1;
    while(counter<n){
        for(int i=0;i<n-counter;i++){
            if(arr[i]>arr[i+1]){
                int temp= arr[i];
                arr[i]=arr[i+1];
                arr[i+1]=temp;
            }

        }
        counter++;
    }
    for(int i=0;i<n;i++){
        cout<<arr[i]<<" ";
    }

    return 0;
}

// NO. OF COMPARISONS:
/* 
With each iteration the largest element in the array bubbles up towards the last place, just like a water bubble rises up to the water surface.
Sorting takes place by stepping through all the data items one-by-one in pairs and comparing adjacent data items and swapping each pair that is out of order.
In Bubble Sort, n-1 comparisons will be done in 1st pass, n-2 in 2nd pass, n-3 in 3rd pass and so on.
So the total number of comparisons will be->

(n−1)+(n−2)+(n−3)+.....+3+2+1 = n(n−1)/2 = O(n^2) 
*/

// NO. OF SWAPS:
/*
Best Case: Already sorted, so -> O(1) swaps.
Average Case: O(N^2) swaps.
Worst Case: Sorted in descending order -> O(N^2) swaps.
*/

// IMPLEMENTATION:
/*
It is an in-place sorting algorithm
*/

// TIME COMPLEXITY:
/*
Best Case: O(n)
Average Case: O(n^2)
Worst Case: O(n^2)
*/

                                       // -> SELECTION SORT <-

// CODE:

#include <iostream>
using namespace std;

int main(){

    int n;
    cin>>n;

    int arr[n];
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }

    for(int i=0;i<n-1;i++){
        for(int j=i+1;j<n;j++){
            if(arr[j]<arr[i]){
             int temp=arr[j];
                arr[j]=arr[i];
                arr[i]=temp;
            }
        }
        }

    for(int i=0;i<n;i++){
        cout<<arr[i]<<" ";
        }
        
    return 0;
}

// NO. OF COMPARISONS:
/* 
Selecting the lowest element requires scanning all n elements (this takes n − 1 comparisons) and then swapping it into the first position.
Finding the next lowest element requires scanning the remaining (n − 1) elements and so on,
for (n − 1) + (n − 2) + ... + 2 + 1 = n(n − 1) / 2 = O(n^2) comparisons.
*/

// NO. OF SWAPS:
/*
Best Case: Already sorted, so -> O(1) swaps.
Average Case: O(N) swaps.
Worst Case: Sorted in descending order -> O(N) swaps.
*/

// IMPLEMENTATION:
/*
It can be implemented by in-place as well as out-place sorting algorithm
*/

// TIME COMPLEXITY:
/*
Best Case: O(n^2)
Average Case: O(n^2)
Worst Case: O(n^2)
*/


