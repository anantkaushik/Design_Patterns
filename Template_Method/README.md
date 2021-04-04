# Template Method
> Template Method is a behavioral design pattern that defines the skeleton of an algorithm in the superclass but lets 
> subclasses override specific steps of the algorithm without changing its structure.

### Applicability:
- Use the Template Method pattern when you want to let clients extend only particular steps of an algorithm, but not 
  the whole algorithm or its structure.
- Use the pattern when you have several classes that contain almost identical algorithms with some minor differences. 
  As a result, you might need to modify all classes when the algorithm changes.
  