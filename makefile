# `make zip` to run

ZIP_NAME = wild_lawnmower.zip

EXCLUDES = .git/* .git/**

.PHONY: zip

zip:
	zip -r $(ZIP_NAME) . -x $(EXCLUDES)
