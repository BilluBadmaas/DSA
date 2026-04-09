#include<iostream.h>
#include<conio.h>
void main()
{
clrscr();
int i,j,a[3][3],b[3][3],c[3][3];
cout<<"Enter Elements for Matrix 1: ";
for(i=0;i<=2;i++)
{
for(j=0;j<=2;j++)
{
cin>>a[i][j];
}
cout<<endl;
}
cout<<"Matrix 1 : "<<endl;
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
cout<<"Enter Elements for Matrix 2: ";
for(i=0;i<=2;i++)
{
for(j=0;j<=2;j++)
{
cin>>b[i][j];
}
cout<<endl;
}
cout<<"Matrix 2 : "<<endl;
cout<<endl;
for(i=0;i<=2;i++)
{
for(j=0;j<=2;j++)
{
cout<<b[i][j]<<" ";
}
cout<<endl;
}
cout<<endl;
cout<<"Addition of Matrix 1 & Matrix 2: "<<endl;
cout<<endl;
for(i=0;i<=2;i++)
{
for(j=0;j<=2;j++)
{
c[i][j]=a[i][j]+b[i][j];
cout<<c[i][j]<<" ";
}
cout<<endl;
}
cout<<endl;
getch();
}
