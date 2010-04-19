GitHub Universe
===============

What is GitHub Universe?
------------------------

**GitHub Universe** is a way to create a sort of *meta repository* out of your projects in **GitHub** using `make`.

What is *meta repository*?
--------------------------

> *Meta* means that you step back from your own place. What you used to do is now what 
> you see. What you were is now what you act on. Verbs turn to nouns. What you used to 
> think of as a pattern is now treated as a thing to put in the slot of an other pattern. 
> A meta  foo is a foo in whose slots you can put foos.
>
> - **Guy L. Steele Jr.**, *Growing a Language*

**Gnu Arch** has a concept of *meta project* which allows you to checkout multiple repositories into your work directory.
We went a bit overboard with it when we started using **Gnu Arch** as our version control system at work. When we moved
to `git` we still had to work with several source code repositories. We built a git repository that only contained a
`makefile` that had rules to checkout all other repositories and called it **Universe** because it had every source code
repository our team worked with.

Because those rules contain lot of repetition, I decided to implement `makefile` macros to collect all common code together.
That way the rules are easier to maintain since changes need to be done only in single place. Thus, **universe.make** was born.

What does **GitHub Universe** do?
---------------------------------

It uses **GitHub APi** through **github** Python  library and small Python command-line utility to get a list of repositories
watched by a given user. Then it uses `makefile` macros to build **universe.make** projects out of that. The end result is a `makefile`
that can be used to check-out any project from **GitHub** that is watched by certain user. Since it uses the unauthorizing interface,
it doesn't require password and it will only get list of repositories that are public information.

How do I use it?
----------------

Just set apropriate **GitHub** user name in `projects.make` and run `make help`.
