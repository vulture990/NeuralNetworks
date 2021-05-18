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
 #### Based on the following equations is how to adjust the weight and biases
 #### (1) ∂E/∂W=∂E/∂Y * X.transposed
 #### (2) ∂E/∂B=∂E/∂Y
 #### (3)∂E/∂X= W.transposed * ∂E/∂Y
