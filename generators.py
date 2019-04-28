import math

def checksum(mac):
  mac %= 10000000
  counter = 0
  temp = mac
  while temp:
    counter += 3 * (temp % 10)
    temp = floor(temp / 10)
    counter += temp % 10
    temp = floor(temp / 10)
  return (mac * 10) + ((10 - (counter % 10)) % 10)

def pinASUS(mac):
	wpspin = fill(format(int(mac, 16), '02x'), 12)
	b = [int(wpspin[0:2], 16), int(wpspin[2:4], 16), int(wpspin[4:6], 16), int(wpspin[6:8], 16),int(wpspin[8:10], 16), int(wpspin[10:12], 16)]
	pin = []
	for i in range(7):
		pin.append((b[i % 6] + b[5]) % (10 - ((i + b[1] + b[2] + b[3] + b[4] + b[5]) % 7)))
	wpspin = fill(int(checksum(int(''.join(str(i) for i in pin), 10))), 8)
	return wpspin