# rotating-equations: Finding an equation that has the same solution when rotated

This code performs an exhaustive search for an equation in a particular format that gives the same solutions when rotated.

To make this isn’t completely trivial. It seems clear that x, 1 and 8 have rotational symmetry, such that they work either way up (you may have to draw an unusually symmetric 8). The same is true of +, -, implicit multiplication and the horizontal line in a fraction. It is also clear that some numbers have no rotational symmetry and so cannot be used. A 2, 3, 4 or 7, no matter how you draw it, won’t look like anything useful when rotated. If you draw them right, a 6 and a 9 can be rotations of each other. This leaves 5. As far as I am concerned, if you draw it in a certain way it is recognisable when rotated (think of a digital clock).

There are lots of ways one could write a potential rearrangment equation. I chose a format (x+a)/b = c/(d+x) and this code looks for solutions that are the same for the standard and rotated versions.

For more details on the background, see this blog post [Finding an equation that has the same solution when rotated](https://aperiodical.com/2018/12/finding-an-equation-that-has-the-same-solution-when-rotated/).

I used this code to generate the equation in [this tweet](https://twitter.com/peterrowlett/status/1074599768993787904).
