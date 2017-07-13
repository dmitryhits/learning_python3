import ROOT

h = ROOT.TH1F('h', 'h', 100, 0, 20)
fLandau = ROOT.TF1("fa3","TMath::Landau(x,4,1,0)",0,20)

#h.FillRandom('fLandau')

c = ROOT.TCanvas('c')

fLandau.Draw()

