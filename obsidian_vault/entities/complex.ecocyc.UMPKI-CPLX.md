---
entity_id: "complex.ecocyc.UMPKI-CPLX"
entity_type: "complex"
name: "UMP kinase"
source_database: "EcoCyc"
source_id: "UMPKI-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# UMP kinase

`complex.ecocyc.UMPKI-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:UMPKI-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0A7E9|protein.P0A7E9]]

## Enriched Summary

UMP kinase (PyrH) is an essential enzyme involved in the de novo biosynthesis of pyrimidine nucleotides. The enzyme is subject to complex regulatory control by GTP and UTP . Feedback inhibition of UMP kinase by UTP is important for an optimal response to nutritional conditions such as growth on orotate . Temperature-sensitive and site-directed mutants in pyrH have been studied to reveal residues essential for thermodynamic stability, catalysis and allosteric regulation . Crystal structures of PyrH bound to its substrate, product, competitive inhibitor UTP and allosteric regulator GTP have been solved. The GTP and UTP binding sites do not overlap . A comparative study of E. coli UMP kinase with UMP kinases from several other Gram-negative and Gram-positive bacteria showed that regulation by GTP and UTP differed, suggesting different recognition sites on the different enzymes . PyrH appears to play a direct role in the transcriptional regulation of the carAB operon . SmbA: "suppressor of mukB" UMP kinase (PyrH) is an essential enzyme involved in the de novo biosynthesis of pyrimidine nucleotides. The enzyme is subject to complex regulatory control by GTP and UTP . Feedback inhibition of UMP kinase by UTP is important for an optimal response to nutritional conditions such as growth on orotate...

## Biological Role

Catalyzes RXN-12002 (reaction.ecocyc.RXN-12002).

## Annotation

UMP kinase (PyrH) is an essential enzyme involved in the de novo biosynthesis of pyrimidine nucleotides. The enzyme is subject to complex regulatory control by GTP and UTP . Feedback inhibition of UMP kinase by UTP is important for an optimal response to nutritional conditions such as growth on orotate . Temperature-sensitive and site-directed mutants in pyrH have been studied to reveal residues essential for thermodynamic stability, catalysis and allosteric regulation . Crystal structures of PyrH bound to its substrate, product, competitive inhibitor UTP and allosteric regulator GTP have been solved. The GTP and UTP binding sites do not overlap . A comparative study of E. coli UMP kinase with UMP kinases from several other Gram-negative and Gram-positive bacteria showed that regulation by GTP and UTP differed, suggesting different recognition sites on the different enzymes . PyrH appears to play a direct role in the transcriptional regulation of the carAB operon . SmbA: "suppressor of mukB"

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-12002|reaction.ecocyc.RXN-12002]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0A7E9|protein.P0A7E9]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## External IDs

- `EcoCyc:UMPKI-CPLX`
- `QSPROTEOME:QS00188601`

## Notes

6*protein.P0A7E9
