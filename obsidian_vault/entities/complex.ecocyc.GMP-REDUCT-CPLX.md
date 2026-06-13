---
entity_id: "complex.ecocyc.GMP-REDUCT-CPLX"
entity_type: "complex"
name: "GMP reductase"
source_database: "EcoCyc"
source_id: "GMP-REDUCT-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# GMP reductase

`complex.ecocyc.GMP-REDUCT-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:GMP-REDUCT-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P60560|protein.P60560]]

## Enriched Summary

GMP reductase catalyzes the conversion of GMP to IMP by reductive deamination. This reaction is part of the purine salvage pathway and becomes essential when purine-requiring mutants are grown with guanine or xanthine as the sole sources of purine. GMP reductase follows an ordered bi-bi kinetic mechanism . Expression of guaC is induced by guanine derivatives and repressed by adenine . GMP is thought to be the most probable inducer in vivo . Expression is sensitive to cAMP levels, although not due to catabolite repression . Sequences in the predicted guaC promoter region indicate that expression may be regulated by the stringent response . GMP reductase catalyzes the conversion of GMP to IMP by reductive deamination. This reaction is part of the purine salvage pathway and becomes essential when purine-requiring mutants are grown with guanine or xanthine as the sole sources of purine. GMP reductase follows an ordered bi-bi kinetic mechanism . Expression of guaC is induced by guanine derivatives and repressed by adenine . GMP is thought to be the most probable inducer in vivo . Expression is sensitive to cAMP levels, although not due to catabolite repression . Sequences in the predicted guaC promoter region indicate that expression may be regulated by the stringent response .

## Biological Role

Catalyzes GMP-REDUCT-RXN (reaction.ecocyc.GMP-REDUCT-RXN).

## Annotation

GMP reductase catalyzes the conversion of GMP to IMP by reductive deamination. This reaction is part of the purine salvage pathway and becomes essential when purine-requiring mutants are grown with guanine or xanthine as the sole sources of purine. GMP reductase follows an ordered bi-bi kinetic mechanism . Expression of guaC is induced by guanine derivatives and repressed by adenine . GMP is thought to be the most probable inducer in vivo . Expression is sensitive to cAMP levels, although not due to catabolite repression . Sequences in the predicted guaC promoter region indicate that expression may be regulated by the stringent response .

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.GMP-REDUCT-RXN|reaction.ecocyc.GMP-REDUCT-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P60560|protein.P60560]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:GMP-REDUCT-CPLX`
- `QSPROTEOME:QS00049721`

## Notes

4*protein.P60560
