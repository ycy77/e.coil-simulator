---
entity_id: "complex.ecocyc.CPLX0-2982"
entity_type: "complex"
name: "FtsH/HflKC protease complex"
source_database: "EcoCyc"
source_id: "CPLX0-2982"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: "CCI-PM-BAC-NEG-GN"
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "FtsH holoenzyme"
---

# FtsH/HflKC protease complex

`complex.ecocyc.CPLX0-2982`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-2982`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Location: CCI-PM-BAC-NEG-GN
- Complex type: `regulatory`
- Components: [[complex.ecocyc.CPLX0-1321|complex.ecocyc.CPLX0-1321]], [[protein.P0AAI3|protein.P0AAI3]]

## Enriched Summary

Intracellular proteases enforce protein quality control and modify the proteome composition in response to environmental and nutritional cues. Most targeted proteolysis in bacteria is performed by a group of proteases that was named the AAA+ family (ATPases Associated with various cellular Activities) . All of these proteins contain ring-shaped hexamers that use energy from ATP hydrolysis to unfold protein substrates, followed by translocation of the unfolded chains through a central channel into a degradation chamber, where they are degraded. TAX-562 encodes five AAA+ proteases: CPLX0-2982 FtsH, CPLX0-3107 ClpXP, CPLX0-3104 ClpAP, EG10542-MONOMER Lon, and CPLX0-1163 HslUV . FtsH is a zinc-dependent metalloendoprotease required for survival . FtsH degrades a number of cellular proteins, including the membrane protein EG11113-MONOMER "YccA" and orphaned complex components such as SecY in the absence of SecE and unaccompanied ATPB-MONOMER "subunit a" of ATPase F0 . FtsH degrades SecY and to a lesser extent SecE in LamB-LacZ fusion strains with a 'jammed' Sec translocator . FtsH degrades the heat shock promoter protein RPOH-MONOMER σ32 and UDPACYLGLCNACDEACETYL-MONOMER (LpxC) which catalyses the first committed step in lipopolysaccharide biosnthesis (see further )...

## Biological Role

Catalyzes RXN-21299 (reaction.ecocyc.RXN-21299). Bound by Zinc cation (molecule.C00038).

## Annotation

Intracellular proteases enforce protein quality control and modify the proteome composition in response to environmental and nutritional cues. Most targeted proteolysis in bacteria is performed by a group of proteases that was named the AAA+ family (ATPases Associated with various cellular Activities) . All of these proteins contain ring-shaped hexamers that use energy from ATP hydrolysis to unfold protein substrates, followed by translocation of the unfolded chains through a central channel into a degradation chamber, where they are degraded. TAX-562 encodes five AAA+ proteases: CPLX0-2982 FtsH, CPLX0-3107 ClpXP, CPLX0-3104 ClpAP, EG10542-MONOMER Lon, and CPLX0-1163 HslUV . FtsH is a zinc-dependent metalloendoprotease required for survival . FtsH degrades a number of cellular proteins, including the membrane protein EG11113-MONOMER "YccA" and orphaned complex components such as SecY in the absence of SecE and unaccompanied ATPB-MONOMER "subunit a" of ATPase F0 . FtsH degrades SecY and to a lesser extent SecE in LamB-LacZ fusion strains with a 'jammed' Sec translocator . FtsH degrades the heat shock promoter protein RPOH-MONOMER σ32 and UDPACYLGLCNACDEACETYL-MONOMER (LpxC) which catalyses the first committed step in lipopolysaccharide biosnthesis (see further ). Further substrates (G7321-MONOMER "YfgM", FDOH-MONOMER "FdoH", CPLX0-248 "IscS", DALADEHYDROG-CPLX "DadA", G7651-MONOMER "YhbT", G6253-MONOMER "YlaC", EG10272-MONOMER "ExbD" and SECD "SecD") have been identified using a substrate trapping variant of FtsH . FtsH degrades CFA-CPLX cyclopropane fatty acid synthase in vitro and in vivo . FtsH degrades partially unfolded DIHYDROFOLATEREDUCT-MONOMER by recognizing an internal sequence . FtsH also controls the abundance of a number of phage proteins, modulating levels

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-21299|reaction.ecocyc.RXN-21299]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (5)

- `binds` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[complex.ecocyc.CPLX0-1321|complex.ecocyc.CPLX0-1321]] `EcoCyc` `database` - EcoCyc component coefficient=6
- `is_component_of` <-- [[protein.P0AAI3|protein.P0AAI3]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6
- `is_component_of` <-- [[protein.P0ABC3|protein.P0ABC3]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=6
- `is_component_of` <-- [[protein.P0ABC7|protein.P0ABC7]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=6

## External IDs

- `EcoCyc:CPLX0-2982`
- `PDB:7WI3`
- `PDB:7VHQ`
- `PDB:7VHP`

## Notes

6*complex.ecocyc.CPLX0-1321|6*protein.P0AAI3
