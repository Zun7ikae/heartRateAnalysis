if ($ARGV[2] eq "")
{
	print "\n\nplease call this script: ".$0." inputfile(Timecourse) inputfile(peaks) outputfile\n\n\n";
	exit();
}

$inTimecourse=$ARGV[0];
$inPeaks=$ARGV[1];
$out=$ARGV[2];



### open timecourse
open(IN,"<$inTimecourse");
while ($line=<IN>)
{
	chop $line;
	$lc++;
	@ele = split /\t/, $line;
	$data[$lc][1]=$ele[0]; $data[$lc][2]=$ele[1];
}
close(IN);



### open peaks
open(IN,"<$inPeaks");
while ($line=<IN>)
{
	chop $line;
	$pc++;
	@ele = split /\t/, $line;
	$peaks[$pc]=$ele[0];
}
close(IN);



### check if there is a peak
for ($a=2; $a<=$lc; $a++)
{
	$p=0;
	for ($b=2; $b<=$pc; $b++)
	{
		if ($data[$a][1] eq $peaks[$b])
		{
			$p=1;
		}
	}
	
	$data[$a][3]=$p;
}



### print data
$data[1][3]="peaks";
open(OUT, ">$out");
for ($a=1; $a<=$lc; $a++)
{
	print OUT $data[$a][1]."\t".$data[$a][2]."\t".$data[$a][3]."\n";
}
close(OUT);
