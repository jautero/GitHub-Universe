# Makefile macros to generate projects using GitHub API
#
# Copyright (C) 2010 Juha Autero <jautero@iki.fi>

# Turn github repository given as parameter into a universe.make project.
# Expects repo as a parameter in form of name=url
define githubhandlerepo
$(eval $(call createproject,$(word 1,$(subst =, ,$(1))),git,$(word 2,$(subst =, ,$(1))),$(word 1,$(subst =, ,$(1))) from $(word 2,$(subst =, ,$(1)))))
endef

# Get list of repositories using get-watched.py helper program and pass them to githubhabdlerepo
define githubwatched
$(foreach repo,$(shell python get-watched.py $(1)),$(call githubhandlerepo,$(repo)))
endef