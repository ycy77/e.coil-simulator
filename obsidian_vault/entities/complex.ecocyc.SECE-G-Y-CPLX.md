---
entity_id: "complex.ecocyc.SECE-G-Y-CPLX"
entity_type: "complex"
name: "SecYEG translocon"
source_database: "EcoCyc"
source_id: "SECE-G-Y-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# SecYEG translocon

`complex.ecocyc.SECE-G-Y-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:SECE-G-Y-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0AG96|protein.P0AG96]], [[protein.P0AG99|protein.P0AG99]], [[protein.P0AGA2|protein.P0AGA2]]

## Enriched Summary

SecYEG is a cytoplasmic membrane complex that mediates the transport of newly synthesized polypeptides across, or their integration into, the inner membrane of E. coli K-12. SecY, SecE and an unidentified polypeptide termed 'band1' (later shown to be SecG ) form a stable complex which supports precursor protein translocation in vitro ; the energy for protein translocation is provided by the motor protein ATPase CPLX0-8089 "SecA" and the proton motive force. SecYEG and YIDC YidC are implicated as receptors in an mRNA targeting pathway that acts in parallel to the canonical SRP-dependent pathway for membrane protein insertion . Escherichia coli SecYEG has been shown to form dimers in membranes. SecYEG has been stabilized with monoclonal antibodies to form dimers in detergent solution . FRET and freeze-fracture analyses indicate the heterotrimeric SecYEG exists in the membrane in an equilibrium of monomers, dimers, and tetramers, which is shifted toward oligomerization by insertion into the membrane of preprotein-bound SecA in the presence of ATP . The oligomeric state of the SecYEG complex may be influenced by the substrate that is to be transported . A SecYEG monomer is sufficient for SecA driven protein translocation in vitro . The SecYEG dimer binds one substrate polypeptide . Two copies of SecY are required for pre-protein transport in vitro...

## Biological Role

Component of SecYEG-SecA complex (complex.ecocyc.CPLX0-12269), Sec Holo-Translocon (complex.ecocyc.SEC-SECRETION-CPLX).

## Annotation

SecYEG is a cytoplasmic membrane complex that mediates the transport of newly synthesized polypeptides across, or their integration into, the inner membrane of E. coli K-12. SecY, SecE and an unidentified polypeptide termed 'band1' (later shown to be SecG ) form a stable complex which supports precursor protein translocation in vitro ; the energy for protein translocation is provided by the motor protein ATPase CPLX0-8089 "SecA" and the proton motive force. SecYEG and YIDC YidC are implicated as receptors in an mRNA targeting pathway that acts in parallel to the canonical SRP-dependent pathway for membrane protein insertion . Escherichia coli SecYEG has been shown to form dimers in membranes. SecYEG has been stabilized with monoclonal antibodies to form dimers in detergent solution . FRET and freeze-fracture analyses indicate the heterotrimeric SecYEG exists in the membrane in an equilibrium of monomers, dimers, and tetramers, which is shifted toward oligomerization by insertion into the membrane of preprotein-bound SecA in the presence of ATP . The oligomeric state of the SecYEG complex may be influenced by the substrate that is to be transported . A SecYEG monomer is sufficient for SecA driven protein translocation in vitro . The SecYEG dimer binds one substrate polypeptide . Two copies of SecY are required for pre-protein transport in vitro . Purified SecYEG has been incorporated into nanodiscs (soluble lipid bilayer structures of controlled size). Nanodisc reconstituted SecYEG binds monomeric SecA. Acidic lipids in the vicinity of nanodisc reconstituted SecYEG contribute to both SecA binding and ATPase activity . An inner membrane glycolipid, termed CPD-15878, modulates the dimer orientation of SecYEG . Cardiolipin binding to SecY is critical for SecYEG mediated pro

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-12269|complex.ecocyc.CPLX0-12269]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` --> [[complex.ecocyc.SEC-SECRETION-CPLX|complex.ecocyc.SEC-SECRETION-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=

## Incoming Edges (3)

- `is_component_of` <-- [[protein.P0AG96|protein.P0AG96]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P0AG99|protein.P0AG99]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P0AGA2|protein.P0AGA2]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## External IDs

- `EcoCyc:SECE-G-Y-CPLX`
- `PDB:2AKH`
- `PDB:2AKI`
- `PDB:3J46`
- `PDB:3J45`
- `PDB:4V6M`
- `PDB:5GAE`
- `PDB:5NCO`
- `PDB:5MG3`
- `QSPROTEOME:QS00049527`

## Notes

protein.P0AG96|protein.P0AG99|protein.P0AGA2
