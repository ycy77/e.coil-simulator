---
entity_id: "complex.ecocyc.CPLX0-7761"
entity_type: "complex"
name: "bifunctional aconitate hydratase B/2-methylisocitrate dehydratase"
source_database: "EcoCyc"
source_id: "CPLX0-7761"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "bifunctional aconitate hydratase 2 and 2-methylisocitrate dehydratase"
---

# bifunctional aconitate hydratase B/2-methylisocitrate dehydratase

`complex.ecocyc.CPLX0-7761`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7761`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P36683|protein.P36683]]

## Enriched Summary

EcoCyc complex CPLX0-7761

## Biological Role

Catalyzes 4.2.1.99-RXN (reaction.ecocyc.4.2.1.99-RXN), ACONITATEDEHYDR-RXN (reaction.ecocyc.ACONITATEDEHYDR-RXN), cis-aconitate hydratase (reaction.ecocyc.ACONITATEHYDR-RXN). Bound by a [4Fe-4S] iron-sulfur cluster (molecule.ecocyc.CPD-7).

## Annotation

EcoCyc complex CPLX0-7761

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.4.2.1.99-RXN|reaction.ecocyc.4.2.1.99-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.ACONITATEDEHYDR-RXN|reaction.ecocyc.ACONITATEDEHYDR-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.ACONITATEHYDR-RXN|reaction.ecocyc.ACONITATEHYDR-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.ecocyc.CPD-7|molecule.ecocyc.CPD-7]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P36683|protein.P36683]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-7761`

## Notes

2*protein.P36683
