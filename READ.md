Mail sync is setup using:
- offlineimap3
- notmuch for filtering
- afew to add python tagging / customization to notmuch

Intent is to get this working with some useful generic filters & then add AI over time

May need this to make it work with my office365: https://www.macs.hw.ac.uk/~rs46/posts/2022-01-11-mu4e-oauth.html

Contacs / Cal Sync (doesn't seem to support gmail / o365 very well): https://github.com/pimutils/vdirsyncer

Protonmail: https://github.com/shenxn/protonmail-bridge-docker

Use email keyword header to update search terms / automate taggings

lieer:
cd to directory to store mail
run: gmi --noauth_local_webserver init frederick.lamming@gmail.com
gmi set --replace-slash-with-dot
gmi set --ignore-tags-local new
