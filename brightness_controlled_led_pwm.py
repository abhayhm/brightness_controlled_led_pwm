import machine
import time
import utime

led = machine.Pin(14,machine.Pin.OUT)
rpwm = machine.PWM(machine.Pin(5))							
gpwm = machine.PWM(machine.Pin(4))
bpwm = machine.PWM(machine.Pin(12))

ldr=machine.ADC(0)

f1=nr=nb=ng=base1=0

while True:
	l1=utime.ticks_ms()
	if(l1-base1>500):
		base1=l1
		if(f1==0):
			led.on()
			f1=1
		else:
			led.off()
			f1=0

	val=ldr.read()
	if(val>876):
		r=255
		g=0
		b=0
	if(val>730 and val<=876):
		r=255
		g=165
		b=0
	if(val>584 and val<=730):
		r=255
		g=255
		b=0
	if(val>438 and val<=584):
		r=0
		g=255
		b=0
	if(val>292 and val<=438):
		r=0
		g=0
		b=255
	if(val>146 and val<=292):
		r=238
		g=130
		b=238
	if(val<=146):
		r=255
		g=255
		b=255

	if(r>nr):
		#r
		for i in range(nr,r):
			rpwm.duty(i)
			time.sleep(0.0015)
	if(r<nr):
		for i in range(nr,r,-1):
			rpwm.duty(i)
			time.sleep(0.0015)
	if(g>ng):
		#g
		for i in range(ng,g):
			gpwm.duty(i)
			time.sleep(0.0015)
	if(g<ng):
		for i in range(ng,g,-1):
			gpwm.duty(i)
			time.sleep(0.0015)
	if(b>nb):	
		#b
		for i in range(nb,b):
			bpwm.duty(i)
			time.sleep(0.0015)
	if(b<nb):		
		for i in range(nb,b,-1):
			bpwm.duty(i)
			time.sleep(0.0015)

	nr=r;ng=g;nb=b;






















	'''
	for i in range(1024):
		led.duty(i)
		time.sleep(0.001)

	time.sleep(1)
	for i in range(1023,-1,-1):
		led.duty(i)
		time.sleep(0.001)
	time.sleep(1)
	'''