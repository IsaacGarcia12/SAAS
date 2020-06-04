#!/usr/bin/perl
use strict;
use warnings;
use LWP::UserAgent;
 
my $ua = LWP::UserAgent->new;
$ua->timeout(10);
$ua->default_header( 'Accept' => 'application/json' );

my $cadena = $#ARGV+1;

my $url = 'http://www.cathdb.info/search/by_funfhmmer';
my %data = ();
$data{fasta} = $cadena;

my $response = $ua->post( $url , \%data );
 
if ($response->is_success) {
    print $response->decoded_content;
}
else {
    die $response->status_line;
}

my $filename = 'report.json';
open(my $fh, '>', $filename) or die "Could not open file '$filename' $!";
print $fh $response->decoded_content;
close $fh;
print "done\n";