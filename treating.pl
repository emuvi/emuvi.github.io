#!/usr/bin/perl
use warnings;
use strict;

open(SRC, '<', 'index.html') or die $!;
my $inside = 0;
while(<SRC>){
    if(/<!-- BEGIN TREATING SECTION -->/){
        $inside = 1;
    }
    if($inside){
        if(/<a href="(.*?)">(.*?)<\/a>/){
          my $link = $1;
          my $title = $2;
          my $treat = qq{<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Éverton M. Vieira</title>
    <link rel="stylesheet" href="../styles.css" />
  </head>

  <body>
    <div id="divBody">
      <div id="divLittleTopBar"></div>
      <div id="divContent">
        <div class="divRowContent">
          <div class="divColExpand">
            <div id="divNavBar"><a href="../index.html">Back</a></div>
            <h1>$title</h1>
            <p>Processing a small essay about it...</p>
          </div>
        </div>
      </div>
    </div>
  </body>
</html>};
          open(DES, '>', $link) or die $!;
          print DES $treat;
          close(DES);
        }
    }
    if(/<!-- END TREATING SECTION -->/){
        $inside = 0;
    }
}
close(SRC);