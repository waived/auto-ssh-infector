┌─┐  ┬ ┬  ┌┬┐  ┌─┐      ┌─┐  ┌─┐  ┬ ┬      ┌─┐  ┌┬┐  ┌─┐  ┌─┐  ┬    ┌─┐  ┬─┐
├─┤  │ │   │   │ │      └─┐  └─┐  ├─┤      └─┐   │   ├┤   ├─┤  │    ├┤   ├┬┘
┴ ┴  └─┘   ┴   └─┘      └─┘  └─┘  ┴ ┴      └─┘   ┴   └─┘  ┴ ┴  ┴─┘  └─┘  ┴└─

OVERVIEW:
     This script acts as a password-spraying engine. It generates random IP addresses
     and probes them for an SSH connection. If a connection is found, the script will
     then attempt to login via either user-specific credentials or the ones pre-set in
     the script. If a connection is successful, the script will send BASH commands which
     will download and auto-execute the user-specified payload.

     Beware: scanning with this tool can anger ISPs, and termination of internet service
     is a possibility. All responsibility falls on the end-user. You have been warned!


FEATURES:
     THREADING: This script supports multi-threading. This boosts effeciency as multiple
                IP addresses can be scanned at any given time. However, the downside is
                that when engaging multiple IP addresses, this activity can bog down a
                network. Be cautious of your bandwidth consumption and system resources.

     BLACKLIST: This script generates IP addresses following no particular scheme. By
                default, internal IPs and subnets are blocked for efficiency and to 
                reduce and false positives. If specified by the user, this script will
                avoid all known IP addresses belonging to local and foreign Goverments, 
                Intelligence Agencies, miscellaneous federal assets and Law Enforcement.
                It is recommended that you enable this option.

    HOST COUNT: The user can specify how many IP addresses that are to be probed. Of
                course, this script also has to option to run indefinitely. 

       COMMAND: The user can specify a command statement to run upon the successful breach
                of an SSH connection. It must be wrapped in quotes.

     COMBOLIST: By default, this script uses known weak SSH credentials to attempt a
                breach. Additionally, a combo-list (with the format <username>:<password>)
                can also be specified. Default preset credentials will still be used against
                the host.


KNOWN BUGS: 
     I'm lazy and spent very little time field testing this. It is possible.

FUTURE UPDATES:
     Maybe, idk...lmao
