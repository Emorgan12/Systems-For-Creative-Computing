(
{
	var freq = 150;
	var env = EnvGen.kr(Env.perc(0.001, 0.05));

	SinOsc.ar(freq, 0, 1*env) !2
}.play
)

(
SynthDef(\kick, {
	arg freq = 30;
	var env = EnvGen.kr(Env.perc(0.001, 0.05), doneAction:2);
	var sig = SinOsc.ar(freq, 0, 1*env) !2;

	Out.ar(0, sig)
}).add
)

(
SynthDef(\bass, {
	arg freq = 100, on = 1, rel = 0.5;
	var env = EnvGen.kr(Env.perc(0.001, rel), doneAction:2);
	var sig = Saw.ar(freq, 0.2*env*on) !2;

	Out.ar(0, sig)
}).add
)

Synth(\kick)

TempoClock.default.tempo = 110/60;

(
Pbind(
	\instrument, \kick,
	\dur, Pseq([1, 1, 1, 1/4, 1/4, 1/4, 1/4], inf),
	\freq, 60,
).play;

(
Pbind(
	\instrument, \bass,
	\dur, Pseq([0.5, 0.25], inf),
	\freq, Pwhite(500, 1000, inf),
	\rel, Pwhite(0.1, 0.8, inf),
	\on, Prand([0,1], inf),
).play
)
)

Synth(\bass)

