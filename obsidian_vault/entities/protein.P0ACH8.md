---
entity_id: "protein.P0ACH8"
entity_type: "protein"
name: "melR"
source_database: "UniProt"
source_id: "P0ACH8"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "melR b4118 JW4079"
---

# melR

`protein.P0ACH8`

## Static

- Type: `protein`
- Source: `UniProt:P0ACH8`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Transcription activator for the expression of the melAB operon. MelR binds at two sites located upstream of the melAB transcription site. {ECO:0000269|PubMed:2684786}.

## Biological Role

Component of DNA-binding transcriptional activator MelR-melibiose (complex.ecocyc.MONOMER0-161).

## Annotation

FUNCTION: Transcription activator for the expression of the melAB operon. MelR binds at two sites located upstream of the melAB transcription site. {ECO:0000269|PubMed:2684786}.

## Outgoing Edges (7)

- `activates` --> [[gene.b4118|gene.b4118]] `RegulonDB` `C` - regulator=MelR; target=melR; function=-+
- `activates` --> [[gene.b4119|gene.b4119]] `RegulonDB` `S` - regulator=MelR; target=melA; function=-+
- `activates` --> [[gene.b4120|gene.b4120]] `RegulonDB` `S` - regulator=MelR; target=melB; function=-+
- `is_component_of` --> [[complex.ecocyc.MONOMER0-161|complex.ecocyc.MONOMER0-161]] `EcoCyc` `database` - EcoCyc component coefficient=
- `represses` --> [[gene.b4118|gene.b4118]] `RegulonDB` `C` - regulator=MelR; target=melR; function=-+
- `represses` --> [[gene.b4119|gene.b4119]] `RegulonDB` `S` - regulator=MelR; target=melA; function=-+
- `represses` --> [[gene.b4120|gene.b4120]] `RegulonDB` `S` - regulator=MelR; target=melB; function=-+

## Incoming Edges (1)

- `encodes` <-- [[gene.b4118|gene.b4118]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ACH8`
- `KEGG:ecj:JW4079;eco:b4118;ecoc:C3026_22250;`
- `GeneID:75169636;75204000;948637;`
- `GO:GO:0000976; GO:0003677; GO:0003700; GO:0006355`

## Notes

Melibiose operon regulatory protein
