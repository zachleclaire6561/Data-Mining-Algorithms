%LDA: 
load WineData.mat X I

%centered data
Xc = [];
%centered X-bar data
Xbarc = [];
for c = 1:3
    I_c = find(I==c);
    X_c = X(:,I_c);
    m = mean(X_c');
    p = size(X_c);
    %subtract mean to find center
    X_c = X_c - repmat(m, p(2), 1)';
    Xbar = repmat(m, p(2),1)';
    Xc = [Xc, X_c];    
    Xbarc = [Xbarc, Xbar];
end
p=size(X);
Xbarc = Xbarc - repmat(mean(X'),p(2),1)';
%within cluster scatter matrix
Sw = Xc*Xc';
Sb = Xbarc*Xbarc';

%check if Sw is positive definite
eig_SW = eig(Sw);
flag = 0;
for i = 1:rank(Sw)
  if eig_SW(i) <= 0 
  flag = 1;
  end
end

%regularize if not positive definite
if flag == 1
    p = size(Sw);
    tau = 10^(-8);
    [U,S,V] = svd(Sw);
    %take the largest singular value
    d = S(1,1);
    epsilon = tau*d*d;
    Sw = Sw + epsilon*eye(p(1));
end

R = chol(Sw);
%eigenvectors of inverse of K transpose * Sb * K transpose
[V,D] = eig(inv(R)'*Sb*R');

%find LDA vectors
q1 = inv(R)*V(:,1);
q2 = inv(R)*V(:,2);

%project each x onto 
%project A onto B: (dot(A,B)/norm(B)^2)*B
p = size(X);
X_1 = [];
X_2 = [];
for i = 1:p(2)
    qx1 = (dot(q1,X(:,i))/norm(q1)^2);
    qx2 = (dot(q2,X(:,i))/norm(q1)^2);
    X_1 = [X_1, qx1];
    X_2 = [X_2, qx2];
end


L = 4*ones(1,178);
C = I;

scatter(X_1,X_2, L, C);
title('Components along q1 and q2');
xlabel('Components along q1');
ylabel('Components along q2');
axis('equal');
set(gca,'FontSize',15);


%find the component vectors in direction of LDA components

%display data in LDA directions