---
entity_id: "complex.ecocyc.CPLX0-8212"
entity_type: "complex"
name: "erythronate-4-phosphate dehydrogenase"
source_database: "EcoCyc"
source_id: "CPLX0-8212"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# erythronate-4-phosphate dehydrogenase

`complex.ecocyc.CPLX0-8212`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8212`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P05459|protein.P05459]]

## Enriched Summary

Erythronate-4-phosphate dehydrogenase (PdxB) catalyzes the second reaction in the PYRIDOXSYN-PWY pathway, the NAD-dependent oxidation of 4-phosphoerythronate to 2-oxo-3-hydroxy-4-phosphobutanoate . PdxB is a nicotino-enzyme that contains a tightly bound NAD cofactor that must be re-oxidized after oxidation of erythronate 4-phosphate. The three α-keto acids α-ketoglutarate, oxaloacetate and pyruvate can serve as cosubstrates . pdxB is essential for growth in minimal medium . pdxB mutants show pyridoxine auxotrophy . Multicopy suppressors of the PLP auxotrophy of a pdxB deletion strain have been isolated and may be part of a serendipitous metabolic pathway that produces an intermediate of the PYRIDOXSYN-PWY pathway, 2-oxo-3-hydroxy-4-phosphobutanoate, that lies downstream of PdxB . An additional promiscuous enzyme activity that can bypass PdxB has been discovered . pdxB transcription is positively growth rate-regulated . Erythronate-4-phosphate dehydrogenase (PdxB) catalyzes the second reaction in the PYRIDOXSYN-PWY pathway, the NAD-dependent oxidation of 4-phosphoerythronate to 2-oxo-3-hydroxy-4-phosphobutanoate . PdxB is a nicotino-enzyme that contains a tightly bound NAD cofactor that must be re-oxidized after oxidation of erythronate 4-phosphate. The three α-keto acids α-ketoglutarate, oxaloacetate and pyruvate can serve as cosubstrates...

## Biological Role

Catalyzes ERYTHRON4PDEHYDROG-RXN (reaction.ecocyc.ERYTHRON4PDEHYDROG-RXN). Bound by NAD+ (molecule.C00003).

## Annotation

Erythronate-4-phosphate dehydrogenase (PdxB) catalyzes the second reaction in the PYRIDOXSYN-PWY pathway, the NAD-dependent oxidation of 4-phosphoerythronate to 2-oxo-3-hydroxy-4-phosphobutanoate . PdxB is a nicotino-enzyme that contains a tightly bound NAD cofactor that must be re-oxidized after oxidation of erythronate 4-phosphate. The three α-keto acids α-ketoglutarate, oxaloacetate and pyruvate can serve as cosubstrates . pdxB is essential for growth in minimal medium . pdxB mutants show pyridoxine auxotrophy . Multicopy suppressors of the PLP auxotrophy of a pdxB deletion strain have been isolated and may be part of a serendipitous metabolic pathway that produces an intermediate of the PYRIDOXSYN-PWY pathway, 2-oxo-3-hydroxy-4-phosphobutanoate, that lies downstream of PdxB . An additional promiscuous enzyme activity that can bypass PdxB has been discovered . pdxB transcription is positively growth rate-regulated .

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.ERYTHRON4PDEHYDROG-RXN|reaction.ecocyc.ERYTHRON4PDEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P05459|protein.P05459]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-8212`
- `QSPROTEOME:QS00181841`

## Notes

2*protein.P05459
