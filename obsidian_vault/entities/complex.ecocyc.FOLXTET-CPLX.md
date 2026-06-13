---
entity_id: "complex.ecocyc.FOLXTET-CPLX"
entity_type: "complex"
name: "dihydroneopterin triphosphate 2'-epimerase"
source_database: "EcoCyc"
source_id: "FOLXTET-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# dihydroneopterin triphosphate 2'-epimerase

`complex.ecocyc.FOLXTET-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:FOLXTET-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0AC19|protein.P0AC19]]

## Enriched Summary

Dihydroneopterin triphosphate 2'-epimerase (FolX) has been known in E. coli for some time . FolX is required for tetrahydromonapterin biosynthesis. The epimerase reaction yields dihydromonapterin triphosphate, from which tetrahydromonapterin is produced after successive dephosphorylation and oxidation . Tetrahydromonapterin is the major pterin in E. coli . Subinhibitory levels of the antifolate antibiotic CPD-21032 (SMX) upregulate the production of a family of hybrid pterin-phenylpyruvate conjugates called colipterins. FolX is involved in the production of these colipterins, suggesting that they are derived from the monapterin biosynthesis pathway. Several colipterins ameliorate colitis in an IL-10-dependent manner in a mouse model . A crystal structure of FolX has been solved at 2.9 Å resolution. Two tetramers associate head-to-head to form the active enzyme complex . A folX deletion mutant shows no detectable growth defect on complete and minimal medium . E. coli normally excretes a form of monapterin into the medium ; the extracellular monapterin is lost in a folX mutant, while the folate profile of the cells remains the same as in wild type . Disruption of either folX or folM leads to decreased sensitivity to the antibiotics trimethoprim and slufamonomethoxine . A ΔfolX mutant lacks production of the major colipterins in response to subinihibitory levels of SMX...

## Biological Role

Catalyzes H2NTPEPIM-RXN (reaction.ecocyc.H2NTPEPIM-RXN). Bound by Magnesium cation (molecule.C00305).

## Annotation

Dihydroneopterin triphosphate 2'-epimerase (FolX) has been known in E. coli for some time . FolX is required for tetrahydromonapterin biosynthesis. The epimerase reaction yields dihydromonapterin triphosphate, from which tetrahydromonapterin is produced after successive dephosphorylation and oxidation . Tetrahydromonapterin is the major pterin in E. coli . Subinhibitory levels of the antifolate antibiotic CPD-21032 (SMX) upregulate the production of a family of hybrid pterin-phenylpyruvate conjugates called colipterins. FolX is involved in the production of these colipterins, suggesting that they are derived from the monapterin biosynthesis pathway. Several colipterins ameliorate colitis in an IL-10-dependent manner in a mouse model . A crystal structure of FolX has been solved at 2.9 Å resolution. Two tetramers associate head-to-head to form the active enzyme complex . A folX deletion mutant shows no detectable growth defect on complete and minimal medium . E. coli normally excretes a form of monapterin into the medium ; the extracellular monapterin is lost in a folX mutant, while the folate profile of the cells remains the same as in wild type . Disruption of either folX or folM leads to decreased sensitivity to the antibiotics trimethoprim and slufamonomethoxine . A ΔfolX mutant lacks production of the major colipterins in response to subinihibitory levels of SMX . Review:

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.H2NTPEPIM-RXN|reaction.ecocyc.H2NTPEPIM-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0AC19|protein.P0AC19]] `EcoCyc` `database` - EcoCyc component coefficient=8 | EcoCyc protcplxs.col coefficient=8

## External IDs

- `EcoCyc:FOLXTET-CPLX`
- `QSPROTEOME:QS00181777`

## Notes

8*protein.P0AC19
