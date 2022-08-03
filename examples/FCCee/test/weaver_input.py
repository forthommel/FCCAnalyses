#Mandatory: List of processes
processList = {
    'p8_noBES_ee_H_Hbb_ecm125':{'fraction':0.01, 'chunks':1, 'output':'test_out'}
}
#Mandatory: Production tag when running over EDM4Hep centrally produced events, this points to the yaml files for getting sample statistics
prodTag = "FCCee/spring2021/IDEA/"

#Optional: output directory, default is local running directory
outputDir   = "."

#Optional
nCPUS       = 8
runBatch    = False
#batchQueue = "longlunch"
#compGroup = "group_u_FCC.local_gen"

#Optional test file
testFile = "root://eospublic.cern.ch//eos/experiment/fcc/ee/generation/DelphesEvents/spring2021/IDEA/p8_ee_ZH_ecm240/events_101027117.root"

class JetAccumulator():
    def __init__(self, oth=None):
        if oth is not None:
            pass
        pass
    def Fill(self, jets):
        pass
    def Merge(self, jets):
        pass
import ROOT
ROOT.gInterpreter.ProcessLine('''
class CJetAccumulator {
public:
  CJetAccumulator() {}
  CJetAccumulator(const CJetAccumulator& oth) {}
  void Fill(const edm4hep::ReconstructedParticleData& jet) { jets_.emplace_back(jet);}
  void Merge(const std::vector<CJetAccumulator*>& coll) {std::cout << __PRETTY_FUNCTION__ << ": " << coll.size() << std::endl;}
private:
  std::vector<edm4hep::ReconstructedParticleData> jets_;
};
''')

#Mandatory: RDFanalysis class where the use defines the operations on the TTree
class RDFanalysis():

    #__________________________________________________________
    #Mandatory: analysers function to define the analysers to process, please make sure you return the last dataframe, in this example it is df2
    def analysers(df):
        '''import numpy as np
        import pandas as pd

        to_keep = ROOT.vector('string')()
        for br in ['Jet']:
            to_keep.emplace_back(br)
        fltr_df = df.Snapshot(to_keep)

        pdf = pd.DataFrame(fltr_df.AsNumpy())
        print(pdf)'''
        #jdf = ROOT.RDataFrame('tree')

        def aggreg(vec: ROOT.vector('string'), vecb: ROOT.vector('string')):
            print(vec)

        #ja = JetAccumulator()
        #test = df.Fill(ja, ("Jet",))
        #test = df.Fill(ROOT.CJetAccumulator(), ("Jet",))
        df2 = (
            df
               .Fill(ROOT.CJetAccumulator(), ("Jet",))
           )
        print(df2)
        return df2

    #__________________________________________________________
    #Mandatory: output function, please make sure you return the branchlist as a python list
    def output():
        branchList = [
                #'MC_PDG',
                ]
        return branchList
