overlay_name := prio
design_name := prio

all: static dynamic bitstream check_timing
	@echo
	@tput setaf 2 ; echo "Built $(overlay_name) successfully!"; tput sgr0;
	@echo

static:
	vivado -mode batch -source scripts/$(overlay_name).tcl -notrace
	vivado -mode batch -source scripts/create_design.tcl -notrace

dynamic:
	vivado -mode batch -source scripts/create_pr.tcl -notrace

bitstream:
	vivado -mode batch -source scripts/build_bitstream.tcl -notrace

check_timing:
	vivado -mode batch -source scripts/check_$(overlay_name).tcl -notrace

clean:
	rm -rf $(overlay_name) *.jou *.log NA
	rm -rf .dsa
