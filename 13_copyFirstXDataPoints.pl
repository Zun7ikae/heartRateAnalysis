$numberOfDataPoints=50000;

$in=$ARGV[1];

if ($in eq "")
{
	$in="pilot_01_hr_5000hz_c.tab";
}

$out=substr $in, 0, (length($in)-4);
$out=$out."_".$numberOfDataPoints."_dp.tab";

open(IN,"<$in");
open(OUT, ">$out");
while ($line=<IN>)
{
	chop $line;
	if ($line ne "ekg"){$counter++;}
	if ($counter <= $numberOfDataPoints)
	{
		print OUT $line."\n";
	}
	else {exit();}

}
close(IN);
close(OUT);
