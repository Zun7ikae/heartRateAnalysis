if ($ARGV[1] eq "")
{
	print "\n\nplease call this script: ".$0." inputfile outputfile\n\n\n";
	exit();
}

$in=$ARGV[0];
$out=$ARGV[1];

open(IN,"<$in");

while ($line=<IN>)
{
	chop $line;
	$lc++;
	@ele=split /\t/, $line;
	$data[$lc][1]=$ele[0];
	$data[$lc][2]=$ele[1];
	#print $ele[0]." ".$ele[1]."\n";	
}
close(IN);

open(OUT, ">$out");
print OUT "time\tnormalized_value\tdelta_t\tdelta_delta_t\tdelta_y\tfrequency\n";
$tLastPeak=0;
for ($a=2; $a<$lc; $a++)
{
	$deltaYLast10= $data[$a][2]-$data[$a-10][2];
	#$deltaYLast20= $data[$a][2]-$data[$a-20][2];
	#$deltaYNext20= $data[$a][2]-$data[$a+20][2];
	#$deltaYNext30= $data[$a][2]-$data[$a+30][2];


	#if (($data[$a][2]>$data[$a+1][2]) && ($data[$a][2]>$data[$a-1][2]) && ($deltaYNext30 > 0.5))
	#{
	#	print $data[$a][1]."\t".$data[$a][2]."\t".$deltaYNext30."\n";
	#}

	if (($data[$a][2]>$data[$a+1][2]) && ($data[$a][2]>$data[$a-1][2]))
	{			
		$deltaT=$data[$a][1]-$tLastPeak;
		$frequency=60/$deltaT;



		if (($frequency > 45) && ($frequency < 200) && $data[$a][2] > 0.6)
		{
			$tLastPeak=$data[$a][1];
			$deltaDeltaT=$deltaT-$lastDeltaT;
			$lastDeltaT=$deltaT;
			$deltaTSw=0;
			if ($deltaDeltaT > 0.05){$deltaTSw=1;}
			print OUT $data[$a][1]."\t".$data[$a][2]."\t".$deltaT."\t".$deltaTSw."\t".$deltaYLast10."\t".$frequency."\n";
			#print $data[$a][1]."\t".$data[$a][2]."\t".$deltaT."\t".$frequency."\n";
		}

	}
}
close(OUT);

