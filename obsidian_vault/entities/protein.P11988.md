---
entity_id: "protein.P11988"
entity_type: "protein"
name: "bglB"
source_database: "UniProt"
source_id: "P11988"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "bglB b3721 JW3699"
---

# bglB

`protein.P11988`

## Static

- Type: `protein`
- Source: `UniProt:P11988`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the hydrolysis of phosphorylated beta-glucosides into glucose-6-phosphate (G-6-P) and aglycone. It has a high affinity for phosphorylated aromatic beta-glucosides (p-nitrophenyl-beta-glucoside, phenyl beta-glucoside, arbutin and phosphorylated salicin), and a low affinity for phosphorylated beta-methyl-glucoside. {ECO:0000269|PubMed:4576407}. BglB is a phospho-β-glucosidase encoded within the cryptic bgl operon .

## Biological Role

Catalyzes 6-phospho-beta-D-glucosyl-(1->4)-D-glucose 6-phosphoglucohydrolase (reaction.R00839), 6-PHOSPHO-BETA-GLUCOSIDASE-RXN (reaction.ecocyc.6-PHOSPHO-BETA-GLUCOSIDASE-RXN), RXN0-5295 (reaction.ecocyc.RXN0-5295), RXN0-5297 (reaction.ecocyc.RXN0-5297).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00500` Starch and sucrose metabolism (KEGG)

## Annotation

FUNCTION: Catalyzes the hydrolysis of phosphorylated beta-glucosides into glucose-6-phosphate (G-6-P) and aglycone. It has a high affinity for phosphorylated aromatic beta-glucosides (p-nitrophenyl-beta-glucoside, phenyl beta-glucoside, arbutin and phosphorylated salicin), and a low affinity for phosphorylated beta-methyl-glucoside. {ECO:0000269|PubMed:4576407}.

## Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00500` Starch and sucrose metabolism (KEGG)

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.R00839|reaction.R00839]] `KEGG` `database` - via EC:3.2.1.86
- `catalyzes` --> [[reaction.ecocyc.6-PHOSPHO-BETA-GLUCOSIDASE-RXN|reaction.ecocyc.6-PHOSPHO-BETA-GLUCOSIDASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-5295|reaction.ecocyc.RXN0-5295]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-5297|reaction.ecocyc.RXN0-5297]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3721|gene.b3721]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P11988`
- `KEGG:ecj:JW3699;eco:b3721;ecoc:C3026_20170;`
- `GeneID:948234;`
- `GO:GO:0004553; GO:0005829; GO:0008422; GO:0008706; GO:0016052`
- `EC:3.2.1.86`

## Notes

6-phospho-beta-glucosidase BglB (EC 3.2.1.86) (Phospho-beta-glucosidase B)
