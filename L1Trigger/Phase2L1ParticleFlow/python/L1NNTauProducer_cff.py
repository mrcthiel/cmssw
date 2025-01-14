import FWCore.ParameterSet.Config as cms

from L1Trigger.Phase2L1ParticleFlow.l1ctLayer1_cff import l1ctLayer1Barrel,l1ctLayer1HGCal,l1ctLayer1

#from L1Trigger.Phase2L1ParticleFlow.L1NNTauProducer_cfi import *

#L1NNTauProducerPuppi = L1NNTauProducer.clone(
#                                NNFileName      = cms.string("L1Trigger/Phase2L1ParticleFlow/data/tau_3layer_puppi.pb")
#                                )


L1NNTauProducerPuppi = cms.EDProducer("L1NNTauProducer",
                                      seedpt          = cms.double(10),
                                      conesize        = cms.double(0.4),
                                      tausize         = cms.double(0.1),
                                      maxtaus         = cms.int32(5),
                                      nparticles      = cms.int32(10),
                                      L1PFObjects     = cms.InputTag("l1ctLayer1:Puppi"), #1pfCandidates:Puppi"),#l1pfCandidates
                                      NNFileName      = cms.string("L1Trigger/Phase2L1ParticleFlow/data/tau_3layer_puppi.pb")
)

L1NNTauProducerPF = cms.EDProducer("L1NNTauProducer",
                                      seedpt          = cms.double(10),
                                      conesize        = cms.double(0.4),
                                      tausize         = cms.double(0.1),
                                      maxtaus         = cms.int32(5),
                                      nparticles      = cms.int32(10),
                                      L1PFObjects     = cms.InputTag("l1ctLayer1:PF"),#l1pfCandidates
                                      NNFileName      = cms.string("L1Trigger/Phase2L1ParticleFlow/data/tau_3layer.pb")
)

