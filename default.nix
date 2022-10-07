with import <nixpkgs> {};
with pkgs.python3Packages;


let

  mutwo-core-archive = builtins.fetchTarball "https://github.com/mutwo-org/mutwo.core/archive/97aea97f996973955889630c437ceaea405ea0a7.tar.gz";
  mutwo-core = import (mutwo-core-archive + "/default.nix");

  treelib = pkgs.python39Packages.buildPythonPackage rec {
    name = "treelib";
    src = fetchFromGitHub {
      owner = "caesar0301";
      repo = name;
      rev = "12d7efd50829a5a18edaab01911b1e546bff2ede";
      sha256 = "sha256-QGgWsMfPm4ZCSeU/ODY0ewg1mu/mRmtXgHtDyHT9dac=";
    };
    doCheck = true;
    propagatedBuildInputs = [ python39Packages.future ];
  };

  python-ranges = pkgs.python39Packages.buildPythonPackage rec {
    name = "python-ranges";
    src = fetchFromGitHub {
      owner = "Superbird11";
      repo = "ranges";
      rev = "38ac789b61e1e33d1a8be999ca969f909bb652c0";
      sha256 = "sha256-oRQCtDBQnViNP6sJZU0NqFWkn2YpcIeGWmfx3Ne/n2c=";
    };
    # TypeError: calling <class 'ranges.RangeDict.RangeDict'> returned {}, not a test
    doCheck = false;
    propagatedBuildInputs = [ python39Packages.pytest ];
  };


in

  buildPythonPackage rec {
    name = "mutwo.common";
    src = fetchFromGitHub {
      owner = "mutwo-org";
      repo = name;
      rev = "6b7a280159bb0518bcfe4cc9baa84942944eedd0";
      sha256 = "sha256-s41Yud6AQw8LWDT08tyXdKtZ9iQhtdOIn4DoKj125p0=";
    };
    propagatedBuildInputs = [ 
      treelib
      python39Packages.numpy
      python39Packages.scipy
      python-ranges
      mutwo-core
    ];
    doCheck = true;
  }
