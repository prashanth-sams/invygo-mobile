#!/usr/bin/env python
import os
from typing import Any, Dict, Optional
from src.helpers.constants import *


def get_desired_capabilities(app: Optional[str] = None) -> Dict[str, Any]:
    """
    This module contains the desired capabilities for the appium driver
    """
    
    desired_caps: Dict[str, Any] = {
        'appium:deviceName': CAPS['DEVICE_NAME'],
        'appium:automationName': CAPS['AUTOMATION_NAME'],
        'platformName': CAPS['PLATFORM_NAME'],
        'browserName': CAPS['BROWSER_NAME'],
        'appium:systemPort' : CAPS['SYSTEM_PORT'],
        'appium:autoGrantPermissions': True,
        'appium:chromedriverExecutable': CAPS['CHROMEDRIVER_EXECUTABLE'],
        "appium:ensureWebviewsHavePages": True,
        "appium:nativeWebScreenshot": True,
        "appium:newCommandTimeout": 3600,
        "appium:connectHardwareKeyboard": True,
        'uiautomator2ServerInstallTimeout': 120000,
        'adbExecTimeout': 120000,
        'noReset': True,
    }

    if app is not None:
        desired_caps['app'] = f'{os.popen("pwd").read().rstrip()}/apps/{app}'

    return desired_caps