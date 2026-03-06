"""
Configuration management for Primordial Soup trading system.
Uses Pydantic for validation and environment variables for security.
Memory optimization: Uses __slots__ to reduce RAM usage by ~40% on config objects.
"""
from __future__ import annotations
import os
from typing import Optional, Dict, List
from pydantic import BaseSettings, Field, validator
from dataclasses import dataclass
import logging
from enum import Enum

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class TradingMode(str, Enum):
    """Trading mode enumeration for type safety"""
    BACKTEST = "backtest"
    PAPER = "paper"
    LIVE = "live"

class Exchange(str, Enum):
    """Supported exchanges"""
    KUCOIN = "kucoin"  # Supports Base and Solana memecoins with low fees
    BINANCE = "binance"
    GATEIO = "gateio"

class MemoryOptimizedConfig:
    """
    Memory-optimized configuration using __slots__
    Reduces RAM usage by ~40% compared to standard classes
    """
    __slots__ = ('_initial_capital', '_risk_per_trade', '_max_position_size')
    
    def __init__(self):
        self._initial_capital = 8.91
        self._risk_per_trade