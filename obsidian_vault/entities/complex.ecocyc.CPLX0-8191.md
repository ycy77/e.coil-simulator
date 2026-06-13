---
entity_id: "complex.ecocyc.CPLX0-8191"
entity_type: "complex"
name: "chaperone protein DnaJ"
source_database: "EcoCyc"
source_id: "CPLX0-8191"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# chaperone protein DnaJ

`complex.ecocyc.CPLX0-8191`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8191`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P08622|protein.P08622]]

## Enriched Summary

DnaJ is a cochaperone in E. coli K-12; DnaJ modulates the substrate binding and ATPase activity of the Hsp70 chaperone, EG10241-MONOMER "DnaK". DnaJ is required for λdv in vitro replication; purified DnaJ is dimeric . DnaJ accelerates hydrolysis of DnaK-bound ATP . DnaJ has disulfide isomerase and thiol-disulfide oxidoreductase activity in vitro . DnaJ acts as a sensor for non-native proteins; DnaJ in ternary (DnaK-ATP)-substrate-DnaJ complexes selectively feeds non-native proteins with at least two exposed hydrophobic stretches into the ATP-consuming chaperone cycle . The consensus motif recognised by DnaJ is a hydrophobic core of approximately eight residues enriched for aromatic and large aliphatic hydrophobic residues and arginine . DnaJ binds to RPOH-MONOMER "σ32" in vitro; binding is independent of ATP and DnaK . In the presence of ATP a stable DnaJ-σ32-DnaK complex is formed in vitro; in the presence of ATP, the DnaJ and DnaK proteins can interfere with the efficient binding of σ32 to RNA polymerase, and are capable of disrupting a preexisting σ32-RNA polymerase complex . DnaJ acts catalytically to help DnaK bind to σ32 . Binding of DnaJ to σ32 mediates binding of DnaK to σ32 and formation of a DnaK-σ32-DnaJ complex; DnaK and DnaJ synergistically repress σ32 mediated heat shock gene transcription in vitro...

## Biological Role

Catalyzes DISULFOXRED-RXN (reaction.ecocyc.DISULFOXRED-RXN).

## Annotation

DnaJ is a cochaperone in E. coli K-12; DnaJ modulates the substrate binding and ATPase activity of the Hsp70 chaperone, EG10241-MONOMER "DnaK". DnaJ is required for λdv in vitro replication; purified DnaJ is dimeric . DnaJ accelerates hydrolysis of DnaK-bound ATP . DnaJ has disulfide isomerase and thiol-disulfide oxidoreductase activity in vitro . DnaJ acts as a sensor for non-native proteins; DnaJ in ternary (DnaK-ATP)-substrate-DnaJ complexes selectively feeds non-native proteins with at least two exposed hydrophobic stretches into the ATP-consuming chaperone cycle . The consensus motif recognised by DnaJ is a hydrophobic core of approximately eight residues enriched for aromatic and large aliphatic hydrophobic residues and arginine . DnaJ binds to RPOH-MONOMER "σ32" in vitro; binding is independent of ATP and DnaK . In the presence of ATP a stable DnaJ-σ32-DnaK complex is formed in vitro; in the presence of ATP, the DnaJ and DnaK proteins can interfere with the efficient binding of σ32 to RNA polymerase, and are capable of disrupting a preexisting σ32-RNA polymerase complex . DnaJ acts catalytically to help DnaK bind to σ32 . Binding of DnaJ to σ32 mediates binding of DnaK to σ32 and formation of a DnaK-σ32-DnaJ complex; DnaK and DnaJ synergistically repress σ32 mediated heat shock gene transcription in vitro . DnaJ binds to the N-terminal domain of native (ie folded) σ32; DnaJ and DnaK bind to distinct sites in native σ32; binding of each chaperone results in conformational change in σ32 DnaJ exhibits bipartite binding to DnaK . The DnaJ family members are a heterogeneous group of multidomain proteins sharing a conserved, typically N-terminal, ~80 amino acid domain (the J domain), a central conserved region rich in glycine and phenylalanine residues (the G-F motif)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.DISULFOXRED-RXN|reaction.ecocyc.DISULFOXRED-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P08622|protein.P08622]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-8191`
- `QSPROTEOME:QS00049701`

## Notes

2*protein.P08622
