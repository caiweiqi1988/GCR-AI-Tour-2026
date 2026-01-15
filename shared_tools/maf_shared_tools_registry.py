"""
Shared Tools Registry for MAF Workflows
This is the source of truth for all local deterministic tools.
"""
import sys
from pathlib import Path
from typing import Any, Callable, Dict


class SharedToolsRegistry:
    """Registry for local deterministic tools."""
    
    def __init__(self):
        self._tools: Dict[str, Callable] = {}
    
    def register_tool(self, name: str, func: Callable) -> None:
        """Register a tool with the given name."""
        self._tools[name] = func
    
    def get_tool(self, name: str) -> Callable:
        """Get a tool by name."""
        if name not in self._tools:
            raise KeyError(f"Tool '{name}' not found in registry")
        return self._tools[name]
    
    def list_tools(self) -> list:
        """List all registered tool names."""
        return sorted(self._tools.keys())
    
    def has_tool(self, name: str) -> bool:
        """Check if a tool is registered."""
        return name in self._tools


def get_registry() -> SharedToolsRegistry:
    """Get or create the shared tools registry instance."""
    registry = SharedToolsRegistry()
    
    # Auto-discover and register tools from shared_tools directory
    shared_tools_dir = Path(__file__).parent
    
    # Import and register tools from social_signal_tools
    try:
        from . import social_signal_tools
        if hasattr(social_signal_tools, 'register_tools'):
            social_signal_tools.register_tools(registry)
    except ImportError:
        pass
    
    # Add more tool modules here as needed
    # try:
    #     from . import other_tools
    #     if hasattr(other_tools, 'register_tools'):
    #         other_tools.register_tools(registry)
    # except ImportError:
    #     pass
    
    return registry


if __name__ == "__main__":
    # Allow running as standalone to list tools
    registry = get_registry()
    print("Registered tools:")
    for tool_name in registry.list_tools():
        print(f"  - {tool_name}")
