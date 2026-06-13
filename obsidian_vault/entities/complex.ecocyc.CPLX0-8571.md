---
entity_id: "complex.ecocyc.CPLX0-8571"
entity_type: "complex"
name: "dihydromonapterin reductase"
source_database: "EcoCyc"
source_id: "CPLX0-8571"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# dihydromonapterin reductase

`complex.ecocyc.CPLX0-8571`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8571`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0AFS3|protein.P0AFS3]]

## Enriched Summary

FolM is a dihydromonapterin reductase. The activity of the enzyme with the dihydromonapterin substrate is 16-fold higher than with dihydrofolate. Neither dihydroneopterin nor monapterin are substrates . Subinhibitory levels of the antifolate antibiotic CPD-21032 (SMX) upregulate the production of a family of hybrid pterin-phenylpyruvate conjugates called colipterins. FolM is involved in the production of these colipterins, suggesting that they are derived from the monapterin biosynthesis pathway. Several colipterins ameliorate colitis in an IL-10-dependent manner in a mouse model . Certain osmolytes preferentially interact with FolM; these interactions destabilize the protein and can affect ligand binding . Overexpression of folM from a plasmid can complement the severe growth defect of a folA deletion mutant. A folM deletion mutant has no detectable growth defect; folA is synthetically lethal with folM . Disruption of either folM or folX leads to decreased sensitivity to the antibiotics trimethoprim and sulfamonomethoxine . A ΔfolM mutant lacks production of the major colipterins in response to subinihibitory levels of SMX . FolM is a dihydromonapterin reductase. The activity of the enzyme with the dihydromonapterin substrate is 16-fold higher than with dihydrofolate. Neither dihydroneopterin nor monapterin are substrates...

## Biological Role

Catalyzes DIHYDROFOLATEREDUCT-RXN (reaction.ecocyc.DIHYDROFOLATEREDUCT-RXN), RXN0-6367 (reaction.ecocyc.RXN0-6367).

## Annotation

FolM is a dihydromonapterin reductase. The activity of the enzyme with the dihydromonapterin substrate is 16-fold higher than with dihydrofolate. Neither dihydroneopterin nor monapterin are substrates . Subinhibitory levels of the antifolate antibiotic CPD-21032 (SMX) upregulate the production of a family of hybrid pterin-phenylpyruvate conjugates called colipterins. FolM is involved in the production of these colipterins, suggesting that they are derived from the monapterin biosynthesis pathway. Several colipterins ameliorate colitis in an IL-10-dependent manner in a mouse model . Certain osmolytes preferentially interact with FolM; these interactions destabilize the protein and can affect ligand binding . Overexpression of folM from a plasmid can complement the severe growth defect of a folA deletion mutant. A folM deletion mutant has no detectable growth defect; folA is synthetically lethal with folM . Disruption of either folM or folX leads to decreased sensitivity to the antibiotics trimethoprim and sulfamonomethoxine . A ΔfolM mutant lacks production of the major colipterins in response to subinihibitory levels of SMX .

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.DIHYDROFOLATEREDUCT-RXN|reaction.ecocyc.DIHYDROFOLATEREDUCT-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-6367|reaction.ecocyc.RXN0-6367]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0AFS3|protein.P0AFS3]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:CPLX0-8571`
- `QSPROTEOME:QS00188525`

## Notes

4*protein.P0AFS3
