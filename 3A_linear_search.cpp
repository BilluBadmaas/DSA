#include<iostream.h>
#include<conio.h>
void main()
{
clrscr();
int a[20], n, item, i, flag=0;
cout<<"Enter Total Number of Elements : ";
cin>>n;
cout<<endl;
cout<<"Enter the Elements : ";
for(i=0;i<n;i++)
{
cin>>a[i];
}
cout<<endl;
cout<<"Enter the Element to be Searched : ";
cin>>item;
cout<<endl;
for(i=0;i<n;i++)
{
if(a[i]==item)
{
cout<<"Element is Found at Position "<<i+1;
flag=1;
break;
}
}
if(flag==0)
{
cout<<"Desired Element is not Found in the Array!";
}
getch();
}