"""Entry point for the Employee Training Application."""

import json
from argparse import ArgumentParser
from add_campaign_and_channels.presention_layer.user_interface import userInterface



def main():
	"""Entry point."""
	args = configure_and_parse_commandline_arguments()

	if args.configfile:
		config = None
		with open(args.configfile, 'r') as f:
			config = json.loads(f.read())

		print("configuration loaded successfully.")	
	ui = UserInterface(config)
	ui.start()
			
		


def configure_and_parse_commandline_arguments():
	"""configure and parse command-line arguments."""
	parser =ArgumentParser(
	prog='main.py',
	description='start the application with aconfiguration file.',
	epilog='poc:refah | alharbi@mymu.edu')	


	parser.add_argument('-c','--configfile',
	help= "configuration file to load.",
	required=True) 
	args = parser. parse_args()
	return args

	

if __name__ == "__main__":
	main	
	
		
	
	
		





					
	
	
	
	


