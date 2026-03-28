{
  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";

  outputs = { self, nixpkgs }:
    let
      system = "x86_64-linux";
      pkgs = nixpkgs.legacyPackages.${system};
    in
    {
      packages.${system} = {
        greenwithenvy = pkgs.python3Packages.buildPythonPackage {
          pname = "greenwithenvy";
          version = "3.5.2";
          src = self;
          pyproject = true;
          build-system = [ pkgs.python3Packages.setuptools ];
        };
        default = self.packages.${system}.greenwithenvy;
      };

      buildInputs = with pkgs; [ pciutils ];

      devShells.default = pkgs.mkShellNoCC {
        packages = with pkgs; [
          (python3.withPackages(ps: with ps; [ setuptools ]))
          pciutils
        ];
      };
    };
}
