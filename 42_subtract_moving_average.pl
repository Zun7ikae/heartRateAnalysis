if ($ARGV[2] eq "")
{
print "\n\nplease call this script: ".$0." inputfile outputfile moving_average_range\n\n\n";
exit();
}

$in=$ARGV[0];
$out=$ARGV[1];
$movingAveragePoints=$ARGV[2];

open(IN,"<$in");

while ($line=<IN>)
{
	chop $line;
	$lc++;
	@ele = split /\t/, $line;
	if ($lc==1)
	{
		$newData[$lc][1]=$ele[0];
		$newData[$lc][2]=$ele[1]."_moving_average_subtracted";
	}
	else {$newData[$lc][1]=$ele[0]; $data[$lc][2]=$ele[1];}
}
close(IN);


### normalize timecourse
for ($a=2; $a<=$lc; $a++)
{
	$sum=0;
	$nb=0;
	#print $a." ";
	if ($a < $movingAveragePoints/2+2)
	{
		for ($b=2; $b<=$a+$movingAveragePoints/2+2; $b++)
		{
			$sum+=$data[$b][2];
			$nb++;
		}
	}

	if (($a >= $movingAveragePoints/2+2) && ($a <= $lc-$movingAveragePoints/2))
	{
		for ($b=$a-$movingAveragePoints/2; $b<=$a+$movingAveragePoints/2; $b++)
		{
			$sum+=$data[$b][2];
			$nb++;
		}		
	}
	

	if ($a > $lc-$movingAveragePoints/2)
	{
		for ($b=$a-$movingAveragePoints/2; $b<=$lc; $b++)
		{
			$sum+=$data[$b][2];
			$nb++;
		}
	}

	$mean=$sum/$nb;
	$newData[$a][2]=$data[$a][2]-$mean;
	
}


### print data
open(OUT, ">$out");
for ($a=1; $a<=$lc; $a++)
{
	print OUT $newData[$a][1]."\t".$newData[$a][2]."\n";
}
close(OUT);

