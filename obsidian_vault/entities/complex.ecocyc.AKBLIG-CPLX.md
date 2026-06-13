---
entity_id: "complex.ecocyc.AKBLIG-CPLX"
entity_type: "complex"
name: "2-amino-3-ketobutyrate CoA ligase"
source_database: "EcoCyc"
source_id: "AKBLIG-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# 2-amino-3-ketobutyrate CoA ligase

`complex.ecocyc.AKBLIG-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:AKBLIG-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0AB77|protein.P0AB77]]

## Enriched Summary

2-Amino-3-ketobutyrate CoA ligase (Kbl, AKB ligase) catalyzes the reversible, coenzyme A-dependent cleavage/condensation reaction between 2-amino-3-oxobutanoate (2-amino-3-ketobutyrate) and glycine plus acetyl-CoA. It is the second reaction in the threonine dehydrogenase-initiated pathway by which threonine is converted to glycine which is then converted to serine. This pathway is the primary route for threonine utilization in prokaryotes and is an alternate pathway for serine biosynthesis in E. coli . Because 2-amino-3-oxobutanoate can spontaneously decarboxylate to aminoacetone, a second threonine dehydrogenase-initiated pathway is also possible (see THRDLCTCAT-PWY). The crystal structure of Kbl in complex with a pyridoxal-5'-phosphate-substrate intermediate has been determined at 2.0 Å resolution and a reaction mechanism was proposed. Kbl belongs to the α family of PLP-dependent enzymes. It was noted that this enzyme has been evolutionarily conserved and E. coli Kbl shares 54% amino acid sequence identity with the human enzyme . Details of the condensation mechanism have been studied . Review: Reitzer, L. (2005) "Catabolism of Amino Acids and Related Compounds" EcoSal 3.4...

## Biological Role

Catalyzes AKBLIG-RXN (reaction.ecocyc.AKBLIG-RXN). Bound by Pyridoxal phosphate (molecule.C00018).

## Annotation

2-Amino-3-ketobutyrate CoA ligase (Kbl, AKB ligase) catalyzes the reversible, coenzyme A-dependent cleavage/condensation reaction between 2-amino-3-oxobutanoate (2-amino-3-ketobutyrate) and glycine plus acetyl-CoA. It is the second reaction in the threonine dehydrogenase-initiated pathway by which threonine is converted to glycine which is then converted to serine. This pathway is the primary route for threonine utilization in prokaryotes and is an alternate pathway for serine biosynthesis in E. coli . Because 2-amino-3-oxobutanoate can spontaneously decarboxylate to aminoacetone, a second threonine dehydrogenase-initiated pathway is also possible (see THRDLCTCAT-PWY). The crystal structure of Kbl in complex with a pyridoxal-5'-phosphate-substrate intermediate has been determined at 2.0 Å resolution and a reaction mechanism was proposed. Kbl belongs to the α family of PLP-dependent enzymes. It was noted that this enzyme has been evolutionarily conserved and E. coli Kbl shares 54% amino acid sequence identity with the human enzyme . Details of the condensation mechanism have been studied . Review: Reitzer, L. (2005) "Catabolism of Amino Acids and Related Compounds" EcoSal 3.4.7

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.AKBLIG-RXN|reaction.ecocyc.AKBLIG-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00018|molecule.C00018]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0AB77|protein.P0AB77]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:AKBLIG-CPLX`
- `QSPROTEOME:QS00196207`

## Notes

2*protein.P0AB77
