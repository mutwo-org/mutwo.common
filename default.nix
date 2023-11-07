let
  sourcesTarball = fetchTarball "https://github.com/mutwo-org/mutwo-nix/archive/refs/heads/main.tar.gz";
  mutwo-common = import (sourcesTarball + "/mutwo.common/default.nix") {};
  mutwo-common-local = mutwo-common.overrideAttrs (
    finalAttrs: previousAttrs: {
       src = ./.;
    }
  );
in
  mutwo-common-local
