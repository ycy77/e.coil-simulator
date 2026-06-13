---
entity_id: "complex.ecocyc.CPLX0-7841"
entity_type: "complex"
name: "sulfite reductase, flavoprotein subunit complex"
source_database: "EcoCyc"
source_id: "CPLX0-7841"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# sulfite reductase, flavoprotein subunit complex

`complex.ecocyc.CPLX0-7841`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7841`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P38038|protein.P38038]]

## Enriched Summary

CysJ is the flavin or α subunit (SiRFP) of sulfite reductase (SiR). Sulfite reductase is involved in the assimilation of sulfate and catalyzes the transfer of six electrons from NADPH to sulfite to produce sulfide. CysJ binds one FMN and one FAD per polypeptide chain. This subunit is responsible for the flavin reductase activity . An N-terminal 23 kDa fragment of CysJ contains the FMN cofactor and is responsible for homomultimerization, while a C-terminal 43 kDa fragment contains the FAD cofactor and NADPH-dependent catalytic activity . CysJ is a homo-octomeric flavoprotein in which each α protein binds one FAD and one FMN and contains an NADPH-binding site . Experiments with the purified E. coli B enzyme showed that FAD is bound much more tightly than FMN; the FAD prosthetic group serves as the entry port for electrons from NADPH . The isolated flavoprotein is able to catalyze the reduction of riboflavins , paraquat and a variety of diaphorase acceptors . NMR studies of CysJ showed that the redox cofactors FMN, FAD and NADPH are located near each other and close to the protein surface . Crystal structures of a monomeric CysJ fragment have been solved . A 3D structure of the flavodoxin-like domain of CysJ was determined by NMR. This domain is involved with shuttling electrons from the FAD to CysJ...

## Biological Role

Catalyzes NADPH-DEHYDROGENASE-FLAVIN-RXN (reaction.ecocyc.NADPH-DEHYDROGENASE-FLAVIN-RXN). Component of assimilatory sulfite reductase (NADPH) (complex.ecocyc.SULFITE-REDUCT-CPLX). Bound by FAD (molecule.C00016), FMN (molecule.C00061).

## Annotation

CysJ is the flavin or α subunit (SiRFP) of sulfite reductase (SiR). Sulfite reductase is involved in the assimilation of sulfate and catalyzes the transfer of six electrons from NADPH to sulfite to produce sulfide. CysJ binds one FMN and one FAD per polypeptide chain. This subunit is responsible for the flavin reductase activity . An N-terminal 23 kDa fragment of CysJ contains the FMN cofactor and is responsible for homomultimerization, while a C-terminal 43 kDa fragment contains the FAD cofactor and NADPH-dependent catalytic activity . CysJ is a homo-octomeric flavoprotein in which each α protein binds one FAD and one FMN and contains an NADPH-binding site . Experiments with the purified E. coli B enzyme showed that FAD is bound much more tightly than FMN; the FAD prosthetic group serves as the entry port for electrons from NADPH . The isolated flavoprotein is able to catalyze the reduction of riboflavins , paraquat and a variety of diaphorase acceptors . NMR studies of CysJ showed that the redox cofactors FMN, FAD and NADPH are located near each other and close to the protein surface . Crystal structures of a monomeric CysJ fragment have been solved . A 3D structure of the flavodoxin-like domain of CysJ was determined by NMR. This domain is involved with shuttling electrons from the FAD to CysJ . Structural characterization of the SiRFP subunit reveals its domains are flexible and can interact with each other both intermolecularly and intramolecularly whether the subunit is restricted to the open, electron-donating conformation or to the closed, electron-accepting conformation . CysJ can substitute for FMNREDUCT-MONOMER in generating the tyrosine free radical of the R2 subunit of ribonucleotide reductase . A cysJ mutant is less sensitive to paraquat than wild type . c

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.NADPH-DEHYDROGENASE-FLAVIN-RXN|reaction.ecocyc.NADPH-DEHYDROGENASE-FLAVIN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_component_of` --> [[complex.ecocyc.SULFITE-REDUCT-CPLX|complex.ecocyc.SULFITE-REDUCT-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1

## Incoming Edges (3)

- `binds` <-- [[molecule.C00016|molecule.C00016]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.C00061|molecule.C00061]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P38038|protein.P38038]] `EcoCyc` `database` - EcoCyc component coefficient=8 | EcoCyc protcplxs.col coefficient=8

## External IDs

- `EcoCyc:CPLX0-7841`
- `QSPROTEOME:QS00188581`

## Notes

8*protein.P38038
