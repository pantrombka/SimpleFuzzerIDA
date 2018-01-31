from winappdbg import Debug

import sys
def nabreak(Event):
	thr=Event.get_thread()
	#print thr.get_context()
	adr=Event.breakpoint.get_address()
	print hex(adr)
	disasm=thr.disassemble_instruction(adr)
	print disasm
# Instance a Debug object.
debug = Debug()
try:
	debug.execv( sys.argv[ 1 : ] )
	pidProc=debug.get_debugee_pids()[0]
	print pidProc

    # Wait for the debugee to finish.
	debug.break_at(pidProc,0x0101c3b4,nabreak)
	debug.loop()
	
# Stop the debugger.
finally:
    debug.stop()
	
