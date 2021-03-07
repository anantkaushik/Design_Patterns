# Bridge
> Bridge is a structural design pattern that lets you split a large class or a set of closely related classes into two 
> separate hierarchies—abstraction and implementation—which can be developed independently of each other.

> Note that we’re not talking about interfaces or abstract classes from your programming language. 
> These aren’t the same things.
> When talking about real applications, the abstraction can be represented by a graphical user interface (GUI), and the 
> implementation could be the underlying operating system code (API) which the GUI layer calls in response to user 
> interactions.

### Applicability:
- Use the Bridge pattern when you want to divide and organize a monolithic class that has several variants of some 
  functionality (for example, if the class can work with various database servers).
- Use the pattern when you need to extend a class in several orthogonal (independent) dimensions.
- Use the Bridge if you need to be able to switch implementations at runtime.