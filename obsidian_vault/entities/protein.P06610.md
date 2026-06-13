---
entity_id: "protein.P06610"
entity_type: "protein"
name: "btuE"
source_database: "UniProt"
source_id: "P06610"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000305|PubMed:3528129}. Note=Appears to have a periplasmic location. It has the mean hydropathy of a soluble protein but lacks an obvious signal sequence. {ECO:0000305|PubMed:3528129}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "btuE b1710 JW1700"
---

# btuE

`protein.P06610`

## Static

- Type: `protein`
- Source: `UniProt:P06610`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000305|PubMed:3528129}. Note=Appears to have a periplasmic location. It has the mean hydropathy of a soluble protein but lacks an obvious signal sequence. {ECO:0000305|PubMed:3528129}.

## Enriched Summary

FUNCTION: Non-specific peroxidase that can use thioredoxin or glutathione as a reducing agent. In vitro, utilizes preferentially thioredoxin A to decompose hydrogen peroxide as well as cumene-, tert-butyl-, and linoleic acid hydroperoxides, suggesting that it may have one or more organic hydroperoxide as its physiological substrate. {ECO:0000269|PubMed:20621065}. BtuE is a relatively non-specific peroxidase that is able to utilize both thioredoxins as well as glutathione. Using thioredoxin as a reducing agent, the enzyme is able to decompose a variety of organic hydroperoxides . BtuE is encoded as part of the btuCED operon, which also encodes proteins that are part of a vitamin B12 transport system . Transposon insertions in the btuC and btuD regions conferred a deficiency in vitamin B12 utilization and transport . However, there are indications that BtuE (residing within the operon) is not required for transport. Transposon insertions in btuE were not complemented by plasmids carrying btuE alone, whereas insertions in btuC and btuD were effectively complemented by plasmids carrying the corresponding functional gene . btuE mutants were also shown to have little effect on vitamin B12 binding and transport and did not affect the utilization of vitamin B12 or other cobalamins for methionine biosynthesis...

## Biological Role

Catalyzes glutathione:hydrogen-peroxide oxidoreductase (reaction.R00274), GLUTATHIONE-PEROXIDASE-RXN (reaction.ecocyc.GLUTATHIONE-PEROXIDASE-RXN), RXN0-267 (reaction.ecocyc.RXN0-267).

## Enriched Pathways

- `eco00480` Glutathione metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Non-specific peroxidase that can use thioredoxin or glutathione as a reducing agent. In vitro, utilizes preferentially thioredoxin A to decompose hydrogen peroxide as well as cumene-, tert-butyl-, and linoleic acid hydroperoxides, suggesting that it may have one or more organic hydroperoxide as its physiological substrate. {ECO:0000269|PubMed:20621065}.

## Pathways

- `eco00480` Glutathione metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R00274|reaction.R00274]] `KEGG` `database` - via EC:1.11.1.9
- `catalyzes` --> [[reaction.ecocyc.GLUTATHIONE-PEROXIDASE-RXN|reaction.ecocyc.GLUTATHIONE-PEROXIDASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-267|reaction.ecocyc.RXN0-267]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1710|gene.b1710]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P06610`
- `KEGG:ecj:JW1700;eco:b1710;ecoc:C3026_09790;`
- `GeneID:945915;`
- `GO:GO:0000302; GO:0004602; GO:0008379; GO:0033194; GO:0034599; GO:0042597`
- `EC:1.11.1.24; 1.11.1.9`

## Notes

Thioredoxin/glutathione peroxidase BtuE (EC 1.11.1.24) (EC 1.11.1.9)
