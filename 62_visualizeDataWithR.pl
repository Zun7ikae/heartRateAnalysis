### variables
if ($ARGV[5] ne "")
{
	$inputFile=$ARGV[0]; $minimum=$ARGV[1]; $maximum=$ARGV[2]; $startTime=$ARGV[3]; $endTime=$ARGV[4]; $showImageSwitch=$ARGV[5];
}

else
{
	print "\n\nplease call this script like this: ".$0." inputfile minimum maximum startTime endTime showImageSwitch\n\n\n";
	exit();
}



$rOutputFile="dataPlotter.4r";


### automatic variables
$jpgOutputFile=$inputFile."_timewindow_".$startTime."-".$endTime.".jpg";


open(IN, "<$inputFile");
while ($line=<IN>)
{
	$lc++;
	chop $line;
	@ele=split /\t/, $line;
	if ($lc==1){@labels=@ele;}
}
close(IN);


print "  starting plot processing with R";


$string4R="file = \"".$inputFile."\"

data <- read.table(file, header=TRUE)
attach(data)


jpeg(\"".$jpgOutputFile."\", width = 2400, height = 800)

#par(mfcol=c(2,1))
";

$newString="### ekg ###
plot(
	".$labels[0].", ".$labels[1].", 
	xlab=\"".$labels[0]."\", 
	xlim=c(".$startTime.",".$endTime."),
	xaxp   = c(0, ".($endTime-$startTime).", ".($endTime-$startTime)."),
	ylab=\"".$labels[1]."\", 
	ylim=c(".$minimum.",".$maximum."),
	#col.lab=\"green\",
	pch=20, cex = 1, #pch=20: small dot, pch=19: big dot; pch=3: cross
	col=\"red\"
)

axis(side = 4)

mtext(
	\"".$dataLabel."\",
	side = 4
	#line = 3
)";

if ($labels[2] ne "")
{
	$newString=$newString."
points(
	".$labels[0].", ".$labels[2].",
	pch=19, cex = 1,
	col=\"black\"
)";
}



#lines(
#	lowess(dateInFloat,weight), 
#	col=\"blue\"
#)";
$string4R=$string4R.$newString;



$newString="
dev.off()";
$string4R=$string4R.$newString;

open (OUT, ">$rOutputFile");
print OUT $string4R;
close OUT;


  #################
 ### print jpg ###
#################

$c="R CMD BATCH ".$rOutputFile;
print "\n\n   ... running command: ".$c."";
print "\n\n";
system(`$c`);

if ($showImageSwitch == 1)
{
	$c="xviewer ".$jpgOutputFile;
	print "   ... running command: ".$c."";
	print "\n\n";
}
system(`$c`);

