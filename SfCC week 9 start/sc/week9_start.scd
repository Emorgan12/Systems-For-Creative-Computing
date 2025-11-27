s.boot;

a = Buffer.read(s, thisProcess.nowExecutingPath.dirname +/+ "../audio/amen-short.wav");

({
	var mouse = MouseX.kr(-1, 1);

	PlayBuf.ar(
		2,
		a.bufnum,
		BufRateScale.kr(a.bufnum) * mouse,
		loop:1
	)
}.play
)

(
SynthDef(\amen, {
	arg pitch = 1, volume = 0.5;
	var sig = PlayBuf.ar(
		2,
		a.bufnum,
		BufRateScale.kr(a.bufnum) * pitch,
		loop:1
	) * volume;
	Out.ar(0, sig)
}).add
)

a = Synth(\amen);
a.set(\pitch, 0.8);
a.set(\volume, 1);
a.set(\pitch, 1.1, \volume, 0.6);
a.free;

