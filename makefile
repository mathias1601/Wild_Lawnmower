ZIP_NAME = wild_lawnmower.zip

.PHONY: zip

zip:
	zip -r $(ZIP_NAME) . -x ".git/*" ".git/**"
