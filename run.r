pathToClimDownWrapper = "C:/Users/Harshul Shukla/Desktop/climate/source/ClimDownWrapper.R"
source(pathToClimDownWrapper)
variable = "pr"
obs = "C:/Users/Harshul Shukla/Desktop/climate/source/obs_1980_1989_pr.nc"
gcm = "C:/Users/Harshul Shukla/Desktop/climate/source/gcm_1980_1989_pr.nc"

vanillaAnalogsPath = "C:/Users/Harshul Shukla/Desktop/climate/source/vanillaAnalogs.RData"
LSHAnalogsPath = "C:/Users/Harshul Shukla/Desktop/climate/source/LSHAnalogs.RData"
LSHEucAnalogsPath = "C:/Users/Harshul Shukla/Desktop/climate/source/LSHAnalogsEuc.RData"

vanillaProjectionPath = "C:/Users/Harshul Shukla/Desktop/climate/source/vanillaProjection.nc"
LSHProjectionPath = "C:/Users/Harshul Shukla/Desktop/climate/source/LSHProjection.nc"
LSHEucProjectionPath = "C:/Users/Harshul Shukla/Desktop/climate/source/LSHProjectionEuc.nc"

# Depending on the memory specs of your machine, you may not be able to 
# run both CA in the same run (without clearing memory)
# Should print out runtime of the CA + finding weights algo
#vanillaAnalogs = run.CA.vanilla(gcm, obs, variable, vanillaAnalogsPath)
#LSHAnalogs = run.CA.LSH(gcm, obs, variable, LSHAnalogsPath, 'Ang')
#LSHEucAnalogs = run.CA.LSH(gcm, obs, variable, LSHEucAnalogsPath, 'Euc')


# Load the analogs x 1 -- Name of LSH and LSHEuc will be same in terms of variable in environ
#load(vanillaAnalogsPath)
#construct.projection.output(obs, vanillaAnalogs, vanillaProjectionPath, variable)

#load(LSHAnalogsPath)
#construct.projection.output(obs, LSHAnalogs,   LSHProjectionPath, variable)
#Same variable name so reload with different path (overwrite)
#load(LSHEucAnalogsPath)
#construct.projection.output(obs, LSHAnalogs,   LSHEucProjectionPath, variable) 

RMSEvanilla = calculate.projection.error(obs, vanillaProjectionPath, 'pr')
RMSELSH = calculate.projection.error(obs, LSHProjectionPath, 'pr')
RMSELSHEuc = calculate.projection.error(obs, LSHEucProjectionPath, 'pr')
