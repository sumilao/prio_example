BOARDS ?= ZCU104 Pynq-Z1

DTC_DIR := ${CURDIR}/dtc-1.4.4
DTC := ${DTC_DIR}/dtc

BOARDDIR := ../boards

all: real_all

define BOARD_SPECIFIC_RULES
# $1 is the board name
BOARDDIR_$1 := $$(BOARDDIR)/$1

SRCDIR_$1 := $${BOARDDIR_$1}/prio_linux/dtso
BINDIR_$1 := $${BOARDDIR_$1}/prio_linux/dtbo

DTO_DTS_$1 := $$(wildcard $${SRCDIR_$1}/*.dts)
DTO_DTB_$1 := $$(patsubst %.dts,%.dtbo,$$(patsubst $${SRCDIR_$1}/%,$${BINDIR_$1}/%,$${DTO_DTS_$1}))

overlays_$1: $${DTO_DTB_$1} 

$${BINDIR_$1}/%.dtbo: $${SRCDIR_$1}/%.dts
	$${DTC} -@ -I dts -O dtb -o $$@ $$<

endef

$(foreach board, $(BOARDS), $(eval $(call BOARD_SPECIFIC_RULES,$(board))))

real_all: ${DTC} $(patsubst %, overlays_%, $(BOARDS))

${DTC}: 
	bash install.sh

clean: 
	rm -r ${DTC_DIR}

