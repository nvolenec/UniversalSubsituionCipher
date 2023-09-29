# UniversalSubsituionCipher

This code is a generic subsitituion cipher engine that is very configurable.  It does not currently support encryption/decryiption to enable this you would need to write custom configuration files for each.

The problem I was attempting to solve with this is I could not find existing substition cipher code that supported nulls and multi-character subsitition.

When writing a config file be aware that the config files are processed top to bottom, so if you wrote a config file that subsitited both 'aa' and 'a' if the 'aa' is not first in the config file it would never be run.
 
