---
entity_id: "protein.P0A6I9"
entity_type: "protein"
name: "coaE"
source_database: "UniProt"
source_id: "P0A6I9"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00376, ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "coaE yacE b0103 JW0100"
---

# coaE

`protein.P0A6I9`

## Static

- Type: `protein`
- Source: `UniProt:P0A6I9`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00376, ECO:0000305}.

## Enriched Summary

FUNCTION: Catalyzes the phosphorylation of the 3'-hydroxyl group of dephosphocoenzyme A to form coenzyme A. {ECO:0000255|HAMAP-Rule:MF_00376, ECO:0000269|PubMed:11292795}. Dephospho-CoA kinase catalyzes the final step in coenzyme A biosynthesis . The enzyme appeared to be a monomer in solution ; subsequent analysis of the crystal structure, where it appears as a trimer, led to the discovery that the presence of sulfate ions stabilizes a trimeric state in solution as well. The biological role of the trimeric form is unclear . Crystal structures of the enzyme have been solved . coaE is essential for growth .

## Biological Role

Catalyzes ATP:dephospho-CoA 3'-phosphotransferase (reaction.R00130), DEPHOSPHOCOAKIN-RXN (reaction.ecocyc.DEPHOSPHOCOAKIN-RXN).

## Enriched Pathways

- `eco00770` Pantothenate and CoA biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Catalyzes the phosphorylation of the 3'-hydroxyl group of dephosphocoenzyme A to form coenzyme A. {ECO:0000255|HAMAP-Rule:MF_00376, ECO:0000269|PubMed:11292795}.

## Pathways

- `eco00770` Pantothenate and CoA biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00130|reaction.R00130]] `KEGG` `database` - via EC:2.7.1.24
- `catalyzes` --> [[reaction.ecocyc.DEPHOSPHOCOAKIN-RXN|reaction.ecocyc.DEPHOSPHOCOAKIN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0103|gene.b0103]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A6I9`
- `KEGG:ecj:JW0100;eco:b0103;ecoc:C3026_00420;`
- `GeneID:93777332;949060;`
- `GO:GO:0004140; GO:0005524; GO:0005737; GO:0015937`
- `EC:2.7.1.24`

## Notes

Dephospho-CoA kinase (EC 2.7.1.24) (Dephosphocoenzyme A kinase)
