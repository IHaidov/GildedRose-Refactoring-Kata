# Gilded Rose Refactoring Kata: Changes and Justifications

## Repository Link
[GitHub Repository - GildedRose Refactoring Kata](https://github.com/IHaidov/GildedRose-Refactoring-Kata/commits/main)

## Changes Made

### 1. Fix Methods Parameters
- **Commit**: [fix methods parameters](https://github.com/IHaidov/GildedRose-Refactoring-Kata/commit/fix-methods-parameters)
- **Description**: Added the `self` parameter to `update_sulfuras`, `update_normal_item`, and `update_conjured`.
- **Justification**: Fixed `TypeError` caused by missing `self` in instance methods.

### 2. Complete `update_conjured` and `_update_backstage_passes`
- **Commit**: [complete update_conjured and _update_backstage_passes methods](https://github.com/IHaidov/GildedRose-Refactoring-Kata/commit/complete-update_conjured-and-_update_backstage_passes-methods)
- **Description**: Implemented logic for "Conjured" items (degrade twice as fast) and refactored "Backstage Passes" using constants for clarity.
- **Justification**: Ensures correct behavior for these items and improves readability.

### 3. Add Aged Brie Test
- **Commit**: [add Aged Brie test](https://github.com/IHaidov/GildedRose-Refactoring-Kata/commit/add-aged-brie-test)
- **Description**: Added a unit test to validate the behavior of "Aged Brie" (quality increases over time and doubles after the sell-by date).
- **Justification**: Ensures functionality aligns with requirements.

### 4. Complete `update_aged_brie` and `update_normal_item`
- **Commit**: [complete update_aged_brie and update_normal_item functions](https://github.com/IHaidov/GildedRose-Refactoring-Kata/commit/complete-update_aged_brie-and-update_normal_item-functions)
- **Description**: 
  - `update_aged_brie`: Implements quality increase over time.
  - `update_normal_item`: Implements quality degradation, accelerating after the sell-by date.
- **Justification**: Adheres to requirements for specific item behaviors.

### 5. Add Logic Separation Placeholders
- **Commit**: [add logic separation placeholders and max quality for items variables](https://github.com/IHaidov/GildedRose-Refactoring-Kata/commit/add-logic-separation-placeholders-and-max-quality-for-items-variables)
- **Description**: Added placeholders to separate logic for item types and introduced `MAX_QUALITY` for constraints.
- **Justification**: Improves maintainability and clarity.

### 6. Delete Non-Python Files
- **Commit**: [delete everything that is not python](https://github.com/IHaidov/GildedRose-Refactoring-Kata/commit/delete-everything-that-is-not-python)
- **Description**: Removed unnecessary files from the repository.
- **Justification**: Focuses the repository on Python implementation and testing.

## Testing Strategy

1. **Unit Tests**:
   - Verified functionality for all item types ("Aged Brie", "Backstage Passes", "Conjured", normal items).
   - Covered edge cases (e.g., maximum quality, sell-in date passed).

2. **Test Cases**:
   - Added `test_aged_brie` to verify:
     - Quality increases correctly before and after the sell-by date.
     - Quality stops at the maximum (50).

3. **Outcome**:
   - All tests passed without errors, confirming correct implementation.



_Support this and all my katas via [Patreon](https://www.patreon.com/EmilyBache)_

# Gilded Rose Refactoring Kata

You can find out more about this exercise in my YouTube video [Why Developers LOVE The Gilded Rose Kata](https://youtu.be/Mt4XpGxigT4). I also have a video of a worked solution in Java - [Gilded Rose Kata, Hands-on](https://youtu.be/OdnV8hc9L7I)

I use this kata as part of my work as a technical coach. I wrote a lot about the coaching method I use in this book [Technical Agile Coaching with the Samman method](https://leanpub.com/techagilecoach). A while back I wrote this article ["Writing Good Tests for the Gilded Rose Kata"](http://coding-is-like-cooking.info/2013/03/writing-good-tests-for-the-gilded-rose-kata/) about how you could use this kata in a [coding dojo](https://leanpub.com/codingdojohandbook).


## How to use this Kata

The simplest way is to just clone the code and start hacking away improving the design. You'll want to look at the ["Gilded Rose Requirements"](https://github.com/emilybache/GildedRose-Refactoring-Kata/blob/main/GildedRoseRequirements.md) which explains what the code is for. I strongly advise you that you'll also need some tests if you want to make sure you don't break the code while you refactor.

You could write some unit tests yourself, using the requirements to identify suitable test cases. I've provided a failing unit test in a popular test framework as a starting point for most languages.

Alternatively, use the Approval tests provided in this repository. (Read more about that in the section "Text-based Approval Testing").

The idea of the exercise is to do some deliberate practice, and improve your skills at designing test cases and refactoring. The idea is not to re-write the code from scratch, but rather to practice taking small steps, running the tests often, and incrementally improving the design. 

### Gilded Rose Requirements in other languages 

- [English](GildedRoseRequirements.md)
- [Español](GildedRoseRequirements_es.md)
- [Français](GildedRoseRequirements_fr.md)
- [Italiano](GildedRoseRequirements_it.md)
- [日本語](GildedRoseRequirements_jp.md)
- [Português](GildedRoseRequirements_pt-BR.md)
- [Русский](GildedRoseRequirements_ru.md)
- [ไทย](GildedRoseRequirements_th.md)
- [中文](GildedRoseRequirements_zh.txt)
- [한국어](GildedRoseRequirements_kr.md)
- [German](GildedRoseRequirements_de.md)
- [Euskara](GildedRoseRequirements_eu.md)

## Text-Based Approval Testing

Most language versions of this code have a [TextTest](https://texttest.org) fixture for Approval testing. For information about this, see the [TextTests README](https://github.com/emilybache/GildedRose-Refactoring-Kata/tree/main/texttests)

## History of the exercise

This Kata was originally created by Terry Hughes (http://twitter.com/TerryHughes). It is already on GitHub [here](https://github.com/NotMyself/GildedRose). Bobby Johnson described the kata in an article titled "Refactor This: The Gilded Rose Kata", but unfortunately it is no longer on the internet. I found it on the Wayback Machine [here](https://web.archive.org/web/20240525015111/https://iamnotmyself.com/refactor-this-the-gilded-rose-kata/).

I translated the original C# into a few other languages, (with a little help from my friends!), and slightly changed the starting position. This means I've actually done a small amount of refactoring already compared with the original form of the kata, and made it easier to get going with writing tests by giving you one failing unit test to start with. I also added test fixtures for Text-Based approval testing with TextTest (see [the TextTests](https://github.com/emilybache/GildedRose-Refactoring-Kata/tree/main/texttests))

As Bobby Johnson points out in his article "Why Most Solutions to Gilded Rose Miss The Bigger Picture" (on the Wayback Machine [here](https://web.archive.org/web/20230530152324/https://iamnotmyself.com/why-most-solutions-to-gilded-rose-miss-the-bigger-picture/)), it'll actually give you
better practice at handling a legacy code situation if you do this Kata in the original C#. However, I think this kata
is also really useful for practicing writing good tests using different frameworks and approaches, and the small changes I've made help with that. I think it's also interesting to compare what the refactored code and tests look like in different programming languages.

## Contributing

Contributions are encouraged! You could add a translations of the specification
in another language or a new starting point for your favorite programming
language. Please see [CONTRIBUTING.md](./CONTRIBUTING.md) for more details.
