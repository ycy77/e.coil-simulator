---
entity_id: "complex.ecocyc.CPLX0-12207"
entity_type: "complex"
name: "oxamate carbamoyltransferase"
source_database: "EcoCyc"
source_id: "CPLX0-12207"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# oxamate carbamoyltransferase

`complex.ecocyc.CPLX0-12207`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-12207`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0AAS5|protein.P0AAS5]], [[protein.P77129|protein.P77129]], [[protein.Q47208|protein.Q47208]]

## Enriched Summary

This enzyme complex is a novel transcarbamylase with no known similarity to other enzymes of the transcarbamylase family. The specific stoichiometry of the complex was inferred . This enzyme complex is a novel transcarbamylase with no known similarity to other enzymes of the transcarbamylase family. The specific stoichiometry of the complex was inferred .

## Biological Role

Catalyzes OXAMATE-CARBAMOYLTRANSFERASE-RXN (reaction.ecocyc.OXAMATE-CARBAMOYLTRANSFERASE-RXN).

## Annotation

This enzyme complex is a novel transcarbamylase with no known similarity to other enzymes of the transcarbamylase family. The specific stoichiometry of the complex was inferred .

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.OXAMATE-CARBAMOYLTRANSFERASE-RXN|reaction.ecocyc.OXAMATE-CARBAMOYLTRANSFERASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `is_component_of` <-- [[protein.P0AAS5|protein.P0AAS5]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P77129|protein.P77129]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` <-- [[protein.Q47208|protein.Q47208]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-12207`
- `QSPROTEOME:QS00196461`

## Notes

1*protein.P0AAS5|2*protein.P77129|2*protein.Q47208
