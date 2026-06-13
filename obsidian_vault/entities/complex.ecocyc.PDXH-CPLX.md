---
entity_id: "complex.ecocyc.PDXH-CPLX"
entity_type: "complex"
name: "pyridoxine 5'-phosphate oxidase / pyridoxamine 5'-phosphate oxidase"
source_database: "EcoCyc"
source_id: "PDXH-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# pyridoxine 5'-phosphate oxidase / pyridoxamine 5'-phosphate oxidase

`complex.ecocyc.PDXH-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:PDXH-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0AFI7|protein.P0AFI7]]

## Enriched Summary

PdxH catalyzes the oxidation of pyridoxine 5'-phosphate (PNP) to pyridoxal 5'-phosphate (PLP) in the final step of PYRIDOXSYN-PWY. It also oxidizes pyridoxamine 5'-phosphate (PMP) to PLP as part of the PLPSAL-PWY pathway. In vitro, the enzyme shows no activity in the absence of oxygen . The reaction mechanism of PdxH was suggested to involve the transfer of a hydride ion between C4' of the substrate and N5 of FMN . Product inhibition by PLP was shown to be of a mixed type that results from binding to an allosteric site . The pool sizes of free and protein-bound B6 vitamers in E. coli has been measured . The enzyme is homodimeric and contains two molecules of flavin mononucleotide (FMN) per dimer . Crystal structures of PdxH have been solved . Each subunit forms a two-domain α/β-barrel fold; the two non-covalently bound FMN cofactors each interact with both subunits at the dimer interface . Site-directed mutagenesis of several residues within the active site showed that R197 is required for both substrate binding and catalysis . One molecule of the reaction product PLP is able to bind tightly to each PdxH subunit at a non-catalytic site; PLP can be transferred from there to apo-GLYOHMETRANS-MONOMER in vitro . Crystal structures of PLP-bound PdxH suggested that PLP is able to transfer from the active site to the non-catalytic binding site via a tunnel between the sites...

## Biological Role

Catalyzes PMPOXI-RXN (reaction.ecocyc.PMPOXI-RXN), PNPOXI-RXN (reaction.ecocyc.PNPOXI-RXN). Bound by FMN (molecule.C00061).

## Annotation

PdxH catalyzes the oxidation of pyridoxine 5'-phosphate (PNP) to pyridoxal 5'-phosphate (PLP) in the final step of PYRIDOXSYN-PWY. It also oxidizes pyridoxamine 5'-phosphate (PMP) to PLP as part of the PLPSAL-PWY pathway. In vitro, the enzyme shows no activity in the absence of oxygen . The reaction mechanism of PdxH was suggested to involve the transfer of a hydride ion between C4' of the substrate and N5 of FMN . Product inhibition by PLP was shown to be of a mixed type that results from binding to an allosteric site . The pool sizes of free and protein-bound B6 vitamers in E. coli has been measured . The enzyme is homodimeric and contains two molecules of flavin mononucleotide (FMN) per dimer . Crystal structures of PdxH have been solved . Each subunit forms a two-domain α/β-barrel fold; the two non-covalently bound FMN cofactors each interact with both subunits at the dimer interface . Site-directed mutagenesis of several residues within the active site showed that R197 is required for both substrate binding and catalysis . One molecule of the reaction product PLP is able to bind tightly to each PdxH subunit at a non-catalytic site; PLP can be transferred from there to apo-GLYOHMETRANS-MONOMER in vitro . Crystal structures of PLP-bound PdxH suggested that PLP is able to transfer from the active site to the non-catalytic binding site via a tunnel between the sites . An additional crystal structure in a different conformation enabled modeling of the mechanistic reaction pathway that may allow passage of PLP from the active site to the non-catalytic secondary PLP site . However, structural analysis of PdxH with an impaired active site showed that the allosteric site for tight PLP binding is located at the subunit interface. The PLP binding and allosteric properties of

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.PMPOXI-RXN|reaction.ecocyc.PMPOXI-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.PNPOXI-RXN|reaction.ecocyc.PNPOXI-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00061|molecule.C00061]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0AFI7|protein.P0AFI7]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:PDXH-CPLX`
- `QSPROTEOME:QS00181759`

## Notes

2*protein.P0AFI7
