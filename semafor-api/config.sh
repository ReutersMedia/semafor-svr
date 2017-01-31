#!/bin/sh
######################## ENVIRONMENT VARIABLES ###############################
######### change the following according to your own local setup #############



# path to the absolute path
# where you decompressed SEMAFOR.
export SEMAFOR_HOME="/semafor-master"

export CLASSPATH=".:${SEMAFOR_HOME}/target/Semafor-3.0-alpha-04.jar"

# Change the following to the bin directory of your $JAVA_HOME
export JAVA_HOME_BIN="/usr/bin"

# Change the following to the directory where you decompressed 
# the models for SEMAFOR 2.0.
export MALT_MODEL_DIR="${BASE_DIR}/models/semafor_malt_model_20121129"
#export TURBO_MODEL_DIR="{BASE_DIR}/models/turbo_20130606"



######################## END ENVIRONMENT VARIABLES #########################

echo "Environment variables:"
echo "SEMAFOR_HOME=${SEMAFOR_HOME}"
echo "CLASSPATH=${CLASSPATH}"
echo "JAVA_HOME_BIN=${JAVA_HOME_BIN}"
echo "MALT_MODEL_DIR=${MALT_MODEL_DIR}"
