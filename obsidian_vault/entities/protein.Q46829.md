---
entity_id: "protein.Q46829"
entity_type: "protein"
name: "bglA"
source_database: "UniProt"
source_id: "Q46829"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "bglA bglD yqfC b2901 JW2869"
---

# bglA

`protein.Q46829`

## Static

- Type: `protein`
- Source: `UniProt:Q46829`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the hydrolysis of phosphorylated beta-glucosides into glucose-6-phosphate (G-6-P) and aglycone. It has a high affinity for phosphorylated aromatic beta-glucosides (p-nitrophenyl-beta-glucoside, phenyl beta-glucoside, arbutin), with the exception of phosphorylated salicin, and a low affinity for phosphorylated beta-methyl-glucoside. Apparently, it has only a very limited role in the utilization of external beta-glucosides. {ECO:0000269|PubMed:4576407}. BglA is a 6-phospho-β-glucosidase with a high affinity for phosphorylated aromatic β-glucosides and a low affinity for phosphorylated β-methyl-glucoside . BglA is one of several 6-phospho-β-glucosidases in E. coli; transporters for these compounds are present, but appear to be not expressed. Because its potential phosphorylated substrates are not commercially available, the true substrate range of BglA is unknown. Mutants that are able to utilize β-methyl-glucoside as the source of carbon and energy have increased levels of 6-phospho-β-glucosidase . A crystal structure of BglA has been solved at 2.3 Å resolution. BglA likely forms a homomultimer and has an 8-strand alpha/beta TIM barrel structure .

## Biological Role

Catalyzes 6-phospho-beta-D-glucosyl-(1->4)-D-glucose 6-phosphoglucohydrolase (reaction.R00839), RXN0-5295 (reaction.ecocyc.RXN0-5295), RXN0-6994 (reaction.ecocyc.RXN0-6994).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00500` Starch and sucrose metabolism (KEGG)

## Annotation

FUNCTION: Catalyzes the hydrolysis of phosphorylated beta-glucosides into glucose-6-phosphate (G-6-P) and aglycone. It has a high affinity for phosphorylated aromatic beta-glucosides (p-nitrophenyl-beta-glucoside, phenyl beta-glucoside, arbutin), with the exception of phosphorylated salicin, and a low affinity for phosphorylated beta-methyl-glucoside. Apparently, it has only a very limited role in the utilization of external beta-glucosides. {ECO:0000269|PubMed:4576407}.

## Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00500` Starch and sucrose metabolism (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R00839|reaction.R00839]] `KEGG` `database` - via EC:3.2.1.86
- `catalyzes` --> [[reaction.ecocyc.RXN0-5295|reaction.ecocyc.RXN0-5295]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-6994|reaction.ecocyc.RXN0-6994]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2901|gene.b2901]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:Q46829`
- `KEGG:ecj:JW2869;eco:b2901;`
- `GeneID:947378;`
- `GO:GO:0005829; GO:0008422; GO:0008706; GO:0015926; GO:0016052`
- `EC:3.2.1.86`

## Notes

6-phospho-beta-glucosidase BglA (EC 3.2.1.86) (Phospho-beta-glucosidase A)
