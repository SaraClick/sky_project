-- media_url data updates to contain the actual SRC for the iframe instead of the website URL
-- These updates are needed so the iframe reaches the correct source for the diaplay or the youtube video or spotify playlist
use fortyWinks;

-- ************VIDEO UPDATES************
-- 1	https://youtu.be/Q6MemVxEquE
CALL UpdateUrl(1, "https://www.youtube.com/embed/Q6MemVxEquE");
-- 2	https://www.youtube.com/live/pvnMgBz_ehU?feature=share
CALL UpdateUrl(2, "https://www.youtube.com/embed/pvnMgBz_ehU");
-- 3	https://youtu.be/-YUR5I-sdBk
CALL UpdateUrl(3, "https://www.youtube.com/embed/-YUR5I-sdBk");
-- 4	https://youtu.be/qYnA9wWFHLI
CALL UpdateUrl(4, "https://www.youtube.com/embed/qYnA9wWFHLI");
-- 5	https://www.youtube.com/watch?v=RqzGzwTY-6w&ab_channel=JasonLewis-MindAmend
CALL UpdateUrl(5, "https://www.youtube.com/embed/RqzGzwTY-6w");
-- 6	https://www.youtube.com/watch?v=yIQd2Ya0Ziw&ab_channel=Calm
CALL UpdateUrl(6, "https://www.youtube.com/embed/yIQd2Ya0Ziw");
-- 7	https://www.youtube.com/watch?v=AqJuVSu58oI&ab_channel=HALIDONMUSIC
CALL UpdateUrl(7, "https://www.youtube.com/embed/NChORYXuprE");


-- ************SOUND UPDATES************
-- 8	https://open.spotify.com/playlist/37i9dQZF1DX4hpot8sYudB?si=c18e6df788554773
CALL UpdateUrl(8, "https://open.spotify.com/embed/playlist/37i9dQZF1DX4hpot8sYudB?utm_source=generator&theme=0");
-- 9	https://open.spotify.com/playlist/37i9dQZF1DWVSZlCPJ6VZl?si=303447d58a244153
CALL UpdateUrl(9, "https://open.spotify.com/embed/playlist/37i9dQZF1DWVSZlCPJ6VZl?utm_source=generator&theme=0");
-- 10	https://open.spotify.com/playlist/3I20P0gW1ua9Pd3tcRDyaj?si=8cb5289ba7c44ac2
CALL UpdateUrl(10, "https://open.spotify.com/embed/playlist/3I20P0gW1ua9Pd3tcRDyaj?utm_source=generator&theme=0");
-- 11	https://open.spotify.com/playlist/37i9dQZF1DX9M0XCg3OHJ6?si=2cdc007069bb4814
CALL UpdateUrl(11, "https://open.spotify.com/embed/playlist/37i9dQZF1DX9M0XCg3OHJ6?utm_source=generator&theme=0");
-- 12	https://open.spotify.com/playlist/6KE4MokBWv1w52zDZVBpId?si=312c44079837485d
CALL UpdateUrl(12, "https://open.spotify.com/embed/playlist/6KE4MokBWv1w52zDZVBpId?utm_source=generator&theme=0");
-- 14	https://open.spotify.com/album/54vGSK50oe08qxz2xXECEC?si=xspMQI-zRJmRcw8gI-ksgQ
CALL UpdateUrl(14, "https://open.spotify.com/embed/album/54vGSK50oe08qxz2xXECEC?utm_source=generator&theme=0");
-- 15	https://open.spotify.com/playlist/37i9dQZF1DWXzR2GKEiHgT?si=8159263fb53b4139
CALL UpdateUrl(15, "https://open.spotify.com/embed/playlist/37i9dQZF1DWXzR2GKEiHgT?utm_source=generator&theme=0");
-- 16	https://open.spotify.com/playlist/37i9dQZF1DX60xkhEfNtud?si=e5446ee335c84816
CALL UpdateUrl(16, "https://open.spotify.com/embed/playlist/37i9dQZF1DX60xkhEfNtud?utm_source=generator&theme=0");

CALL UpdateUrl(18, "https://open.spotify.com/embed/playlist/37i9dQZF1DX2PQDq3PdrHQ?utm_source=generator&theme=0");
CALL UpdateUrl(17, "https://open.spotify.com/embed/playlist/37i9dQZF1DWYcDQ1hSjOpY?utm_source=generator&theme=0");
CALL UpdateUrl(13, "https://open.spotify.com/embed/playlist/7pFkxDrpvBSlxY9qcrVMWQ?utm_source=generator&theme=0");