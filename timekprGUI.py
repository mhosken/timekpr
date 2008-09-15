#!/usr/bin/env python

import sys, glob, os
try:
 	import pygtk
  	pygtk.require("2.0")
except:
  	pass
try:
	import gtk
  	import gtk.glade
except:
	sys.exit(1)

class timekprGUI:
	"""This is the PyWine application"""

	def __init__(self):
		
		#Set the Glade file
		self.gladefile = "/usr/local/bin/Timekpr.glade"
		self.wTree = gtk.glade.XML(self.gladefile, "window1")
		self.limitSpin0 = self.wTree.get_widget("limitSpin0")
		self.limitSpin1 = self.wTree.get_widget("limitSpin1")
		self.limitSpin2 = self.wTree.get_widget("limitSpin2")
		self.limitSpin3 = self.wTree.get_widget("limitSpin3")
		self.limitSpin4 = self.wTree.get_widget("limitSpin4")
		self.limitSpin5 = self.wTree.get_widget("limitSpin5")
		self.limitSpin6 = self.wTree.get_widget("limitSpin6")
		self.fromSpin0 = self.wTree.get_widget("fromSpin0")
		self.fromSpin1 = self.wTree.get_widget("fromSpin1")
		self.fromSpin2 = self.wTree.get_widget("fromSpin2")
		self.fromSpin3 = self.wTree.get_widget("fromSpin3")
		self.fromSpin4 = self.wTree.get_widget("fromSpin4")
		self.fromSpin5 = self.wTree.get_widget("fromSpin5")
		self.fromSpin6 = self.wTree.get_widget("fromSpin6")
		self.toSpin0 = self.wTree.get_widget("toSpin0")
		self.toSpin1 = self.wTree.get_widget("toSpin1")
		self.toSpin2 = self.wTree.get_widget("toSpin2")
		self.toSpin3 = self.wTree.get_widget("toSpin3")
		self.toSpin4 = self.wTree.get_widget("toSpin4")
		self.toSpin5 = self.wTree.get_widget("toSpin5")
		self.toSpin6 = self.wTree.get_widget("toSpin6")
		self.singleLimits = self.wTree.get_widget("singleLimits")
		self.singleBoundaries = self.wTree.get_widget("singleBoundaries")
		self.limitCheck = self.wTree.get_widget("limitCheck")
		self.boundariesCheck = self.wTree.get_widget("boundariesCheck")
		self.userSelect = self.wTree.get_widget("userSelect")
		self.extendLimitsButton = self.wTree.get_widget("extendLimitsButton")
		self.rewardButton = self.wTree.get_widget("rewardButton")
		self.rewardSpin = self.wTree.get_widget("rewardSpin")
		self.configRoot = '/var/lib/timekpr/'

		dic = { "on_limitCheck_toggled" : \
			self.limitCheck_toggled,
			"on_boundariesCheck_toggled" : \
			self.boundariesCheck_toggled,
			"on_rewardButton_clicked" : \
			self.rewardButton_clicked,
			"on_extendLimitsButton_clicked" : \
			self.extendLimitsButton_clicked,
			"on_apply_clicked" : \
			self.apply_clicked,
			"on_singleBoundaries_toggled" : \
			self.singleBoundariesCheck_toggled,
			"on_singleLimits_toggled" : \
			self.singleLimitsCheck_toggled,
			"on_ok_clicked" : \
			self.ok_clicked,
			"on_cancel_clicked" : \
			self.cancel_clicked }

		self.wTree.signal_autoconnect (dic)
		self.root = "/home/"
		self.wildcard = "*"
		for folder in glob.glob( self.root + self.wildcard ):
			self.userSelect.append_text(folder.replace( self.root, "" ) )
			self.userSelect.set_active( 0 )
		
		
		return

	def ok_clicked(self, widget):
		self.apply_clicked(self)
		gtk.main_quit()
	
	def cancel_clicked(self, widget):
		gtk.main_quit()
		
	def rewardButton_clicked(self, widget):
		user = self.userSelect.get_active_text()
		arg = str(self.limitSpin0.get_value_as_int())
		cmd = 'addtime.sh ' + user + " " + arg
		os.system(cmd)
		
		
	def extendLimitsButton_clicked(self, widget):
		user = self.userSelect.get_active_text()
		cmd = 'extendlimits.sh ' + user
		os.system(cmd)

	def boundariesCheck_toggled(self, widget):
		if self.boundariesCheck.get_active():	
			self.fromSpin0.set_sensitive(True)	
			self.toSpin0.set_sensitive(True)	
			self.singleBoundaries.set_sensitive(True)
			self.wTree.get_widget("labelTo").set_sensitive(True)
			self.wTree.get_widget("labelFrom").set_sensitive(True)
			self.wTree.get_widget("lb0").set_sensitive(True)
		else:
			self.fromSpin0.set_sensitive(False)
			self.toSpin0.set_sensitive(False)
			self.singleBoundaries.set_sensitive(False)
			self.wTree.get_widget("labelTo").set_sensitive(False)
			self.wTree.get_widget("labelFrom").set_sensitive(False)
			self.wTree.get_widget("lb0").set_sensitive(False)
		self.singleBoundariesCheck_toggled(self)
			
	def singleBoundariesCheck_toggled(self, widget):
		if self.singleBoundaries.get_active() and self.boundariesCheck.get_active():
			self.wTree.get_widget("fromSpin1").set_sensitive(True)
			self.wTree.get_widget("fromSpin2").set_sensitive(True)
			self.wTree.get_widget("fromSpin3").set_sensitive(True)
			self.wTree.get_widget("fromSpin4").set_sensitive(True)
			self.wTree.get_widget("fromSpin5").set_sensitive(True)
			self.wTree.get_widget("fromSpin6").set_sensitive(True)
			self.wTree.get_widget("toSpin1").set_sensitive(True)
			self.wTree.get_widget("toSpin2").set_sensitive(True)
			self.wTree.get_widget("toSpin3").set_sensitive(True)
			self.wTree.get_widget("toSpin4").set_sensitive(True)
			self.wTree.get_widget("toSpin5").set_sensitive(True)
			self.wTree.get_widget("toSpin6").set_sensitive(True)
			self.wTree.get_widget("lb1").set_sensitive(True)
			self.wTree.get_widget("lb2").set_sensitive(True)
			self.wTree.get_widget("lb3").set_sensitive(True)
			self.wTree.get_widget("lb4").set_sensitive(True)
			self.wTree.get_widget("lb5").set_sensitive(True)
			self.wTree.get_widget("lb6").set_sensitive(True)
			self.wTree.get_widget("lb0").set_text("    Sun     ")
		else:
			self.wTree.get_widget("fromSpin1").set_sensitive(False)
			self.wTree.get_widget("fromSpin2").set_sensitive(False)
			self.wTree.get_widget("fromSpin3").set_sensitive(False)
			self.wTree.get_widget("fromSpin4").set_sensitive(False)
			self.wTree.get_widget("fromSpin5").set_sensitive(False)
			self.wTree.get_widget("fromSpin6").set_sensitive(False)
			self.wTree.get_widget("toSpin1").set_sensitive(False)
			self.wTree.get_widget("toSpin2").set_sensitive(False)
			self.wTree.get_widget("toSpin3").set_sensitive(False)
			self.wTree.get_widget("toSpin4").set_sensitive(False)
			self.wTree.get_widget("toSpin5").set_sensitive(False)
			self.wTree.get_widget("toSpin6").set_sensitive(False)
			self.wTree.get_widget("lb1").set_sensitive(False)
			self.wTree.get_widget("lb2").set_sensitive(False)
			self.wTree.get_widget("lb3").set_sensitive(False)
			self.wTree.get_widget("lb4").set_sensitive(False)
			self.wTree.get_widget("lb5").set_sensitive(False)
			self.wTree.get_widget("lb6").set_sensitive(False)
			self.wTree.get_widget("lb0").set_text("Every day")
			

	def limitCheck_toggled(self, widget):
		if self.limitCheck.get_active():		
			self.limitSpin0.set_sensitive(True)
			self.singleLimits.set_sensitive(True)
			self.wTree.get_widget("labelMinutes").set_sensitive(True)
			self.wTree.get_widget("ll0").set_sensitive(True)
		else:
			self.limitSpin0.set_sensitive(False)
			self.singleLimits.set_sensitive(False)
			self.wTree.get_widget("labelMinutes").set_sensitive(False)
			self.wTree.get_widget("ll0").set_sensitive(False)
		self.singleLimitsCheck_toggled(self)
	
	def singleLimitsCheck_toggled(self, widget):
		if self.singleLimits.get_active() and self.limitCheck.get_active():
			self.wTree.get_widget("ll1").set_sensitive(True)
			self.wTree.get_widget("ll2").set_sensitive(True)
			self.wTree.get_widget("ll3").set_sensitive(True)
			self.wTree.get_widget("ll4").set_sensitive(True)
			self.wTree.get_widget("ll5").set_sensitive(True)
			self.wTree.get_widget("ll6").set_sensitive(True)
			self.wTree.get_widget("limitSpin1").set_sensitive(True)
			self.wTree.get_widget("limitSpin2").set_sensitive(True)
			self.wTree.get_widget("limitSpin3").set_sensitive(True)
			self.wTree.get_widget("limitSpin4").set_sensitive(True)
			self.wTree.get_widget("limitSpin5").set_sensitive(True)
			self.wTree.get_widget("limitSpin6").set_sensitive(True)
			self.wTree.get_widget("ll0").set_text("    Sun     ")
		else:
			self.wTree.get_widget("ll1").set_sensitive(False)
			self.wTree.get_widget("ll2").set_sensitive(False)
			self.wTree.get_widget("ll3").set_sensitive(False)
			self.wTree.get_widget("ll4").set_sensitive(False)
			self.wTree.get_widget("ll5").set_sensitive(False)
			self.wTree.get_widget("ll6").set_sensitive(False)
			self.wTree.get_widget("limitSpin1").set_sensitive(False)
			self.wTree.get_widget("limitSpin2").set_sensitive(False)
			self.wTree.get_widget("limitSpin3").set_sensitive(False)
			self.wTree.get_widget("limitSpin4").set_sensitive(False)
			self.wTree.get_widget("limitSpin5").set_sensitive(False)
			self.wTree.get_widget("limitSpin6").set_sensitive(False)
			self.wTree.get_widget("ll0").set_text("Every day")

	def apply_clicked(self, widget):
		print "User=" + self.userSelect.get_active_text()
		space = " "
		limit = "limit=( 86400 86400 86400 86400 86400 86400 86400 )"
		bTo = "to=( 24 24 24 24 24 24 24 )"
		bFrom = "from=( 0 0 0 0 0 0 0 )"
		if self.limitCheck.get_active():
			if self.singleLimits.get_active():
				limit = "limit=( " + str(self.limitSpin0.get_value_as_int() * 60) + space + str(self.limitSpin1.get_value_as_int() * 60) + space + str(self.limitSpin2.get_value_as_int() * 60) + space + str(self.limitSpin3.get_value_as_int() * 60) + space + str(self.limitSpin4.get_value_as_int() * 60) + space + str(self.limitSpin5.get_value_as_int() * 60) + space + str(self.limitSpin6.get_value_as_int() * 60) + " )"
			else:
				limit = "limit=( " + str(self.limitSpin0.get_value_as_int() * 60) + space + str(self.limitSpin0.get_value_as_int() * 60) + space + str(self.limitSpin0.get_value_as_int() * 60) + space + str(self.limitSpin0.get_value_as_int() * 60) + space + str(self.limitSpin0.get_value_as_int() * 60) + space + str(self.limitSpin0.get_value_as_int() * 60) + space + str(self.limitSpin0.get_value_as_int() * 60) + " )"
		if self.boundariesCheck.get_active():
			if self.singleBoundaries.get_active():
				bFrom = "from=( " + str(self.fromSpin0.get_value_as_int()) + space + str(self.fromSpin1.get_value_as_int()) + space + str(self.fromSpin2.get_value_as_int()) + space + str(self.fromSpin3.get_value_as_int()) + space + str(self.fromSpin4.get_value_as_int()) + space + str(self.fromSpin5.get_value_as_int()) + space + str(self.fromSpin6.get_value_as_int()) + " )"
				bTo =  "to=( " + str(self.toSpin0.get_value_as_int()) + space + str(self.toSpin1.get_value_as_int()) + space + str(self.toSpin2.get_value_as_int()) + space + str(self.toSpin3.get_value_as_int()) + space + str(self.toSpin4.get_value_as_int()) + space + str(self.toSpin5.get_value_as_int()) + space + str(self.toSpin6.get_value_as_int()) + " )"
			else:
				bFrom = "from=( " + str(self.fromSpin0.get_value_as_int()) + space + str(self.fromSpin0.get_value_as_int()) + space + str(self.fromSpin0.get_value_as_int()) + space + str(self.fromSpin0.get_value_as_int()) + space + str(self.fromSpin0.get_value_as_int()) + space + str(self.fromSpin0.get_value_as_int()) + space + str(self.fromSpin0.get_value_as_int()) + " )"
				bTo = "to=( " + str(self.toSpin0.get_value_as_int()) + space + str(self.toSpin0.get_value_as_int()) + space + str(self.toSpin0.get_value_as_int()) + space + str(self.toSpin0.get_value_as_int()) + space + str(self.toSpin0.get_value_as_int()) + space + str(self.toSpin0.get_value_as_int()) + space + str(self.toSpin0.get_value_as_int()) + " )"
		configFile = self.configRoot + self.userSelect.get_active_text()
		fileHandle = open(configFile, 'w')
		if self.limitCheck.get_active() or self.boundariesCheck.get_active():
			fileHandle.write(limit + "\n")
			fileHandle.write(bFrom + "\n")
			fileHandle.write(bTo + "\n")
			fileHandle.close()
		else:
			fileHandle.close()
			os.remove(configFile)
		
if __name__ == "__main__":
	tkg = timekprGUI()
	gtk.main()
