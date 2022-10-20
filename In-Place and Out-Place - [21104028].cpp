#include <iostream>
using namespace std;

int main(){

    // INSERTION SORT USING IN-PLACE ALGORITHM.........................

    int n;
    cout<<"Enter number of elements in array: ";
    cin>>n;

    int arr[n];
    cout<<"Enter the elements of array: ";
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }
    for(int i=1;i<n;i++){
        int current=arr[i];
        int j=i-1;
        while(arr[j]>current && j>=0){
            arr[j+1]=arr[j];
            j--;
        }
        arr[j+1]=current;

    }
    cout<<"The sorted array using in-place insertion sort algorithm: ";
    for(int i=0;i<n;i++){
        cout<<arr[i]<<" ";
    }
    cout<<endl;


    // INSERTION SORT USING OUT-PLACE ALGORITHM.........................


    int n1;
    cout<<"Enter number of elements in array: ";
    cin>>n1;

    int arr1[n1];
    cout<<"Enter the elements of array: ";
    for(int i=0;i<n1;i++){
        cin>>arr1[i];
    }
    int arr2[n1];
    for(int i=0; i<n1; i++){
        arr2[i] = arr1[i];
    }
    for(int i=1;i<n1;i++){
        int current=arr2[i];
        int j=i-1;
        while(arr2[j]>current && j>=0){
            arr2[i]=arr2[j];
            j--;
        }
        arr2[j+1]=current;

    }
    cout<<"The sorted array using out-place insertion sort algorithm: ";
    for(int i=0;i<n1;i++){
        cout<<arr2[i]<<" ";
    }
    cout<<endl;

    return 0;
}
