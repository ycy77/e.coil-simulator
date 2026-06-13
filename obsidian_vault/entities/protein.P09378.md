---
entity_id: "protein.P09378"
entity_type: "protein"
name: "rhaR"
source_database: "UniProt"
source_id: "P09378"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_01533}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rhaR rhaC1 b3906 JW3877"
---

# rhaR

`protein.P09378`

## Static

- Type: `protein`
- Source: `UniProt:P09378`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_01533}.

## Enriched Summary

FUNCTION: Activates expression of the rhaSR operon in response to L-rhamnose. {ECO:0000255|HAMAP-Rule:MF_01533, ECO:0000269|PubMed:8230210, ECO:0000269|PubMed:8757746}.

## Biological Role

Component of RhaR-L-rhamnose DNA-binding transcriptional activator (complex.ecocyc.MONOMER-47).

## Annotation

FUNCTION: Activates expression of the rhaSR operon in response to L-rhamnose. {ECO:0000255|HAMAP-Rule:MF_01533, ECO:0000269|PubMed:8230210, ECO:0000269|PubMed:8757746}.

## Outgoing Edges (3)

- `activates` --> [[gene.b3905|gene.b3905]] `RegulonDB` `C` - regulator=RhaR; target=rhaS; function=+
- `activates` --> [[gene.b3906|gene.b3906]] `RegulonDB` `C` - regulator=RhaR; target=rhaR; function=+
- `is_component_of` --> [[complex.ecocyc.MONOMER-47|complex.ecocyc.MONOMER-47]] `EcoCyc` `database` - EcoCyc component coefficient=

## Incoming Edges (1)

- `encodes` <-- [[gene.b3906|gene.b3906]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P09378`
- `KEGG:ecj:JW3877;eco:b3906;ecoc:C3026_21120;`
- `GeneID:948396;`
- `GO:GO:0000976; GO:0003700; GO:0005737; GO:0006351; GO:0006355; GO:0043565; GO:0045893`

## Notes

HTH-type transcriptional activator RhaR (L-rhamnose operon transcriptional activator RhaR)
