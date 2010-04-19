# This is generic Makefile based on F-Secure's Mac & Linux Team's universe.
#
# Copyright (C) 2010 Juha Autero.
#
# What is universe?
#	It is a way to collect together bunch of separate projects from separate version control repositories by simply creating a makefile that
#	has rules for checking out each individual project.
# What is this file?
#	It is an attempt to create a simple template that makes it easy to build "universe" makefiles by putting common parts of rules in functions.
#	The goal is that adding new project is as simple as $(call project). After reading GNU Make manual, it actually is $(eval $(call createproject)).

ECHOE=echo -e
GIT=git

define git-checkout
$(GIT) clone $(1) $(2)
endef

define createproject
PROJECTS += $(1)
$(1)-help:
	@$(ECHOE) "\t$(1)  $(4)"
$(1):
	$(call $(2)-checkout,$(3),$(1))
endef

define alias
PROJECTS += $(2)
$(2)-help:
	@$(ECHOE) "\t$(2)  Alias for $(1)"
$(2): $(1)
endef

all: help


include github.make
include projects.make

.PHONY: $(PROJECTS:=-help) help generic-help

help: generic-help $(PROJECTS:=-help)
	@echo "Please run make <projectname>"

generic-help:
	@echo "This Makefile can checkout following projects:"
