if ($ARGV[1] eq "")
{
	print "\n\nplease call this script like this: perl ".$0." inputfile samplingRate\n\n\”";
	exit();
}

$in=$ARGV[0];
$samplingRate=$ARGV[1];

open(IN,"<$in");
while ($line=<IN>)
{
	chop $line;
	if ($line ne "")
	{
		$dataPointCounter++;
		
		
		if ($dataPointCounter == 2)
		{
			$minimum=$line;
			$maximum=$line;
		}

		if ($line < $minimum){$minimum=$line;}
		if ($line > $maximum){$maximum=$line;}
	}
}


print "\n\ncharacteristics of ".$in.":";
print "\n";
print "\ndatapoints: ".($dataPointCounter-1);
print "\ntime:       ".($dataPointCounter-1)/$samplingRate;
print "\nminimum:    ".$minimum;
print "\nmaximum:    ".$maximum;

print "\n\n";
exit;
