from mpd import MPDClient
import time 

print('started');
client = MPDClient();
print('client created');

client.connect("localhost", 6600);
print(client.mpd_version);

print(client.currentsong());
client.play(0);
time.sleep(5);

print('sleep stopped');
client.pause();
print('paused');

client.clear();
print('cleared');

client.stop();
print('client stopped');
client.close();
time.sleep(1);
print('client closed');
client.disconnect();

print('stopped');

