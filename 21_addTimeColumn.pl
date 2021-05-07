if ($ARGV[2] eq "")
{
	print "\n\nplease call this script like this: ".$0." inputfile outputfile samplingrate\n\n\n";
	exit();
}

$in=$ARGV[0];
$out=$ARGV[1];
$samplingRate=$ARGV[2];
$deltaTime=1/$samplingRate;



open(IN,"<$in");
open(OUT, ">$out");
while ($line=<IN>)
{
	chop $line;
	if ($line ne "")
	{
		$lc++;
		if ($lc==1){print OUT "time\t".$line."\n";}
		else {print OUT $time."\t".$line."\n";}
		$time+=$deltaTime;
	}
}
close(IN);
close(OUT);

