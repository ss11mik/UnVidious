# UnVidious
### Replace bookmarked Invidious instances links to YouTube

[Invidious](https://invidious.io/) instances come and go and so bookmarked links to videos can become unavailable. This script changes all the links to videos on alternative YouTube frontends (not only Invidious) to the original YouTube domain so that a browser plugin, such as [Invidition](https://gitlab.com/Booteille/Invidition), can choose currently available instance every time.

The script has only one parameter, a JSON file with bookmarks in a format that current Firefox (102) exports.

It basically matches all bookmarks URI with regex `http(s){0,1}://.*/watch\?v=` and replaces the domain part. It also removes parameters "quality" and "listen=0".
