#! /usr/bin/perl -w

# Scrape2.cgi - demonstrate screen-scraping in Perl
#               this one follows 5 links from Oatmeal
# D Provine and Bob S.

use strict;
use CGI;
use WWW::Mechanize;
use HTML::TokeParser;

my $cgi = new CGI;
print $cgi->header(-type=>'text/html'),
    $cgi->start_html('Bob S.\'s Screen Scraper');
print $cgi->h1("5 Comic Scraper"), "\n";

# div to center all body of html
print $cgi->div({style=>"width:100%;", align=>"center"});

# collection of urls that are published sites of cartoons
my @urls = ("http://theoatmeal.com/comics/selfie_public", "http://theoatmeal.com/comics/trust", "http://theoatmeal.com/comics/dog_paradox", "http://theoatmeal.com/comics/literally", "http://theoatmeal.com/comics/apple");

# for every url in the above collection
foreach my $url (@urls){
    
    # create new web agent and get a page
    my $agent = WWW::Mechanize->new();
    $agent->get($url); # change URL every time

    # create new HTML parser and get the content from the web agent
    my $stream = HTML::TokeParser->new(\$agent->{content});

    print $cgi->h2($url), "\n";

    my $tag = $stream->get_tag("div");
    # advance to the div ofthe cartoon:
    while ($tag->[1]{id} and $tag->[1]{id} ne "comic") {
	$tag = $stream->get_tag("div");
    }
    $tag = $stream->get_tag("img");
    
    # get the attribute src from the "img" tag:
    my $source = $tag->[1]{'src'};
    my $caption = "Comic Goes Here";

    my $str = "link to, ";
    print $cgi->p($str);
    print $cgi->a({href=>$url}), "\n", $url, "</a>\n\n";
    print $cgi->br();
    print $cgi->img({src=>$source, alt=>$caption}), "\n\n";
    print $cgi->br();
    
    do { 
	$tag = $stream->get_tag("img");
	$source = $tag->[1]{'src'};
	print $cgi->img({src=>$source, alt=>$caption}), "\n";
	print $cgi->br();
    } while (defined $source);
}

# ALL DONE!                                                                    
print $cgi->end_html, "\n";
