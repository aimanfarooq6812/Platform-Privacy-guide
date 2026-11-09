"""
Content for Trapdoor — the privacy and account control guide.

Each platform:
    slug    -> used for the sidebar anchor link (#instagram)
    groups  -> sections shown inside the platform dropdown
    items   -> one dropdown each: what it does (1 line) + how to get there

`how` is a list of routes. Write a route as "Step → Step → Step" using the
arrow character (→, not ->). Add a device or context label with a pipe:
    "On iPhone|Settings → Support → ...".

LAST_REVIEWED is shown at the bottom of the page. Update it whenever you do
a pass over these paths.
"""

LAST_REVIEWED = "November 2026"

PLATFORMS = [
    # ------------------------------------------------------------------ #
    {
        "name": "Instagram",
        "slug": "instagram",
        "section": "Social media & messaging",
        "groups": [
            {
                "title": "Leaving the app",
                "items": [
                    {
                        "name": "Log out",
                        "tag": "This device",
                        "what": "Signs you out on this device only — your account and posts stay exactly as they are.",
                        "how": ["Profile picture (bottom right) → menu (top right) → scroll down → Log out"],
                    },
                    {
                        "name": "Deactivate account",
                        "tag": "Reversible",
                        "what": "Hides your profile, photos and comments from everyone until you log back in.",
                        "how": [
                            "If you see Personal details|Settings and privacy → Accounts Centre → Personal details → Account ownership and control → Deactivation or deletion → pick your account → Deactivate account → confirm with password",
                            "If you see Manage accounts|Settings and privacy → Accounts Centre → Manage accounts → Manage next to your profile → Deactivation or deletion → pick your account → Deactivate account → confirm with password",
                            "On the web|More (left sidebar) → Settings → Accounts Centre → Personal details → Account ownership and control → Deactivation or deletion → pick your account → Deactivate account",
                        ],
                        "note": "Meta has shipped more than one version of this menu, so check which one your screen shows. No time limit on staying deactivated, but Instagram only lets you deactivate once every 7 days.",
                    },
                    {
                        "name": "Delete account",
                        "tag": "Permanent",
                        "what": "Erases your profile, photos, videos, comments, likes and followers for good.",
                        "how": [
                            "Same path as Deactivate → Delete account → pick a reason → enter password → confirm"
                        ],
                        "note": "Usually 30 days to change your mind, though Meta says the exact window varies by region. Logging back in during it cancels the deletion. Download your data first — the export tool stops working once deletion starts. Deleting Instagram can affect any Facebook logins linked through Accounts Centre.",
                    },
                ],
            },
            {
                "title": "Core privacy settings",
                "items": [
                    {
                        "name": "Private account",
                        "what": "Only followers you approve can see your posts, photos and stories.",
                        "how": ["Settings and privacy → Account privacy → turn on Private account"],
                    },
                    {
                        "name": "Activity status",
                        "what": "Hides the green dot and the 'last active' label from people you follow or message.",
                        "how": ["Settings and privacy → Messages and story replies → turn off Show activity status"],
                    },
                ],
            },
            {
                "title": "Hidden settings",
                "items": [
                    {
                        "name": "Restrict someone",
                        "what": "Limits a person without blocking them — their comments only show to them, and they are never told.",
                        "how": ["Their profile → options (three dots) → Restrict"],
                    },
                    {
                        "name": "Hide story from",
                        "what": "Stops chosen people seeing your stories without blocking them from your profile.",
                        "how": ["Settings and privacy → Story → Hide story from → pick people"],
                    },
                    {
                        "name": "Limits",
                        "what": "Automatically hides comments and DM requests from accounts that don't follow you.",
                        "how": ["Settings and privacy → Limited interactions → turn on"],
                        "note": "Built for a wave of harassment, when blocking people one by one isn't fast enough.",
                    },
                    {
                        "name": "Manual tag approval",
                        "what": "Photos you're tagged in only reach your profile once you approve them.",
                        "how": ["Settings and privacy → Tags and mentions → Manually approve tags"],
                    },
                    {
                        "name": "Mute without unfollowing",
                        "what": "Stops someone's posts or stories reaching your feed without unfollowing or telling them.",
                        "how": ["Their profile → options (three dots) → Mute"],
                    },
                    {
                        "name": "Who can message and add you to groups",
                        "what": "Stops strangers starting a DM thread or pulling you into a group chat.",
                        "how": ["Settings and privacy → Messages and story replies → set each category"],
                    },
                    {
                        "name": "Activity from other businesses",
                        "tag": "Replaced",
                        "what": "Controls whether information other websites and apps share with Meta is used to personalise your ads, Feed and Meta AI answers.",
                        "how": ["Settings and privacy → Accounts Centre → Ad preferences → Activity from other businesses"],
                        "note": "Meta retired the older 'Your activity off Meta technologies' switch from July 2026 in the US and several other countries. The new one limits how the data is used, not whether Meta receives it. Same setting as on Facebook — see there for details.",
                    },
                ],
            },
        ],
    },
    # ------------------------------------------------------------------ #
    {
        "name": "Facebook",
        "slug": "facebook",
        "section": "Social media & messaging",
        "groups": [
            {
                "title": "Leaving the app",
                "items": [
                    {
                        "name": "Log out",
                        "tag": "This device",
                        "what": "Signs you out on this device only.",
                        "how": ["Menu → scroll to the bottom → Log out"],
                    },
                    {
                        "name": "Deactivate account",
                        "tag": "Reversible",
                        "what": "Hides your profile and content from everyone while keeping all your data intact.",
                        "how": [
                            "Settings & privacy → Settings → See more in Accounts Centre → Personal details → Account ownership and control → Deactivation or deletion → pick account → Deactivate account",
                            "If you don't see Accounts Centre|Settings & privacy → Settings → Your Facebook information → Deactivation and deletion → Deactivate account",
                        ],
                        "note": "Logging back in reactivates you instantly. Messenger stays active when you deactivate Facebook — deactivate it separately from the Messenger app if you want both gone. If your Accounts Centre shows Manage accounts instead of Personal details, go through that and then Deactivation or deletion.",
                    },
                    {
                        "name": "Delete account",
                        "tag": "Permanent",
                        "what": "Removes your profile and data for good.",
                        "how": ["Same path as Deactivate → Delete account → confirm"],
                        "note": "30-day grace period — don't log back in if you want the deletion to stick. Download your information first from Accounts Centre → Your information and permissions → Export your information.",
                    },
                ],
            },
            {
                "title": "Core privacy settings",
                "items": [
                    {
                        "name": "Active status",
                        "what": "Hides the indicator that tells friends when you're online on Facebook or Messenger.",
                        "how": ["Settings & privacy → Settings → Active Status → turn off"],
                    },
                    {
                        "name": "Who can see your posts",
                        "what": "Sets the default audience — Public, Friends or Only me — for everything you post from now on.",
                        "how": ["Settings & privacy → Settings → Privacy"],
                    },
                ],
            },
            {
                "title": "Hidden settings",
                "items": [
                    {
                        "name": "Limit past posts",
                        "what": "Turns every public post you've ever made into Friends-only in one click.",
                        "how": ["Settings & privacy → Privacy → Limit who can see your past posts"],
                    },
                    {
                        "name": "Activity from other businesses",
                        "tag": "Replaced",
                        "what": "Controls whether information other websites and apps share with Meta is used to personalise your ads, Feed and Meta AI answers.",
                        "how": ["Settings & privacy → Settings → Accounts Centre → Ad preferences → Activity from other businesses"],
                        "note": "This replaces 'Your activity off Meta technologies' (originally Off-Facebook Activity), which Meta retired from July 2026 in the US and a number of other countries, with more to follow. The new switch only limits how the data is used — it doesn't stop Meta receiving it — and that data now also shapes your Feed and Meta AI, not just ads. Meta's announcement didn't give the exact menu path; this setting was formerly called 'Activity information from ad partners', so look under Ad preferences. In countries where the rollout hasn't reached yet you may still see the old setting under Accounts Centre → Your information and permissions.",
                    },
                    {
                        "name": "Profile and tagging review",
                        "what": "Lets you approve tags and posts before they appear on your timeline.",
                        "how": ["Settings & privacy → Privacy → Profile and tagging"],
                    },
                    {
                        "name": "Ad preferences",
                        "what": "Shows the interest categories advertisers use to target you, and lets you delete them.",
                        "how": ["Settings & privacy → Settings → Accounts Centre → Ad preferences"],
                        "note": "Ad controls have moved into Accounts Centre, so the old Settings → Ads route may no longer be there.",
                    },
                    {
                        "name": "Location history",
                        "what": "Clears and switches off the running log of places you've been that the app keeps.",
                        "how": ["Settings → Location → Location History"],
                    },
                ],
            },
        ],
    },
    # ------------------------------------------------------------------ #
    {
        "name": "Snapchat",
        "slug": "snapchat",
        "section": "Social media & messaging",
        "groups": [
            {
                "title": "Leaving the app",
                "items": [
                    {
                        "name": "Log out",
                        "tag": "This device",
                        "what": "Signs you out on this device only.",
                        "how": ["Profile (top left) → gear icon → scroll down → Log out"],
                    },
                    {
                        "name": "Deactivate account",
                        "tag": "Reversible",
                        "what": "There's no separate pause button — starting deletion triggers a 30-day hold that works the same way.",
                        "how": ["Use the Delete account steps — the hold starts automatically"],
                        "note": "The hold is longer in some regions. Log back in during the window to restore everything.",
                    },
                    {
                        "name": "Delete account",
                        "tag": "Permanent",
                        "what": "Erases your profile, Snap Map presence and account data.",
                        "how": [
                            "In the app|Profile (top left) → gear icon → scroll to Account Actions → Delete Account → re-enter your details → confirm",
                            "On the web|accounts.snapchat.com → log in → Delete My Account → re-enter your details → confirm",
                            "If you don't see Account Actions|Settings (gear) → Support → I Need Help → My Account & Security → Account Information → Delete My Account",
                        ],
                        "note": "Snapchat now offers deletion straight from the app's settings on iPhone and Android, not just the web portal. Save your Memories and download your data first (Settings → Privacy Controls → My Data, or My Data on accounts.snapchat.com). There's no instant deletion — everything goes after the 30-day hold.",
                    },
                ],
            },
            {
                "title": "Core privacy settings",
                "items": [
                    {
                        "name": "Ghost Mode",
                        "what": "Removes your avatar from the Snap Map so no other user can see where you are.",
                        "how": ["Snap Map → gear icon (top right of the map) → turn on Ghost Mode → choose 3 hours, 24 hours or Until Turned Off"],
                        "note": "Ghost Mode hides your location from other users on the Map. Snaps you submit to Snap Map can still show up there.",
                    },
                    {
                        "name": "Who can contact you",
                        "what": "Limits who can send you snaps and chats to friends only, instead of everyone.",
                        "how": ["Settings → Privacy Controls → Contact Me → My Friends"],
                        "note": "The choices are friends only, or friends plus your phone contacts. People who aren't friends can only message you if they're 18 or over.",
                    },
                ],
            },
            {
                "title": "Hidden settings",
                "items": [
                    {
                        "name": "Custom location sharing",
                        "what": "Shares your location with a chosen few friends instead of everyone or no one.",
                        "how": ["Snap Map → gear icon → See My Location → My Friends, Except… or Only These Friends"],
                    },
                    {
                        "name": "See me in Quick Add",
                        "what": "Stops your profile being suggested to other people as a friend recommendation.",
                        "how": ["Settings → Privacy Controls → See Me in Quick Add → turn off"],
                    },
                    {
                        "name": "Hide story from",
                        "what": "Blocks specific people from seeing your story without unfriending them.",
                        "how": ["Settings → Privacy Controls → View My Story → Custom → pick who to block"],
                    },
                    {
                        "name": "Contact syncing",
                        "what": "Stops Snapchat matching your phone contacts against its user database to suggest friends.",
                        "how": ["Settings → Contacts → turn off syncing"],
                    },
                    {
                        "name": "My AI data",
                        "what": "Clears what Snapchat's built-in chatbot has stored from your conversations with it.",
                        "how": ["Settings → Privacy Controls → Clear Data → Clear My AI Data"],
                    },
                ],
            },
        ],
    },
    # ------------------------------------------------------------------ #
    {
        "name": "Discord",
        "slug": "discord",
        "section": "Social media & messaging",
        "groups": [
            {
                "title": "Leaving the app",
                "items": [
                    {
                        "name": "Log out",
                        "tag": "This device",
                        "what": "Signs you out on this device only.",
                        "how": ["User Settings (gear, bottom left) → scroll to the bottom → Log out"],
                    },
                    {
                        "name": "Disable account",
                        "tag": "Reversible",
                        "what": "Discord's version of deactivating — removes your account from view without deleting anything.",
                        "how": ["User Settings → Account → scroll to the bottom → Disable Account"],
                        "note": "Discord's help pages still call the Account page 'My Account'.",
                    },
                    {
                        "name": "Delete account",
                        "tag": "Permanent",
                        "what": "Wipes your account for good.",
                        "how": [
                            "User Settings → Account → scroll to the bottom → Delete Account → enter password and 2FA code → confirm"
                        ],
                        "note": "Hand over or delete any servers you own first, or Discord won't let you continue. Your messages stay visible in servers, relabelled 'Deleted User' — delete anything you want gone before you go. Takes about 14 days, and logging in cancels it. If you want a copy of your data, request it first: the package can take up to 30 days, and the request is cancelled if you disable or delete the account before it arrives. Discord may also delete accounts left inactive for two years.",
                    },
                ],
            },
            {
                "title": "Core privacy settings",
                "items": [
                    {
                        "name": "DM restrictions",
                        "what": "Decides whether people who share a server with you, but aren't friends, can message you.",
                        "how": ["User Settings → Content & Social (previously Privacy & Safety) → turn off direct messages from server members"],
                    },
                    {
                        "name": "Activity privacy",
                        "what": "Hides the games, music and apps you're using from friends and server members.",
                        "how": ["User Settings → Activity Privacy → turn off globally, or limit it per server"],
                    },
                ],
            },
            {
                "title": "Hidden settings",
                "items": [
                    {
                        "name": "Data & privacy toggles",
                        "what": "Separate switches for using your data to improve Discord, personalising sponsored content (from your Discord activity and from third-party data), and voice recording in Clips.",
                        "how": [
                            "User Settings → Data & Privacy",
                            "On mobile|You tab → gear icon → Data & Privacy, plus Clips for the voice recording switch",
                        ],
                        "note": "Most of these are on by default.",
                    },
                    {
                        "name": "Message content on web pages",
                        "tag": "New",
                        "what": "Stops new messages you send in Discoverable server channels appearing on Discord's public Server Web Pages and in search results.",
                        "how": ["User Settings → Data & Privacy → turn off 'Show my message content from Discoverable channels on web pages'"],
                        "note": "Only affects messages you send after switching it off — delete older ones to remove them from public pages. If it's missing from the mobile app, use the desktop app or discord.com/settings/data-and-privacy. It applies to your whole account.",
                    },
                    {
                        "name": "Safe direct messaging",
                        "what": "Scans incoming DMs for explicit images before you have to look at them.",
                        "how": ["User Settings → Content & Social → Sensitive content filters"],
                    },
                    {
                        "name": "Who can add you as a friend",
                        "what": "Limits friend requests to everyone, friends of friends, server members or no one.",
                        "how": ["User Settings → Content & Social → Friend Requests"],
                    },
                    {
                        "name": "Request your data",
                        "what": "Downloads a full archive of everything Discord has stored about you.",
                        "how": ["User Settings → Data & Privacy → Request Data"],
                        "note": "Discord says the package can take up to 30 days to arrive.",
                    },
                    {
                        "name": "Ignore someone",
                        "what": "A quieter alternative to blocking — you stop seeing them, and they aren't told.",
                        "how": ["Their profile → options (three dots) → Ignore"],
                    },
                ],
            },
        ],
    },
    # ------------------------------------------------------------------ #
    {
        "name": "TikTok",
        "slug": "tiktok",
        "section": "Social media & messaging",
        "groups": [
            {
                "title": "Leaving the app",
                "items": [
                    {
                        "name": "Log out",
                        "tag": "This device",
                        "what": "Signs you out on this device only.",
                        "how": ["Profile → menu (top right) → Settings and privacy → scroll down → Log out"],
                    },
                    {
                        "name": "Deactivate account",
                        "tag": "Reversible",
                        "what": "There's no separate pause — asking to delete puts your account into a reversible 30-day hold.",
                        "how": ["Use the Delete account steps — the hold starts automatically"],
                    },
                    {
                        "name": "Delete account",
                        "tag": "Permanent",
                        "what": "Erases your profile, videos and data.",
                        "how": [
                            "Settings and privacy → Account → Deactivate or delete account → follow the prompts and verify with your password or a code"
                        ],
                        "note": "30 days before it's final — logging in cancels it. Download your data first (see below).",
                    },
                ],
            },
            {
                "title": "Core privacy settings",
                "items": [
                    {
                        "name": "Private account",
                        "what": "Only followers you approve can see your videos.",
                        "how": ["Settings and privacy → Privacy → turn on Private account"],
                    },
                    {
                        "name": "Comment, duet, stitch and DM controls",
                        "what": "Separately decides who can comment on, duet, stitch or message you.",
                        "how": ["Settings and privacy → Privacy → set each one"],
                    },
                ],
            },
            {
                "title": "Hidden settings",
                "items": [
                    {
                        "name": "Comment keyword filters",
                        "what": "Hides comments containing words you choose — up to 100 — before you ever see them.",
                        "how": ["Settings and privacy → Privacy → Comments → Filter keywords"],
                    },
                    {
                        "name": "Reuse of content",
                        "what": "Stops other people adding your posts to their Stories or reusing your sounds and clips.",
                        "how": ["Settings and privacy → Privacy → Reuse of content"],
                        "note": "Only appears if your account is public — a private account blocks this by default.",
                    },
                    {
                        "name": "Video downloads",
                        "what": "Stops anyone saving your videos to their phone from the share menu.",
                        "how": ["Settings and privacy → Privacy → Downloads → turn off"],
                    },
                    {
                        "name": "Profile view history",
                        "what": "Shows who viewed your profile, but only people who also turned this on themselves.",
                        "how": ["Settings and privacy → Privacy → Profile view history"],
                    },
                    {
                        "name": "Suggest your account to others",
                        "what": "Stops TikTok recommending you to people who have your number or synced contacts.",
                        "how": ["Settings and privacy → Privacy → Suggest your account to others → turn off"],
                    },
                    {
                        "name": "Personalisation and data",
                        "what": "Turns off ad personalisation and resets what the algorithm has learned about you.",
                        "how": ["Settings and privacy → Privacy → Personalisation and data"],
                    },
                    {
                        "name": "Download your data",
                        "what": "Saves a copy of your videos and account information before you delete or leave.",
                        "how": ["Settings and privacy → Account → Download your data → Request data"],
                    },
                    {
                        "name": "Restricted mode",
                        "what": "Filters mature and sensitive content out of your feed.",
                        "how": ["Settings and privacy → Content preferences → Restricted Mode"],
                    },
                ],
            },
        ],
    },
    # ------------------------------------------------------------------ #
    {
        "name": "X (Twitter)",
        "slug": "x-twitter",
        "section": "Social media & messaging",
        "groups": [
            {
                "title": "Leaving the app",
                "items": [
                    {
                        "name": "Log out",
                        "tag": "This device",
                        "what": "Signs you out on this device only.",
                        "how": ["Profile icon → More → Log out"],
                    },
                    {
                        "name": "Deactivate account",
                        "tag": "Reversible",
                        "what": "Hides your profile, posts and followers from public view — nothing is erased yet.",
                        "how": ["Settings and privacy → Your Account → Deactivate your account → confirm with password"],
                        "note": "On X, deactivating is also the first step of deleting.",
                    },
                    {
                        "name": "Delete account",
                        "tag": "Permanent",
                        "what": "There's no delete button — stay logged out for 30 days after deactivating and X erases everything.",
                        "how": ["Deactivate → don't log back in for 30 days"],
                        "note": "Logging in at any point in those 30 days cancels the deletion and restores the account.",
                    },
                ],
            },
            {
                "title": "Core privacy settings",
                "items": [
                    {
                        "name": "Protect your posts",
                        "what": "Makes your account private so only approved followers see your posts.",
                        "how": ["Settings and privacy → Privacy and safety → Audience, media and tagging → Protect your posts"],
                    },
                ],
            },
            {
                "title": "Hidden settings",
                "items": [
                    {
                        "name": "Discoverability and contacts",
                        "what": "Decides whether people who have your phone number or email can find your account.",
                        "how": ["Settings and privacy → Privacy and safety → Discoverability and contacts"],
                    },
                    {
                        "name": "Apps and sessions",
                        "what": "Lists every third-party app and active login so you can revoke ones you don't recognise.",
                        "how": ["Settings and privacy → Security and account access → Apps and sessions"],
                    },
                    {
                        "name": "Muted words",
                        "what": "Hides posts and notifications containing words you choose, without unfollowing anyone.",
                        "how": ["Settings and privacy → Privacy and safety → Mute and block → Muted words"],
                    },
                    {
                        "name": "Direct message requests filter",
                        "what": "Limits DMs to people you already follow.",
                        "how": ["Settings and privacy → Privacy and safety → Direct Messages"],
                    },
                    {
                        "name": "Photo tagging",
                        "what": "Stops strangers tagging you in photos, which pushes your account into their replies.",
                        "how": ["Settings and privacy → Privacy and safety → Audience, media and tagging → Photo tagging"],
                    },
                    {
                        "name": "Grok and third-party data sharing",
                        "tag": "Renamed",
                        "what": "Stops your posts and activity being used to train X's AI model, Grok, and being shared with outside collaborators and ad partners.",
                        "how": [
                            "Settings and privacy → Privacy and safety → Data sharing and personalisation → Grok & Third-party Collaborators → turn off",
                            "On mobile|Profile icon → Settings and Support → Settings and privacy → Privacy and safety → Data sharing and personalisation → Grok & Third-party Collaborators",
                            "For ad partners|Settings and privacy → Privacy and safety → Data sharing and personalisation → Data sharing with business partners",
                        ],
                        "note": "Older guides say this switch is desktop-only; recent ones show it in the app too, so try the app first and fall back to x.com in a browser. It only affects future use. The standalone Grok app has its own separate 'Improve the model' setting, and xAI's Privacy Portal handles requests about data already collected.",
                    },
                ],
            },
        ],
    },
    # ------------------------------------------------------------------ #
    {
        "name": "WhatsApp",
        "slug": "whatsapp",
        "section": "Social media & messaging",
        "groups": [
            {
                "title": "Leaving the app",
                "items": [
                    {
                        "name": "Log out",
                        "tag": "Web only",
                        "what": "The mobile app has no logout — it's tied to your phone number. You can only sign out of Web or Desktop.",
                        "how": [
                            "On Web or Desktop|Menu → Log out",
                            "On mobile|Settings → Linked Devices → manage active sessions",
                        ],
                    },
                    {
                        "name": "Deactivate account",
                        "tag": "Reversible",
                        "what": "There's no deactivation — uninstalling pauses your presence while messages queue up for your return.",
                        "how": ["Uninstall the app — your account stays live on WhatsApp's servers"],
                    },
                    {
                        "name": "Delete account",
                        "tag": "Permanent",
                        "what": "Immediately removes your profile, chat history and payment records.",
                        "how": ["Settings → Account → Delete my account → confirm your phone number"],
                        "note": "Data can sit on Meta's backend for up to 90 days, and messages you sent stay in other people's chats.",
                    },
                ],
            },
            {
                "title": "Core privacy settings",
                "items": [
                    {
                        "name": "Last seen and online",
                        "what": "Decides who can see when you were last active, or whether you're online right now.",
                        "how": ["Settings → Privacy → Last seen and online → Everyone, My contacts or Nobody"],
                    },
                    {
                        "name": "Profile photo and About visibility",
                        "what": "Decides who can see your profile picture and your About text.",
                        "how": ["Settings → Privacy"],
                    },
                    {
                        "name": "Two-step verification",
                        "what": "A six-digit PIN needed to register your number on a new device — the single best defence against a stolen account.",
                        "how": ["Settings → Account → Two-step verification → Turn on → set a PIN and add your email"],
                        "note": "Nobody will ever legitimately ask you for this PIN or for the code WhatsApp texts you. That request is always a scam.",
                    },
                ],
            },
            {
                "title": "Hidden settings",
                "items": [
                    {
                        "name": "Advanced Chat Privacy",
                        "what": "Per-chat switch that blocks others exporting the chat, auto-saving its media, and using the messages for AI features.",
                        "how": ["Open the chat → tap the chat or group name → Advanced Chat Privacy → turn on"],
                        "note": "Added in 2025 and expanded since. It does not stop screenshots, and in a group any admin can switch it back off.",
                    },
                    {
                        "name": "Strict account settings",
                        "what": "A lockdown mode that blocks media and attachments from people outside your contacts, turns off link previews, silences unknown callers, switches on two-step verification and lets only your contacts add you to groups.",
                        "how": ["Settings → Privacy → Advanced → turn on Strict account settings"],
                        "note": "Launched in January 2026 for people at higher risk of targeted attacks. It can only be switched on or off from your phone, not WhatsApp Web, and it trades some convenience for a much smaller attack surface.",
                    },
                    {
                        "name": "Username and username key",
                        "tag": "Rolling out",
                        "what": "Lets people reach you by username instead of your phone number, with an optional key so only people who have both can start a chat.",
                        "how": ["Settings → Account → Username"],
                        "note": "Username reservations opened in late June 2026 and the wider rollout is gradual, so it may not have reached your account yet. If you have Facebook or Instagram you can reuse the same username. WhatsApp also now limits how many new people one account can contact, as a guard against spam accounts.",
                    },
                    {
                        "name": "Chat lock",
                        "what": "Puts one chat behind a fingerprint, Face ID or PIN and keeps it out of notification previews.",
                        "how": ["Open the chat → tap the contact's name → Chat Lock"],
                    },
                    {
                        "name": "Protect IP address in calls",
                        "what": "Routes calls through WhatsApp's servers so the other person can't see your IP or rough location.",
                        "how": ["Settings → Privacy → Advanced → Protect IP address in calls"],
                    },
                    {
                        "name": "Silence unknown callers",
                        "what": "Stops calls from numbers not in your contacts from ringing — they still appear in your call list.",
                        "how": ["Settings → Privacy → Calls → Silence unknown callers"],
                    },
                    {
                        "name": "Disable link previews",
                        "what": "Stops WhatsApp fetching shared links to build preview cards, which can leak metadata to that site.",
                        "how": ["Settings → Privacy → Advanced → turn off link previews"],
                    },
                    {
                        "name": "Default disappearing messages timer",
                        "what": "Auto-deletes messages in every new chat after 24 hours up to 90 days.",
                        "how": ["Settings → Privacy → Default message timer"],
                    },
                    {
                        "name": "Read receipts",
                        "what": "Stops others seeing when you've read their messages — you also stop seeing theirs.",
                        "how": ["Settings → Privacy → turn off Read receipts"],
                    },
                    {
                        "name": "Who can add you to groups",
                        "what": "Stops strangers pulling you into group chats without asking.",
                        "how": ["Settings → Privacy → Groups → My contacts or My contacts except..."],
                    },
                ],
            },
        ],
    },
    # ------------------------------------------------------------------ #
    {
        "name": "Telegram",
        "slug": "telegram",
        "section": "Social media & messaging",
        "groups": [
            {
                "title": "Leaving the app",
                "items": [
                    {
                        "name": "Log out",
                        "tag": "This device",
                        "what": "Signs you out on this device only.",
                        "how": ["Settings → scroll to the bottom → Log out"],
                    },
                    {
                        "name": "Auto-delete if away",
                        "tag": "Safety net",
                        "what": "Instead of deactivating, Telegram deletes your account after a set stretch of inactivity.",
                        "how": ["Settings → Privacy and Security → Delete my account if away for → 1, 3, 6 or 12 months"],
                        "note": "Telegram's default is 6 months of inactivity.",
                    },
                    {
                        "name": "Delete account",
                        "tag": "Permanent",
                        "what": "Immediately wipes your account, contacts, chats and media from Telegram's cloud.",
                        "how": [
                            "On iPhone|Settings → Privacy and Security → Delete my account → If Away For → Delete Account Now",
                            "On Android|Settings → Telegram FAQ → Delete your Telegram account (opens a web page where you confirm your phone number)",
                        ],
                        "note": "Groups and channels you own pass to the next longest-serving admin unless you delete or transfer them first. The in-app route differs by phone, so if one doesn't match, use the delete page on Telegram's website.",
                    },
                ],
            },
            {
                "title": "Core privacy settings",
                "items": [
                    {
                        "name": "Last seen and phone number",
                        "what": "Decides who can see your online status and your phone number.",
                        "how": ["Settings → Privacy and Security → set each to Nobody or My Contacts"],
                    },
                ],
            },
            {
                "title": "Hidden settings",
                "items": [
                    {
                        "name": "Secret chats",
                        "what": "A fully end-to-end encrypted chat stored only on your devices, with messages that self-destruct.",
                        "how": ["Open a chat → tap the contact's name → Start Secret Chat"],
                        "note": "Normal Telegram chats are not end-to-end encrypted — only secret chats are. Timers run from 2 seconds to 1 week, and messages can't be forwarded.",
                    },
                    {
                        "name": "Who can add me to groups",
                        "what": "Stops strangers pulling you into random group chats without asking.",
                        "how": ["Settings → Privacy and Security → Groups → My Contacts"],
                    },
                    {
                        "name": "Two-step verification",
                        "what": "Adds a password on top of the SMS code, so someone with your SIM still can't get in.",
                        "how": ["Settings → Privacy and Security → Two-Step Verification"],
                    },
                    {
                        "name": "Active sessions",
                        "what": "Shows every device logged into your account and lets you kick off ones you don't recognise.",
                        "how": ["Settings → Devices"],
                    },
                ],
            },
        ],
    },
    # ------------------------------------------------------------------ #
    {
        "name": "Reddit",
        "slug": "reddit",
        "section": "Social media & messaging",
        "groups": [
            {
                "title": "Leaving the app",
                "items": [
                    {
                        "name": "Log out",
                        "tag": "This device",
                        "what": "Ends your current session — your account and data are untouched.",
                        "how": ["Profile icon → Log out"],
                    },
                    {
                        "name": "Deactivate account",
                        "tag": "Not available",
                        "what": "Reddit has no deactivation — logging out is the only reversible pause.",
                        "how": ["Profile icon → Log out"],
                    },
                    {
                        "name": "Delete account",
                        "tag": "Permanent",
                        "what": "Immediate and permanent, with no grace period or undo window.",
                        "how": [
                            "On the web|Avatar → Settings → Account tab → scroll to Advanced → Delete account → confirm with username and password",
                            "On iPhone|Avatar → menu → Settings → Support → Delete account",
                            "On Android|Avatar → menu → Settings → Account settings → Delete account",
                        ],
                        "note": "Your posts and comments stay up as '[deleted]' unless you remove them yourself first. Cancel Reddit Premium separately beforehand — deleting the account doesn't stop billing. If you sign in with Google or Apple, Reddit asks you to create a password first.",
                    },
                ],
            },
            {
                "title": "Core privacy settings",
                "items": [
                    {
                        "name": "Privacy tab",
                        "what": "The central hub for most of Reddit's visibility controls.",
                        "how": ["Settings → Privacy"],
                        "note": "Older versions of the site and app label this tab 'Safety & Privacy'.",
                    },
                ],
            },
            {
                "title": "Hidden settings",
                "items": [
                    {
                        "name": "Content visibility",
                        "what": "Hides your posts and comments from search engines and from logged-out visitors.",
                        "how": ["Settings → Privacy → turn off content visibility"],
                    },
                    {
                        "name": "Allow people to follow you",
                        "what": "Decides whether your posting activity can be followed like a feed.",
                        "how": ["Settings → Privacy → Allow people to follow you"],
                    },
                    {
                        "name": "Active in communities",
                        "what": "Hides which subreddits you're active in from your public profile.",
                        "how": ["Settings → Privacy → turn off Show active communities"],
                    },
                    {
                        "name": "Personalised ads",
                        "what": "Turns off ad targeting based on your browsing and posting.",
                        "how": ["Settings → Privacy → Ad personalisation"],
                    },
                    {
                        "name": "Download your data",
                        "what": "Requests a copy of your account data, or lets you file a formal deletion request.",
                        "how": [
                            "reddit.com/settings/data-request",
                            "Or|Settings → Privacy → Data request",
                        ],
                    },
                ],
            },
        ],
    },
    # ------------------------------------------------------------------ #
    {
        "name": "YouTube",
        "slug": "youtube",
        "section": "Social media & messaging",
        "groups": [
            {
                "title": "Leaving the app",
                "items": [
                    {
                        "name": "Sign out",
                        "tag": "This device",
                        "what": "Signs you out on this device only.",
                        "how": ["Profile picture → Sign out"],
                    },
                    {
                        "name": "Hide your channel",
                        "tag": "Reversible",
                        "what": "YouTube's version of deactivating — your name, videos, likes and subscribers go private.",
                        "how": [
                            "YouTube Studio → Settings (left sidebar) → Channel → Advanced settings → Remove YouTube content → I want to hide my content"
                        ],
                        "note": "You can re-enable the channel later from YouTube Studio.",
                    },
                    {
                        "name": "Delete channel",
                        "tag": "Permanent",
                        "what": "Erases your videos, comments, playlists, messages and watch history.",
                        "how": [
                            "Same path as Hide → I want to permanently delete my content → tick both boxes",
                            "Or|Google Account → Data & Privacy → Delete a Google service → bin icon next to YouTube",
                        ],
                        "note": "Your wider Google Account — Gmail, Drive and the rest — is left alone. Download your videos with Google Takeout first.",
                    },
                ],
            },
            {
                "title": "Core privacy settings",
                "items": [
                    {
                        "name": "Keep subscriptions private",
                        "what": "Hides your subscription list from anyone visiting your channel.",
                        "how": ["YouTube Settings → Privacy"],
                    },
                ],
            },
            {
                "title": "Hidden settings",
                "items": [
                    {
                        "name": "Pause or auto-delete history",
                        "what": "Stops YouTube recording what you watch and search, or clears it every 3, 18 or 36 months.",
                        "how": [
                            "myactivity.google.com/product/youtube",
                            "Or|YouTube Settings → History & privacy",
                        ],
                    },
                    {
                        "name": "Restricted mode",
                        "what": "Filters mature content out of search, recommendations and comments.",
                        "how": ["YouTube Settings → General → Restricted Mode"],
                    },
                    {
                        "name": "Ad personalisation",
                        "what": "Controls whether your activity shapes ads across all of Google, not just YouTube.",
                        "how": [
                            "myadcenter.google.com",
                            "Or|Google Account → Data & Privacy → Ad settings",
                        ],
                    },
                ],
            },
        ],
    },
    # ------------------------------------------------------------------ #
    {
        "name": "LinkedIn",
        "slug": "linkedin",
        "section": "Social media & messaging",
        "groups": [
            {
                "title": "Leaving the app",
                "items": [
                    {
                        "name": "Sign out",
                        "tag": "This device",
                        "what": "Signs you out on this device only.",
                        "how": ["Me icon (top right) → Sign out"],
                    },
                    {
                        "name": "Hibernate account",
                        "tag": "Reversible",
                        "what": "LinkedIn's version of deactivating — hides your profile while keeping connections, messages and posts.",
                        "how": ["Settings & Privacy → Account preferences → Account management → Hibernate account"],
                        "note": "This cancels any Premium subscription straight away — cancel it separately first if you've paid ahead.",
                    },
                    {
                        "name": "Close account",
                        "tag": "Permanent",
                        "what": "Removes your profile, connections, messages, endorsements and recommendations.",
                        "how": [
                            "Settings & Privacy → Account preferences → Account management → Close account → pick a reason → confirm password"
                        ],
                        "note": "Short grace period before it's final — signing back in during it cancels the request. If a current or former employer put you on a Learning licence or Recruiter seat, LinkedIn can block closing until their admin removes it.",
                    },
                ],
            },
            {
                "title": "Core privacy settings",
                "items": [
                    {
                        "name": "Public profile visibility",
                        "what": "Decides whether your profile, or parts of it, is visible outside LinkedIn and to search engines.",
                        "how": ["Settings & Privacy → Visibility → Edit your public profile"],
                    },
                ],
            },
            {
                "title": "Hidden settings",
                "items": [
                    {
                        "name": "Private browsing mode",
                        "what": "Lets you view profiles anonymously — you show up as 'LinkedIn Member'.",
                        "how": ["Settings & Privacy → Visibility → Profile viewing options → Private mode"],
                        "note": "You lose your own 'Who viewed your profile' data unless you have Premium.",
                    },
                    {
                        "name": "Open to work visibility",
                        "what": "Signals availability to recruiters only, rather than to everyone including your employer.",
                        "how": ["Profile → Open to → Finding a new job → Recruiters only"],
                    },
                    {
                        "name": "Data for generative AI training",
                        "what": "Stops LinkedIn using your profile and posts to train its AI models.",
                        "how": ["Settings & Privacy → Data privacy → Data for Generative AI Improvement → turn off"],
                        "note": "This was switched on by default for most accounts when it launched. It only affects future use, and it doesn't appear in every region.",
                    },
                    {
                        "name": "Third-party applications",
                        "what": "Shows every outside app connected to your account so you can revoke access.",
                        "how": ["Settings & Privacy → Data privacy → Other applications → Permitted services"],
                    },
                ],
            },
        ],
    },
    # ------------------------------------------------------------------ #
    {
        "name": "Roblox",
        "slug": "roblox",
        "section": "Social media & messaging",
        "groups": [
            {
                "title": "Leaving the app",
                "items": [
                    {
                        "name": "Log out",
                        "tag": "This device",
                        "what": "Signs you out on this device only.",
                        "how": ["Profile icon → Log out"],
                    },
                    {
                        "name": "Deactivate account",
                        "tag": "Reversible",
                        "what": "Temporarily disables your account — log back in any time to restore it.",
                        "how": [
                            "Settings (gear) → Privacy & content restrictions → Account data, deactivation & deletion → Deactivate",
                            "Older menus|Settings (gear) → Account Info → Account Deactivation and Deletion → Deactivate",
                        ],
                        "note": "Roblox moved these controls under Privacy & content restrictions, so the older Account Info route may be gone from your screen.",
                    },
                    {
                        "name": "Delete account",
                        "tag": "Permanent",
                        "what": "Erases your profile, Robux, items and progress.",
                        "how": [
                            "Settings (gear) → Privacy & content restrictions → Account data, deactivation & deletion → Delete next to Delete Account → follow the prompts",
                            "If you can't use that|Roblox Support contact form → Data Privacy Requests → Right to Be Forgotten",
                            "Older menus|Settings → Account Info → Account Deactivation and Deletion → Delete Account",
                        ],
                        "note": "Needs a verified email, and Roblox checks your identity before it deletes anything. If you used 'Sign in with Roblox' on other sites you may lose access to them. Unlinking a parent account only removes the parent's controls — it doesn't delete the child's account.",
                    },
                ],
            },
            {
                "title": "Core privacy settings",
                "items": [
                    {
                        "name": "Who can chat, join or friend you",
                        "what": "Separately decides who can message you, join your games or send friend requests.",
                        "how": ["Settings → Privacy"],
                        "note": "Chat now depends on an age check, which became mandatory in 2026 — accounts that haven't completed one can't use chat.",
                    },
                    {
                        "name": "Parental controls and PIN",
                        "what": "Locks the privacy settings behind a PIN so they can't be loosened without it.",
                        "how": [
                            "Settings → Parental Controls → Account PIN → turn on",
                            "Linking a child's account|From the child's account: Settings → Parental Controls → Add a parent → accept the request from the parent's email",
                        ],
                        "note": "Roblox introduced age-based accounts in 2026 — Kids for under 9s and Select for 9 to 15 — with parental controls running through age 15. Linking a parent account requires the parent to verify their age, and what you see depends on your account's age check and region.",
                    },
                ],
            },
            {
                "title": "Hidden settings",
                "items": [
                    {
                        "name": "Social media link visibility",
                        "what": "Decides whether your other social accounts show on your Roblox profile.",
                        "how": ["Settings → Privacy → Social Networks"],
                    },
                    {
                        "name": "Spatial voice and face tracking",
                        "what": "Turns off voice chat and webcam-based avatar face tracking entirely.",
                        "how": ["Settings → Privacy → Voice Chat / Camera"],
                    },
                    {
                        "name": "Trade and inventory privacy",
                        "what": "Decides who can see the items in your inventory and send you trade requests.",
                        "how": ["Settings → Privacy → Trading and inventory"],
                    },
                    {
                        "name": "Content maturity",
                        "what": "Limits which experiences your account can open, by age rating.",
                        "how": ["Settings → Parental Controls → Content Maturity"],
                    },
                ],
            },
        ],
    },
    # ------------------------------------------------------------------ #
    {
        "name": "Wattpad",
        "slug": "wattpad",
        "section": "Social media & messaging",
        "groups": [
            {
                "title": "Leaving the app",
                "items": [
                    {
                        "name": "Log out",
                        "tag": "This device",
                        "what": "Signs you out on this device only.",
                        "how": ["Profile icon → Log out"],
                    },
                    {
                        "name": "Deactivate account",
                        "tag": "Reversible",
                        "what": "Closing your account first hides your profile while your comments stay on the site, anonymised.",
                        "how": ["Profile icon → Settings → Close Account"],
                        "note": "Wattpad labels this button 'Close Account'. Reversible for 6 months just by logging back in — Wattpad uses one button for both steps.",
                    },
                    {
                        "name": "Delete account",
                        "tag": "Permanent",
                        "what": "After 6 months without logging in, your username, stories and library are deleted for good.",
                        "how": [
                            "Happens automatically 6 months after deactivating",
                            "Or sooner|contact Wattpad support with a data deletion request",
                        ],
                        "note": "Back up or unpublish your stories first — Wattpad won't do it for you and nothing is recoverable.",
                    },
                ],
            },
            {
                "title": "Core privacy settings",
                "items": [
                    {
                        "name": "Story visibility and mature content",
                        "what": "Sets whether your stories are public or unlisted, and filters mature content in your feed.",
                        "how": ["Settings → Privacy Settings"],
                    },
                ],
            },
            {
                "title": "Hidden settings",
                "items": [
                    {
                        "name": "Who can message or comment",
                        "what": "Limits who can contact you or comment on your stories.",
                        "how": ["Settings → Privacy Settings"],
                    },
                    {
                        "name": "Reading list visibility",
                        "what": "Hides what you're reading or have bookmarked from people viewing your profile.",
                        "how": ["Settings → Privacy Settings"],
                    },
                    {
                        "name": "Block specific users",
                        "what": "Stops one person viewing your profile, following you or commenting on your stories.",
                        "how": ["Their profile → Block"],
                    },
                ],
            },
        ],
    },
    # ------------------------------------------------------------------ #
    {
        "name": "ChatGPT",
        "slug": "chatgpt",
        "section": "AI tools",
        "groups": [
            {
                "title": "Leaving the app",
                "items": [
                    {
                        "name": "Log out",
                        "tag": "This device",
                        "what": "Signs you out on this device only.",
                        "how": ["Profile icon → Log out"],
                    },
                    {
                        "name": "Delete account",
                        "tag": "Permanent",
                        "what": "Deletes your account and the conversation data attached to it.",
                        "how": [
                            "Settings → Data Controls → Delete account",
                            "Or|submit a request through OpenAI's Privacy Portal",
                        ],
                        "note": "Deletion is processed within about 30 days, subject to legal retention exceptions.",
                    },
                ],
            },
            {
                "title": "Core privacy settings",
                "items": [
                    {
                        "name": "Stop chats training future models",
                        "what": "Keeps your conversations out of future model training — it can't undo training that already happened.",
                        "how": [
                            "Settings → Data Controls → turn off 'Improve the model for everyone'"
                        ],
                        "note": "Applies to your whole account, on every device, and doesn't delete or hide your saved chats. Business, Enterprise, Edu and API accounts are already excluded by default.",
                    },
                ],
            },
            {
                "title": "Hidden settings",
                "items": [
                    {
                        "name": "Ads controls",
                        "tag": "New",
                        "what": "On the Free and Go plans, decides whether ChatGPT uses your past chats, memory and ads history to pick the ads you see.",
                        "how": ["Settings → Ads controls → turn off Personalize ads"],
                        "note": "Turning personalisation off does not remove ads — they just rely on your current chat instead. It's a separate switch from the training one above, so you can have either on without the other. You can also view and delete your ads history here. Plus, Pro, Business, Enterprise and Edu plans don't show ads, and ad availability varies by country.",
                    },
                    {
                        "name": "Temporary chat",
                        "what": "A chat that never saves to your history, never creates or updates memories, and is never used for training.",
                        "how": ["New chat → Temporary Chat icon (top right)"],
                        "note": "Before you start you can choose whether the chat is personalised, meaning it may use your existing memories and custom instructions. Treat it as 'not saved and not trained on', not as private — OpenAI still holds it for about 30 days for abuse monitoring.",
                    },
                    {
                        "name": "Memory",
                        "what": "Controls whether ChatGPT remembers things about you and draws on your past chats, files and connected apps to personalise replies.",
                        "how": [
                            "Settings → Personalization → Memory → turn Enable memory off (some versions show separate switches for saved memories and chat history)",
                            "To see what it holds|Settings → Personalization → Memory summary → Manage",
                        ],
                        "note": "Deleting a conversation does not delete the memory it created — you have to clear the memory itself. Memory and model training are independent switches.",
                    },
                    {
                        "name": "Review your shared links",
                        "what": "Any conversation you've ever hit Share on has a live public URL until you revoke it.",
                        "how": ["Settings → Data Controls → Shared links → delete the ones you don't need"],
                    },
                    {
                        "name": "Audit connected apps",
                        "what": "Shows which outside services ChatGPT can read from, and lets you disconnect them.",
                        "how": ["Settings → Connected apps"],
                    },
                ],
            },
        ],
    },
    # ------------------------------------------------------------------ #
    {
        "name": "Google Gemini",
        "slug": "gemini",
        "section": "AI tools",
        "groups": [
            {
                "title": "Leaving the app",
                "items": [
                    {
                        "name": "Log out",
                        "tag": "Google Account",
                        "what": "There's no separate Gemini login — signing out of your Google Account signs you out everywhere.",
                        "how": ["Google Account → Sign out"],
                    },
                    {
                        "name": "Delete your Gemini data",
                        "tag": "Permanent",
                        "what": "There's no Gemini account to delete, so removal means wiping its stored data and switching the assistant off.",
                        "how": [
                            "myactivity.google.com/product/gemini → delete all activity → turn off Keep Activity → optionally disable the Gemini app on your device"
                        ],
                    },
                ],
            },
            {
                "title": "Core privacy settings",
                "items": [
                    {
                        "name": "Keep Activity",
                        "what": "Decides whether your Gemini conversations are saved to your account and used to improve Google's models.",
                        "how": [
                            "myactivity.google.com/product/gemini",
                            "On the web|gemini.google.com → Settings & help → Activity → Keep Activity → Turn off",
                            "In the app|Gemini app → menu → profile picture → Gemini Apps Activity → Keep Activity → Turn off",
                        ],
                        "note": "Formerly called Gemini Apps Activity. While it's on, a sample of your uploads, such as files and photos, can be used to improve Google services. Google may still hold data for around 72 hours to run the service, even with this off.",
                    },
                ],
            },
            {
                "title": "Hidden settings",
                "items": [
                    {
                        "name": "Temporary Chat",
                        "what": "A chat that doesn't appear in your recent chats or Activity and isn't used to train Google's models.",
                        "how": ["Gemini app → start a new chat → Temporary chat"],
                        "note": "Temporary chats are kept for 72 hours so you can pick the thread back up, then deleted.",
                    },
                    {
                        "name": "Past chats as personal context",
                        "what": "Lets Gemini draw on your earlier conversations to personalise its answers.",
                        "how": ["Gemini app → Settings → Personal context → Your past chats with Gemini"],
                    },
                    {
                        "name": "Files & data",
                        "what": "Lists every file you've ever attached to a Gemini prompt so you can delete them one by one.",
                        "how": ["myactivity.google.com/product/gemini → Files & data"],
                        "note": "Web only — this isn't in the mobile app.",
                    },
                    {
                        "name": "App permissions",
                        "what": "Decides which apps — Gmail, Calendar, Maps, Messages — Gemini can read from and act on.",
                        "how": ["Gemini app → Settings → Apps → turn off each connected app"],
                    },
                    {
                        "name": "Auto-delete activity",
                        "what": "Clears saved Gemini activity older than 3, 18 or 36 months instead of keeping it forever.",
                        "how": ["myactivity.google.com/product/gemini → Auto-delete"],
                    },
                ],
            },
        ],
    },
    # ------------------------------------------------------------------ #
    {
        "name": "Meta AI",
        "slug": "meta-ai",
        "section": "AI tools",
        "groups": [
            {
                "title": "Leaving the app",
                "items": [
                    {
                        "name": "Log out",
                        "tag": "No separate account",
                        "what": "Meta AI runs on your Facebook, Instagram or WhatsApp login — there's nothing separate to log out of.",
                        "how": ["Log out of Facebook, Instagram or WhatsApp"],
                    },
                    {
                        "name": "Object to AI training",
                        "tag": "Request",
                        "what": "There's no opt-out toggle — you file a formal objection and Meta reviews it case by case.",
                        "how": ["Facebook → Settings & privacy → Privacy Centre → How Meta uses information for generative AI models and features → Right to object"],
                        "note": "These rights are strongest for users in the EU, UK and Brazil under data-protection law. Elsewhere Meta may refuse.",
                    },
                ],
            },
            {
                "title": "Hidden settings",
                "items": [
                    {
                        "name": "Delete your Meta AI conversations",
                        "what": "Removes Meta's copy of what you've said to Meta AI — deleting the chat from your phone alone does not.",
                        "how": [
                            "In WhatsApp|Open the Meta AI chat → type /reset-ai and send it (use /reset-all-ais to clear every Meta AI chat)",
                            "In the Meta AI app|Menu → Settings → Data and privacy → Manage your information → delete your chats and media",
                        ],
                    },
                    {
                        "name": "Stop others sharing your chats with Meta AI",
                        "what": "Stops people in a Messenger chat sharing your messages with Meta AI.",
                        "how": ["Messenger → open the chat → Information → Privacy and support → Message permissions → turn off Allow message sharing"],
                    },
                    {
                        "name": "Third-party info objection",
                        "what": "A separate objection covering data Meta bought or collected about you from outside sources.",
                        "how": ["Facebook Privacy Centre → search 'Generative AI Data Subject Rights'"],
                        "note": "Since mid-2026 Meta also uses data other businesses share with it to personalise Meta AI answers. The 'Activity from other businesses' switch (see Facebook) is the control for that.",
                    },
                    {
                        "name": "Mute Meta AI",
                        "what": "Stops Meta AI appearing and notifying you inside the apps, without a full opt-out.",
                        "how": ["Mute the Meta AI chat thread the way you'd mute any contact"],
                        "note": "There's no setting that removes Meta AI from Facebook, Instagram or WhatsApp. Muting and not starting chats is as close as it gets.",
                    },
                ],
            },
        ],
    },
    # ------------------------------------------------------------------ #
    {
        "name": "Claude",
        "slug": "claude",
        "section": "AI tools",
        "groups": [
            {
                "title": "Leaving the app",
                "items": [
                    {
                        "name": "Log out",
                        "tag": "This device",
                        "what": "Signs you out on this device only.",
                        "how": ["Your name (bottom left) → Log out"],
                    },
                    {
                        "name": "Delete account",
                        "tag": "Permanent",
                        "what": "Deletes your account for good — export anything you want to keep first.",
                        "how": ["Settings → Account → Delete account → confirm"],
                        "note": "If you pay for a plan, cancel the subscription first and wait for the current period to end before deleting.",
                    },
                ],
            },
            {
                "title": "Core privacy settings",
                "items": [
                    {
                        "name": "Stop chats training the model",
                        "what": "Keeps your conversations out of model training.",
                        "how": ["Settings → Privacy → turn off 'Help improve Claude'"],
                        "note": "Only reaches forward — it doesn't undo anything already used. Work, Enterprise, Education and API accounts are already excluded by default.",
                    },
                ],
            },
            {
                "title": "Hidden settings",
                "items": [
                    {
                        "name": "Incognito mode",
                        "what": "Chats that are never used for training and never saved to your history or Claude's memory.",
                        "how": ["New chat → ghost icon (Incognito)"],
                        "note": "Incognito chats are still held for a limited time for safety (30 days, longer if flagged) — not saved to your history is not the same as never stored.",
                    },
                    {
                        "name": "Delete one conversation",
                        "what": "Removes a single chat from your history now, and from Anthropic's systems within 30 days.",
                        "how": ["Chat list → pick a conversation → Delete"],
                    },
                    {
                        "name": "Memory and past chat search",
                        "what": "Controls whether Claude can look back through your earlier conversations for context, and whether it builds memory from them.",
                        "how": ["Settings → Capabilities → turn off search and reference chats and generate memory from chat history"],
                    },
                    {
                        "name": "Review your shared links",
                        "what": "Any chat you've shared has a link that anyone holding it can open until you unshare it.",
                        "how": ["Settings → Privacy → Manage next to Shared links → Unshare"],
                    },
                ],
            },
        ],
    },
]

GENERAL_NOTES = [
    (
        "Deactivate and delete are not the same thing",
        "Deactivating hides your profile but keeps your data and can be undone any time. "
        "Deleting starts a countdown — usually about 30 days — and logging back in during that "
        "window quietly cancels it. That catches out a lot of people who meant to leave for good.",
    ),
    (
        "Turn on two-step verification before anything else",
        "Most stolen accounts are not hacked in any clever way. Someone talks you into forwarding "
        "the six-digit code the app just texted you. A second PIN or passkey stops that cold, and "
        "no company will ever ask you for that code or PIN.",
    ),
    (
        "Opting out of AI training only affects what comes next",
        "Turning training off protects future conversations. Anything already absorbed into a "
        "finished training run stays there — none of these companies have an unlearn button.",
    ),
    (
        "Training, ads and personalisation are separate switches",
        "Turning off AI training doesn't turn off ad personalisation, and the reverse is true too — "
        "ChatGPT and Meta now keep separate controls for each. Turning personalisation off usually "
        "still leaves ads on the screen. It only changes what they're based on.",
    ),
    (
        "EU and UK users have stronger rights",
        "GDPR gives you legally enforceable rights to access, export and delete your data, and to "
        "object to AI training. These requests usually go through a company's Privacy Centre rather "
        "than the normal in-app settings.",
    ),
    (
        "Menus move — check the source if a path fails",
        "Apps rename and relocate these controls every few months, and sometimes show different "
        "menus to different people at the same time. If a path here doesn't match what you see, the "
        "platform's own help centre article is the thing to trust.",
    ),
]
