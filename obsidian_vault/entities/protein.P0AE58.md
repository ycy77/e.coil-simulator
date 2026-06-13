---
entity_id: "protein.P0AE58"
entity_type: "protein"
name: "caiF"
source_database: "UniProt"
source_id: "P0AE58"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "caiF b0034 JW0033"
---

# caiF

`protein.P0AE58`

## Static

- Type: `protein`
- Source: `UniProt:P0AE58`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Potential transcriptional activator of carnitine metabolism.

## Biological Role

Component of DNA-binding transcriptional activator CaiF (complex.ecocyc.CPLX0-7666).

## Annotation

FUNCTION: Potential transcriptional activator of carnitine metabolism.

## Outgoing Edges (11)

- `activates` --> [[gene.b0035|gene.b0035]] `RegulonDB` `S` - regulator=CaiF; target=caiE; function=+
- `activates` --> [[gene.b0036|gene.b0036]] `RegulonDB` `S` - regulator=CaiF; target=caiD; function=+
- `activates` --> [[gene.b0037|gene.b0037]] `RegulonDB` `S` - regulator=CaiF; target=caiC; function=+
- `activates` --> [[gene.b0038|gene.b0038]] `RegulonDB` `S` - regulator=CaiF; target=caiB; function=+
- `activates` --> [[gene.b0039|gene.b0039]] `RegulonDB` `S` - regulator=CaiF; target=caiA; function=+
- `activates` --> [[gene.b0040|gene.b0040]] `RegulonDB` `S` - regulator=CaiF; target=caiT; function=+
- `activates` --> [[gene.b0041|gene.b0041]] `RegulonDB` `S` - regulator=CaiF; target=fixA; function=+
- `activates` --> [[gene.b0042|gene.b0042]] `RegulonDB` `S` - regulator=CaiF; target=fixB; function=+
- `activates` --> [[gene.b0043|gene.b0043]] `RegulonDB` `S` - regulator=CaiF; target=fixC; function=+
- `activates` --> [[gene.b0044|gene.b0044]] `RegulonDB` `S` - regulator=CaiF; target=fixX; function=+
- `is_component_of` --> [[complex.ecocyc.CPLX0-7666|complex.ecocyc.CPLX0-7666]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0034|gene.b0034]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AE58`
- `KEGG:ecj:JW0033;eco:b0034;ecoc:C3026_00180;`
- `GeneID:944795;`
- `GO:GO:0003700; GO:0006351; GO:0006355; GO:0009437`

## Notes

Transcriptional activatory protein CaiF
