import FWCore.ParameterSet.Config as cms

process = cms.Process("GeometryDumperProcess")

process.load('Configuration/StandardSequences/Services_cff')
process.load('FWCore/MessageService/MessageLogger_cfi')

### From autoCond at https://github.com/cms-sw/cmssw/blob/master/Configuration/AlCa/python/autoCond.py
#process.load("Configuration.StandardSequences.GeometryDB_cff")
#process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
#from Configuration.AlCa.autoCond import autoCond
#process.GlobalTag.globaltag = autoCond['run3_data']

### From specific global tag at https://cms-conddb.cern.ch/cmsDbBrowser/index/Prod
process.load("Configuration.StandardSequences.GeometryDB_cff")
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '140X_mcRun3_2024_design_v6', '')

### From specific xml file at https://github.com/cms-sw/cmssw/tree/master/Configuration/Geometry/python
#process.load('Configuration.Geometry.GeometryExtended2024Reco_cff')

### The source data defines the time zone of the Geometry that the tag will load.
### Consider the payload of the tag (e.g. https://cms-conddb.cern.ch/cmsDbBrowser/list/Prod/tags/RecoIdealGeometry_RPC_v3_hlt)
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('file:sample.root')
) 

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1) )

process.RPCGeometryDumper = cms.EDAnalyzer("RPCGeometryDumper",
    outputFileName = cms.untracked.string("140X_mcRun3_2024_design_v6.csv"),
)

process.p = cms.Path(process.RPCGeometryDumper)
