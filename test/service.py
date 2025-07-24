#!/usr/bin/env python3
"""
Slack API Test Script - Tests SlackBotAPIService functionality only
"""

import os
import asyncio
import sys
from datetime import datetime
from pathlib import Path

# Setup imports
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    from mcp.services.slack_bot_api import SlackBotAPIService
except ImportError as e:
    print(f"❌ Import failed: {e}")
    sys.exit(1)


class SlackAPITester:
    """Test suite for SlackBotAPIService functionality only"""
    
    def __init__(self):
        self.bot_token = os.getenv("BOT_TOKEN")
        self.channel_id = os.getenv("CHANNEL_ID")
        
        if not self.bot_token or not self.channel_id:
            raise ValueError("BOT_TOKEN and CHANNEL_ID required")
            
        self.slack = SlackBotAPIService(self.bot_token)
        self.test_message_ts = None
        self.test_file_id = None
    
    async def test_auth(self):
        """Test authentication"""
        result = await self.slack.test_auth()
        if result.ok:
            print(f"✅ Auth: {result.data.get('user', 'Unknown')}")
            return True
        print(f"❌ Auth failed: {result.error}")
        return False
    
    async def test_send_message(self):
        """Test basic messaging"""
        result = await self.slack.send_message(
            channel=self.channel_id,
            text=f"🧪 Test - {datetime.now().strftime('%H:%M:%S')}"
        )
        if result.ok:
            self.test_message_ts = result.data.get("ts")
            print(f"✅ Message sent: {self.test_message_ts}")
            return True
        print(f"❌ Message failed: {result.error}")
        return False
    
    async def test_rich_message(self):
        """Test rich message with blocks"""
        blocks = [{
            "type": "section",
            "text": {"type": "mrkdwn", "text": "*🚀 Rich Test*\nFormatted message!"}
        }]
        result = await self.slack.send_message(
            channel=self.channel_id, text="Rich test", blocks=blocks
        )
        if result.ok:
            print("✅ Rich message sent")
            return True
        print(f"❌ Rich message failed: {result.error}")
        return False
    
    async def test_update_message(self):
        """Test message updates"""
        if not self.test_message_ts:
            return False
        result = await self.slack.update_message(
            channel=self.channel_id,
            ts=self.test_message_ts,
            text="🔄 Updated test message"
        )
        if result.ok:
            print("✅ Message updated")
            return True
        print(f"❌ Update failed: {result.error}")
        return False
    
    async def test_reactions(self):
        """Test reactions"""
        if not self.test_message_ts:
            return False
        result = await self.slack.add_reaction("thumbsup", self.channel_id, self.test_message_ts)
        if result.ok:
            print("✅ Reaction added")
            return True
        print(f"❌ Reaction failed: {result.error}")
        return False
    
    async def test_channels(self):
        """Test channel operations"""
        result = await self.slack.list_channels(limit=5)
        if result.ok:
            channels = result.data.get("channels", [])
            print(f"✅ Channels: {len(channels)} found")
            return True
        print(f"❌ Channels failed: {result.error}")
        return False
    
    async def test_channel_info(self):
        """Test channel info"""
        result = await self.slack.get_channel_info(self.channel_id)
        if result.ok:
            name = result.data.get("channel", {}).get("name", "Unknown")
            print(f"✅ Channel info: #{name}")
            return True
        print(f"❌ Channel info failed: {result.error}")
        return False
    
    async def test_users(self):
        """Test user operations"""
        result = await self.slack.list_users(limit=3)
        if result.ok:
            users = result.data.get("members", [])
            print(f"✅ Users: {len(users)} found")
            return True
        print(f"❌ Users failed: {result.error}")
        return False
    
    async def test_upload_url(self):
        """Test upload from URL"""
        test_url = "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"
        result = await self.slack.upload_file(
            channels=self.channel_id,
            file_source=test_url,
            title="Test PDF"
        )
        if result.ok:
            file_info = result.data.get("file", {})
            self.test_file_id = file_info.get("id")
            print(f"✅ URL upload: {file_info.get('name', 'Unknown')}")
            return True
        print(f"❌ URL upload failed: {result.error}")
        return False
    
    async def test_upload_content(self):
        """Test upload text content"""
        content = f"Test content - {datetime.now().isoformat()}"
        result = await self.slack.upload_file(
            channels=self.channel_id,
            file_source=content,
            filename="test.txt",
            title="Test Content"
        )
        if result.ok:
            print("✅ Content upload successful")
            return True
        print(f"❌ Content upload failed: {result.error}")
        return False
    
    async def test_file_operations(self):
        """Test file list and info"""
        result = await self.slack.list_files(count=3)
        if result.ok:
            files = result.data.get("files", [])
            print(f"✅ File list: {len(files)} files")
            return True
        print(f"❌ File list failed: {result.error}")
        return False
    
    async def test_pins(self):
        """Test pin operations"""
        if not self.test_message_ts:
            return False
        result = await self.slack.pin_message(self.channel_id, self.test_message_ts)
        if result.ok:
            print("✅ Pin successful")
            return True
        print(f"❌ Pin failed: {result.error}")
        return False
    
    async def test_channel_history(self):
        """Test channel history"""
        result = await self.slack.get_channel_history(self.channel_id, limit=3)
        if result.ok:
            messages = result.data.get("messages", [])
            print(f"✅ History: {len(messages)} messages")
            return True
        print(f"❌ History failed: {result.error}")
        return False
    
    async def test_team_info(self):
        """Test team operations"""
        result = await self.slack.get_team_info()
        if result.ok:
            team = result.data.get("team", {}).get("name", "Unknown")
            print(f"✅ Team: {team}")
            return True
        print(f"❌ Team info failed: {result.error}")
        return False
    
    async def test_emoji(self):
        """Test emoji operations"""
        result = await self.slack.list_emoji()
        if result.ok:
            emoji = result.data.get("emoji", {})
            print(f"✅ Emoji: {len(emoji)} custom")
            return True
        print(f"❌ Emoji failed: {result.error}")
        return False
    
    async def test_presence(self):
        """Test presence operations"""
        result = await self.slack.set_user_presence("auto")
        if result.ok:
            print("✅ Presence set")
            return True
        print(f"❌ Presence failed: {result.error}")
        return False
    
    async def test_usergroups(self):
        """Test usergroup operations"""
        result = await self.slack.list_usergroups()
        if result.ok:
            groups = result.data.get("usergroups", [])
            print(f"✅ Usergroups: {len(groups)} found")
            return True
        print(f"❌ Usergroups failed: {result.error}")
        return False
    
    async def test_bookmarks(self):
        """Test bookmark operations"""
        result = await self.slack.list_bookmarks(self.channel_id)
        if result.ok:
            bookmarks = result.data.get("bookmarks", [])
            print(f"✅ Bookmarks: {len(bookmarks)} found")
            return True
        print(f"❌ Bookmarks failed: {result.error}")
        return False
    
    async def test_dnd(self):
        """Test DND operations"""
        result = await self.slack.get_dnd_info()
        if result.ok:
            dnd_enabled = result.data.get("dnd_enabled", False)
            print(f"✅ DND info: {'enabled' if dnd_enabled else 'disabled'}")
            return True
        print(f"❌ DND failed: {result.error}")
        return False
    
    async def run_all_tests(self):
        """Run comprehensive test suite"""
        print("🧪 Slack Bot API Test Suite")
        print("=" * 40)
        
        tests = [
            ("Auth", self.test_auth),
            ("Send Message", self.test_send_message),
            ("Rich Message", self.test_rich_message),
            ("Update Message", self.test_update_message),
            ("Reactions", self.test_reactions),
            ("Channels", self.test_channels),
            ("Channel Info", self.test_channel_info),
            ("Users", self.test_users),
            ("Upload URL", self.test_upload_url),
            ("Upload Content", self.test_upload_content),
            ("File Operations", self.test_file_operations),
            ("Pins", self.test_pins),
            ("History", self.test_channel_history),
            ("Team Info", self.test_team_info),
            ("Emoji", self.test_emoji),
            ("Presence", self.test_presence),
            ("Usergroups", self.test_usergroups),
            ("Bookmarks", self.test_bookmarks),
            ("DND", self.test_dnd),
        ]
        
        results = {}
        for test_name, test_func in tests:
            try:
                results[test_name] = await test_func()
            except Exception as e:
                print(f"❌ {test_name}: {str(e)[:50]}...")
                results[test_name] = False
        
        # Summary
        print("\n" + "=" * 40)
        passed = sum(results.values())
        total = len(results)
        
        # Show results in compact format
        for test_name, result in results.items():
            status = "✅" if result else "❌"
            print(f"{status} {test_name:<15}")
        
        print(f"\n🏁 Results: {passed}/{total} passed")
        
        if passed == total:
            print("🎉 All tests passed! Ready for FastMCP!")
        elif passed > total * 0.85:
            print("⚠️  Most tests passed. Ready for FastMCP!")
        else:
            print("🔧 Several failures. Check permissions and setup.")
        
        return passed >= total * 0.85  # 85% pass rate considered success


async def main():
    """Main test runner"""
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError:
        pass
    
    try:
        tester = SlackAPITester()
        success = await tester.run_all_tests()
        sys.exit(0 if success else 1)
    except ValueError as e:
        print(f"❌ Config error: {e}")
        print("Set BOT_TOKEN and CHANNEL_ID in environment")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())