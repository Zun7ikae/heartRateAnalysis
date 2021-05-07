$in=$ARGV[1];
$sampleFactor=50;

if ($in eq "")
{
	$in="pilot_01_hr_5000hz_c_50000_dp.tab";
}
$out=substr $in, 0, (length($in)-4);
$out=$out."_downsampled_by_factor_".$sampleFactor.".tab";

open(IN,"<$in");
open(OUT,">$out");
while ($line=<IN>)
{	
	chop $line;
	if ($line eq "ekg"){print OUT $line."\n";}
	else
	{
		$sum=$sum+$line;
		$lineCounter++;

		if ($lineCounter%$sampleFactor == 0)
		{
			$mean=$sum/$sampleFactor;
			print OUT $mean."\n";
			$sum=0;
		}
	}
}
close(IN);
close(OUT);

