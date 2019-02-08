# name of the overal project and design within the project
set overlay_name "gpio_pr"
set design_name "gpio_pr"

# six of each of these
#variable pr_array
array set pr_array {
  0 pr_0
  1 pr_1
  2 pr_2
  3 pr_3
  4 pr_4
  5 pr_5
}

array set pd_array {
  0 pd_pr_0
  1 pd_pr_1
  2 pd_pr_2
  3 pd_pr_3
  4 pd_pr_4
  5 pd_pr_5
}

# as many of these as we have sub designs
array set rm_array {
  0 led_pattern_C
  1 led_pattern_3
}

#set pr ${pr_array(0)}
#set pd ${pd_array(0)}
source ./create_pr_mult.tcl

#set pr ${pr_array(1)}
#set pd ${pd_array(1)}
#source ./create_pr_mult.tcl

#set pr ${pr_array(2)}
#set pd ${pd_array(2)}
#source ./create_pr_mult.tcl

#set pr ${pr_array(3)}
#set pd ${pd_array(3)}
#source ./create_pr_mult.tcl

#set pr ${pr_array(4)}
#set pd ${pd_array(4)}
#source ./create_pr_mult.tcl

#set pr ${pr_array(5)}
#set pd ${pd_array(5)}
#source ./create_pr_mult.tcl
