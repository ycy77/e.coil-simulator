---
entity_id: "protein.P27111"
entity_type: "protein"
name: "cynR"
source_database: "UniProt"
source_id: "P27111"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "cynR b0338 JW5894"
---

# cynR

`protein.P27111`

## Static

- Type: `protein`
- Source: `UniProt:P27111`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Positively regulates the cynTSX operon, and negatively regulates its own transcription. Binds specifically to the cynR-cynTSX intergenic region. {ECO:0000269|PubMed:1592818}.

## Biological Role

Component of CynR-cyanate DNA-binding transcriptional dual regulator (complex.ecocyc.MONOMER0-164).

## Annotation

FUNCTION: Positively regulates the cynTSX operon, and negatively regulates its own transcription. Binds specifically to the cynR-cynTSX intergenic region. {ECO:0000269|PubMed:1592818}.

## Outgoing Edges (5)

- `activates` --> [[gene.b0339|gene.b0339]] `RegulonDB` `S` - regulator=CynR; target=cynT; function=+
- `activates` --> [[gene.b0340|gene.b0340]] `RegulonDB` `S` - regulator=CynR; target=cynS; function=+
- `activates` --> [[gene.b0341|gene.b0341]] `RegulonDB` `S` - regulator=CynR; target=cynX; function=+
- `is_component_of` --> [[complex.ecocyc.MONOMER0-164|complex.ecocyc.MONOMER0-164]] `EcoCyc` `database` - EcoCyc component coefficient=
- `represses` --> [[gene.b0338|gene.b0338]] `RegulonDB` `S` - regulator=CynR; target=cynR; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b0338|gene.b0338]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P27111`
- `KEGG:ecj:JW5894;eco:b0338;ecoc:C3026_01655;ecoc:C3026_24825;`
- `GeneID:945001;`
- `GO:GO:0003677; GO:0003700; GO:0005737; GO:0006355; GO:0032993`

## Notes

HTH-type transcriptional regulator CynR (Cyn operon transcriptional activator)
