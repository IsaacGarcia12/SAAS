#!/usr/bin/perl
use strict;
use warnings;
use LWP::UserAgent;
 
my $ua = LWP::UserAgent->new;
$ua->timeout(10);
$ua->default_header( 'Accept' => 'application/json' );

my $cadena = $#ARGV+1;
print $cadena;
=head
my $cadena ='>tr|F8WFZ5|F8WFZ5_RAT Insulin-like growth factor 1, isoform CRA_b OS=Rattus norvegicus OX=10116 GN=Igf1 PE=1 SV=2
MGKISSLPTQLFKICLCDFLKIKIHIMSSSHLFYLALCLLTFTSSATAGPETLCGAELVD
ALQFVCGPRGFYFNKPTGYGSSIRRAPQTGIVDECCFRSCDLRRLEMYCAPLKPTKSARS
IRAQRHTDMPKTQKSQPLSTHKKRKLQRRRKGSTLEEHK';
=cut
my $url = 'http://www.cathdb.info/search/by_funfhmmer';
my %data = ();
$data{fasta} = $cadena;

my $response = $ua->post( $url , \%data );
 
if ($response->is_success) {
    print $response->decoded_content;
    my $filename = '/home/isaac/Escritorio/SAmin/TT/static/TT/report.json';
    open(FH, '>', $filename) or die "No se pudo abrir el archivo '$filename' $!";
    print FH $response->decoded_content;
    close (FH);
    print "Se imprimio correctamente\n"; )
}
else {
    die $response->status_line;
}
