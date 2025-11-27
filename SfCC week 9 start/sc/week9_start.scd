s.boot;

a = Buffer.read(s, thisProcess.nowExecutingPath.dirname +/+ "../audio/amen-short.wav");

(
{
	PlayBuf.ar(
		2,
		a.bufnum,
		BufRateScale.kr(a.bufnum),
		loop:1
	)
}.play
)