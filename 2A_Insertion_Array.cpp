#include<iostream.h>
#include<conio.h>
void main()
{
clrscr();
int number;
cout<<"Enter Total Number of Elements : ";
cin>>number;
cout<<endl;
int a[50];
int count=number;
cout<<"Enter Elements : ";
for(int i=0;i<number;i++)
{
cin>>a[i];
}
cout<<endl;
int k;
cout<<"Enter the Position where you want the Element to be Inserted : ";
cin>>k;
cout<<endl;
int b;
cout<<"Enter the Element to be Inserted : ";
cin>>b;
cout<<endl;
while(count>=k)
{
a[count+1]=a[count];
count--;
}
a[k]=b;
for(int j=0;j<=number;j++)
{
cout<<"After Insertion : "<<a[j]<<endl;
}
getch();
}