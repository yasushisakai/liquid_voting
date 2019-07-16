
using Base
using LinearAlgebra

num_ppl = 3;
num_pln = 2;
m_size = num_ppl + num_pln;
iter_limit = 10000;

V = [0 0.2 0.4 0 0; 0.1 0 0.4 0 0; 0.1 0.3 0 0 0; 0.1 0.5 0 1 0; 0.7 0 0.2 0 1]
f = y -> V * y;

# a = [1.0; 1.0; 1.0; 0; 0]

A = zeros(m_size,m_size) + I

println(A)

for i = 1:iter_limit
      global A
      A = f(A)
    end


for i = num_ppl+1:m_size
    println(sum(A[i, 1:num_ppl]))
end
