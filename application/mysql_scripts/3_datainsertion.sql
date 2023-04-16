-- data insertion using stored procedures
-- how to use stored procedures
-- CALL StoredProcedureName(data) 

use fortywinks;

-- type_media insertions
-- CALL InsertType(type_name)
CALL InsertType("video");
CALL InsertType("sound");

-- source_media insertions
-- CALL InsertSource(source_name)
CALL InsertSource("youtube");
CALL InsertSource("spotify");

-- category_media insertions
-- CALL InsertCategory(category_name)
CALL InsertCategory("brown noise");
CALL InsertCategory("white noise");
CALL InsertCategory("ocean");
CALL InsertCategory("whale");
CALL InsertCategory("rain");
CALL InsertCategory("instrumental");

-- media insertions
-- CALL InsertMedia(media_title, media_url, type_id, source_id, category_id)
CALL InsertMedia("Deep Layered Brown Noise ( 12 Hours )", "https://youtu.be/Q6MemVxEquE)", 1, 1, 1);
CALL InsertMedia("Sound Of Rain And Thunder For Sleep - Rain Sounds For Relaxing Your Mind And Sleep Tonight", "https://www.youtube.com/live/pvnMgBz_ehU?feature=share", 1, 1, 5);
CALL InsertMedia("Rain sounds ASMR | Forest rain sounds for sleeping, relaxing, studying", "https://youtu.be/-YUR5I-sdBk", 1, 1, 5);
CALL InsertMedia("Marconi Union - Weightless (Official 10 Hour Version", "https://youtu.be/qYnA9wWFHLI", 1, 1, 6);
CALL InsertMedia("Smoothed Brown Noise 8 Hours - Remastered for Relaxation, Sleep, Studying & Tinnitus", "https://www.youtube.com/watch?v=RqzGzwTY-6w&ab_channel=JasonLewis-MindAmend", 1, 1, 1);
CALL InsertMedia("Rainstorm Sounds for Relaxing, Focus or Deep Sleep", "https://www.youtube.com/watch?v=yIQd2Ya0Ziw&ab_channel=Calm", 1, 1, 5);
CALL InsertMedia("Classical Music for Sleeping", "https://www.youtube.com/watch?v=AqJuVSu58oI&ab_channel=HALIDONMUSIC", 1, 1, 6);
CALL InsertMedia("Brown Noise", "https://open.spotify.com/playlist/37i9dQZF1DX4hpot8sYudB?si=c18e6df788554773", 2, 2, 1);
CALL InsertMedia("8 Hours of Sleep Brown Noise", "https://open.spotify.com/playlist/37i9dQZF1DWVSZlCPJ6VZl?si=303447d58a244153", 2, 2, 1);
CALL InsertMedia("Depp Brown Noise | Sleep Sound (12 hrs)", "https://open.spotify.com/playlist/3I20P0gW1ua9Pd3tcRDyaj?si=8cb5289ba7c44ac2", 2, 2, 1);
CALL InsertMedia("8 Hours of Sleep White Noise", "https://open.spotify.com/playlist/37i9dQZF1DX9M0XCg3OHJ6?si=2cdc007069bb4814", 2, 2, 2);
CALL InsertMedia("White Noise for sleeping", "https://open.spotify.com/playlist/6KE4MokBWv1w52zDZVBpId?si=312c44079837485d", 2, 2, 2);
CALL InsertMedia("Sleep Music for Anxiety", "https://open.spotify.com/playlist/7pFkxDrpvBSlxY9qcrVMWQ?si=69656a5f194b45a0", 2 , 2, 6);
CALL InsertMedia("10 Hours of Continuous Rain Sounds for Sleeping", "https://open.spotify.com/album/54vGSK50oe08qxz2xXECEC?si=xspMQI-zRJmRcw8gI-ksgQ", 2, 2, 5);
CALL InsertMedia("Deep Ocean Deep Sleep", "https://open.spotify.com/playlist/37i9dQZF1DWXzR2GKEiHgT?si=8159263fb53b4139", 2, 2, 3);
CALL InsertMedia("Whale Sounds", "https://open.spotify.com/playlist/37i9dQZF1DX60xkhEfNtud?si=e5446ee335c84816", 2, 2, 4);
CALL InsertMedia("Deep Sleep", "https://open.spotify.com/playlist/37i9dQZF1DWYcDQ1hSjOpY?si=7227318af1194a0c", 2, 2, 6);
CALL InsertMedia("Lofi Sleep", "https://open.spotify.com/playlist/37i9dQZF1DX2PQDq3PdrHQ?si=4dcd2f9157a44c6e", 2, 2, 6); 


