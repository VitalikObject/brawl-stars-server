# ObjectBrawl
A first open source Python 3.8 Brawl Stars Server for version 27!
![ScreenShot](https://cdn.discordapp.com/attachments/728556050285985823/765908293385715762/Screenshot_20201014-150540_BS_v27.jpg) 

## Configuration
You can change default name in config.json
(```"default_name": "YOUR_NAME"```)
And you can change the starting resources in config.json

## Client
To connect to your server, you need a custom client. Here the only solution is to use a [pre-made client](https://drive.google.com/file/d/14dR35AJbVfFN83kbMb6GLBHyomHE0hWj/view?usp=sharing).
Just edit the IP in the frida-gadget config (```/lib/armeabi-v7a/libgg.config.so```)
```{"interaction":{"interaction":{"type":"script","path":"libscript.so","on_change":"reload","parameters":{"redirectHost":"YOUR_IP","relocate":true}}}```

### Friendly reminder
The server is in a very early state. Right now, it is NOT recommended to run this on a production environment. Please not open issues about missing features, i'm well aware of this. 

#### Need help? Join [Huza's Discord channel](https://discord.gg/VPWMxWm) or [Antz's Discord channel](https://discord.com/invite/RgYcF3b)
