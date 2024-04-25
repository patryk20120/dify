from typing import Any, Union
import requests

from core.tools.tool.builtin_tool import BuiltinTool
from core.tools.entities.tool_entities import ToolInvokeMessage


class CrawlTool(BuiltinTool):
    def _invoke(self, user_id: str, tool_parameters: dict[str, Any]) -> Union[ToolInvokeMessage, list[ToolInvokeMessage]]:
        url = "https://api.firecrawl.dev/v0/crawl"
        headers = {
            "Authorization": f"Bearer {self.runtime.credentials['firecrawl_api_key']}",
            "Content-Type": "application/json"
        }
        response = requests.post(url, json=tool_parameters, headers=headers)
        return self.create_text_message(response.text)