---
entity_id: "protein.P0A9G2"
entity_type: "protein"
name: "nhaR"
source_database: "UniProt"
source_id: "P0A9G2"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nhaR antO b0020 JW0019"
---

# nhaR

`protein.P0A9G2`

## Static

- Type: `protein`
- Source: `UniProt:P0A9G2`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Plays a role in the positive regulation of NhaA. {ECO:0000269|PubMed:1316901}.

## Biological Role

Component of NhaR-Na+ DNA-binding transcriptional activator (complex.ecocyc.MONOMER0-46).

## Annotation

FUNCTION: Plays a role in the positive regulation of NhaA. {ECO:0000269|PubMed:1316901}.

## Outgoing Edges (10)

- `activates` --> [[gene.b0019|gene.b0019]] `RegulonDB` `S` - regulator=NhaR; target=nhaA; function=+
- `activates` --> [[gene.b0020|gene.b0020]] `RegulonDB` `S` - regulator=NhaR; target=nhaR; function=+
- `activates` --> [[gene.b1021|gene.b1021]] `RegulonDB` `S` - regulator=NhaR; target=pgaD; function=+
- `activates` --> [[gene.b1022|gene.b1022]] `RegulonDB` `S` - regulator=NhaR; target=pgaC; function=+
- `activates` --> [[gene.b1023|gene.b1023]] `RegulonDB` `S` - regulator=NhaR; target=pgaB; function=+
- `activates` --> [[gene.b1024|gene.b1024]] `RegulonDB` `S` - regulator=NhaR; target=pgaA; function=+
- `activates` --> [[gene.b1482|gene.b1482]] `RegulonDB` `S` - regulator=NhaR; target=osmC; function=+
- `is_component_of` --> [[complex.ecocyc.MONOMER0-46|complex.ecocyc.MONOMER0-46]] `EcoCyc` `database` - EcoCyc component coefficient=
- `represses` --> [[gene.b0953|gene.b0953]] `RegulonDB` `S` - regulator=NhaR; target=rmf; function=-
- `represses` --> [[gene.b3995|gene.b3995]] `RegulonDB` `S` - regulator=NhaR; target=rsd; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b0020|gene.b0020]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A9G2`
- `KEGG:ecj:JW0019;eco:b0020;`
- `GeneID:944757;`
- `GO:GO:0001216; GO:0003677; GO:0003700; GO:0005737; GO:2000142; GO:2000144`

## Notes

Transcriptional activator protein NhaR (Na(+)/H(+) antiporter regulatory protein)
