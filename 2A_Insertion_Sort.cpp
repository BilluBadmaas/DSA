#include<iostream.h>
#include<conio.h>
void main()
{
clrscr();
int a[20], n, i, del, count=0;
cout<<"Enter Total Number of Elements : ";
cin>>n;
cout<<endl;
cout<<"Enter Elements : ";
for(i=0;i<n;i++)
{
cin>>a[i];
}
cout<<endl;
cout<<"Enter the Value to be Deleted : ";
cin>>del;
cout<<endl;
for(i=0;i<n;i++)
{
if(a[i]==del)
{
for(int j=i;j<(n-1);j++)
{
a[j]=a[j+1];
}
count++;
n=n-1;
break;
}
}
if(count==0)
{
cout<<"Element Not Found!";
}
else
{
cout<<"Element Deleted Successfully!"<<endl<<endl;
cout<<"New Array : "<<endl;
for(i=0;i<n;i++)
{
cout<<a[i]<<endl;
}
}
getch();
}