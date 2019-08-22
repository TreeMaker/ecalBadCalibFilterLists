//ROOT Headers
#include "TTree.h"
#include "TChain.h"
#include "TBenchmark.h"

//STL Headers
#include <iostream> //std::cout, std::endl, std::flush
#include <iomanip> //std::setw
#include <fstream> //std::fstream
#include <cstdlib>
#include <sys/stat.h> //std::stat
#include <algorithm> //std::find_if
#include <sys/types.h>
#include <dirent.h>
#include <errno.h>

using namespace std;

inline bool exists (const std::string& name) {
  struct stat buffer;   
  return (stat (name.c_str(), &buffer) == 0); 
}

void progressbar(unsigned int x, unsigned int n, unsigned int w, std::string prefix, std::pair<float,float> time) {
	if ( (x != n) && (x % (n/100) != 0) ) return;

	float ratio  =  x/(float)n;
	int   c      =  ratio * w;

	std::cout << prefix << " [";
	for (int x=0; x<c; x++) std::cout << "=";
	for (unsigned int x=c; x<w; x++) std::cout << " ";
	if(time.first == 0.0 && time.second == 0.0)
		std::cout << "] " << std::setw(3) << (int)(ratio*100) << "% (" << x << "/" << n << ")\r" << std::flush;
	else
		std::cout << "] " << std::setw(3) << (int)(ratio*100) << "% (" << x << "/" << n << ")\n"
				  << "  (CPU: " << time.first << "s | Real: " << time.second << "s) (CPU: "
				  << n/time.first << "<evts/s> | Real: " << n/time.second << "<evts/s>)\r" << std::flush;
}

//Notes:
// Selects/filters on files and folder separately.
// Selects if any of the words included, not all of them.
// By default the output files are places in the same folder as the file lists.
// This can be overridden by specifying an outpath.
//
//Example:
// root -n ../MakeEcalBadCalibFilterList.C+\(\"root://cmsxrootd.fnal.gov/\",\"./\",\{\"2018C-Nano\",\"EGamma\"\},{},true,0\)
int MakeEcalBadCalibFilterList(string redirector = "root://cmsxrootd-site.fnal.gov/", string outpath = "", vector<string> selectors = {}, vector<string> filters = {},
                               bool progress = true, int debug = 0, string suffix = "_ecalBadCalibFilterList") {
	// Setup the basepath where the input folder/files are located
	string basepath;
	if(const char* env_p = std::getenv("CMSSW_BASE")) {
		basepath = env_p;
		basepath += "/src/TreeMaker/ecalBadCalibFilterLists/python/";
		cout << "Basepath: " << basepath << endl << endl;
	}

	// Setup the output path
	if(outpath.back()!='/' && outpath!="") outpath += '/';

	// Setup the list of possible input folders
	DIR *dp;
	struct dirent *dirp;
	map<string,vector<string>> folders;
	// Get the folder names or fallback to a predefined list
	if((dp = opendir(basepath.c_str())) == NULL) {
		cout << "Error(" << errno << ") opening " << basepath << "." << endl
			 << "Falling back to the default list." << endl;
		//return errno;
		folders = {
					{"Run2016B-Nano14Dec2018_ver1-v1/",{}},
					{"Run2016B-Nano14Dec2018_ver2-v1/",{}},
					{"Run2016C-Nano14Dec2018-v1/",{}},
					{"Run2016D-Nano14Dec2018-v1/",{}},
				    {"Run2016E-Nano14Dec2018-v1/",{}},
				    {"Run2016F-Nano14Dec2018-v1/",{}},
				    {"Run2016G-Nano14Dec2018-v1/",{}},
				    {"Run2016H-Nano14Dec2018-v1/",{}},
				    {"Run2017B-Nano14Dec2018-v1/",{}},
				    {"Run2017C-Nano14Dec2018-v1/",{}},
				    {"Run2017D-Nano14Dec2018-v1/",{}},
				    {"Run2017E-Nano14Dec2018-v1/",{}},
				    {"Run2017F-Nano14Dec2018-v1/",{}},
				    {"Run2018A-Nano14Dec2018-v1/",{}},
				    {"Run2018B-Nano14Dec2018-v1/",{}},
				    {"Run2018C-Nano14Dec2018-v1/",{}},
				    {"Run2018D-Nano14Dec2018-v1/",{}}
				};
	}
	else {
		string cdir = "";
		while ((dirp = readdir(dp)) != NULL) {
			cdir = string(dirp->d_name);
			auto selector_it = find_if(selectors.begin(), selectors.end(),[&](auto &f) {if(cdir.find(f)!=string::npos) return true; else return false;});
			auto filter_it = find_if(filters.begin(), filters.end(),[&](auto &f) {if(cdir.find(f)!=string::npos) return true; else return false;});
			if(dirp->d_type == DT_DIR && strncmp(dirp->d_name,".",1)!=0 && selector_it!=selectors.end() && filter_it==filters.end()) {
				folders[cdir+"/"] = {};
			}
			else if(selector_it==selectors.end() && debug >= 2) {
				cout << "WARNING::Skipping " << basepath << cdir << " because it didn't contain any of the selectors." << endl << endl;
			}
			else if(filter_it!=filters.end() && debug >= 2) {
				cout << "WARNING::Skipping " << basepath << cdir << " because it was filtered on \'" << *filter_it << "\'." << endl << endl;
			}			
		}
		closedir(dp);

		// Get the PD names or fallback to a predefined list
		for (auto folder_it = folders.begin(); folder_it!=folders.end(); folder_it++) {
			if((dp = opendir( (basepath+folder_it->first).c_str()  )) == NULL) {
				cout << "Error(" << errno << ") opening " << basepath << folder_it->first << "." << endl
					 << "Falling back to the default list." << endl;
				if (folder_it->first.find("Run2018")!=string::npos) {
					folder_it->second = {"EGamma","JetHT","MET","SingleMuon"};
				}
				else {
					folder_it->second = {"HTMHT","JetHT","MET","SingleElectron","SingleMuon","SinglePhoton"};
				}
			}
			else {
				string pd_file = "";
				while ((dirp = readdir(dp)) != NULL) {
					pd_file = string(dirp->d_name);
					auto selector_it = find_if(selectors.begin(), selectors.end(),[&](auto &f) {if(pd_file.find(f)!=string::npos) return true; else return false;});
					auto filter_it = find_if(filters.begin(), filters.end(),[&](auto &f) {if(pd_file.find(f)!=string::npos) return true; else return false;});
					if(dirp->d_type == DT_REG && pd_file.find("_cff.py")!=string::npos && pd_file.find("_cff.pyc")==string::npos && selector_it!=selectors.end() && filter_it==filters.end()) {
						folder_it->second.push_back(pd_file.substr(0,pd_file.find("_cff.py")));
					}
					else if(selector_it==selectors.end() && debug >= 2) {
						cout << "WARNING::Skipping " << basepath << folder_it->first << pd_file << " because it didn't contain any of the selectors." << endl << endl;
					}
					else if(filter_it!=filters.end() && debug >= 2) {
						cout << "WARNING::Skipping " << basepath << folder_it->first << pd_file << " because it was filtered on \'" << *filter_it << "\'." << endl << endl;
					}	
				}
				closedir(dp);
			}
		}
	}

	cout << "Selectors:" << endl;
	for (auto selector : selectors) {
		cout << "\t" << selector << endl;
	}

	cout << endl << "Filters:" << endl;
	for (auto filter : filters) {
		cout << "\t" << filter << endl;
	}

	cout << endl << "Filtered folders and primary datasets:" << endl;
	for (auto folder : folders) {
		cout << "\t" << folder.first << endl;
		for (auto pd : folder.second) {
			cout << "\t\t" << pd << endl;
		}
	}
	cout << endl;

	TBenchmark* benchmark = new TBenchmark();
	for (auto folder : folders) {
		for (auto pd : folder.second) {
			string current_dataset = basepath+folder.first+pd+"_cff.py";
			if (exists(current_dataset)) {
				cout << "Making list for " << current_dataset << " ... " << flush;
				if (progress) cout << endl;

				// Reset the TBenchmark
				benchmark->Reset();
				benchmark->Start("dataset");

				// Get the files belonging to the current dataset
				ifstream inf(current_dataset);
				if(!inf.is_open()) {
					cout << "WARNING::Unable to open the list of files belonging to the current PD." << endl
						 << "  Failed to open " << current_dataset << "." << endl;
					continue;
				}
				std::string line;
				vector<string> files;
				while (std::getline(inf, line)) {
					if(line.find("/store/data")==string::npos) continue;
					line = line.substr(0,line.rfind('\''));
					line = line.substr(line.find("/store"));
					line = redirector+line;
					files.push_back(line);
				}
				inf.close();

				// Setup the TCahin
				TChain * c = new TChain("Events");
				int nfiles = files.size();
				int nfiles_added = 0;
				for (auto f : files) {
					if(debug > 0 && nfiles_added>=1) continue;
					c->AddFile(f.c_str());
					nfiles_added++;
				}
				if (nfiles_added==nfiles) {
					if(progress) {
						cout << "\tAdded " << nfiles_added << " files to the chain." << endl;
					}
				}
				else {
					if (!progress) cout << endl;
					cout << "WARNING::Only " << nfiles_added << " of the " << nfiles << " files in the dataset were added to the chain." << endl;
				}
				c->SetBranchStatus("*",0);
				c->SetBranchStatus("run",1);
				c->SetBranchStatus("event",1);
				c->SetBranchStatus("luminosityBlock",1);
				c->SetBranchStatus("Flag_ecalBadCalibFilter",1);

				// Set up the access to the TChain
				int run(0),luminosityBlock(0);
				long event(0);
				bool ecalBadCalibFilter(1);
				long failed_events(0);
				c->SetBranchAddress("run",&run);
				c->SetBranchAddress("luminosityBlock",&luminosityBlock);
				c->SetBranchAddress("event",&event);
				c->SetBranchAddress("Flag_ecalBadCalibFilter",&ecalBadCalibFilter);

				// Setup the output file for this dataset
				ofstream outf;
				string outfilename;
				if(outpath=="") {
					outfilename = basepath+folder.first+pd+suffix+".txt";
					outf.open(outfilename);
				}
				else {
					string current_folder = (folder.first.back()=='/') ? folder.first.substr(0,folder.first.size()-1) : folder.first;
					outfilename = outpath+current_folder+"_"+pd+suffix+".txt";
					outf.open(outfilename);
				}

				// Loop over the TChain
				if (debug > 0) cout << "Getting the entries in the chain ... " << flush;
				size_t nentries = (debug == 0) ? c->GetEntries() : 1000;
				if (debug > 0) cout << "DONE" << endl;
				for (size_t ientry=0; ientry<nentries; ientry++) {
					// Report every now and then
					if (ientry==0) benchmark->Start("dataset");
					if (ientry==nentries-1) benchmark->Stop("dataset");
					if (progress) {
						progressbar(ientry+1,nentries,50,"Event Loop Progress:",
									(ientry==nentries-1) ? std::make_pair((float)benchmark->GetCpuTime("dataset"),
																		  (float)benchmark->GetRealTime("dataset"))
														 : std::make_pair(float(0.0),float(0.0)));
						if(ientry==nentries-1) cout << endl;
					}
					c->GetEntry(ientry);
					if(ecalBadCalibFilter==1) continue;
					outf << run << ":" << luminosityBlock << ":" << event << endl;
					failed_events++;
				}

				if (!progress) {
					cout << "DONE" << "  (CPU: " << benchmark->GetCpuTime("dataset") << "s | Real: " << benchmark->GetRealTime("dataset") << "s) (CPU: "
						 << nentries/benchmark->GetCpuTime("dataset") << "<evts/s> | Real: " << nentries/benchmark->GetRealTime("dataset") << "<evts/s>)\r" << endl;
				}
				cout << "\t" << failed_events << " events failed the ecalBadCalibFilter." << endl;
				cout << "\t" << "Written to file " << outfilename << endl << endl;

				outf.close();
				delete c;
			}
			else {
				cout << "WARNING::Skipping " << current_dataset << ". The file list does not exist." << endl << endl;
			}
		}
	}
	return 0;
}


/*
Interactive version of the code:
================================

int run(0),luminosityBlock(0);
long event(0);
bool ecalBadCalibFilter(1);

ofstream outf;
outf.open ("ecalBadCalibFilter.txt");
TChain* c = new TChain("Events")
c->AddFile("root://cmsxrootd-site.fnal.gov//store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/05265503-0C6E-314D-ADF7-D6F985DCF8F2.root")
...
c->AddFile("root://cmsxrootd-site.fnal.gov//store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/C1A5E354-23FE-D947-90BD-9C8CCBD982C3.root")

c->SetBranchStatus("*",0)
c->SetBranchStatus("run",1)
c->SetBranchStatus("event",1)
c->SetBranchStatus("luminosityBlock",1)
c->SetBranchStatus("Flag_ecalBadCalibFilter",1)
c->SetBranchAddress("run",&run)
c->SetBranchAddress("luminosityBlock",&luminosityBlock)
c->SetBranchAddress("event",&event)
c->SetBranchAddress("Flag_ecalBadCalibFilter",&ecalBadCalibFilter)
size_t nentries = c->GetEntries()
for(size_t i=0; i<nentries; i++) {c->GetEntry(i);if(ecalBadCalibFilter==1) continue;outf << run << ":" << luminosityBlock << ":" << event << endl;}
outf.close();


Alternate version of the code with TTree::Scan formatting:
==========================================================
TChain* c = new TChain("Events")
c->AddFile("root://cmsxrootd-site.fnal.gov//store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/05265503-0C6E-314D-ADF7-D6F985DCF8F2.root")
...
c->AddFile("root://cmsxrootd-site.fnal.gov//store/data/Run2017F/MET/NANOAOD/Nano14Dec2018-v1/00000/C1A5E354-23FE-D947-90BD-9C8CCBD982C3.root")
c->SetScanField(0)
.> ecalBadCalibFilter.txt
c->Scan("run:luminosityBlock:event","Flag_ecalBadCalibFilter==0")
*/
