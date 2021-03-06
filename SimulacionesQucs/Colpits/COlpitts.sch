<Qucs Schematic 0.0.19>
<Properties>
  <View=140,111,827,865,1,0,0>
  <Grid=10,10,1>
  <DataSet=COlpitts.dat>
  <DataDisplay=COlpitts.dpl>
  <OpenDisplay=1>
  <Script=COlpitts.m>
  <RunScript=0>
  <showFrame=0>
  <FrameText0=Título>
  <FrameText1=Dibujado por:>
  <FrameText2=Fecha:>
  <FrameText3=Revisión:>
</Properties>
<Symbol>
</Symbol>
<Components>
  <GND * 1 500 580 0 0 0 0>
  <GND * 1 510 800 0 0 0 0>
  <_BJT Q2N3904_1 1 460 390 8 -26 0 0 "npn" 0 "1.4e-14" 0 "1" 0 "1" 0 "0.025" 0 "0" 0 "100" 0 "0" 0 "3e-13" 0 "1.5" 0 "0" 0 "2" 0 "300" 0 "7.5" 0 "0" 0 "0" 0 "2.4" 0 "0" 0 "0" 0 "4.5e-12" 0 "0.75" 0 "0.33" 0 "3.5e-12" 0 "0.75" 0 "0.33" 0 "1" 0 "0" 0 "0.75" 0 "0" 0 "0.5" 0 "4e-10" 0 "0" 0 "0" 0 "0" 0 "2.1e-08" 0 "26.85" 0 "9e-16" 0 "1" 0 "1" 0 "0" 0 "1" 0 "1" 0 "0" 0 "1.5" 0 "3" 0 "1.11" 0 "26.85" 0 "1" 0>
  <GND * 1 620 310 0 0 0 0>
  <L L1 1 500 650 -26 10 0 0 "100 uH" 1 "" 0>
  <Vdc V1 1 620 260 18 -26 0 1 "10 V" 1>
  <C C3 1 590 500 17 -26 0 1 "470 nF" 1 "" 0 "neutral" 0>
  <R R1 1 360 290 15 -26 0 1 "47 kOhm" 1 "26.85" 0 "0.0" 0 "0.0" 0 "26.85" 0 "european" 0>
  <R R2 1 360 490 15 -26 0 1 "10 kOhm" 1 "26.85" 0 "0.0" 0 "0.0" 0 "26.85" 0 "european" 0>
  <C C1 1 630 710 17 -26 0 1 "0.1 nF" 1 "" 0 "neutral" 0>
  <C C2 1 380 710 17 -26 0 1 "1 nF" 1 "" 0 "neutral" 0>
  <.DC SimulacionDC 1 360 160 0 43 0 0 "26.85" 0 "0.001" 0 "1 pA" 0 "1 uV" 0 "no" 0 "150" 0 "no" 0 "none" 0 "CroutLU" 0>
  <R Re 1 470 500 15 -26 0 1 "1.2 kOhm" 1 "26.85" 0 "0.0" 0 "0.0" 0 "26.85" 0 "european" 0>
  <.TR Transitoria 1 190 160 0 71 0 0 "lin" 1 "0" 1 "5 us" 1 "100001" 0 "Trapezoidal" 0 "2" 0 "1 ns" 0 "1e-16" 0 "150" 0 "0.001" 0 "1 pA" 0 "1 uV" 0 "26.85" 0 "1e-3" 0 "1e-6" 0 "1" 0 "CroutLU" 0 "no" 0 "yes" 0 "0" 0>
  <C C15 1 240 390 -26 17 0 0 "100 nF" 1 "" 0 "neutral" 0>
  <C C6 1 660 390 -26 17 0 0 "100 nF" 1 "" 0 "neutral" 0>
  <R Rc 1 490 290 15 -26 0 1 "4.7 kOhm" 1 "26.85" 0 "0.0" 0 "0.0" 0 "26.85" 0 "european" 0>
</Components>
<Wires>
  <360 320 360 390 "" 0 0 0 "">
  <270 390 360 390 "" 0 0 0 "">
  <380 650 380 680 "" 0 0 0 "">
  <380 650 470 650 "" 0 0 0 "">
  <530 650 630 650 "" 0 0 0 "">
  <630 650 630 680 "" 0 0 0 "">
  <380 740 380 800 "" 0 0 0 "">
  <380 800 510 800 "" 0 0 0 "">
  <630 740 630 800 "" 0 0 0 "">
  <510 800 630 800 "" 0 0 0 "">
  <360 390 430 390 "" 0 0 0 "">
  <460 420 460 440 "" 0 0 0 "">
  <460 320 460 350 "" 0 0 0 "">
  <460 320 490 320 "" 0 0 0 "">
  <360 260 410 260 "" 0 0 0 "">
  <620 290 620 310 "" 0 0 0 "">
  <410 230 620 230 "" 0 0 0 "">
  <410 260 490 260 "" 0 0 0 "">
  <410 230 410 260 "" 0 0 0 "">
  <500 580 590 580 "" 0 0 0 "">
  <590 530 590 580 "" 0 0 0 "">
  <590 440 590 470 "" 0 0 0 "">
  <460 440 460 450 "" 0 0 0 "">
  <460 440 590 440 "" 0 0 0 "">
  <460 350 460 360 "" 0 0 0 "">
  <460 350 570 350 "" 0 0 0 "">
  <570 350 570 390 "" 0 0 0 "">
  <570 390 630 390 "" 0 0 0 "">
  <210 390 210 650 "" 0 0 0 "">
  <210 650 380 650 "" 0 0 0 "">
  <470 580 500 580 "" 0 0 0 "">
  <360 390 360 460 "" 0 0 0 "">
  <360 580 470 580 "" 0 0 0 "">
  <360 520 360 580 "" 0 0 0 "">
  <460 450 470 450 "" 0 0 0 "">
  <470 450 470 470 "" 0 0 0 "">
  <470 530 470 580 "" 0 0 0 "">
  <630 390 630 470 "" 0 0 0 "">
  <630 470 680 470 "" 0 0 0 "">
  <680 470 680 650 "" 0 0 0 "">
  <630 650 680 650 "" 0 0 0 "">
  <690 390 760 390 "Vout" 750 360 28 "">
  <210 390 210 390 "Vin" 240 360 0 "">
</Wires>
<Diagrams>
</Diagrams>
<Paintings>
</Paintings>
