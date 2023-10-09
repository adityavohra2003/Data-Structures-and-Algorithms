#include <iostream>
using namespace std;

void Shellsort(int A[],int n){
    int gap,i,j,temp;

    for(gap=n/2;gap>=1;gap/=2){
        for(i=gap;i<n;i++){
            temp= A[i];
            j= i-gap;
            while(j>=0 && A[j]>temp){
                A[j+gap] = A[j];
                j=j-gap;
            }
            A[j+gap]=temp;
        }
    }
}

int main(){
    int A[] = {11,13,7,12,16,9,26,5,10,3},n=10;
    Shellsort(A,n);
    cout<<"Sorted array is: ";
    for(int i=0;i<10;i++){
        cout<<A[i]<<" ";
    }
    cout<<endl;
    return 0;
}