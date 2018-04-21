/***********************************************************************
Config - Daemon for distributed VR device driver architecture.
Copyright (c) 2014-2016 Oliver Kreylos

This file is part of the Vrui VR Device Driver Daemon (VRDeviceDaemon).

The Vrui VR Device Driver Daemon is free software; you can redistribute
it and/or modify it under the terms of the GNU General Public License as
published by the Free Software Foundation; either version 2 of the
License, or (at your option) any later version.

The Vrui VR Device Driver Daemon is distributed in the hope that it will
be useful, but WITHOUT ANY WARRANTY; without even the implied warranty
of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License along
with the Vrui VR Device Driver Daemon; if not, write to the Free
Software Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA
02111-1307 USA
***********************************************************************/

#ifndef VRDEVICEDAEMON_CONFIG_INCLUDED
#define VRDEVICEDAEMON_CONFIG_INCLUDED

#define VRDEVICEDAEMON_CONFIG_VRDEVICESDIR "/usr/local/lib/x86_64-linux-gnu/Vrui-4.5/VRDevices"
#define VRDEVICEDAEMON_CONFIG_VRCALIBRATORSDIR "/usr/local/lib/x86_64-linux-gnu/Vrui-4.5/VRCalibrators"
#define VRDEVICEDAEMON_CONFIG_DSONAMETEMPLATE "lib%s.so"

#define VRDEVICEDAEMON_CONFIG_CONFIGFILENAME "/usr/local/etc/Vrui-4.5/VRDevices.cfg"
#define VRDEVICEDAEMON_CONFIG_CONFIGDIR "/usr/local/etc/Vrui-4.5/VRDeviceDaemon"

#define VRDEVICEDAEMON_CONFIG_INPUT_H_HAS_STRUCTS 1

#endif
