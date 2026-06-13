---
entity_id: "complex.ecocyc.CPLX0-8588"
entity_type: "complex"
name: "N-acetylmannosamine kinase"
source_database: "EcoCyc"
source_id: "CPLX0-8588"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# N-acetylmannosamine kinase

`complex.ecocyc.CPLX0-8588`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8588`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P45425|protein.P45425]]

## Enriched Summary

NanK is an N-acetylmannosamine kinase that belongs to the family of ROK sugar kinases . An L84P mutant within a variable loop region relaxes the substrate specificity of the enzyme . A nanK mutant is unable to utilize N-acetylneuraminate or N-glycolylneuraminate as the sole carbon source . Overexpression of nanK rescues the glucose auxotrophy of a glucokinase mutant . Transcription of the nanATEKQ (sialic acid catabolic) operon is repressed by NanR . NanK: NanK is an N-acetylmannosamine kinase that belongs to the family of ROK sugar kinases . An L84P mutant within a variable loop region relaxes the substrate specificity of the enzyme . A nanK mutant is unable to utilize N-acetylneuraminate or N-glycolylneuraminate as the sole carbon source . Overexpression of nanK rescues the glucose auxotrophy of a glucokinase mutant . Transcription of the nanATEKQ (sialic acid catabolic) operon is repressed by NanR . NanK:

## Biological Role

Catalyzes NANK-RXN (reaction.ecocyc.NANK-RXN).

## Annotation

NanK is an N-acetylmannosamine kinase that belongs to the family of ROK sugar kinases . An L84P mutant within a variable loop region relaxes the substrate specificity of the enzyme . A nanK mutant is unable to utilize N-acetylneuraminate or N-glycolylneuraminate as the sole carbon source . Overexpression of nanK rescues the glucose auxotrophy of a glucokinase mutant . Transcription of the nanATEKQ (sialic acid catabolic) operon is repressed by NanR . NanK:

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.NANK-RXN|reaction.ecocyc.NANK-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P45425|protein.P45425]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-8588`
- `QSPROTEOME:QS00183055`

## Notes

2*protein.P45425
