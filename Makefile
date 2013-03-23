PELICAN=pelican
PELICANOPTS=

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/output
CONFFILE=$(BASEDIR)/pelicanconf.py
PUBLISHCONF=$(BASEDIR)/publishconf.py

S3_BUCKET=www.rdegges.com

help:
	@echo 'Makefile for a pelican Web site                                        '
	@echo '                                                                       '
	@echo 'Usage:                                                                 '
	@echo '   make html                        (re)generate the web site          '
	@echo '   make clean                       remove the generated files         '
	@echo '   make regenerate                  regenerate files upon modification '
	@echo '   make publish                     generate using production settings '
	@echo '   make serve                       serve site at http://localhost:8000'
	@echo '   make devserver                   start/restart develop_server.sh    '
	@echo '   s3_upload                        upload the web site via s3         '
	@echo '                                                                       '


html: clean $(OUTPUTDIR)/index.html
	@echo 'Done'

$(OUTPUTDIR)/%.html:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

clean:
	find $(OUTPUTDIR) -mindepth 1 -delete

regenerate: clean
	$(PELICAN) -r $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

serve:
	cd $(OUTPUTDIR) && python -m SimpleHTTPServer

devserver:
	$(BASEDIR)/develop_server.sh restart

publish:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF) $(PELICANOPTS)

s3_upload: publish
	s3cmd sync --acl-public --exclude='*.*' --include='*.html' --mime-type='text/html; charset=utf-8' --no-preserve output/ s3://$(S3_BUCKET)/
	s3cmd sync --acl-public --exclude='*.*' --include='*.xml' --mime-type='application/xml; charset=utf-8' --no-preserve output/ s3://$(S3_BUCKET)/
	s3cmd sync --acl-public --exclude='*.*' --include='*.css' --mime-type='text/css; charset=utf-8' --no-preserve output/ s3://$(S3_BUCKET)/
	s3cmd sync --acl-public --exclude='*.*' --include='*.js' --mime-type='application/javascript; charset=utf-8' --no-preserve output/ s3://$(S3_BUCKET)/
	s3cmd sync --acl-public --exclude='*.*' --include='*.png' --mime-type='image/png' --no-preserve output/ s3://$(S3_BUCKET)/
	s3cmd sync --acl-public --exclude='*.*' --include='*.gif' --mime-type='image/gif' --no-preserve output/ s3://$(S3_BUCKET)/
	s3cmd sync --acl-public --delete-removed --no-preserve output/ s3://$(S3_BUCKET)/

.PHONY: html help clean regenerate serve devserver publish s3_upload
