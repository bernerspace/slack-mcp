import sys
import os
from pathlib import Path
from fastmcp import FastMCP
from typing import List, Optional, Dict, Any, Literal, Union
from datetime import datetime
from pydantic import Field
from typing_extensions import Annotated
from mcp.tools import SlackTools




# Create MCP instance in the server
mcp = FastMCP("Slack Bot MCP Server")

bot_token = os.getenv("SLACK_BOT_TOKEN")
slack_tools = SlackTools(bot_token)

# ==================== AUTHENTICATION & TESTING ====================

@mcp.tool
async def test_slack_auth() -> Dict[str, Any]:
    """Test Slack authentication and get bot information"""
    if not slack_tools:
        raise ValueError("Slack tools not initialized")
    return await slack_tools.test_slack_auth()

# ==================== MESSAGING TOOLS ====================

@mcp.tool
async def send_slack_message(
    channel: Annotated[str, Field(description="Channel ID or name (e.g., '#general' or 'C1234567890')")],
    text: Annotated[Optional[str], Field(description="Message text to send")] = None,
    blocks: Annotated[Optional[List[Dict]], Field(description="Slack Block Kit blocks for rich formatting")] = None,
    attachments: Annotated[Optional[List[Dict]], Field(description="Message attachments (legacy)")] = None,
    thread_ts: Annotated[Optional[str], Field(description="Reply in thread to this message timestamp")] = None,
    username: Annotated[Optional[str], Field(description="Custom username for the message")] = None,
    icon_emoji: Annotated[Optional[str], Field(description="Custom emoji icon (e.g., ':robot_face:')")] = None,
    icon_url: Annotated[Optional[str], Field(description="Custom icon URL")] = None
) -> Dict[str, Any]:
    """Send a message to a Slack channel with optional rich formatting"""
    if not slack_tools:
        raise ValueError("Slack tools not initialized")
    return await slack_tools.send_slack_message(channel, text, blocks, attachments, thread_ts, username, icon_emoji, icon_url)

@mcp.tool
async def update_slack_message(
    channel: Annotated[str, Field(description="Channel ID where the message is located")],
    message_ts: Annotated[str, Field(description="Timestamp of the message to update")],
    text: Annotated[Optional[str], Field(description="New text for the message")] = None,
    blocks: Annotated[Optional[List[Dict]], Field(description="New blocks for the message")] = None,
    attachments: Annotated[Optional[List[Dict]], Field(description="New attachments for the message")] = None
) -> Dict[str, Any]:
    """Update an existing Slack message"""
    if not slack_tools:
        raise ValueError("Slack tools not initialized")
    return await slack_tools.update_slack_message(channel, message_ts, text, blocks, attachments)

@mcp.tool
async def delete_slack_message(
    channel: Annotated[str, Field(description="Channel ID where the message is located")],
    message_ts: Annotated[str, Field(description="Timestamp of the message to delete")]
) -> Dict[str, Any]:
    """Delete a Slack message"""
    if not slack_tools:
        raise ValueError("Slack tools not initialized")
    return await slack_tools.delete_slack_message(channel, message_ts)

@mcp.tool
async def schedule_slack_message(
    channel: Annotated[str, Field(description="Channel ID or name")],
    post_at: Annotated[int, Field(description="Unix timestamp when to post the message")],
    text: Annotated[Optional[str], Field(description="Message text")] = None,
    blocks: Annotated[Optional[List[Dict]], Field(description="Slack Block Kit blocks")] = None,
    attachments: Annotated[Optional[List[Dict]], Field(description="Message attachments")] = None
) -> Dict[str, Any]:
    """Schedule a message to be sent at a specific time"""
    if not slack_tools:
        raise ValueError("Slack tools not initialized")
    return await slack_tools.schedule_slack_message(channel, post_at, text, blocks, attachments)

# ==================== CHANNEL TOOLS ====================

@mcp.tool
async def list_slack_channels(
    limit: Annotated[int, Field(description="Maximum number of channels to return", ge=1, le=1000)] = 100,
    exclude_archived: Annotated[bool, Field(description="Whether to exclude archived channels")] = True,
    types: Annotated[str, Field(description="Channel types to include")] = "public_channel,private_channel",
    cursor: Annotated[Optional[str], Field(description="Pagination cursor")] = None
) -> List[Dict[str, Any]]:
    """List Slack channels in the workspace"""
    if not slack_tools:
        raise ValueError("Slack tools not initialized")
    return await slack_tools.list_slack_channels(limit, exclude_archived, types, cursor)

@mcp.tool
async def get_slack_channel_info(
    channel: Annotated[str, Field(description="Channel ID or name")]
) -> Dict[str, Any]:
    """Get detailed information about a specific Slack channel"""
    if not slack_tools:
        raise ValueError("Slack tools not initialized")
    return await slack_tools.get_slack_channel_info(channel)

@mcp.tool
async def create_slack_channel(
    name: Annotated[str, Field(description="Channel name (without # prefix)")],
    is_private: Annotated[bool, Field(description="Whether to create a private channel")] = False
) -> Dict[str, Any]:
    """Create a new Slack channel"""
    if not slack_tools:
        raise ValueError("Slack tools not initialized")
    return await slack_tools.create_slack_channel(name, is_private)

@mcp.tool
async def join_slack_channel(
    channel: Annotated[str, Field(description="Channel ID or name to join")]
) -> Dict[str, Any]:
    """Join a Slack channel"""
    if not slack_tools:
        raise ValueError("Slack tools not initialized")
    return await slack_tools.join_slack_channel(channel)

@mcp.tool
async def leave_slack_channel(
    channel: Annotated[str, Field(description="Channel ID or name to leave")]
) -> Dict[str, Any]:
    """Leave a Slack channel"""
    if not slack_tools:
        raise ValueError("Slack tools not initialized")
    return await slack_tools.leave_slack_channel(channel)

@mcp.tool
async def invite_to_slack_channel(
    channel: Annotated[str, Field(description="Channel ID or name")],
    users: Annotated[Union[str, List[str]], Field(description="User ID(s) to invite")]
) -> Dict[str, Any]:
    """Invite users to a Slack channel"""
    if not slack_tools:
        raise ValueError("Slack tools not initialized")
    return await slack_tools.invite_to_slack_channel(channel, users)

@mcp.tool
async def kick_from_slack_channel(
    channel: Annotated[str, Field(description="Channel ID or name")],
    user: Annotated[str, Field(description="User ID to remove")]
) -> Dict[str, Any]:
    """Remove a user from a Slack channel"""
    if not slack_tools:
        raise ValueError("Slack tools not initialized")
    return await slack_tools.kick_from_slack_channel(channel, user)

@mcp.tool
async def set_slack_channel_topic(
    channel: Annotated[str, Field(description="Channel ID or name")],
    topic: Annotated[str, Field(description="New topic for the channel")]
) -> Dict[str, Any]:
    """Set the topic for a Slack channel"""
    if not slack_tools:
        raise ValueError("Slack tools not initialized")
    return await slack_tools.set_slack_channel_topic(channel, topic)

@mcp.tool
async def set_slack_channel_purpose(
    channel: Annotated[str, Field(description="Channel ID or name")],
    purpose: Annotated[str, Field(description="New purpose for the channel")]
) -> Dict[str, Any]:
    """Set the purpose for a Slack channel"""
    if not slack_tools:
        raise ValueError("Slack tools not initialized")
    return await slack_tools.set_slack_channel_purpose(channel, purpose)

@mcp.tool
async def archive_slack_channel(
    channel: Annotated[str, Field(description="Channel ID or name to archive")]
) -> Dict[str, Any]:
    """Archive a Slack channel"""
    if not slack_tools:
        raise ValueError("Slack tools not initialized")
    return await slack_tools.archive_slack_channel(channel)

@mcp.tool
async def unarchive_slack_channel(
    channel: Annotated[str, Field(description="Channel ID or name to unarchive")]
) -> Dict[str, Any]:
    """Unarchive a Slack channel"""
    if not slack_tools:
        raise ValueError("Slack tools not initialized")
    return await slack_tools.unarchive_slack_channel(channel)

# ==================== USER TOOLS ====================

@mcp.tool
async def list_slack_users(
    limit: Annotated[int, Field(description="Maximum number of users to return", ge=1, le=1000)] = 100,
    cursor: Annotated[Optional[str], Field(description="Pagination cursor")] = None
) -> List[Dict[str, Any]]:
    """List users in the Slack workspace"""
    if not slack_tools:
        raise ValueError("Slack tools not initialized")
    return await slack_tools.list_slack_users(limit, cursor)

@mcp.tool
async def get_slack_user_info(
    user: Annotated[str, Field(description="User ID to get information about")]
) -> Dict[str, Any]:
    """Get detailed information about a specific Slack user"""
    if not slack_tools:
        raise ValueError("Slack tools not initialized")
    return await slack_tools.get_slack_user_info(user)

@mcp.tool
async def get_slack_user_profile(
    user: Annotated[str, Field(description="User ID to get profile for")]
) -> Dict[str, Any]:
    """Get user's profile information"""
    if not slack_tools:
        raise ValueError("Slack tools not initialized")
    return await slack_tools.get_slack_user_profile(user)

@mcp.tool
async def set_slack_presence(
    presence: Annotated[Literal["auto", "away"], Field(description="Presence to set (auto or away)")]
) -> Dict[str, Any]:
    """Set bot's presence status"""
    if not slack_tools:
        raise ValueError("Slack tools not initialized")
    return await slack_tools.set_slack_presence(presence)

# ==================== FILE TOOLS ====================

@mcp.tool
async def upload_slack_file(
    channels: Annotated[Union[str, List[str]], Field(description="Channel(s) to upload file to")],
    file_source: Annotated[str, Field(description="File source: URL, local path, or text content")],
    filename: Annotated[Optional[str], Field(description="Filename (required for text content)")] = None,
    title: Annotated[Optional[str], Field(description="File title")] = None,
    initial_comment: Annotated[Optional[str], Field(description="Comment to add with file")] = None,
    thread_ts: Annotated[Optional[str], Field(description="Thread timestamp if uploading to thread")] = None
) -> Dict[str, Any]:
    """Upload a file to Slack (supports URLs, local paths, or text content)"""
    if not slack_tools:
        raise ValueError("Slack tools not initialized")
    return await slack_tools.upload_slack_file(channels, file_source, filename, title, initial_comment, thread_ts)

@mcp.tool
async def list_slack_files(
    count: Annotated[int, Field(description="Number of files to return", ge=1, le=1000)] = 20,
    channel: Annotated[Optional[str], Field(description="Filter by channel")] = None,
    user: Annotated[Optional[str], Field(description="Filter by user")] = None,
    ts_from: Annotated[Optional[str], Field(description="Filter files created after this timestamp")] = None,
    ts_to: Annotated[Optional[str], Field(description="Filter files created before this timestamp")] = None,
    types: Annotated[Optional[str], Field(description="Filter by file types (comma-separated)")] = None,
    page: Annotated[int, Field(description="Page number for pagination", ge=1)] = 1
) -> List[Dict[str, Any]]:
    """List files in the Slack workspace"""
    if not slack_tools:
        raise ValueError("Slack tools not initialized")
    return await slack_tools.list_slack_files(count, channel, user, ts_from, ts_to, types, page)

@mcp.tool
async def get_slack_file_info(
    file_id: Annotated[str, Field(description="File ID to get information about")]
) -> Dict[str, Any]:
    """Get information about a specific file"""
    if not slack_tools:
        raise ValueError("Slack tools not initialized")
    return await slack_tools.get_slack_file_info(file_id)

@mcp.tool
async def delete_slack_file(
    file_id: Annotated[str, Field(description="File ID to delete")]
) -> Dict[str, Any]:
    """Delete a file from Slack"""
    if not slack_tools:
        raise ValueError("Slack tools not initialized")
    return await slack_tools.delete_slack_file(file_id)

# ==================== REACTION TOOLS ====================

@mcp.tool
async def add_slack_reaction(
    channel: Annotated[str, Field(description="Channel ID where the message is located")],
    message_ts: Annotated[str, Field(description="Timestamp of the message to react to")],
    emoji: Annotated[str, Field(description="Emoji name (without colons, e.g., 'thumbsup')")]
) -> Dict[str, Any]:
    """Add an emoji reaction to a Slack message"""
    if not slack_tools:
        raise ValueError("Slack tools not initialized")
    return await slack_tools.add_slack_reaction(channel, message_ts, emoji)

@mcp.tool
async def remove_slack_reaction(
    channel: Annotated[str, Field(description="Channel ID where the message is located")],
    message_ts: Annotated[str, Field(description="Timestamp of the message")],
    emoji: Annotated[str, Field(description="Emoji name to remove (without colons)")]
) -> Dict[str, Any]:
    """Remove an emoji reaction from a Slack message"""
    if not slack_tools:
        raise ValueError("Slack tools not initialized")
    return await slack_tools.remove_slack_reaction(channel, message_ts, emoji)

@mcp.tool
async def get_slack_reactions(
    channel: Annotated[str, Field(description="Channel ID where the message is located")],
    message_ts: Annotated[str, Field(description="Timestamp of the message")]
) -> Dict[str, Any]:
    """Get reactions for a message"""
    if not slack_tools:
        raise ValueError("Slack tools not initialized")
    return await slack_tools.get_slack_reactions(channel, message_ts)

# ==================== HISTORY & INFORMATION TOOLS ====================

@mcp.tool
async def get_slack_channel_history(
    channel: Annotated[str, Field(description="Channel ID to get history from")],
    limit: Annotated[int, Field(description="Number of messages to retrieve", ge=1, le=1000)] = 20,
    cursor: Annotated[Optional[str], Field(description="Pagination cursor")] = None,
    latest: Annotated[Optional[str], Field(description="Latest message timestamp to include")] = None,
    oldest: Annotated[Optional[str], Field(description="Oldest message timestamp to include")] = None
) -> List[Dict[str, Any]]:
    """Get message history from a Slack channel"""
    if not slack_tools:
        raise ValueError("Slack tools not initialized")
    return await slack_tools.get_slack_channel_history(channel, limit, cursor, latest, oldest)

@mcp.tool
async def get_slack_thread_replies(
    channel: Annotated[str, Field(description="Channel ID where the thread is located")],
    thread_ts: Annotated[str, Field(description="Timestamp of the parent message")],
    limit: Annotated[int, Field(description="Number of replies to retrieve", ge=1, le=1000)] = 100,
    cursor: Annotated[Optional[str], Field(description="Pagination cursor")] = None
) -> List[Dict[str, Any]]:
    """Get replies to a threaded message"""
    if not slack_tools:
        raise ValueError("Slack tools not initialized")
    return await slack_tools.get_slack_thread_replies(channel, thread_ts, limit, cursor)

# ==================== PIN TOOLS ====================

@mcp.tool
async def pin_slack_message(
    channel: Annotated[str, Field(description="Channel ID where the message is located")],
    message_ts: Annotated[str, Field(description="Timestamp of the message to pin")]
) -> Dict[str, Any]:
    """Pin a message to a Slack channel"""
    if not slack_tools:
        raise ValueError("Slack tools not initialized")
    return await slack_tools.pin_slack_message(channel, message_ts)

@mcp.tool
async def unpin_slack_message(
    channel: Annotated[str, Field(description="Channel ID where the message is located")],
    message_ts: Annotated[str, Field(description="Timestamp of the message to unpin")]
) -> Dict[str, Any]:
    """Unpin a message from a Slack channel"""
    if not slack_tools:
        raise ValueError("Slack tools not initialized")
    return await slack_tools.unpin_slack_message(channel, message_ts)

@mcp.tool
async def list_slack_pins(
    channel: Annotated[str, Field(description="Channel ID to list pins from")]
) -> List[Dict[str, Any]]:
    """List pinned items in a Slack channel"""
    if not slack_tools:
        raise ValueError("Slack tools not initialized")
    return await slack_tools.list_slack_pins(channel)

# ==================== BOOKMARK TOOLS ====================

@mcp.tool
async def add_slack_bookmark(
    channel_id: Annotated[str, Field(description="Channel ID to add bookmark to")],
    title: Annotated[str, Field(description="Bookmark title")],
    type: Annotated[str, Field(description="Bookmark type")],
    link: Annotated[Optional[str], Field(description="Bookmark URL")] = None,
    emoji: Annotated[Optional[str], Field(description="Bookmark emoji")] = None
) -> Dict[str, Any]:
    """Add a bookmark to a Slack channel"""
    if not slack_tools:
        raise ValueError("Slack tools not initialized")
    return await slack_tools.add_slack_bookmark(channel_id, title, type, link, emoji)

@mcp.tool
async def remove_slack_bookmark(
    channel_id: Annotated[str, Field(description="Channel ID where the bookmark is located")],
    bookmark_id: Annotated[str, Field(description="Bookmark ID to remove")]
) -> Dict[str, Any]:
    """Remove a bookmark from a Slack channel"""
    if not slack_tools:
        raise ValueError("Slack tools not initialized")
    return await slack_tools.remove_slack_bookmark(channel_id, bookmark_id)

@mcp.tool
async def list_slack_bookmarks(
    channel_id: Annotated[str, Field(description="Channel ID to list bookmarks from")]
) -> List[Dict[str, Any]]:
    """List bookmarks in a Slack channel"""
    if not slack_tools:
        raise ValueError("Slack tools not initialized")
    return await slack_tools.list_slack_bookmarks(channel_id)

# ==================== USERGROUP TOOLS ====================

@mcp.tool
async def create_slack_usergroup(
    name: Annotated[str, Field(description="Usergroup name")],
    handle: Annotated[Optional[str], Field(description="Usergroup handle (without @)")] = None,
    description: Annotated[Optional[str], Field(description="Usergroup description")] = None,
    channels: Annotated[Optional[List[str]], Field(description="Default channels for the usergroup")] = None
) -> Dict[str, Any]:
    """Create a new user group"""
    if not slack_tools:
        raise ValueError("Slack tools not initialized")
    return await slack_tools.create_slack_usergroup(name, handle, description, channels)

@mcp.tool
async def list_slack_usergroups(
    include_disabled: Annotated[bool, Field(description="Include disabled usergroups")] = False
) -> List[Dict[str, Any]]:
    """List user groups in the workspace"""
    if not slack_tools:
        raise ValueError("Slack tools not initialized")
    return await slack_tools.list_slack_usergroups(include_disabled)

@mcp.tool
async def update_slack_usergroup(
    usergroup: Annotated[str, Field(description="Usergroup ID to update")],
    name: Annotated[Optional[str], Field(description="New name for the usergroup")] = None,
    handle: Annotated[Optional[str], Field(description="New handle for the usergroup")] = None,
    description: Annotated[Optional[str], Field(description="New description for the usergroup")] = None
) -> Dict[str, Any]:
    """Update a user group"""
    if not slack_tools:
        raise ValueError("Slack tools not initialized")
    return await slack_tools.update_slack_usergroup(usergroup, name, handle, description)

@mcp.tool
async def disable_slack_usergroup(
    usergroup: Annotated[str, Field(description="Usergroup ID to disable")]
) -> Dict[str, Any]:
    """Disable a user group"""
    if not slack_tools:
        raise ValueError("Slack tools not initialized")
    return await slack_tools.disable_slack_usergroup(usergroup)

# ==================== TEAM TOOLS ====================

@mcp.tool
async def get_slack_team_info() -> Dict[str, Any]:
    """Get information about the Slack workspace/team"""
    if not slack_tools:
        raise ValueError("Slack tools not initialized")
    return await slack_tools.get_slack_team_info()

@mcp.tool
async def get_slack_team_profile() -> Dict[str, Any]:
    """Get team profile fields"""
    if not slack_tools:
        raise ValueError("Slack tools not initialized")
    return await slack_tools.get_slack_team_profile()

# ==================== EMOJI TOOLS ====================

@mcp.tool
async def list_slack_emoji() -> List[Dict[str, Any]]:
    """List custom emoji for the team"""
    if not slack_tools:
        raise ValueError("Slack tools not initialized")
    return await slack_tools.list_slack_emoji()

# ==================== DND (DO NOT DISTURB) TOOLS ====================

@mcp.tool
async def get_slack_dnd_info(
    user: Annotated[Optional[str], Field(description="User ID to get DND info for (defaults to current user)")] = None
) -> Dict[str, Any]:
    """Get Do Not Disturb information for a user"""
    if not slack_tools:
        raise ValueError("Slack tools not initialized")
    return await slack_tools.get_slack_dnd_info(user)

@mcp.tool
async def get_slack_team_dnd_info(
    users: Annotated[Optional[List[str]], Field(description="List of user IDs to get DND info for")] = None
) -> Dict[str, Any]:
    """Get Do Not Disturb information for multiple users"""
    if not slack_tools:
        raise ValueError("Slack tools not initialized")
    return await slack_tools.get_slack_team_dnd_info(users)


if __name__ == "__main__":
    print("Starting FastMCP server on http://0.0.0.0:8000/mcp")
    mcp.run(transport="http", host="0.0.0.0", port=8000, path="/mcp")