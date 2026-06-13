---
entity_id: "complex.ecocyc.LTARTDEHYDRA-CPLX"
entity_type: "complex"
name: "L(+)-tartrate dehydratase"
source_database: "EcoCyc"
source_id: "LTARTDEHYDRA-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "L-Ttd"
---

# L(+)-tartrate dehydratase

`complex.ecocyc.LTARTDEHYDRA-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:LTARTDEHYDRA-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P05847|protein.P05847]], [[protein.P0AC35|protein.P0AC35]]

## Enriched Summary

L-tartrate dehydratase is a stereospecific enzyme that is induced during anaerobic growth on glycerol plus L- and meso-tartrates . The structure of the heterotetrameric enzyme has been modeled . L-tartrate dehydratase is a stereospecific enzyme that is induced during anaerobic growth on glycerol plus L- and meso-tartrates . The structure of the heterotetrameric enzyme has been modeled .

## Biological Role

Catalyzes LTARTDEHYDRA-RXN (reaction.ecocyc.LTARTDEHYDRA-RXN), RXN0-7485 (reaction.ecocyc.RXN0-7485). Bound by a [4Fe-4S] iron-sulfur cluster (molecule.ecocyc.CPD-7).

## Annotation

L-tartrate dehydratase is a stereospecific enzyme that is induced during anaerobic growth on glycerol plus L- and meso-tartrates . The structure of the heterotetrameric enzyme has been modeled .

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.LTARTDEHYDRA-RXN|reaction.ecocyc.LTARTDEHYDRA-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7485|reaction.ecocyc.RXN0-7485]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `binds` <-- [[molecule.ecocyc.CPD-7|molecule.ecocyc.CPD-7]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P05847|protein.P05847]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` <-- [[protein.P0AC35|protein.P0AC35]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:LTARTDEHYDRA-CPLX`
- `QSPROTEOME:QS00049504`

## Notes

2*protein.P05847|2*protein.P0AC35
