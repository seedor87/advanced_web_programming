# Sample Makefile for Web Programming students
# Nothing too fancy; should be mostly understandable
# (Remember that Makefile commands are interpreted by /bin/sh, not
# by the C-shell.)
#
# by Darren Provine, 14 September 2002

DESTDIR   = /home/seedor87/public_html/awp/hw3/
X_TARGETS = formout.cgi
R_TARGETS = form_get.html webline.css
SOURCES   = formout.py form_get.html
# Note use of -Wall to take advantage of compiler testing
CFLAGS    = -O -Wall

.SUFFIXES:
.SUFFIXES: .py .cgi

# C programs don't need -static when compiled in order to work
.c.cgi:; gcc -o $@ $(CFLAGS) $<

# This target is just here to be the top target in the Makefile.
# Thus, "make" will compile but not install the program.
all: $(X_TARGETS) $(R_TARGETS)

# You might want to look up mkdir(1) to see about that -p flag.
install: $(X_TARGETS) $(R_TARGETS)
	@if [ ! -d $(DESTDIR) ] ; then mkdir -p $(DESTDIR); fi
	@for f in $(R_TARGETS)               ; \
	do                                     \
		/usr/bin/install -v -t $(DESTDIR) -m 444 $$f ; \
	done
	@for f in $(X_TARGETS)               ; \
	do                                     \
		/usr/bin/install -v -t $(DESTDIR) -m 555 $$f ; \
	done

# Note that here we don't blow away the directory, and so we
# be sure and tell the user.  The reason not to delete the
# directory is that it may have other files in it.  Checking
# for, and deleting, any such files will have to be done manually.
# (How could this be improved?)
#
# Note also that the @ sign keeps the echo lines from being echoed
# before they are run.  (That could be confusing.)  This little
# trick (and many more) can be discovered by consulting make(1S).
deinstall:
	cd $(DESTDIR) ; /bin/rm -f $(R_TARGETS) $(X_TARGETS)
	@echo "   ==>   removed file(s): $(R_TARGETS) $(X_TARGETS)"
	@echo "   ==>   left directory : $(DESTDIR)"

redo: deinstall install

# note Makefile added to RCS checklist
rcscheck:
	@for f in $(SOURCES) Makefile     ; \
	do                        \
		rcsdiff -q $$f > /dev/null || echo "  ==>  "$$f is not checked in ;\
	done

clean:
	/bin/rm -f core $(X_TARGETS)

depend:
	makedepend $(SOURCES)

# DO NOT DELETE

sample.o: /usr/include/stdio.h /usr/include/iso/stdio_iso.h
sample.o: /usr/include/sys/feature_tests.h /usr/include/sys/isa_defs.h
sample.o: /usr/include/sys/va_list.h /usr/include/stdio_tag.h
sample.o: /usr/include/stdio_impl.h /usr/include/sys/types.h
sample.o: /usr/include/sys/machtypes.h /usr/include/sys/int_types.h
sample.o: /usr/include/sys/select.h /usr/include/sys/time.h
sample.o: /usr/include/sys/time.h
