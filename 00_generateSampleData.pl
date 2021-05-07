$b=10000;
$loops=10000;
srand();
open(OUT, ">templateData".$loops.".tab");
print OUT "data\n";

for ($a=1; $a<=$loops; $a++)
{
	
	$r=rand(1)*100+1;
	$r2=rand();
	if ($r2<0.5){$b=$b-$r;}
	if ($r2>=0.5){$b=$b+$r;}
	print OUT $b;
	if ($a<$loops){print OUT "\n";}
}
close OUT;
