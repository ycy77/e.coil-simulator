---
entity_id: "complex.ecocyc.CPLX0-7622"
entity_type: "complex"
name: "L-serine deaminase III"
source_database: "EcoCyc"
source_id: "CPLX0-7622"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# L-serine deaminase III

`complex.ecocyc.CPLX0-7622`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7622`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P42630|protein.P42630]]

## Enriched Summary

L-serine deaminase III (TdcG) is one of three enzymes carrying out the sole step in the pathway of L-serine degradation, converting serine into a basic cellular building block, pyruvate. TdcG catalyzes the conversion of L-serine into pyruvate and ammonia . Like the other two known serine deaminases, TdcG has a catalytically critical iron-sulfur cluster that is destroyed by exposure to oxygen . tdcG is part of an operon that is induced under anaerobic conditions . A notable member of this operon is the catabolic threonine deaminase gene EG10990. The presence of both genes on the same operon likely explains early observations that suggested the existence of a bifunctional threonine/serine deaminase . Expression of tdcG is also limited by glucose, much like fellow serine deaminase gene EG11623 . L-serine deaminase III (TdcG) is one of three enzymes carrying out the sole step in the pathway of L-serine degradation, converting serine into a basic cellular building block, pyruvate. TdcG catalyzes the conversion of L-serine into pyruvate and ammonia . Like the other two known serine deaminases, TdcG has a catalytically critical iron-sulfur cluster that is destroyed by exposure to oxygen . tdcG is part of an operon that is induced under anaerobic conditions . A notable member of this operon is the catabolic threonine deaminase gene EG10990...

## Biological Role

Catalyzes 4.3.1.17-RXN (reaction.ecocyc.4.3.1.17-RXN). Bound by a [4Fe-4S] iron-sulfur cluster (molecule.ecocyc.CPD-7).

## Annotation

L-serine deaminase III (TdcG) is one of three enzymes carrying out the sole step in the pathway of L-serine degradation, converting serine into a basic cellular building block, pyruvate. TdcG catalyzes the conversion of L-serine into pyruvate and ammonia . Like the other two known serine deaminases, TdcG has a catalytically critical iron-sulfur cluster that is destroyed by exposure to oxygen . tdcG is part of an operon that is induced under anaerobic conditions . A notable member of this operon is the catabolic threonine deaminase gene EG10990. The presence of both genes on the same operon likely explains early observations that suggested the existence of a bifunctional threonine/serine deaminase . Expression of tdcG is also limited by glucose, much like fellow serine deaminase gene EG11623 .

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.4.3.1.17-RXN|reaction.ecocyc.4.3.1.17-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.ecocyc.CPD-7|molecule.ecocyc.CPD-7]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P42630|protein.P42630]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-7622`
- `QSPROTEOME:QS00049628`

## Notes

2*protein.P42630
