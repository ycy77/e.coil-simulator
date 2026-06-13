---
entity_id: "complex.ecocyc.CPLX0-7877"
entity_type: "complex"
name: "glucose-6-phosphate isomerase"
source_database: "EcoCyc"
source_id: "CPLX0-7877"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# glucose-6-phosphate isomerase

`complex.ecocyc.CPLX0-7877`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7877`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A6T1|protein.P0A6T1]]

## Enriched Summary

Phosphoglucose isomerase catalyzes the interconversion of glucose-6-phosphate and fructose-6-phosphate, an essential step of the glycolysis and gluconeogenesis pathways. The enzyme is dimeric in solution, but an additional higher molecular weight form that is less active and more negatively charged was found as well . The crystal structure of dimeric Pgi from E. coli K-12 has been solved at 2.05 Å resolution . A pgi mutant grows slowly on glucose and utilizes glucose primarily via the PENTOSE-P-PWY as the source of NADPH ; the ENTNER-DOUDOROFF-PWY is also used to a lesser degree . The glyoxylate shunt is also active in a pgi mutant strain . The increased flux through the pentose phosphate pathway leads to overproduction of NADPH and thus disturbs the redox balance , which may be restored by overexpressing SthA or a heterologous NADPH-utilizing pathway . Deletion of pgi is a common strategy for metabolic engineering of E. coli, e.g. . pgi mutant strains that were allowed to evolve for 600-800 generations have been characterized . When grown on maltose, pgi mutants accumulate maltodextrin and thus stain blue with iodine (the "maltose Blu phenotype") . pgi expression is induced by oxidative stress, and a pgi deletion mutant is hypersensitive to oxidative stress induced by paraquat...

## Biological Role

Catalyzes PGLUCISOM-RXN (reaction.ecocyc.PGLUCISOM-RXN).

## Annotation

Phosphoglucose isomerase catalyzes the interconversion of glucose-6-phosphate and fructose-6-phosphate, an essential step of the glycolysis and gluconeogenesis pathways. The enzyme is dimeric in solution, but an additional higher molecular weight form that is less active and more negatively charged was found as well . The crystal structure of dimeric Pgi from E. coli K-12 has been solved at 2.05 Å resolution . A pgi mutant grows slowly on glucose and utilizes glucose primarily via the PENTOSE-P-PWY as the source of NADPH ; the ENTNER-DOUDOROFF-PWY is also used to a lesser degree . The glyoxylate shunt is also active in a pgi mutant strain . The increased flux through the pentose phosphate pathway leads to overproduction of NADPH and thus disturbs the redox balance , which may be restored by overexpressing SthA or a heterologous NADPH-utilizing pathway . Deletion of pgi is a common strategy for metabolic engineering of E. coli, e.g. . pgi mutant strains that were allowed to evolve for 600-800 generations have been characterized . When grown on maltose, pgi mutants accumulate maltodextrin and thus stain blue with iodine (the "maltose Blu phenotype") . pgi expression is induced by oxidative stress, and a pgi deletion mutant is hypersensitive to oxidative stress induced by paraquat . pgi insertion mutants were identified in a genetic screen for genes that are important for survival of exposure to ionizing radiation (IR). A pgi deletion mutant has a moderate decrease in IR survival . Deletion of pgi can suppress the effects of a dnaB8(ts) mutation . In an E. coli MG1655 strain pgi was identified as a knockout target for increasing plasmid DNA production . The effect of perturbation (rather than knockout) of pgi gene expression on central carbon metabolism has been studied us

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.PGLUCISOM-RXN|reaction.ecocyc.PGLUCISOM-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0A6T1|protein.P0A6T1]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-7877`
- `QSPROTEOME:QS00157611`

## Notes

2*protein.P0A6T1
