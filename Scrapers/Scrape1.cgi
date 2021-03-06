#! /usr/bin/perl -w

# Scrape1.cgi - demonstrate screen-scraping in Perl
# D Provine and Bob S.

use strict;
use warnings;
use CGI;
use WWW::Mechanize;     # This is the object that gets stuff
use HTML::TokeParser;   # This is the object that parses HTML
use Scalar::Util qw(looks_like_number); # needed to parse url for number

# create new web agent and get a page
my $agent = WWW::Mechanize->new();
my $url = "http://www.vgcats.com/super/?strip_id=85"; # url of last comic they produced
my $base_url = "http://www.vgcats.com/super/";

# we use this loop to deduce the index of the web page decided by the refernce in $url. We parse the url, as a string, until we stop encountering numbers. This parse yields the base_url and the vlaue of index. We use the value of index in the following do while as a sentinel. The base url is used to construct the following 7 comic page references
my $index = substr($url, -1);
$url = substr($url, 0, (length $url) -1);
my $next_index = substr($url, -1);

while (looks_like_number $next_index) {
    $index = substr($url, -1) . $index;
    $url = substr($url, 0, (length $url) -1);
    $next_index = substr($url, -1);
}
my $base_image = $url;
my $count = 7;
my $new_url = $base_image . $index;

# Generate a bunch of output:
my $cgi = new CGI;

print $cgi->header(-type=>'text/html'),
    $cgi->start_html('Bob S.\'s Screen Scraper');

print $cgi->h1("Super Effective --VGCats"), "\n";

# repeatedly grab the pages and scrape 7 recent images in reverse order starting with the most recent comic. If we subtract one form the value $index and it results in a value < 0 then we stop, we cannot have a reference to the page htt[://..._-1
do {    
    
    $new_url = $base_image . $index;
    $agent->get($new_url); # changed to my URL

    # create new HTML parser and get the content from the web agent
    my $stream = HTML::TokeParser->new(\$agent->{content});

    # get the first "div" tag to setup the loop...
    my $tag = $stream->get_tag("div");

    while ($tag->[1]{align} and $tag->[1]{align} ne 'center') {
	$tag = $stream->get_tag("div");
    }

    # advance to the div with the cartoon:
    while ($tag->[1]{width} and $tag->[1]{width} ne '660') {
	$tag = $stream->get_tag("div");
    }

    $tag = $stream->get_tag("div");
    $tag = $stream->get_tag("div");
    $tag = $stream->get_tag("p");

    # get the cartoon:
    my $toon = $stream->get_tag("img");

    # get the attributes from the "img" tag:
    my $source = $toon->[1]{'src'};
    $source = $base_url . $source;
    my $popup = $base_url . "siteimages/title.gif";
    my $caption = $new_url;

    print $cgi->a({href=>$caption}), "link to comic #" . $index, "\n\n";
    print $cgi->br();
    print $cgi->img({src=>$source, alt=>$caption}), "\n\n";
    print $cgi->br();

    $index = $index - 1;
    $count = $count -1;
} while ($index > 0 && $count > 0);

# ALL DONE!
print $cgi->end_html, "\n";

