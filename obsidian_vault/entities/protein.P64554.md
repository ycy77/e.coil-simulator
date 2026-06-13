---
entity_id: "protein.P64554"
entity_type: "protein"
name: "queE"
source_database: "UniProt"
source_id: "P64554"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "queE ygcF b2777 JW2748"
---

# queE

`protein.P64554`

## Static

- Type: `protein`
- Source: `UniProt:P64554`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the complex heterocyclic radical-mediated conversion of 6-carboxy-5,6,7,8-tetrahydropterin (CPH4) to 7-carboxy-7-deazaguanine (CDG), a step common to the biosynthetic pathways of all 7-deazapurine-containing compounds. {ECO:0000255|HAMAP-Rule:MF_00917}. The QueE ortholog of Bacillus subtilis catalyzes the 7-carboxy-7-deazaguanine synthase reaction of the PWY-6703 pathway . Deletion of queE results in absence of queuosine and epoxyqueuosine from cellular RNA . A transposon insertion mutant or in-frame deletion of queE suppresses the filamentation phenotype due to a strongly stimulated PhoQ/PhoP two-comPonent system , and overexpression of queE leads to cell filamentation . Transcription of queE is regulated by PhoP . QueE is cytoplasmic, but also shows specific localization to the Z ring in filamentous cells .

## Biological Role

Catalyzes RXN0-6575 (reaction.ecocyc.RXN0-6575). Bound by a [4Fe-4S] iron-sulfur cluster (molecule.ecocyc.CPD-7).

## Enriched Pathways

- `eco00790` Folate biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes the complex heterocyclic radical-mediated conversion of 6-carboxy-5,6,7,8-tetrahydropterin (CPH4) to 7-carboxy-7-deazaguanine (CDG), a step common to the biosynthetic pathways of all 7-deazapurine-containing compounds. {ECO:0000255|HAMAP-Rule:MF_00917}.

## Pathways

- `eco00790` Folate biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-6575|reaction.ecocyc.RXN0-6575]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.ecocyc.CPD-7|molecule.ecocyc.CPD-7]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b2777|gene.b2777]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P64554`
- `KEGG:ecj:JW2748;eco:b2777;ecoc:C3026_15250;`
- `GeneID:89517576;947527;`
- `GO:GO:0000287; GO:0005829; GO:0008616; GO:0016840; GO:0032153; GO:0032466; GO:0051539; GO:1904047`
- `EC:4.3.99.3`

## Notes

7-carboxy-7-deazaguanine synthase (CDG synthase) (EC 4.3.99.3) (Queuosine biosynthesis protein QueE)
