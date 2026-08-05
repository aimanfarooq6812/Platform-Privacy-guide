"""
Content for the Privacy & Account Control guide.

Each platform:
    slug    -> used for the sidebar anchor link (#instagram)
    groups  -> sections shown inside the platform dropdown
    items   -> one dropdown each: what it does (1 line) + how to get there

`how` is a list of routes. Write a route as "Step → Step → Step".
Add a label with a pipe: "On iPhone|Settings → Support → ...".
"""

PLATFORMS = [
    # ------------------------------------------------------------------ #
    {
        "name": "Instagram",
        "emoji": "📸",
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
                        "how": ["Profile picture (bottom right) → ☰ (top right) → scroll down → Log out"],
                    },
                    {
                        "name": "Deactivate account",
                        "tag": "Reversible",
                        "what": "Hides your profile, photos and comments from everyone until you log back in.",
                        "how": [
                            "Settings and privacy → Accounts Centre → Personal details → Account ownership and control → Deactivation or deletion → pick your account → Deactivate account → confirm with password"
                        ],
                        "note": "No time limit — you can stay deactivated as long as you like.",
                    },
                    {
                        "name": "Delete account",
                        "tag": "Permanent",
                        "what": "Erases your profile, photos, videos, comments, likes and followers for good.",
                        "how": [
                            "Same path as Deactivate → Delete account → pick a reason → enter password → confirm"
                        ],
                        "note": "You get 30 days first. Logging back in during that window cancels the deletion.",
                    },
                ],
            },
            {
                "title": "Core privacy settings",
                "items": [
                    {
                        "name": "Private account",
                        "what": "Only followers you approve can see your posts, photos and stories.",
                        "how": ["Settings and privacy → Privacy → turn on Private account"],
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
                        "how": ["Their profile → ⋮ → Restrict"],
                    },
                    {
                        "name": "Active together visibility",
                        "what": "Hides whether you are online inside a shared DM thread, even if your activity status is on.",
                        "how": ["Settings and privacy → Messages and story replies → turn off Active together"],
                    },
                    {
                        "name": "Hide story from",
                        "what": "Stops chosen people seeing your stories without blocking them from your profile.",
                        "how": ["Settings and privacy → Story → Hide story from → pick people"],
                    },
                    {
                        "name": "Limits",
                        "what": "Automatically hides comments and DM requests from accounts that don't follow you.",
                        "how": ["Settings and privacy → Privacy → Limits → turn on"],
                        "note": "Useful during a wave of harassment when you don't want to block people one by one.",
                    },
                    {
                        "name": "Manual tag approval",
                        "what": "Photos you're tagged in only reach your profile once you approve them.",
                        "how": ["Settings and privacy → Tags and mentions → Manually approve tags"],
                    },
                    {
                        "name": "Mute without unfollowing",
                        "what": "Stops someone's posts or stories reaching your feed without unfollowing or telling them.",
                        "how": ["Their profile → ⋮ → Mute"],
                    },
                ],
            },
        ],
    },
    # ------------------------------------------------------------------ #
    {
        "name": "Facebook",
        "emoji": "🟦",
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
                        "how": ["Menu (☰) → scroll to the bottom → Log out"],
                    },
                    {
                        "name": "Deactivate account",
                        "tag": "Reversible",
                        "what": "Hides your profile and content from everyone while keeping all your data intact.",
                        "how": [
                            "Settings & privacy → Accounts Centre → Personal details → Account ownership and control → Deactivation or deletion → pick account → Deactivate"
                        ],
                        "note": "Logging back in reactivates you instantly.",
                    },
                    {
                        "name": "Delete account",
                        "tag": "Permanent",
                        "what": "Removes your profile and data for good.",
                        "how": ["Same path as Deactivate → Delete account → confirm"],
                        "note": "30-day grace period — don't log back in if you want the deletion to stick.",
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
                        "name": "Off-Facebook activity",
                        "what": "Shows what other apps and websites report about you to Facebook, and lets you disconnect it.",
                        "how": ["Settings → Your Facebook Information → Off-Facebook Activity"],
                    },
                    {
                        "name": "Profile and tagging review",
                        "what": "Lets you approve tags and posts before they appear on your timeline.",
                        "how": ["Settings & privacy → Privacy → Profile and tagging"],
                    },
                    {
                        "name": "Ad preferences",
                        "what": "Shows the interest categories advertisers use to target you, and lets you delete them.",
                        "how": ["Settings → Ads → Ad preferences"],
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
        "emoji": "👻",
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
                        "how": ["Profile (Bitmoji, top left) → gear icon → scroll down → Log out"],
                    },
                    {
                        "name": "Deactivate account",
                        "tag": "Reversible",
                        "what": "There's no separate pause button — starting deletion triggers a 30-day hold that works the same way.",
                        "how": ["Use the Delete account steps — the hold starts automatically"],
                        "note": "The hold is 180 days in India. Log back in during the window to restore everything.",
                    },
                    {
                        "name": "Delete account",
                        "tag": "Permanent",
                        "what": "Erases your profile, Snap Map presence and account data.",
                        "how": [
                            "On Android or desktop|accounts.snapchat.com/accounts/delete_account → log in → Delete My Account → re-enter your details → confirm",
                            "On iPhone|Settings (gear) → Support → I Need Help → My Account & Security → Account Information → Delete My Account",
                        ],
                    },
                ],
            },
            {
                "title": "Core privacy settings",
                "items": [
                    {
                        "name": "Ghost Mode",
                        "what": "Removes your avatar from the Snap Map so no other user can see where you are.",
                        "how": ["Snap Map → gear icon (top right of the map) → turn on Ghost Mode → choose how long"],
                        "note": "Ghost Mode hides you from other users only — Snapchat keeps collecting your location.",
                    },
                ],
            },
            {
                "title": "Hidden settings",
                "items": [
                    {
                        "name": "Custom location sharing",
                        "what": "Shares your location with a chosen few friends instead of everyone or no one.",
                        "how": ["Snap Map → gear icon → See My Location → pick specific friends"],
                    },
                    {
                        "name": "See me in Quick Add",
                        "what": "Stops your profile being suggested to other people as a friend recommendation.",
                        "how": ["Settings → Privacy Controls → See Me in Quick Add → turn off"],
                    },
                    {
                        "name": "Hide story from",
                        "what": "Blocks specific people from seeing your story without unfriending them.",
                        "how": ["Settings → Who can view my story → Hide my story from"],
                    },
                    {
                        "name": "Contact syncing",
                        "what": "Stops Snapchat matching your phone contacts against its user database to suggest friends.",
                        "how": ["Settings → Contacts → turn off syncing"],
                    },
                ],
            },
        ],
    },
    # ------------------------------------------------------------------ #
    {
        "name": "Discord",
        "emoji": "🎮",
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
                        "how": ["User Settings → My Account → scroll to Account Removal → Disable Account"],
                    },
                    {
                        "name": "Delete account",
                        "tag": "Permanent",
                        "what": "Wipes your account for good.",
                        "how": [
                            "User Settings → My Account → Account Removal → Delete Account → enter password and 2FA code → confirm"
                        ],
                        "note": "Hand over or delete any servers you own first, or Discord won't let you continue. Your messages stay visible in servers, relabelled 'Deleted User'. Takes about 14 days, and logging in cancels it.",
                    },
                ],
            },
            {
                "title": "Core privacy settings",
                "items": [
                    {
                        "name": "DM restrictions",
                        "what": "Decides whether people who share a server with you, but aren't friends, can message you.",
                        "how": ["User Settings → Privacy & Safety (or Content & Social) → turn off direct messages from server members"],
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
                        "what": "Separate switches for personalised recommendations, tailored sponsored content and 'improving Discord'.",
                        "how": ["User Settings → Data & Privacy"],
                        "note": "Most of these are on by default.",
                    },
                    {
                        "name": "Safe direct messaging",
                        "what": "Scans incoming DMs for explicit images before you have to look at them.",
                        "how": ["User Settings → Privacy & Safety"],
                    },
                    {
                        "name": "Who can add you as a friend",
                        "what": "Limits friend requests to everyone, friends of friends, server members or no one.",
                        "how": ["User Settings → Privacy & Safety → Friend Requests"],
                    },
                    {
                        "name": "Request all of my data",
                        "what": "Downloads a full archive of everything Discord has stored about you.",
                        "how": ["User Settings → Data & Privacy → Request all of my data"],
                    },
                ],
            },
        ],
    },
    # ------------------------------------------------------------------ #
    {
        "name": "TikTok",
        "emoji": "🎵",
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
                        "how": ["Profile → ☰ (top right) → Settings and privacy → scroll down → Log out"],
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
                        "note": "30 days before it's final — logging in cancels it.",
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
                        "how": ["Settings and privacy → Privacy → Comment filters → Filter keywords"],
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
        "emoji": "❌",
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
                        "how": ["Settings and privacy → Privacy and safety → Audience and tagging → Protect your posts"],
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
                        "name": "Data sharing with business partners",
                        "what": "Stops your activity data being shared with X's advertising and business partners.",
                        "how": ["Settings and privacy → Privacy and safety → Data sharing with business partners"],
                    },
                ],
            },
        ],
    },
    # ------------------------------------------------------------------ #
    {
        "name": "WhatsApp",
        "emoji": "💬",
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
                ],
            },
            {
                "title": "Hidden settings",
                "items": [
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
                ],
            },
        ],
    },
    # ------------------------------------------------------------------ #
    {
        "name": "Telegram",
        "emoji": "✈️",
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
                    },
                    {
                        "name": "Delete account",
                        "tag": "Permanent",
                        "what": "Immediately wipes your account, contacts, chats and media from Telegram's cloud.",
                        "how": [
                            "Settings → Privacy and Security → scroll to the bottom → Delete my account → confirm your phone number"
                        ],
                        "note": "Groups and channels you own pass to the next longest-serving admin unless you delete or transfer them first.",
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
                        "note": "Self-destruct timers run from 2 seconds to 1 week, and messages can't be forwarded.",
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
        "emoji": "👽",
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
                        "how": ["User Settings → Account → Delete Account → confirm with password"],
                        "note": "Your posts and comments stay up as '[deleted]' unless you remove them yourself first.",
                    },
                ],
            },
            {
                "title": "Core privacy settings",
                "items": [
                    {
                        "name": "Safety & Privacy tab",
                        "what": "The central hub for most of Reddit's visibility controls.",
                        "how": ["User Settings → Safety & Privacy"],
                    },
                ],
            },
            {
                "title": "Hidden settings",
                "items": [
                    {
                        "name": "Content visibility",
                        "what": "Hides your posts and comments from search engines and from logged-out visitors.",
                        "how": ["Settings → Safety & Privacy → turn off content visibility"],
                    },
                    {
                        "name": "Allow people to follow you",
                        "what": "Decides whether your posting activity can be followed like a feed.",
                        "how": ["Settings → Safety & Privacy → Allow people to follow you"],
                    },
                    {
                        "name": "Active in communities",
                        "what": "Hides which subreddits you're active in from your public profile.",
                        "how": ["Profile → Settings → turn off Show active communities"],
                    },
                    {
                        "name": "Personalised ads",
                        "what": "Turns off ad targeting based on your browsing and posting.",
                        "how": ["Settings → Privacy & Ad Settings"],
                    },
                ],
            },
        ],
    },
    # ------------------------------------------------------------------ #
    {
        "name": "YouTube",
        "emoji": "▶️",
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
                            "YouTube Studio → Settings → Channel → Advanced settings → Remove YouTube content → I want to hide my channel"
                        ],
                    },
                    {
                        "name": "Delete channel",
                        "tag": "Permanent",
                        "what": "Erases your videos, comments, playlists, messages and watch history.",
                        "how": [
                            "Same path as Hide → I want to permanently delete my content → tick both boxes",
                            "Or|Google Account → Data & Privacy → Delete a Google service → bin icon next to YouTube",
                        ],
                        "note": "Your wider Google Account — Gmail, Drive and the rest — is left alone.",
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
        "emoji": "💼",
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
                        "how": ["Settings & Privacy → Account preferences → Hibernate account"],
                        "note": "This cancels any Premium subscription straight away — cancel it separately first if you've paid ahead.",
                    },
                    {
                        "name": "Close account",
                        "tag": "Permanent",
                        "what": "Removes your profile, connections, messages, endorsements and recommendations.",
                        "how": [
                            "Settings & Privacy → Account preferences → Account management → Close account → pick a reason → confirm password"
                        ],
                        "note": "14-day grace period before it's final.",
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
                        "how": ["Profile → Open to → Recruiters only"],
                    },
                    {
                        "name": "Third-party applications",
                        "what": "Shows every outside app connected to your account so you can revoke access.",
                        "how": ["Settings & Privacy → Sign-in & Security → Third-party applications"],
                    },
                ],
            },
        ],
    },
    # ------------------------------------------------------------------ #
    {
        "name": "Roblox",
        "emoji": "🧱",
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
                        "how": ["Settings (gear) → Privacy → Account Deactivation and Deletion → Deactivate"],
                    },
                    {
                        "name": "Delete account",
                        "tag": "Permanent",
                        "what": "Roblox doesn't offer instant self-serve deletion to everyone — the reliable route is the support form.",
                        "how": [
                            "If shown|Settings → Privacy & Content Restrictions → Account Deactivation & Deletion → Delete Account",
                            "Otherwise|Roblox Support contact form → Data Privacy Requests → Right to Be Forgotten",
                        ],
                        "note": "Expect an identity check and a short wait. This erases your profile, Robux, items and progress.",
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
                    },
                ],
            },
            {
                "title": "Hidden settings",
                "items": [
                    {
                        "name": "Social media link visibility",
                        "what": "Decides whether your other social accounts show on your Roblox profile.",
                        "how": ["Settings → Privacy → Social media links"],
                    },
                    {
                        "name": "Spatial voice and face tracking",
                        "what": "Turns off voice chat and webcam-based avatar face tracking entirely.",
                        "how": ["Settings → Privacy → Spatial Voice / Face tracking"],
                    },
                    {
                        "name": "Trade and inventory privacy",
                        "what": "Decides who can see the items in your inventory.",
                        "how": ["Settings → Privacy"],
                    },
                    {
                        "name": "Account PIN",
                        "what": "Locks your settings behind a PIN so they can't be changed without it.",
                        "how": ["Settings → Security"],
                    },
                ],
            },
        ],
    },
    # ------------------------------------------------------------------ #
    {
        "name": "Wattpad",
        "emoji": "📖",
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
                        "how": ["Account Settings → Delete Account"],
                        "note": "Reversible for 6 months just by logging back in — Wattpad uses one button for both steps.",
                    },
                    {
                        "name": "Delete account",
                        "tag": "Permanent",
                        "what": "After 6 months without logging in, your username, stories and library are deleted for good.",
                        "how": [
                            "Happens automatically 6 months after deactivating",
                            "Or sooner|email privacy@wattpad.com",
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
                        "how": ["Account Settings → Privacy Settings"],
                    },
                ],
            },
            {
                "title": "Hidden settings",
                "items": [
                    {
                        "name": "Who can message or comment",
                        "what": "Limits who can contact you or comment on your stories.",
                        "how": ["Account Settings → Privacy Settings"],
                    },
                    {
                        "name": "Reading list visibility",
                        "what": "Hides what you're reading or have bookmarked from people viewing your profile.",
                        "how": ["Account Settings → Privacy Settings"],
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
        "emoji": "🤖",
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
                            "Settings → Data Controls → turn off 'Improve the model for everyone' (sometimes called Chat History & Training)"
                        ],
                        "note": "Business, Enterprise, Edu and API accounts are already excluded by default.",
                    },
                ],
            },
            {
                "title": "Hidden settings",
                "items": [
                    {
                        "name": "Temporary chat",
                        "what": "A one-off chat that never saves to your history and is never used for training.",
                        "how": ["New chat menu → Temporary chat"],
                    },
                    {
                        "name": "Memory controls",
                        "what": "Lets you see, edit or clear the things ChatGPT has remembered about you.",
                        "how": ["Settings → Personalisation → Memory"],
                    },
                ],
            },
        ],
    },
    # ------------------------------------------------------------------ #
    {
        "name": "Google Gemini",
        "emoji": "✨",
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
                            "Or|Gemini app → profile picture → Activity → turn off Keep Activity",
                        ],
                        "note": "Google may still hold data for around 72 hours to run the service, even with this off.",
                    },
                ],
            },
            {
                "title": "Hidden settings",
                "items": [
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
        "emoji": "🔷",
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
                        "how": ["Facebook → Settings → Privacy Centre → Generative AI → Right to Object form"],
                        "note": "These rights are strongest for EU and UK users under GDPR. Elsewhere Meta may refuse.",
                    },
                ],
            },
            {
                "title": "Hidden settings",
                "items": [
                    {
                        "name": "Third-party info objection",
                        "what": "A separate objection covering data Meta bought or collected about you from outside sources.",
                        "how": ["Facebook Privacy Centre → search 'Generative AI Data Subject Rights'"],
                    },
                    {
                        "name": "Mute Meta AI",
                        "what": "Stops Meta AI appearing and notifying you inside the apps, without a full opt-out.",
                        "how": ["Mute the Meta AI chat thread the way you'd mute any contact"],
                    },
                ],
            },
        ],
    },
    # ------------------------------------------------------------------ #
    {
        "name": "Claude",
        "emoji": "🅰️",
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
                        "note": "Work, Enterprise, Education and API accounts are already excluded by default.",
                    },
                ],
            },
            {
                "title": "Hidden settings",
                "items": [
                    {
                        "name": "Incognito mode",
                        "what": "Chats that are never used for training and never saved to your history.",
                        "how": ["New chat → Incognito"],
                    },
                    {
                        "name": "Delete one conversation",
                        "what": "Removes a single chat from your history now, and from Anthropic's systems within 30 days.",
                        "how": ["Chat list → pick a conversation → Delete"],
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
        "Opting out of AI training only affects what comes next",
        "Turning training off protects future conversations. Anything already absorbed into a "
        "finished training run stays there — none of these companies have an unlearn button.",
    ),
    (
        "EU and UK users have stronger rights",
        "GDPR gives you legally enforceable rights to access, export and delete your data, and to "
        "object to AI training. These requests usually go through a company's Privacy Centre rather "
        "than the normal in-app settings.",
    ),
    (
        "Menus move — check the source if a path fails",
        "Apps rename and relocate these controls every few months. If a path here doesn't match what "
        "you see, the platform's own help centre article is the thing to trust.",
    ),
]
