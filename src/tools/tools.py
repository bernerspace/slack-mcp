"""
Slack MCP Tools
FastMCP tools for Slack bot operations using SlackBotAPIService
"""

from typing import List, Optional, Dict, Any, Literal, Union
from datetime import datetime
from pydantic import Field
from typing_extensions import Annotated

from src.services.slack_bot_api import SlackBotAPIService


class SlackTools:
    """Slack tools class containing all Slack API functionality"""
    
    def __init__(self, bot_token: str):
        """Initialize the Slack service with bot token"""
        self.slack_service = SlackBotAPIService(bot_token)
    
    # ==================== AUTHENTICATION & TESTING ====================
    
    async def test_slack_auth(self) -> Dict[str, Any]:
        """Test Slack authentication and get bot information"""
        result = await self.slack_service.test_auth()
        if result.ok:
            return {
                "authenticated": True,
                "bot_user": result.data.get("user", "Unknown"),
                "team": result.data.get("team", "Unknown"),
                "user_id": result.data.get("user_id"),
                "team_id": result.data.get("team_id")
            }
        else:
            raise ValueError(f"Authentication failed: {result.error}")

    # ==================== MESSAGING TOOLS ====================
    
    async def send_slack_message(
        self,
        channel: str,
        text: Optional[str] = None,
        blocks: Optional[List[Dict]] = None,
        attachments: Optional[List[Dict]] = None,
        thread_ts: Optional[str] = None,
        username: Optional[str] = None,
        icon_emoji: Optional[str] = None,
        icon_url: Optional[str] = None
    ) -> Dict[str, Any]:
        """Send a message to a Slack channel with optional rich formatting"""
        if not text and not blocks:
            raise ValueError("Either text or blocks must be provided")
        
        result = await self.slack_service.send_message(
            channel=channel,
            text=text,
            blocks=blocks,
            attachments=attachments,
            thread_ts=thread_ts,
            username=username,
            icon_emoji=icon_emoji,
            icon_url=icon_url
        )
        
        if result.ok:
            return {
                "success": True,
                "channel": result.data.get("channel"),
                "timestamp": result.data.get("ts"),
                "message": "Message sent successfully"
            }
        else:
            raise ValueError(f"Failed to send message: {result.error}")

    async def update_slack_message(
        self,
        channel: str,
        message_ts: str,
        text: Optional[str] = None,
        blocks: Optional[List[Dict]] = None,
        attachments: Optional[List[Dict]] = None
    ) -> Dict[str, Any]:
        """Update an existing Slack message"""
        result = await self.slack_service.update_message(
            channel=channel, 
            ts=message_ts, 
            text=text, 
            blocks=blocks, 
            attachments=attachments
        )
        
        if result.ok:
            return {
                "success": True,
                "channel": result.data.get("channel"),
                "timestamp": result.data.get("ts"),
                "message": "Message updated successfully"
            }
        else:
            raise ValueError(f"Failed to update message: {result.error}")

    async def delete_slack_message(self, channel: str, message_ts: str) -> Dict[str, Any]:
        """Delete a Slack message"""
        result = await self.slack_service.delete_message(channel=channel, ts=message_ts)
        
        if result.ok:
            return {
                "success": True,
                "message": "Message deleted successfully"
            }
        else:
            raise ValueError(f"Failed to delete message: {result.error}")

    async def schedule_slack_message(
        self,
        channel: str,
        post_at: int,
        text: Optional[str] = None,
        blocks: Optional[List[Dict]] = None,
        attachments: Optional[List[Dict]] = None
    ) -> Dict[str, Any]:
        """Schedule a message to be sent at a specific time"""
        result = await self.slack_service.schedule_message(
            channel=channel,
            post_at=post_at,
            text=text,
            blocks=blocks,
            attachments=attachments
        )
        
        if result.ok:
            return {
                "success": True,
                "scheduled_message_id": result.data.get("scheduled_message_id"),
                "channel": result.data.get("channel"),
                "post_at": result.data.get("post_at"),
                "message": "Message scheduled successfully"
            }
        else:
            raise ValueError(f"Failed to schedule message: {result.error}")

    # ==================== CHANNEL TOOLS ====================
    
    async def list_slack_channels(
        self,
        limit: int = 100,
        exclude_archived: bool = True,
        types: str = "public_channel,private_channel",
        cursor: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """List Slack channels in the workspace"""
        result = await self.slack_service.list_channels(
            limit=limit, 
            exclude_archived=exclude_archived, 
            types=types, 
            cursor=cursor
        )
        
        if result.ok:
            channels = result.data.get("channels", [])
            return [
                {
                    "id": ch.get("id"),
                    "name": ch.get("name"),
                    "is_private": ch.get("is_private", False),
                    "is_member": ch.get("is_member", False),
                    "topic": ch.get("topic", {}).get("value", ""),
                    "purpose": ch.get("purpose", {}).get("value", ""),
                    "member_count": ch.get("num_members", 0),
                    "created": ch.get("created"),
                    "is_archived": ch.get("is_archived", False)
                }
                for ch in channels
            ]
        else:
            raise ValueError(f"Failed to list channels: {result.error}")

    async def get_slack_channel_info(self, channel: str) -> Dict[str, Any]:
        """Get detailed information about a specific Slack channel"""
        result = await self.slack_service.get_channel_info(channel)
        
        if result.ok:
            ch = result.data.get("channel", {})
            return {
                "id": ch.get("id"),
                "name": ch.get("name"),
                "is_private": ch.get("is_private", False),
                "is_member": ch.get("is_member", False),
                "topic": ch.get("topic", {}).get("value", ""),
                "purpose": ch.get("purpose", {}).get("value", ""),
                "member_count": ch.get("num_members", 0),
                "created": ch.get("created"),
                "creator": ch.get("creator"),
                "is_archived": ch.get("is_archived", False)
            }
        else:
            raise ValueError(f"Failed to get channel info: {result.error}")

    async def create_slack_channel(self, name: str, is_private: bool = False) -> Dict[str, Any]:
        """Create a new Slack channel"""
        result = await self.slack_service.create_channel(name=name, is_private=is_private)
        
        if result.ok:
            channel = result.data.get("channel", {})
            return {
                "success": True,
                "channel_id": channel.get("id"),
                "channel_name": channel.get("name"),
                "is_private": channel.get("is_private", False),
                "message": f"Channel {'#' + name} created successfully"
            }
        else:
            raise ValueError(f"Failed to create channel: {result.error}")

    async def join_slack_channel(self, channel: str) -> Dict[str, Any]:
        """Join a Slack channel"""
        result = await self.slack_service.join_channel(channel)
        
        if result.ok:
            return {
                "success": True,
                "message": f"Successfully joined channel {channel}"
            }
        else:
            raise ValueError(f"Failed to join channel: {result.error}")

    async def leave_slack_channel(self, channel: str) -> Dict[str, Any]:
        """Leave a Slack channel"""
        result = await self.slack_service.leave_channel(channel)
        
        if result.ok:
            return {
                "success": True,
                "message": f"Successfully left channel {channel}"
            }
        else:
            raise ValueError(f"Failed to leave channel: {result.error}")

    async def invite_to_slack_channel(self, channel: str, users: Union[str, List[str]]) -> Dict[str, Any]:
        """Invite users to a Slack channel"""
        result = await self.slack_service.invite_to_channel(channel=channel, users=users)
        
        if result.ok:
            return {
                "success": True,
                "message": f"Users invited to channel {channel} successfully"
            }
        else:
            raise ValueError(f"Failed to invite users to channel: {result.error}")

    async def kick_from_slack_channel(self, channel: str, user: str) -> Dict[str, Any]:
        """Remove a user from a Slack channel"""
        result = await self.slack_service.kick_from_channel(channel=channel, user=user)
        
        if result.ok:
            return {
                "success": True,
                "message": f"User removed from channel {channel} successfully"
            }
        else:
            raise ValueError(f"Failed to remove user from channel: {result.error}")

    async def set_slack_channel_topic(self, channel: str, topic: str) -> Dict[str, Any]:
        """Set the topic for a Slack channel"""
        result = await self.slack_service.set_channel_topic(channel=channel, topic=topic)
        
        if result.ok:
            return {
                "success": True,
                "message": f"Channel topic updated successfully"
            }
        else:
            raise ValueError(f"Failed to set channel topic: {result.error}")

    async def set_slack_channel_purpose(self, channel: str, purpose: str) -> Dict[str, Any]:
        """Set the purpose for a Slack channel"""
        result = await self.slack_service.set_channel_purpose(channel=channel, purpose=purpose)
        
        if result.ok:
            return {
                "success": True,
                "message": f"Channel purpose updated successfully"
            }
        else:
            raise ValueError(f"Failed to set channel purpose: {result.error}")

    async def archive_slack_channel(self, channel: str) -> Dict[str, Any]:
        """Archive a Slack channel"""
        result = await self.slack_service.archive_channel(channel)
        
        if result.ok:
            return {
                "success": True,
                "message": f"Channel {channel} archived successfully"
            }
        else:
            raise ValueError(f"Failed to archive channel: {result.error}")

    async def unarchive_slack_channel(self, channel: str) -> Dict[str, Any]:
        """Unarchive a Slack channel"""
        result = await self.slack_service.unarchive_channel(channel)
        
        if result.ok:
            return {
                "success": True,
                "message": f"Channel {channel} unarchived successfully"
            }
        else:
            raise ValueError(f"Failed to unarchive channel: {result.error}")

    # ==================== USER TOOLS ====================
    
    async def list_slack_users(self, limit: int = 100, cursor: Optional[str] = None) -> List[Dict[str, Any]]:
        """List users in the Slack workspace"""
        result = await self.slack_service.list_users(limit=limit, cursor=cursor)
        
        if result.ok:
            users = result.data.get("members", [])
            return [
                {
                    "id": user.get("id"),
                    "name": user.get("name"),
                    "real_name": user.get("real_name", ""),
                    "display_name": user.get("profile", {}).get("display_name", ""),
                    "email": user.get("profile", {}).get("email", ""),
                    "is_bot": user.get("is_bot", False),
                    "is_admin": user.get("is_admin", False),
                    "status_text": user.get("profile", {}).get("status_text", ""),
                    "status_emoji": user.get("profile", {}).get("status_emoji", ""),
                    "timezone": user.get("tz", "")
                }
                for user in users
                if not user.get("deleted", False)
            ]
        else:
            raise ValueError(f"Failed to list users: {result.error}")

    async def get_slack_user_info(self, user: str) -> Dict[str, Any]:
        """Get detailed information about a specific Slack user"""
        result = await self.slack_service.get_user_info(user)
        
        if result.ok:
            user_data = result.data.get("user", {})
            profile = user_data.get("profile", {})
            return {
                "id": user_data.get("id"),
                "name": user_data.get("name"),
                "real_name": user_data.get("real_name", ""),
                "display_name": profile.get("display_name", ""),
                "email": profile.get("email", ""),
                "phone": profile.get("phone", ""),
                "title": profile.get("title", ""),
                "is_bot": user_data.get("is_bot", False),
                "is_admin": user_data.get("is_admin", False),
                "is_owner": user_data.get("is_owner", False),
                "timezone": user_data.get("tz", ""),
                "status_text": profile.get("status_text", ""),
                "status_emoji": profile.get("status_emoji", "")
            }
        else:
            raise ValueError(f"Failed to get user info: {result.error}")

    async def get_slack_user_profile(self, user: str) -> Dict[str, Any]:
        """Get user's profile information"""
        result = await self.slack_service.get_user_profile(user)
        
        if result.ok:
            profile = result.data.get("profile", {})
            return {
                "display_name": profile.get("display_name", ""),
                "real_name": profile.get("real_name", ""),
                "email": profile.get("email", ""),
                "phone": profile.get("phone", ""),
                "title": profile.get("title", ""),
                "status_text": profile.get("status_text", ""),
                "status_emoji": profile.get("status_emoji", ""),
                "image_24": profile.get("image_24", ""),
                "image_32": profile.get("image_32", ""),
                "image_48": profile.get("image_48", ""),
                "image_72": profile.get("image_72", ""),
                "image_192": profile.get("image_192", "")
            }
        else:
            raise ValueError(f"Failed to get user profile: {result.error}")

    async def set_slack_presence(self, presence: Literal["auto", "away"]) -> Dict[str, Any]:
        """Set bot's presence status"""
        result = await self.slack_service.set_user_presence(presence)
        
        if result.ok:
            return {
                "success": True,
                "message": f"Presence set to {presence}"
            }
        else:
            raise ValueError(f"Failed to set presence: {result.error}")

    # ==================== FILE TOOLS ====================
    
    async def upload_slack_file(
        self,
        channels: Union[str, List[str]],
        file_source: str,
        filename: Optional[str] = None,
        title: Optional[str] = None,
        initial_comment: Optional[str] = None,
        thread_ts: Optional[str] = None
    ) -> Dict[str, Any]:
        """Upload a file to Slack (supports URLs, local paths, or text content)"""
        result = await self.slack_service.upload_file(
            channels=channels,
            file_source=file_source,
            filename=filename,
            title=title,
            initial_comment=initial_comment,
            thread_ts=thread_ts
        )
        
        if result.ok:
            file_data = result.data.get("file", {})
            return {
                "success": True,
                "file_id": file_data.get("id"),
                "filename": file_data.get("name"),
                "size": file_data.get("size"),
                "url": file_data.get("url_private"),
                "message": "File uploaded successfully"
            }
        else:
            raise ValueError(f"Failed to upload file: {result.error}")

    async def list_slack_files(
        self,
        count: int = 20,
        channel: Optional[str] = None,
        user: Optional[str] = None,
        ts_from: Optional[str] = None,
        ts_to: Optional[str] = None,
        types: Optional[str] = None,
        page: int = 1
    ) -> List[Dict[str, Any]]:
        """List files in the Slack workspace"""
        result = await self.slack_service.list_files(
            count=count, 
            channel=channel, 
            user=user, 
            ts_from=ts_from, 
            ts_to=ts_to, 
            types=types, 
            page=page
        )
        
        if result.ok:
            files = result.data.get("files", [])
            return [
                {
                    "id": file.get("id"),
                    "name": file.get("name"),
                    "title": file.get("title", ""),
                    "size": file.get("size"),
                    "type": file.get("filetype", ""),
                    "user": file.get("user"),
                    "created": file.get("created"),
                    "url": file.get("url_private"),
                    "mimetype": file.get("mimetype", "")
                }
                for file in files
            ]
        else:
            raise ValueError(f"Failed to list files: {result.error}")

    async def get_slack_file_info(self, file_id: str) -> Dict[str, Any]:
        """Get information about a specific file"""
        result = await self.slack_service.get_file_info(file_id)
        
        if result.ok:
            file_data = result.data.get("file", {})
            return {
                "id": file_data.get("id"),
                "name": file_data.get("name"),
                "title": file_data.get("title", ""),
                "size": file_data.get("size"),
                "type": file_data.get("filetype", ""),
                "mimetype": file_data.get("mimetype", ""),
                "user": file_data.get("user"),
                "created": file_data.get("created"),
                "url": file_data.get("url_private"),
                "permalink": file_data.get("permalink", ""),
                "channels": file_data.get("channels", [])
            }
        else:
            raise ValueError(f"Failed to get file info: {result.error}")

    async def delete_slack_file(self, file_id: str) -> Dict[str, Any]:
        """Delete a file from Slack"""
        result = await self.slack_service.delete_file(file_id)
        
        if result.ok:
            return {
                "success": True,
                "message": "File deleted successfully"
            }
        else:
            raise ValueError(f"Failed to delete file: {result.error}")

    # ==================== REACTION TOOLS ====================
    
    async def add_slack_reaction(self, channel: str, message_ts: str, emoji: str) -> Dict[str, Any]:
        """Add an emoji reaction to a Slack message"""
        result = await self.slack_service.add_reaction(name=emoji, channel=channel, timestamp=message_ts)
        
        if result.ok:
            return {
                "success": True,
                "message": f"Added :{emoji}: reaction successfully"
            }
        else:
            raise ValueError(f"Failed to add reaction: {result.error}")

    async def remove_slack_reaction(self, channel: str, message_ts: str, emoji: str) -> Dict[str, Any]:
        """Remove an emoji reaction from a Slack message"""
        result = await self.slack_service.remove_reaction(name=emoji, channel=channel, timestamp=message_ts)
        
        if result.ok:
            return {
                "success": True,
                "message": f"Removed :{emoji}: reaction successfully"
            }
        else:
            raise ValueError(f"Failed to remove reaction: {result.error}")

    async def get_slack_reactions(self, channel: str, message_ts: str) -> Dict[str, Any]:
        """Get reactions for a message"""
        result = await self.slack_service.get_reactions(channel=channel, timestamp=message_ts)
        
        if result.ok:
            return {
                "success": True,
                "reactions": result.data.get("message", {}).get("reactions", [])
            }
        else:
            raise ValueError(f"Failed to get reactions: {result.error}")

    # ==================== HISTORY & INFORMATION TOOLS ====================
    
    async def get_slack_channel_history(
        self,
        channel: str,
        limit: int = 20,
        cursor: Optional[str] = None,
        latest: Optional[str] = None,
        oldest: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """Get message history from a Slack channel"""
        result = await self.slack_service.get_channel_history(
            channel=channel, 
            limit=limit, 
            cursor=cursor, 
            latest=latest, 
            oldest=oldest
        )
        
        if result.ok:
            messages = result.data.get("messages", [])
            return [
                {
                    "timestamp": msg.get("ts"),
                    "user": msg.get("user"),
                    "text": msg.get("text", ""),
                    "type": msg.get("type"),
                    "thread_ts": msg.get("thread_ts"),
                    "reply_count": msg.get("reply_count", 0),
                    "reactions": msg.get("reactions", []),
                    "attachments": msg.get("attachments", []),
                    "blocks": msg.get("blocks", [])
                }
                for msg in messages
            ]
        else:
            raise ValueError(f"Failed to get channel history: {result.error}")

    async def get_slack_thread_replies(
        self,
        channel: str,
        thread_ts: str,
        limit: int = 100,
        cursor: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """Get replies to a threaded message"""
        result = await self.slack_service.get_thread_replies(
            channel=channel,
            ts=thread_ts,
            limit=limit,
            cursor=cursor
        )
        
        if result.ok:
            messages = result.data.get("messages", [])
            return [
                {
                    "timestamp": msg.get("ts"),
                    "user": msg.get("user"),
                    "text": msg.get("text", ""),
                    "type": msg.get("type"),
                    "thread_ts": msg.get("thread_ts"),
                    "reactions": msg.get("reactions", []),
                    "attachments": msg.get("attachments", []),
                    "blocks": msg.get("blocks", [])
                }
                for msg in messages
            ]
        else:
            raise ValueError(f"Failed to get thread replies: {result.error}")

    # ==================== PIN TOOLS ====================
    
    async def pin_slack_message(self, channel: str, message_ts: str) -> Dict[str, Any]:
        """Pin a message to a Slack channel"""
        result = await self.slack_service.pin_message(channel=channel, timestamp=message_ts)
        
        if result.ok:
            return {
                "success": True,
                "message": "Message pinned successfully"
            }
        else:
            raise ValueError(f"Failed to pin message: {result.error}")

    async def unpin_slack_message(self, channel: str, message_ts: str) -> Dict[str, Any]:
        """Unpin a message from a Slack channel"""
        result = await self.slack_service.unpin_message(channel=channel, timestamp=message_ts)
        
        if result.ok:
            return {
                "success": True,
                "message": "Message unpinned successfully"
            }
        else:
            raise ValueError(f"Failed to unpin message: {result.error}")

    async def list_slack_pins(self, channel: str) -> List[Dict[str, Any]]:
        """List pinned items in a Slack channel"""
        result = await self.slack_service.list_pins(channel=channel)
        
        if result.ok:
            items = result.data.get("items", [])
            pins = []
            for item in items:
                if "message" in item:
                    msg = item["message"]
                    pins.append({
                        "type": "message",
                        "timestamp": msg.get("ts"),
                        "user": msg.get("user"),
                        "text": msg.get("text", ""),
                        "pinned_by": item.get("created_by"),
                        "pinned_at": item.get("created")
                    })
                elif "file" in item:
                    file = item["file"]
                    pins.append({
                        "type": "file",
                        "file_id": file.get("id"),
                        "filename": file.get("name"),
                        "title": file.get("title", ""),
                        "pinned_by": item.get("created_by"),
                        "pinned_at": item.get("created")
                    })
            return pins
        else:
            raise ValueError(f"Failed to list pins: {result.error}")

    # ==================== BOOKMARK TOOLS ====================
    
    async def add_slack_bookmark(
        self,
        channel_id: str,
        title: str,
        type: str,
        link: Optional[str] = None,
        emoji: Optional[str] = None
    ) -> Dict[str, Any]:
        """Add a bookmark to a Slack channel"""
        result = await self.slack_service.add_bookmark(
            channel_id=channel_id,
            title=title,
            type=type,
            link=link,
            emoji=emoji
        )
        
        if result.ok:
            bookmark = result.data.get("bookmark", {})
            return {
                "success": True,
                "bookmark_id": bookmark.get("id"),
                "title": bookmark.get("title"),
                "message": "Bookmark added successfully"
            }
        else:
            raise ValueError(f"Failed to add bookmark: {result.error}")

    async def remove_slack_bookmark(self, channel_id: str, bookmark_id: str) -> Dict[str, Any]:
        """Remove a bookmark from a Slack channel"""
        result = await self.slack_service.remove_bookmark(channel_id=channel_id, bookmark_id=bookmark_id)
        
        if result.ok:
            return {
                "success": True,
                "message": "Bookmark removed successfully"
            }
        else:
            raise ValueError(f"Failed to remove bookmark: {result.error}")

    async def list_slack_bookmarks(self, channel_id: str) -> List[Dict[str, Any]]:
        """List bookmarks in a Slack channel"""
        result = await self.slack_service.list_bookmarks(channel_id=channel_id)
        
        if result.ok:
            bookmarks = result.data.get("bookmarks", [])
            return [
                {
                    "id": bookmark.get("id"),
                    "title": bookmark.get("title"),
                    "type": bookmark.get("type"),
                    "link": bookmark.get("link", ""),
                    "emoji": bookmark.get("emoji", ""),
                    "created_by": bookmark.get("created_by"),
                    "date_created": bookmark.get("date_created")
                }
                for bookmark in bookmarks
            ]
        else:
            raise ValueError(f"Failed to list bookmarks: {result.error}")

    # ==================== USERGROUP TOOLS ====================
    
    async def create_slack_usergroup(
        self,
        name: str,
        handle: Optional[str] = None,
        description: Optional[str] = None,
        channels: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """Create a new user group"""
        result = await self.slack_service.create_usergroup(
            name=name,
            handle=handle,
            description=description,
            channels=channels
        )
        
        if result.ok:
            usergroup = result.data.get("usergroup", {})
            return {
                "success": True,
                "usergroup_id": usergroup.get("id"),
                "name": usergroup.get("name"),
                "handle": usergroup.get("handle"),
                "message": "Usergroup created successfully"
            }
        else:
            raise ValueError(f"Failed to create usergroup: {result.error}")

    async def list_slack_usergroups(self, include_disabled: bool = False) -> List[Dict[str, Any]]:
        """List user groups in the workspace"""
        result = await self.slack_service.list_usergroups(include_disabled=include_disabled)
        
        if result.ok:
            usergroups = result.data.get("usergroups", [])
            return [
                {
                    "id": ug.get("id"),
                    "name": ug.get("name"),
                    "handle": ug.get("handle"),
                    "description": ug.get("description", ""),
                    "is_external": ug.get("is_external", False),
                    "user_count": ug.get("user_count", 0),
                    "date_create": ug.get("date_create"),
                    "date_update": ug.get("date_update")
                }
                for ug in usergroups
            ]
        else:
            raise ValueError(f"Failed to list usergroups: {result.error}")

    async def update_slack_usergroup(
        self,
        usergroup: str,
        name: Optional[str] = None,
        handle: Optional[str] = None,
        description: Optional[str] = None
    ) -> Dict[str, Any]:
        """Update a user group"""
        result = await self.slack_service.update_usergroup(
            usergroup=usergroup,
            name=name,
            handle=handle,
            description=description
        )
        
        if result.ok:
            usergroup_data = result.data.get("usergroup", {})
            return {
                "success": True,
                "usergroup_id": usergroup_data.get("id"),
                "name": usergroup_data.get("name"),
                "handle": usergroup_data.get("handle"),
                "message": "Usergroup updated successfully"
            }
        else:
            raise ValueError(f"Failed to update usergroup: {result.error}")

    async def disable_slack_usergroup(self, usergroup: str) -> Dict[str, Any]:
        """Disable a user group"""
        result = await self.slack_service.disable_usergroup(usergroup=usergroup)
        
        if result.ok:
            return {
                "success": True,
                "message": "Usergroup disabled successfully"
            }
        else:
            raise ValueError(f"Failed to disable usergroup: {result.error}")

    # ==================== TEAM TOOLS ====================
    
    async def get_slack_team_info(self) -> Dict[str, Any]:
        """Get information about the Slack workspace/team"""
        result = await self.slack_service.get_team_info()
        
        if result.ok:
            team = result.data.get("team", {})
            return {
                "id": team.get("id"),
                "name": team.get("name"),
                "domain": team.get("domain"),
                "email_domain": team.get("email_domain"),
                "icon": team.get("icon", {}),
                "enterprise_id": team.get("enterprise_id"),
                "enterprise_name": team.get("enterprise_name")
            }
        else:
            raise ValueError(f"Failed to get team info: {result.error}")

    async def get_slack_team_profile(self) -> Dict[str, Any]:
        """Get team profile fields"""
        result = await self.slack_service.get_team_profile()
        
        if result.ok:
            profile = result.data.get("profile", {})
            return {
                "fields": profile.get("fields", [])
            }
        else:
            raise ValueError(f"Failed to get team profile: {result.error}")

    # ==================== EMOJI TOOLS ====================
    
    async def list_slack_emoji(self) -> List[Dict[str, Any]]:
        """List custom emoji for the team"""
        result = await self.slack_service.list_emoji()
        
        if result.ok:
            emoji_data = result.data.get("emoji", {})
            return [
                {
                    "name": name,
                    "url": url
                }
                for name, url in emoji_data.items()
            ]
        else:
            raise ValueError(f"Failed to list emoji: {result.error}")

    # ==================== DND (DO NOT DISTURB) TOOLS ====================
    
    async def get_slack_dnd_info(self, user: Optional[str] = None) -> Dict[str, Any]:
        """Get Do Not Disturb information for a user"""
        result = await self.slack_service.get_dnd_info(user=user)
        
        if result.ok:
            return {
                "dnd_enabled": result.data.get("dnd_enabled", False),
                "next_dnd_start_ts": result.data.get("next_dnd_start_ts"),
                "next_dnd_end_ts": result.data.get("next_dnd_end_ts"),
                "snooze_enabled": result.data.get("snooze_enabled", False),
                "snooze_endtime": result.data.get("snooze_endtime"),
                "snooze_remaining": result.data.get("snooze_remaining")
            }
        else:
            raise ValueError(f"Failed to get DND info: {result.error}")

    async def get_slack_team_dnd_info(self, users: Optional[List[str]] = None) -> Dict[str, Any]:
        """Get Do Not Disturb information for multiple users"""
        result = await self.slack_service.get_dnd_team_info(users=users)
        
        if result.ok:
            return {
                "users": result.data.get("users", {})
            }
        else:
            raise ValueError(f"Failed to get team DND info: {result.error}")