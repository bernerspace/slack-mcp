# Slack Bot Permissions Reference 🤖

A comprehensive guide to all Slack bot permissions (scopes) and what they allow your bot to do.

## App & Mentions

### `app_mentions:read`
**What it does:** View messages that directly mention your bot (@yourbot) in conversations  
**Use case:** Respond when users mention your bot  
**Example:** User says "@yourbot help" → your bot can see and respond

### `A:write`
**What it does:** Allow your bot to act as an App Agent  
**Use case:** Advanced automation and workflow management  
**Example:** Your bot can perform complex multi-step actions

## 🔖 Bookmarks

### `bookmarks:read`
**What it does:** List bookmarks in channels  
**Use case:** Display saved links and resources  
**Example:** Get all pinned links in a channel

### `bookmarks:write`
**What it does:** Create, edit, and remove bookmarks  
**Use case:** Manage important links for teams  
**Example:** Add useful documentation links to channels

## 📞 Calls

### `calls:read`
**What it does:** View information about ongoing and past calls  
**Use case:** Meeting analytics and attendance tracking  
**Example:** See who joined the daily standup call

### `calls:write`
**What it does:** Start and manage calls in a workspace  
**Use case:** Automated meeting scheduling  
**Example:** Start a call when critical alert is triggered

## 🎨 Canvases

### `canvases:read`
**What it does:** Access contents of canvases created in Slack  
**Use case:** Read collaborative documents  
**Example:** Extract action items from project canvases

### `canvases:write`
**What it does:** Create, edit and remove canvases  
**Use case:** Automated documentation creation  
**Example:** Generate project status canvases

## 📢 Public Channels

### `channels:history`
**What it does:** View messages and content in public channels your bot is in  
**Use case:** Message analysis, search, archiving  
**Example:** Analyze team communication patterns

### `channels:join`
**What it does:** Join public channels automatically  
**Use case:** Auto-join channels based on keywords  
**Example:** Join any channel with "incident" in the name

### `channels:manage`
**What it does:** Manage public channels and create new ones  
**Use case:** Channel automation and organization  
**Example:** Create project channels automatically

### `channels:read`
**What it does:** View basic info about public channels  
**Use case:** Channel discovery and listing  
**Example:** List all channels in workspace

### `channels:write.invites`
**What it does:** Invite members to public channels  
**Use case:** Automated team assignments  
**Example:** Add new engineers to #engineering channel

### `channels:write.topic`
**What it does:** Set descriptions of public channels  
**Use case:** Keep channel purposes updated  
**Example:** Update channel topic with current sprint info

## 💬 Chat & Messaging

### `chat:write`
**What it does:** Send messages as your bot  
**Use case:** Core messaging functionality  
**Example:** Send notifications, responses, alerts

### `chat:write.customize`
**What it does:** Send messages with custom username and avatar  
**Use case:** Impersonate different systems or personas  
**Example:** Send messages as "GitHub Bot" with GitHub avatar

### `chat:write.public`
**What it does:** Send messages to channels your bot isn't a member of  
**Use case:** Cross-channel notifications  
**Example:** Send alerts to any channel without joining

## ⚡ Commands & Interactions

### `commands`
**What it does:** Add shortcuts and slash commands  
**Use case:** Interactive bot commands  
**Example:** `/deploy production` command

## 🔗 Slack Connect

### `conversations.connect:manage`
**What it does:** Manage Slack Connect channels  
**Use case:** External workspace collaboration  
**Example:** Manage partner company channels

### `conversations.connect:read`
**What it does:** Receive Slack Connect invite events  
**Use case:** Monitor external invitations  
**Example:** Track when other companies invite you

### `conversations.connect:write`
**What it does:** Create and accept Slack Connect invitations  
**Use case:** Automated external collaboration setup  
**Example:** Auto-connect with client workspaces

## 🔕 Do Not Disturb

### `dnd:read`
**What it does:** View Do Not Disturb settings for workspace members  
**Use case:** Respect user availability  
**Example:** Don't send notifications when user is in DND

## 😀 Emojis

### `emoji:read`
**What it does:** View custom emoji in workspace  
**Use case:** Use workspace-specific emojis  
**Example:** React with company-specific emoji

## 📁 Files

### `files:read`
**What it does:** View files shared in channels your bot is in  
**Use case:** File analysis and processing  
**Example:** Scan uploaded documents for sensitive data

### `files:write`
**What it does:** Upload, edit, and delete files  
**Use case:** Automated file management  
**Example:** Generate and share reports

## 🔒 Private Channels (Groups)

### `groups:history`
**What it does:** View messages in private channels your bot is in  
**Use case:** Private channel monitoring  
**Example:** Track sensitive project discussions

### `groups:read`
**What it does:** View basic info about private channels  
**Use case:** Private channel management  
**Example:** List private channels your bot has access to

### `groups:write`
**What it does:** Manage private channels and create new ones  
**Use case:** Confidential project setup  
**Example:** Create secure channels for incidents

### `groups:write.invites`
**What it does:** Invite members to private channels  
**Use case:** Controlled access management  
**Example:** Add specific people to security channels

### `groups:write.topic`
**What it does:** Set descriptions in private channels  
**Use case:** Keep private channel purposes clear  
**Example:** Update incident channel with current status

## 💬 Direct Messages

### `im:history`
**What it does:** View DM content your bot is part of  
**Use case:** Personal assistance and support  
**Example:** Help users with personal queries

### `im:read`
**What it does:** View basic DM information  
**Use case:** DM management  
**Example:** List active DM conversations

### `im:write`
**What it does:** Start direct messages with people  
**Use case:** Personal notifications  
**Example:** Send onboarding messages to new users

### `im:write.topic`
**What it does:** Set descriptions in DMs  
**Use case:** Context setting in DMs  
**Example:** Set DM topic to "Support Ticket #123"

## 📨 Webhooks & Links

### `incoming-webhook`
**What it does:** Post messages to specific channels  
**Use case:** External system notifications  
**Example:** GitHub pushes, CI/CD alerts

### `links.embed:write`
**What it does:** Embed video player URLs in messages  
**Use case:** Rich media sharing  
**Example:** Embed training videos

### `links:read`
**What it does:** View URLs in messages  
**Use case:** Link analysis and security  
**Example:** Scan for malicious links

### `links:write`
**What it does:** Show URL previews in messages  
**Use case:** Enhanced link sharing  
**Example:** Auto-preview documentation links

## 📊 Metadata & Analytics

### `metadata.message:read`
**What it does:** Read message metadata in accessible channels  
**Use case:** Advanced message analysis  
**Example:** Track message threading patterns

## 👥 Group DMs (Multi-party IMs)

### `mpim:history`
**What it does:** View group DM messages your bot is in  
**Use case:** Group conversation support  
**Example:** Facilitate team discussions

### `mpim:read`
**What it does:** View basic group DM information  
**Use case:** Group DM management  
**Example:** List active group conversations

### `mpim:write`
**What it does:** Start group DMs  
**Use case:** Automated team formation  
**Example:** Create incident response groups

### `mpim:write.topic`
**What it does:** Set group DM descriptions  
**Use case:** Group context management  
**Example:** Set topic for project team DM

## 📌 Pins & Reactions

### `pins:read`
**What it does:** View pinned content in channels  
**Use case:** Important content tracking  
**Example:** List all pinned announcements

### `pins:write`
**What it does:** Add and remove pinned messages/files  
**Use case:** Content curation  
**Example:** Pin important updates automatically

### `reactions:read`
**What it does:** View emoji reactions on content  
**Use case:** Sentiment analysis  
**Example:** Track team mood through reactions

### `reactions:write`
**What it does:** Add and edit emoji reactions  
**Use case:** Automated feedback  
**Example:** React with ✅ when tasks are completed

## ⏰ Reminders

### `reminders:read`
**What it does:** View reminders created by your bot  
**Use case:** Reminder management  
**Example:** List all pending reminders

### `reminders:write`
**What it does:** Add, remove, or mark reminders as complete  
**Use case:** Task automation  
**Example:** Set meeting reminders for team

## 📤 Remote Files

### `remote_files:read`
**What it does:** View remote files added by your bot  
**Use case:** External file integration  
**Example:** Access Google Drive files in Slack

### `remote_files:share`
**What it does:** Share remote files on user's behalf  
**Use case:** Automated file sharing  
**Example:** Share Dropbox files in channels

### `remote_files:write`
**What it does:** Add, edit, delete remote files  
**Use case:** External file management  
**Example:** Sync files between systems

## 🏢 Team & Workspace

### `team.billing:read`
**What it does:** Read billing plan for workspaces  
**Use case:** Usage analytics  
**Example:** Track workspace usage limits

### `team.preferences:read`
**What it does:** Read workspace preferences  
**Use case:** Workspace customization  
**Example:** Adapt bot behavior to workspace settings

### `team:read`
**What it does:** View workspace name, domain, and icon  
**Use case:** Multi-workspace management  
**Example:** Display workspace info in reports

## 🎯 Triggers & Workflows

### `triggers:read`
**What it does:** Read new Platform triggers  
**Use case:** Trigger management  
**Example:** Monitor automation triggers

### `triggers:write`
**What it does:** Create new Platform triggers  
**Use case:** Automation setup  
**Example:** Create triggers for incident response

### `workflow.steps:execute`
**What it does:** Add steps for Workflow Builder  
**Use case:** Custom workflow steps  
**Example:** Add "Deploy to Production" step

### `workflows.templates:read`
**What it does:** Manage Slack workflow templates (read)  
**Use case:** Template management  
**Example:** List available workflow templates

### `workflows.templates:write`
**What it does:** Write Slack workflow templates  
**Use case:** Template creation  
**Example:** Create reusable onboarding workflows

## 👤 Users & Groups

### `usergroups:read`
**What it does:** View user groups in workspace  
**Use case:** Team management  
**Example:** List all engineering teams

### `usergroups:write`
**What it does:** Create and manage user groups  
**Use case:** Automated team organization  
**Example:** Create groups for new projects

### `users.profile:read`
**What it does:** View user profile details  
**Use case:** User information access  
**Example:** Get user's role and department

### `users:read`
**What it does:** View people in workspace  
**Use case:** User discovery  
**Example:** List all workspace members

### `users:read.email`
**What it does:** View email addresses of workspace members  
**Use case:** External communication  
**Example:** Send email notifications

### `users:write`
**What it does:** Set presence for your bot  
**Use case:** Bot status management  
**Example:** Set bot as "away" during maintenance

## 🚀 Quick Permission Groups for Common Use Cases

### **Basic Messaging Bot**
```
chat:write
channels:read
```

### **Advanced Chat Bot**
```
chat:write
chat:write.customize
app_mentions:read
channels:read
channels:history
im:write
```

### **Channel Management Bot**
```
channels:manage
channels:write.invites
channels:write.topic
groups:write
users:read
```

### **File & Content Bot**
```
files:read
files:write
pins:read
pins:write
bookmarks:read
bookmarks:write
```

### **Workflow Automation Bot**
```
triggers:read
triggers:write
workflow.steps:execute
reminders:read
reminders:write
```

### **Analytics & Monitoring Bot**
```
channels:history
groups:history
reactions:read
users:read
team:read
metadata.message:read
```

## ⚠️ Security Considerations

- **Principle of Least Privilege**: Only request permissions you actually need
- **Sensitive Permissions**: Be extra careful with `users:read.email`, `groups:history`, `files:read`
- **Regular Audits**: Review and remove unused permissions
- **User Communication**: Clearly explain why each permission is needed

## 📝 Notes

- Some permissions require workspace admin approval
- Bot permissions are different from user permissions (OAuth scopes)
- Permissions can be updated after installation (with user consent)
- Always test with minimal permissions first