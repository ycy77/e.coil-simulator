---
entity_id: "protein.P39359"
entity_type: "protein"
name: "yjhH"
source_database: "UniProt"
source_id: "P39359"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yjhH b4298 JW5775"
---

# yjhH

`protein.P39359`

## Static

- Type: `protein`
- Source: `UniProt:P39359`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Functions as a 2-dehydro-3-deoxy-D-pentonate aldolase. {ECO:0000305|PubMed:23233208}. YjhH appears to be a 2-dehydro-3-deoxy-D-pentonate aldolase . A yjhH yagE double mutant can not use D-xylonate as the sole source of carbon, and crude cell extracts do not contain 2-dehydro-3-deoxy-D-pentonate aldolase activity. Both phenotypes are complemented by providing yjhH on a plasmid . Overexpression of yjhH has been used for metabolic engineering of glycolate production . ArcA appears to activate yjhH gene expression under anaerobiosis. Two putative ArcA binding sites were identified 211 and 597 bp upstream of this gene , but no promoter upstream of it has been identified.

## Biological Role

Catalyzes 4.1.2.28-RXN (reaction.ecocyc.4.1.2.28-RXN).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Functions as a 2-dehydro-3-deoxy-D-pentonate aldolase. {ECO:0000305|PubMed:23233208}.

## Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.4.1.2.28-RXN|reaction.ecocyc.4.1.2.28-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b4298|gene.b4298]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P39359`
- `KEGG:ecj:JW5775;eco:b4298;`
- `GeneID:948825;`
- `GO:GO:0005829; GO:0046176; GO:0047440`
- `EC:4.1.2.28`

## Notes

Probable 2-dehydro-3-deoxy-D-pentonate aldolase YjhH (EC 4.1.2.28)
