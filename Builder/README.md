# Builder Pattern
> Builder pattern is a Creational pattern. Separates construction of an object from its representation.

> - Use the Builder pattern to get rid of a “telescopic constructor” 
     (for example, constructor with 10 optional parameters).
> - Use the Builder pattern when you want your code to be able to create different representations of some product
     (for example, stone and wooden houses).
> - Use the Builder to construct Composite trees or other complex objects.

## Why Builder?
- Some objects require a lot of ceremony to create.
- Having an object with 10 initializer arguments is not productive.
- Instead, opt for piecewise construction.
- Builder provides an API for constructing an object step-by-step.

## Summary:
- A builder is a separate component for building an object.
- To make builder fluent, `return self`.
- Different facets of an object can be built with different builders working in tadem via a base class.