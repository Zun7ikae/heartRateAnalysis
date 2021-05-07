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
	@ele = split /\t/, $line;
	if ($lc==1)
	{
		$newData[$lc][1]=$ele[0];
		$newData[$lc][2]=$ele[1]."_normalized";
	}
	else {$newData[$lc][1]=$ele[0]; $data[$lc][2]=$ele[1];}
}
close(IN);


### find minimum and maximum
$min=$data[2][2];
$max=$data[2][12];
for ($a=2; $a<=$lc; $a++)
{
	$c++;
	if ($min > $data[$a][2]){$min=$data[$a][2];}
	if ($max < $data[$a][2]){$max=$data[$a][2];}
}

print "\n";
print "\n min:  ".$min;
print "\n max:  ".$max;
print "\n";


### normalize timecourse
for ($a=2; $a<=$lc; $a++)
{
	$newData[$a][2]=$data[$a][2]/($max);
}


### print data
open(OUT, ">$out");
for ($a=1; $a<=$lc; $a++)
{
	print OUT $newData[$a][1]."\t".$newData[$a][2]."\n";
}
close(OUT);

