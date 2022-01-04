% Program in MATLAB to perform Union, Intersection and Complement operations.
% Enter Data 
u=input('Enter First Matrix');
v=input('Enter Second Matrix');
% To Perform Operations
w=max(u,v);
p=min(u,v);
q1=1-u;
q2=1-v;
% Output
display('Union Of Two Matrices');
display(w);
display('Intersection Of Two Matrices');
display(p);
display('Complement Of First Matrix');
display(q1);
display('Complement Of Second Matrix');
display(q2);
