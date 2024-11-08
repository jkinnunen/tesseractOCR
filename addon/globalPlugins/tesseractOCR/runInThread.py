#-*- coding: utf-8 -*-
# Module to manage the threads with beeps to signalize the working state of the add-on, get from NVDAExtensionGlobalPlugin
# NVDAExtensionGlobalPlugin/runInThread.py
# A part of NVDAExtensionGlobalPlugin add-on
# Copyright (C) 2017 - 2020 paulber19
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.

# Import the necessary modules
from .vars import *
from logHandler import log
import tones
import threading
import ui
import addonHandler

# To start the translation process
addonHandler.initTranslation()


class RepeatTask(threading.Thread):
	_delay = None
	_armed = False

	def __init__(self, isRunning=None):
		if self._delay is None:
			log.error("Cannot create repeatTask thread because delay is none")
			return
		self.isRunning = isRunning
		super(RepeatTask, self).__init__()
		self._stopevent = threading.Event()

	def task(self):
		# must be overwritten
		return

		tones.beep(400, 200)

	def run(self):
		if self._delay is None:
			log.error("Cannot start repeatTask thread because not delay")
			return
		while not self._stopevent.is_set():
			self._stopevent.wait(self._delay)
			if self.isRunning is not None and not self.isRunning():
				# interrupted before stop
				# Translators: message to user to report an interuption before stop.
				ui.message(_("interrupted"))
				break
			self.task()

	def stop(self):
		self._stopevent.set()


class RepeatBeep(RepeatTask):
	def __init__(self, delay=2.0, beep=(200, 200), isRunning=None):
		self._delay = delay
		self.beep = beep
		super(RepeatBeep, self).__init__(isRunning)

	def task(self):
		# Verify if beeps should be used
		if not config.conf["tesseractOCR"].get("enableBeep", True):
			return  # If beeps are desabilited do nothing
		if self._stopevent.is_set():
			return
		(frequence, length) = self.beep
		tones.beep(frequence, length)
