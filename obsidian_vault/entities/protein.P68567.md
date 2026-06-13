---
entity_id: "protein.P68567"
entity_type: "protein"
name: "rsmJ"
source_database: "UniProt"
source_id: "P68567"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_01523}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rsmJ yhiQ b3497 JW5672"
---

# rsmJ

`protein.P68567`

## Static

- Type: `protein`
- Source: `UniProt:P68567`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_01523}.

## Enriched Summary

FUNCTION: Specifically methylates the guanosine in position 1516 of 16S rRNA. {ECO:0000255|HAMAP-Rule:MF_01523, ECO:0000269|PubMed:22079366}. RsmJ is the methyltransferase responsible for methylation of 16S rRNA at the N2 position of the G1516 nucleotide. In vitro, the enzyme can methylate 16S rRNA within the 30S ribosomal subunit, but not free 16S rRNA . prlC-rsmJ is a heat shock operon regulated by RpoH . An rsmJ mutant strain is cold sensitive, showing a growth defect at 16°C .

## Biological Role

Catalyzes RXN0-6731 (reaction.ecocyc.RXN0-6731).

## Annotation

FUNCTION: Specifically methylates the guanosine in position 1516 of 16S rRNA. {ECO:0000255|HAMAP-Rule:MF_01523, ECO:0000269|PubMed:22079366}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-6731|reaction.ecocyc.RXN0-6731]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3497|gene.b3497]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P68567`
- `KEGG:ecj:JW5672;eco:b3497;ecoc:C3026_18940;`
- `GeneID:948005;`
- `GO:GO:0005737; GO:0008990; GO:0031167; GO:0036308; GO:0070475`
- `EC:2.1.1.242`

## Notes

Ribosomal RNA small subunit methyltransferase J (EC 2.1.1.242) (16S rRNA m2G1516 methyltransferase) (rRNA (guanine-N(2)-)-methyltransferase)
