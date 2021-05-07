if ($ARGV[0] eq "")
{
	print "\n\nplease call this script like this: ".$0." inputfile outputfile\n\n\n";
}
$in=$ARGV[0];
$out=$ARGV[1];

open(IN,"<$in");
$line=<IN>;
close(IN);

@lineElements=split /\ /, $line;

open (OUT, ">$out");
print OUT "ekg\n";

print "\n\nconverting datapoints...\n\n";
foreach(@lineElements)
{
	if (($_ ne "EKG") && ($_ ne ""))
	{
		$ekg=$_;
		$ekg=~ s/\,/./g;
		print OUT $ekg."\n";
		$c++;
		if ($c%5000==0){print ".";}
	}
}

