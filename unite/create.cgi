#!/usr/bin/perl -w



use CGI qw(:standard);
use CGI::Carp qw(fatalsToBrowser);
use File::Slurp;

$file="file.txt";
my $text = read_file($file);

#my $text = read_file('F:\\Coding\\Chatapp Final\\file.txt');
#$file="F:\\Coding\\Chatapp Final\\file.txt";
$chrname = param("chatroomname");
$password = param("Pin1");
$password2 = param("Pin2");
@lines={};
$flag=0;







print header();

print<<EOP;

<html lang="en">
<head>

    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>UNITE</title>

    <!-- Bootstrap core CSS -->
    <link href="vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="css/round-about.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css?family=Lato|Montserrat:200" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css?family=Lato:300" rel="stylesheet">

  </head>

<style type="text/css">
  h2{
    font-family: Lato;
    font-weight: 200;
    margin-left: 3%;
text-align:center;
  }
  h1{
    font-family: Montserrat;
    font-weight: 200;
    font-size: 4rem;
  }
  h3{
    font-family: Lato;
    font-weight: 200;
    text-align: center;
    color:#296AAC;
  }
    body,html{
    height: 100%;
    margin: 0;
    overflow: hidden;
  }
  body{
    display: grid;
    justify-items:center;
  }
  #bm{
    width: 250px;
  }
</style>

    <div id="bm"></div>
<div id="mainpage">


  <body style="background-color:#f4f4f4;" class="">

    <!-- Navigation -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top">
      <div class="container">
        <a class="navbar-brand" href="index.html">UNITE</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarResponsive">
          <ul class="navbar-nav ml-auto">
            <li class="nav-item active">
              <a class="nav-link" href="index.html">Main</a>
                <span class="sr-only">(current)</span>  
            </li>
            <li class="nav-item">
              <a class="nav-link" href="about.html">About us</a>      
            </li>
            <li class="nav-item">
              <a class="nav-link" href="code.html">Code</a>
            </li>     
          </ul>
        </div>
      </div>
    </nav>

    <!-- Page Content -->
    <div class="container" style="max-width:80%">

EOP


if(length($password) != 4){
		print "<h2>Length of password must be 4</h2>";
}else{

	if($password eq $password2){
	@lines = split('---',$text);
		$len = scalar(@lines);
		for($i=0;$i<$len;$i+=1){
			my @splitstr = split(',',@lines[$i]);
			if(@splitstr[0] eq $password){
				$flag=1;
				last;
			}
		}

		if($flag == 1){
			print "<h2>Pin already exists</h2>";
		}else{
			print "<h2>Room Created successfully</h2>";
			print "<a href=\"http://widit.knu.ac.kr:3000\"><h3>Click Here to go to Chatroom</h3></a>";
			open(OUT,">$file") || die "can't writ to $file";
			print OUT "$text---$password,$chrname,";
			close OUT;

		}


		}else{
			print "<h2>Pins dont match</h2>";
		}

}


print<<EOP;
<br><br><br><br><br><br><br>
    </div>
    <!-- /.container -->

    <!-- Footer -->
     <footer class="py-5 bg-dark">
      <div class="container">
        <p class="m-0 text-center text-white">Copyright© Libin &amp; Jaehyoen</p>
      </div>
      <!-- /.container -->
    </footer>
    </div>

    <!-- Bootstrap core JavaScript -->
    <script src="vendor/jquery/jquery.min.js"></script>
    <script src="vendor/bootstrap/js/bootstrap.bundle.min.js"></script>

</body>

</html>

EOP


