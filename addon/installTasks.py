# -*- coding: utf-8 -*-
# Part of tesseractOCR add-on for NVDA.
# Module to choose the appropriate Tesseract library to the system architecture and to preserve the downloaded trainedData files
# written by Rui Fontes <rui.fontes@tiflotecnia.com>, Ângelo Abrantes <ampa4374@gmail.com> and Abel Passos do Nascimento Jr. <abel.passos@gmail.com>
# Thanks to ChatGPT by some hints specially in determining the system architecture
# Copyright (C) 2023-2024 Rui Fontes <rui.fontes@tiflotecnia.com>
# This file is covered by the GNU General Public License.

# import the necessary modules
import os
import platform
import shutil
from addonHandler import ADDON_PENDINGINSTALL_SUFFIX
from globalVars import appArgs

def is_64bit_system():
	# Detect the real system architecture, even if running in a 32-bit process.
	print("system = " + str(os.environ.get("PROCESSOR_ARCHITEW6432")))
	return os.environ.get("PROCESSOR_ARCHITEW6432") in ("AMD64", "ARM64")

def copy_tesseract_library_to_pending():
	# Copy the appropriate Tesseract library to the pending install folder.
	# Directory for 64-bit libraries
	source_64bit = os.path.abspath(
		os.path.join(appArgs.configPath, "addons", "tesseractOCR" + ADDON_PENDINGINSTALL_SUFFIX, "libs", "tesseract64")
	)
	# Destination path for the Tesseract library in the pending install add-on
	destination = os.path.abspath(
		os.path.join(appArgs.configPath, "addons", "tesseractOCR" + ADDON_PENDINGINSTALL_SUFFIX, "globalPlugins", "tesseractOCR", "tesseract")
	)
	source_dir = source_64bit
	# Ensure the destination directory exists and is empty
	if os.path.exists(destination):
		shutil.rmtree(destination)
	os.makedirs(destination)
	# Copy all files and directories from source_dir to destination
	shutil.copytree(source_dir, destination, dirs_exist_ok=True)

def copy_xpdf_library_to_pending():
	# Copy the appropriate xpdf library to the pending install folder.
	# Directory for  64-bit libraries
	source_64bit = os.path.abspath(
		os.path.join(appArgs.configPath, "addons", "tesseractOCR" + ADDON_PENDINGINSTALL_SUFFIX, "libs", "xpdf-tools64")
	)
	# Destination path for the xpdf library in the pending install add-on
	destination = os.path.abspath(
		os.path.join(appArgs.configPath, "addons", "tesseractOCR" + ADDON_PENDINGINSTALL_SUFFIX, "globalPlugins", "tesseractOCR", "xpdf-tools")
	)
	source_dir = source_64bit
	# Ensure the destination directory exists and is empty
	if os.path.exists(destination):
		shutil.rmtree(destination)
	os.makedirs(destination)
	# Copy all files and directories from source_dir to destination
	shutil.copytree(source_dir, destination, dirs_exist_ok=True)
	# Remove the libs directory after copying the appropriate library
	libs_path = os.path.abspath(
		os.path.join(appArgs.configPath, "addons", "tesseractOCR" + ADDON_PENDINGINSTALL_SUFFIX, "libs")
	)
	if os.path.exists(libs_path):
		shutil.rmtree(libs_path)

def move_existing_tessdata_to_pending():
	# Move the existing tessdata folder from the current add-on to the pending install.
	# Current path for the tessdata directory
	configFilePath = os.path.abspath(
		os.path.join(appArgs.configPath, "addons", "tesseractOCR", "globalPlugins", "tesseractOCR", "tesseract", "tessdata")
	)
	# Pending installation path for the new add-on
	pendingInstallPath = os.path.abspath(
		os.path.join(appArgs.configPath, "addons", "tesseractOCR" + ADDON_PENDINGINSTALL_SUFFIX, "globalPlugins", "tesseractOCR", "tesseract", "tessdata")
	)
	# If the current tessdata folder exists, move it to the pending install path
	if os.path.isdir(configFilePath):
		# Remove any existing tessdata folder in the pending install directory
		if os.path.isdir(pendingInstallPath):
			shutil.rmtree(pendingInstallPath)
		# Move the existing tessdata to the pending install location
		shutil.move(configFilePath, pendingInstallPath)

def onInstall():
	# Function called during the add-on installation.
	# Copy the appropriate Tesseract and xpdf libraries to the pending install location
	copy_tesseract_library_to_pending()
	copy_xpdf_library_to_pending()
	# Move the existing tessdata from the old add-on to the new pending install location
	move_existing_tessdata_to_pending()
