---
entity_id: "protein.P09377"
entity_type: "protein"
name: "rhaS"
source_database: "UniProt"
source_id: "P09377"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_01534}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rhaS rhaC2 b3905 JW3876"
---

# rhaS

`protein.P09377`

## Static

- Type: `protein`
- Source: `UniProt:P09377`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_01534}.

## Enriched Summary

FUNCTION: Activates expression of the rhaBAD and rhaT operons. {ECO:0000255|HAMAP-Rule:MF_01534, ECO:0000269|PubMed:8230210, ECO:0000269|PubMed:8757746}.

## Biological Role

Component of transcriptional activator RhaS (complex.ecocyc.PC00086).

## Annotation

FUNCTION: Activates expression of the rhaBAD and rhaT operons. {ECO:0000255|HAMAP-Rule:MF_01534, ECO:0000269|PubMed:8230210, ECO:0000269|PubMed:8757746}.

## Outgoing Edges (7)

- `activates` --> [[gene.b3902|gene.b3902]] `RegulonDB` `C` - regulator=RhaS; target=rhaD; function=+
- `activates` --> [[gene.b3903|gene.b3903]] `RegulonDB` `C` - regulator=RhaS; target=rhaA; function=+
- `activates` --> [[gene.b3904|gene.b3904]] `RegulonDB` `C` - regulator=RhaS; target=rhaB; function=+
- `activates` --> [[gene.b3905|gene.b3905]] `RegulonDB` `S` - regulator=RhaS; target=rhaS; function=+
- `activates` --> [[gene.b3906|gene.b3906]] `RegulonDB` `S` - regulator=RhaS; target=rhaR; function=+
- `activates` --> [[gene.b3907|gene.b3907]] `RegulonDB` `S` - regulator=RhaS; target=rhaT; function=+
- `is_component_of` --> [[complex.ecocyc.PC00086|complex.ecocyc.PC00086]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3905|gene.b3905]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P09377`
- `KEGG:ecj:JW3876;eco:b3905;ecoc:C3026_21115;`
- `GeneID:75204579;948397;`
- `GO:GO:0000976; GO:0003700; GO:0005737; GO:0006355; GO:0045893`

## Notes

HTH-type transcriptional activator RhaS (L-rhamnose operon regulatory protein RhaS)
