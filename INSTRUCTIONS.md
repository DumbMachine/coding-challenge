# Foldtools

This repository is the home for `Funktools` that implements the `fold` function.

## Description

`fold` is a higher order function that takes

- a function f(T, V) -> V
- a sequence of type T
- an initial value of type V

and returns a V. E.g., the `sum` of an array is a special case of fold, where

- the sequence is an array of numbers
- the starting value is 0
- the function is `+`

You can find more information on [Wikipedia](<https://en.wikipedia.org/wiki/Fold_(higher-order_function)>).

## Methodology/Approach

- Replicate `reduce` function from `functools`.
  ( I was unaware whether the mentioned parameter order was strict, thus defaulting to `functools.reduce`'s param order)
- Test consistency with `reduce`.
- Add fold_right & fold_left operations.
- Simple profiling of the function

## Resources

1. [Fold (higher-order function)](<https://en.wikipedia.org/wiki/Fold_(higher-order_function)>)
<figure class="video_container">
  <iframe src="https://en.wikipedia.org/wiki/Fold_(higher-order_function)" frameborder="0" style="position: absolute; height: 80%;width: 80%; border: none"> </iframe>
</figure>
