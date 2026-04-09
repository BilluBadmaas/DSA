#include<iostream.h>
#include<conio.h>
void main()
{
clrscr();
int i,j,a[3][3];
cout<<"Enter Elements : ";
for(i=0;i<=2;i++)
{
for(j=0;j<=2;j++)
{
cin>>a[i][j];
}
cout<<endl;
}
cout<<"3X3 Matrix: "<<endl;
cout<<endl;
for(i=0;i<=2;i++)
{
for(j=0;j<=2;j++)
{
cout<<a[i][j]<<" ";
}
cout<<endl;
}
cout<<endl;
cout<<"Subscript of Matrix:"<<endl;
cout<<endl;
for(i=0;i<=2;i++)
{
for(j=0;j<=2;j++)
{
cout<<"["<<i<<" "<<j<<"]="<<a[i][j]<<endl;
}
cout<<endl;
}
getch();
}
