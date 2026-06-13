---
entity_id: "complex.ecocyc.CPLX0-8303"
entity_type: "complex"
name: "putative aminoacrylate hydrolase RutD"
source_database: "EcoCyc"
source_id: "CPLX0-8303"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# putative aminoacrylate hydrolase RutD

`complex.ecocyc.CPLX0-8303`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8303`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P75895|protein.P75895]]

## Enriched Summary

E. coli K-12 contains a previously undescribed pathway for pyrimidine degradation. RutD is predicted to function as an α/β-hydrolase . RutD is not required for the release of ammonium from uracil in vitro; it may thus be required to remove a toxic intermediate or byproduct of the pathway . It has been proposed that RutD provides catalytic enhancement of the decarboxylation of carbamate, which can also occur spontaneously . A crystal structure of RutD has been solved at 2.1 Å resolution. In the predicted catalytic triad, the nucleophile position (normally Ser, Cys or Asp) is occupied by a histidine residue that is conserved in other known RutD proteins. The proposed aminoacrylate substrate was computationally docked in the active site, and a catalytic mechanism was proposed . Expression of the rutABCDEFG operon is under the control of nitrogen regulatory protein C (NtrC) . A rutD insertion mutant loses the ability to utilize pyrimidine nucleosides and bases as the sole source of nitrogen at room temperature . RutD: "pyrimidine utilization D" Reviews: E. coli K-12 contains a previously undescribed pathway for pyrimidine degradation. RutD is predicted to function as an α/β-hydrolase . RutD is not required for the release of ammonium from uracil in vitro; it may thus be required to remove a toxic intermediate or byproduct of the pathway...

## Biological Role

Catalyzes cyanase (reaction.ecocyc.RXN0-5222).

## Annotation

E. coli K-12 contains a previously undescribed pathway for pyrimidine degradation. RutD is predicted to function as an α/β-hydrolase . RutD is not required for the release of ammonium from uracil in vitro; it may thus be required to remove a toxic intermediate or byproduct of the pathway . It has been proposed that RutD provides catalytic enhancement of the decarboxylation of carbamate, which can also occur spontaneously . A crystal structure of RutD has been solved at 2.1 Å resolution. In the predicted catalytic triad, the nucleophile position (normally Ser, Cys or Asp) is occupied by a histidine residue that is conserved in other known RutD proteins. The proposed aminoacrylate substrate was computationally docked in the active site, and a catalytic mechanism was proposed . Expression of the rutABCDEFG operon is under the control of nitrogen regulatory protein C (NtrC) . A rutD insertion mutant loses the ability to utilize pyrimidine nucleosides and bases as the sole source of nitrogen at room temperature . RutD: "pyrimidine utilization D" Reviews:

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5222|reaction.ecocyc.RXN0-5222]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P75895|protein.P75895]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-8303`
- `QSPROTEOME:QS00182699`

## Notes

2*protein.P75895
