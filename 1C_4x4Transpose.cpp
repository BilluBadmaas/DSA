#include<iostream.h>
#include<conio.h>
void main()
{
clrscr();
int i,j,a[4][4];
cout<<"Enter Elements : ";
for(i=0;i<=3;i++)
{
for(j=0;j<=3;j++)
{
cin>>a[i][j];
}
cout<<endl;
}
cout<<"4X4 Matrix: "<<endl;
cout<<endl;
for(i=0;i<=3;i++)
{
for(j=0;j<=3;j++)
{
cout<<a[i][j]<<" ";
}
cout<<endl;
}
cout<<endl;
cout<<"Transpose of the Matrix: "<<endl;
cout<<endl;
for(j=0;j<=3;j++)
{
for(i=0;i<=3;i++)
{
cout<<a[i][j]<<" ";
}
cout<<endl;
}
cout<<endl;
getch();
}
