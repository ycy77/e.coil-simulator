---
entity_id: "complex.ecocyc.GLUTAMIDOTRANS-CPLX"
entity_type: "complex"
name: "imidazole glycerol phosphate synthase"
source_database: "EcoCyc"
source_id: "GLUTAMIDOTRANS-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# imidazole glycerol phosphate synthase

`complex.ecocyc.GLUTAMIDOTRANS-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:GLUTAMIDOTRANS-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P60595|protein.P60595]], [[protein.P60664|protein.P60664]]

## Enriched Summary

Imidazole glycerol phosphate synthase (HisFH) is a heterodimer that carries out the fifth step in histidine biosynthesis, as well as generating aminoimidazole carboxamide ribonucleotide, an intermediate in purine nucleotide biosynthesis. The two components of the HisFH dimer work together to catalyze the addition of nitrogen from glutamine to the imidazole ring of phosphoribulosylformimino-AICAR-phosphate to generate aminoimidazole carboxamide ribonucleotide, D-erythro-imidazole-glycerol-phosphate, and glutamate . Although isolated HisH has no activity, isolated HisF catalyzes an ammonia-dependent reaction that uses ammonia as a nitrogen donor in the place of the physiological donor glutamine . The kinetics of HisFH have been modeled . HisFH is a 1:1 dimer of HisF and HisH . The critical residues involved in subunit interaction in general and in the specific case of cooperation of the two active sites have been examined . Imidazole glycerol phosphate synthase (HisFH) is a heterodimer that carries out the fifth step in histidine biosynthesis, as well as generating aminoimidazole carboxamide ribonucleotide, an intermediate in purine nucleotide biosynthesis...

## Biological Role

Catalyzes GLUTAMIDOTRANS-RXN (reaction.ecocyc.GLUTAMIDOTRANS-RXN).

## Annotation

Imidazole glycerol phosphate synthase (HisFH) is a heterodimer that carries out the fifth step in histidine biosynthesis, as well as generating aminoimidazole carboxamide ribonucleotide, an intermediate in purine nucleotide biosynthesis. The two components of the HisFH dimer work together to catalyze the addition of nitrogen from glutamine to the imidazole ring of phosphoribulosylformimino-AICAR-phosphate to generate aminoimidazole carboxamide ribonucleotide, D-erythro-imidazole-glycerol-phosphate, and glutamate . Although isolated HisH has no activity, isolated HisF catalyzes an ammonia-dependent reaction that uses ammonia as a nitrogen donor in the place of the physiological donor glutamine . The kinetics of HisFH have been modeled . HisFH is a 1:1 dimer of HisF and HisH . The critical residues involved in subunit interaction in general and in the specific case of cooperation of the two active sites have been examined .

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.GLUTAMIDOTRANS-RXN|reaction.ecocyc.GLUTAMIDOTRANS-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `is_component_of` <-- [[protein.P60595|protein.P60595]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P60664|protein.P60664]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## External IDs

- `EcoCyc:GLUTAMIDOTRANS-CPLX`
- `QSPROTEOME:QS00049500`

## Notes

1*protein.P60595|1*protein.P60664
