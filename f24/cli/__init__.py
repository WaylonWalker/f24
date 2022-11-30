# SPDX-FileCopyrightText: 2022-present Waylon S. Walker <waylon@waylonwalker.com>
#
# SPDX-License-Identifier: MIT

import random
import time

import click
import pyautogui

from f24.__about__ import __version__


@click.group(
    context_settings={"help_option_names": ["-h", "--help"]},
    invoke_without_command=True,
)
@click.version_option(version=__version__, prog_name="f24")
@click.pass_context
def f24(ctx: click.Context):
    print("hey im here")
    pyautogui.press("f24")
    time.sleep(random.randint(60, 5 * 60))
