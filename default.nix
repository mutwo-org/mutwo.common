with import <nixpkgs> {};
with pkgs.python310Packages;


let

  mutwo-core-archive = builtins.fetchTarball "https://github.com/mutwo-org/mutwo.core/archive/069a407e5ac1bd140d92180e21e64dd094df83c5.tar.gz";
  mutwo-core = import (mutwo-core-archive + "/default.nix");

  treelib = pkgs.python310Packages.buildPythonPackage rec {
    name = "treelib";
    src = fetchFromGitHub {
      owner = "caesar0301";
      repo = name;
      rev = "12d7efd50829a5a18edaab01911b1e546bff2ede";
      sha256 = "sha256-QGgWsMfPm4ZCSeU/ODY0ewg1mu/mRmtXgHtDyHT9dac=";
    };
    doCheck = true;
    propagatedBuildInputs = [ python310Packages.future ];
  };

  python-ranges = pkgs.python310Packages.buildPythonPackage rec {
    name = "python-ranges";
    src = fetchFromGitHub {
      owner = "Superbird11";
      repo = "ranges";
      rev = "38ac789b61e1e33d1a8be999ca969f909bb652c0";
      sha256 = "sha256-oRQCtDBQnViNP6sJZU0NqFWkn2YpcIeGWmfx3Ne/n2c=";
    };
    # TypeError: calling <class 'ranges.RangeDict.RangeDict'> returned {}, not a test
    doCheck = false;
    checkInputs = [ python310Packages.pytest ];
  };

in

  buildPythonPackage rec {
    name = "mutwo.common";
    src = fetchFromGitHub {
      owner = "mutwo-org";
      repo = name;
      rev = "dd8b4e5355cb0bacb0085146f975e620a6384abe";
      sha256 = "sha256-L0ruY6ehQFwXnxqq5iY+DF9RTURcI5E+e6NGMFULEoQ=";
    };
    propagatedBuildInputs = [ 
      treelib
      python310Packages.numpy
      python310Packages.scipy
      python-ranges
      mutwo-core
    ];
    doCheck = true;
  }
