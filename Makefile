SOURCE_DOCS := $(wildcard *.md)

EXPORTED_DOCS=\
  $(SOURCE_DOCS:.md=.pdf) \
  $(SOURCE_DOCS:.md=.html)

PANDOC_OPTIONS=--standalone

PANDOC_PDF_OPTIONS=--to=context+tagging -V pdfa=3a
PANDOC_HTML_OPTIONS=--to html5 --mathml

%.pdf : %.md
	pandoc $(PANDOC_OPTIONS) $(PANDOC_PDF_OPTIONS) -o $@ $<

%.html : %.md
	pandoc $(PANDOC_OPTIONS) $(PANDOC_HTML_OPTIONS) -o $@ $<

context : $(SOURCE_DOCS:.md=.pdf)

html : $(SOURCE_DOCS:.md=.html)

all: $(EXPORTED_DOCS)

clean:
	rm ($EXPORTED_DOCS)
