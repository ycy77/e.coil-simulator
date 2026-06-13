---
entity_id: "protein.P0DMC5"
entity_type: "protein"
name: "rcsC"
source_database: "UniProt"
source_id: "P0DMC5"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_00979, ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:2404948}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_00979, ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:2404948}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rcsC b2218 JW5917/JW5920"
---

# rcsC

`protein.P0DMC5`

## Static

- Type: `protein`
- Source: `UniProt:P0DMC5`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_00979, ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:2404948}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_00979, ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:2404948}.

## Enriched Summary

FUNCTION: Component of the Rcs signaling system, which controls transcription of numerous genes. RcsC functions as a membrane-associated protein kinase that phosphorylates RcsD in response to environmental signals. The phosphoryl group is then transferred to the response regulator RcsB. RcsC also has phosphatase activity. The system controls expression of genes involved in colanic acid capsule synthesis, biofilm formation and cell division. {ECO:0000255|HAMAP-Rule:MF_00979, ECO:0000269|PubMed:10564486, ECO:0000269|PubMed:11309126, ECO:0000269|PubMed:11758943, ECO:0000269|PubMed:11807084, ECO:0000269|PubMed:13129944, ECO:0000269|PubMed:14651646}. Represents the His-479 phosphorylated form of RCSC-MONOMER RcsC - the histidine kinase of the Rcs signal transduction system. RcsC is the histidine kinase of the complex Rcs phosphorelay system; RcsC autophosphorylates and transfers a phosphate to the RcsD phosphotransfer protein; RcsC is not thought to act as a direct sensor rather its kinase activity is regulated by the inner membrane protein G7741-MONOMER "IgaA" in response to signals sensed by the outer membrane lipoprotein RCSF-MONOMER "RcsF"; RcsC may be a bifunctional histidine kinase/phosphatase (see )...

## Biological Role

Catalyzes 2.7.13.3-RXN (reaction.ecocyc.2.7.13.3-RXN).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

FUNCTION: Component of the Rcs signaling system, which controls transcription of numerous genes. RcsC functions as a membrane-associated protein kinase that phosphorylates RcsD in response to environmental signals. The phosphoryl group is then transferred to the response regulator RcsB. RcsC also has phosphatase activity. The system controls expression of genes involved in colanic acid capsule synthesis, biofilm formation and cell division. {ECO:0000255|HAMAP-Rule:MF_00979, ECO:0000269|PubMed:10564486, ECO:0000269|PubMed:11309126, ECO:0000269|PubMed:11758943, ECO:0000269|PubMed:11807084, ECO:0000269|PubMed:13129944, ECO:0000269|PubMed:14651646}.

## Pathways

- `eco02020` Two-component system (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.2.7.13.3-RXN|reaction.ecocyc.2.7.13.3-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2218|gene.b2218]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0DMC5`
- `KEGG:ecj:JW5917;ecj:JW5920;eco:b2218;ecoc:C3026_12400;`
- `GeneID:948993;`
- `GO:GO:0000155; GO:0000160; GO:0004673; GO:0004721; GO:0005524; GO:0005829; GO:0005886; GO:0006355; GO:0030288; GO:0044010; GO:0071470`
- `EC:2.7.13.3`

## Notes

Sensor histidine kinase RcsC (EC 2.7.13.3) (Capsular synthesis regulator component C)
