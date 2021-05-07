### open the file
if ($ARGV[2] eq "")
{
	print "\n\nplease use this script like this: ".$0." inputfile outputfile invertfactor\n\n\n";
}
$in=$ARGV[0];
$out=$ARGV[1];
$invertFactor=$ARGV[2];

open(IN,"<$in");

while ($line=<IN>)
{
	chop $line;
	$lc++;
	if ($lc==1){}
	else 
	{
		@ele = split /\t/, $line;
		$data[$lc][1]=$ele[0];
		$data[$lc][2]=$ele[1];
	}
}
close(IN);


### inverte timecourse
$data[1][1]="time";
$data[1][2]="ekg_inverted";
for ($a=2; $a<=$lc; $a++)
{
	$data[$a][2]=$data[$a][2]*$invertFactor;
}


### print data
open(OUT, ">$out");
for ($a=1; $a<=$lc; $a++)
{
	print OUT $data[$a][1]."\t".$data[$a][2]."\n";
}
close(OUT);

