# function to add reconfigurable module
proc add_rm {pd_name rm_name} {
  create_bd_design "rm_${rm_name}_${pd_name}"
  source ${rm_name}.tcl
  validate_bd_design
  save_bd_design
  set_property synth_checkpoint_mode None [get_files rm_${rm_name}_${pd_name}.bd]
  create_reconfig_module -name rm_${rm_name}_${pd_name} -partition_def [get_partition_defs ${pd_name}] -define_from rm_${rm_name}_${pd_name}
}

proc add_region {pr_name pd_name rm_names} {
  upvar $rm_names rm

  # add constraints file into project
  import_files -fileset constrs_1 -norecurse ./vivado/constraints/${pr_name}.xdc
  update_compile_order -fileset sources_1

  # add partition definition and default reconfigurable module
  set_property PR_FLOW true [current_project]
  set curdesign [current_bd_design]
  puts $curdesign
  create_bd_design -cell [get_bd_cells /${pr_name}] ${rm(0)}_${pd_name}
  set_property synth_checkpoint_mode None [get_files ${rm(0)}_${pd_name}.bd]
  set pd_instance [create_partition_def -name ${pd_name} -module ${rm(0)}_${pd_name}]
  create_reconfig_module -name ${rm(0)}_${pd_name} -partition_def $pd_instance -define_from ${rm(0)}_${pd_name}

  # replace the pr region
  current_bd_design $curdesign
  set new_pd_cell [create_bd_cell -type module -reference $pd_instance pr_region_temp]
  replace_bd_cell  [get_bd_cells /${pr_name}] $new_pd_cell
  delete_bd_objs  [get_bd_cells /${pr_name}]
  set_property name ${pr_name} $new_pd_cell

  # validate and save current top design
  validate_bd_design
  save_bd_design

  # add each rm
  foreach n [array names rm] {
    add_rm ${pd_name} $rm($n)
  }
  current_bd_design $curdesign


}


#START OF FLOW
# open project and block design
open_project -quiet ./${overlay_name}/${overlay_name}.xpr
open_bd_design ./${overlay_name}/${overlay_name}.srcs/sources_1/bd/${design_name}/${design_name}.bd
set_param project.enablePRFlowIPI 1
set_param bitstream.enablePR 2341
set_param hd.enablePR 1234

# add constraints file into project
import_files -fileset constrs_1 -norecurse ./vivado/constraints/${overlay_name}.xdc
update_compile_order -fileset sources_1


# add pr regions and the designs for each region
#TODO: make this a for loop
add_region ${pr_array(0)} ${pd_array(0)} rm_array
add_region ${pr_array(1)} ${pd_array(1)} rm_array
add_region ${pr_array(2)} ${pd_array(2)} rm_array
add_region ${pr_array(3)} ${pd_array(3)} rm_array
add_region ${pr_array(4)} ${pd_array(4)} rm_array
add_region ${pr_array(5)} ${pd_array(5)} rm_array




#add_region ${pr} ${pd} rm_array
