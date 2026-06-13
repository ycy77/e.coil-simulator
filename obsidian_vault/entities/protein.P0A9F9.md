---
entity_id: "protein.P0A9F9"
entity_type: "protein"
name: "metR"
source_database: "UniProt"
source_id: "P0A9F9"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "metR b3828 JW3804"
---

# metR

`protein.P0A9F9`

## Static

- Type: `protein`
- Source: `UniProt:P0A9F9`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Control of the last step in methionine biosynthesis; MetR is a positive activator of the metA, metE and metH genes. MetR is also a negative regulator of its own expression. Binds homocysteine as an inducer.

## Biological Role

Component of DNA-binding transcriptional dual regulator MetR (complex.ecocyc.CPLX0-7759).

## Annotation

FUNCTION: Control of the last step in methionine biosynthesis; MetR is a positive activator of the metA, metE and metH genes. MetR is also a negative regulator of its own expression. Binds homocysteine as an inducer.

## Outgoing Edges (6)

- `activates` --> [[gene.b2551|gene.b2551]] `RegulonDB` `C` - regulator=MetR; target=glyA; function=-+
- `activates` --> [[gene.b2552|gene.b2552]] `RegulonDB` `C` - regulator=MetR; target=hmp; function=+
- `activates` --> [[gene.b3829|gene.b3829]] `RegulonDB` `S` - regulator=MetR; target=metE; function=+
- `is_component_of` --> [[complex.ecocyc.CPLX0-7759|complex.ecocyc.CPLX0-7759]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `represses` --> [[gene.b2551|gene.b2551]] `RegulonDB` `C` - regulator=MetR; target=glyA; function=-+
- `represses` --> [[gene.b3828|gene.b3828]] `RegulonDB` `S` - regulator=MetR; target=metR; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b3828|gene.b3828]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A9F9`
- `KEGG:ecj:JW3804;eco:b3828;ecoc:C3026_20715;`
- `GeneID:948310;`
- `GO:GO:0000976; GO:0003677; GO:0003700; GO:0005737; GO:0006355; GO:0009086; GO:0016597`

## Notes

HTH-type transcriptional regulator MetR
