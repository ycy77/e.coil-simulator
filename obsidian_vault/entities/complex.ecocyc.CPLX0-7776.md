---
entity_id: "complex.ecocyc.CPLX0-7776"
entity_type: "complex"
name: "fructose 1,6-bisphosphatase YggF"
source_database: "EcoCyc"
source_id: "CPLX0-7776"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# fructose 1,6-bisphosphatase YggF

`complex.ecocyc.CPLX0-7776`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7776`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P21437|protein.P21437]]

## Enriched Summary

YggF is a type II fructose-1,6-bisphosphatase and shows 58% sequence identity to CPLX0-303 "GlpX" . Genomic SELEX screening predicted a number of novel target genes, including yggF, to be under the control of transcriptional activator cAMP-CRP. The data suggested that CRP has a major role in control of the switch between glycolysis and gluconeogenesis . Genomic SELEX screening is described in . YggF is a type II fructose-1,6-bisphosphatase and shows 58% sequence identity to CPLX0-303 "GlpX" . Genomic SELEX screening predicted a number of novel target genes, including yggF, to be under the control of transcriptional activator cAMP-CRP. The data suggested that CRP has a major role in control of the switch between glycolysis and gluconeogenesis . Genomic SELEX screening is described in .

## Biological Role

Catalyzes F16BDEPHOS-RXN (reaction.ecocyc.F16BDEPHOS-RXN). Bound by Mn2+ (molecule.ecocyc.MN_2).

## Annotation

YggF is a type II fructose-1,6-bisphosphatase and shows 58% sequence identity to CPLX0-303 "GlpX" . Genomic SELEX screening predicted a number of novel target genes, including yggF, to be under the control of transcriptional activator cAMP-CRP. The data suggested that CRP has a major role in control of the switch between glycolysis and gluconeogenesis . Genomic SELEX screening is described in .

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.F16BDEPHOS-RXN|reaction.ecocyc.F16BDEPHOS-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P21437|protein.P21437]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-7776`
- `QSPROTEOME:QS00049664`

## Notes

2*protein.P21437
