# NeuralNetworks
## Personal basic math-oriented Implementation :
### Notations: 
#### X:=Input
#### Y := Output 
#### W :=Weight matrice
#### B:= Biases coloumn
#### E:=Error
### Forward Propagation:
#### Y= W*X +B

### Backwarad Propagation:
 #### (1) ∂E/∂W=∂E/∂Y * X.transposed
 #### (2) ∂E/∂B=∂E/∂Y
 #### (3)∂E/∂X= W.transposed * ∂E/∂y
