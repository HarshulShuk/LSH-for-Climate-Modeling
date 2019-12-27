library(ClimDown)
library(doParallel)

run.CA.vanilla <- function(gcm.path, obs.path, variable, path){
	vanillaAnalogs = ca.netcdf.wrapper(gcm.path, obs.path, variable)
	save(vanillaAnalogs, file = path)
	vanillaAnalogs
}

run.CA.LSH <- function(gcm.path, obs.path, variable, path, metric){
	LSHAnalogs = ca.netcdf.wrapper.LSH(gcm.path, obs.path, variable, metric)
	save(LSHAnalogs, file = path)
	LSHAnalogs
}

construct.projection.output <- function(obs.path, analogs, outputFilePath, variable) {
	apply.analogues.output(obs.path, analogs, outputFilePath, variable)
}

calculate.projection.error <- function(obs.path, projection.path, var){
  ca.netcdf.findRMSE(obs.path,projection.path, var)
}