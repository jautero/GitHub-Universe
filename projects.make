gituser:=$(error Insert your GitHub username here.)

# Include macros for getting projects through GitHUb API
include github.make
# Create rules for watched repositories.
$(call githubwatched,$(gituser))
