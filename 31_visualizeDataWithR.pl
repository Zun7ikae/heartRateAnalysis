### variables
if ($ARGV[4] ne "")
{
	$inputFile=$ARGV[0]; $minimum=$ARGV[1]; $maximum=$ARGV[2]; $timeWindow=$ARGV[3]; $showImageSwitch=$ARGV[4];
}

else
{
	print "\n\nplease call this script like this: ".$0." inputfile minimum maximum timewindow showImageSwitch\n\n\n";
	exit();
}



$rOutputFile="dataPlotter.4r";

$label_x="time [s]";
$label_y="values";


### automatic variables
$jpgOutputFile=$inputFile."_timewindow_".$timeWindow.".jpg";


open(IN, "<$inputFile");
while ($line=<IN>)
{
	$lc++;
	chop $line;
	@ele=split /\t/, $line;
	if ($lc==1){$column1Label=$ele[0]; $column2Label=$ele[1];}
}
close(IN);


print "\n\nstarting plot processing with R";


$string4R="file = \"".$inputFile."\"

data <- read.table(file, header=TRUE)
attach(data)


jpeg(\"".$jpgOutputFile."\", width = 1600, height = 800)

#par(mfcol=c(2,1))
";

$newString="### ekg ###
plot(
	".$column1Label.", ".$column2Label.", 
	xlab=\"".$column2Label."\", 
	xlim=c(0,".$timeWindow."),
	xaxp   = c(0, ".$timeWindow.", ".$timeWindow."),
	ylab=\"".$column1Label."\", 
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
)

#points(
#	time, ".$dataLabel.", 
#	#pch=19, cex = .6,
#	pch=19, cex = .1,
#	col=\"red\"
#)



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

