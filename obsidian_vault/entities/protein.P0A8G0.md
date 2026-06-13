---
entity_id: "protein.P0A8G0"
entity_type: "protein"
name: "uvrC"
source_database: "UniProt"
source_id: "P0A8G0"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "uvrC b1913 JW1898"
---

# uvrC

`protein.P0A8G0`

## Static

- Type: `protein`
- Source: `UniProt:P0A8G0`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: The UvrABC repair system catalyzes the recognition and processing of DNA lesions. UvrC both incises the 5' and 3' sides of the lesion. The N-terminal half is responsible for the 3' incision and the C-terminal half is responsible for the 5' incision. {ECO:0000269|PubMed:10671556, ECO:0000269|PubMed:1387639}.

## Biological Role

Component of excision nuclease UvrABC (complex.ecocyc.UVRABC-CPLX).

## Enriched Pathways

- `eco03420` Nucleotide excision repair (KEGG)

## Annotation

FUNCTION: The UvrABC repair system catalyzes the recognition and processing of DNA lesions. UvrC both incises the 5' and 3' sides of the lesion. The N-terminal half is responsible for the 3' incision and the C-terminal half is responsible for the 5' incision. {ECO:0000269|PubMed:10671556, ECO:0000269|PubMed:1387639}.

## Pathways

- `eco03420` Nucleotide excision repair (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.UVRABC-CPLX|complex.ecocyc.UVRABC-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1913|gene.b1913]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A8G0`
- `KEGG:ecj:JW1898;eco:b1913;ecoc:C3026_10855;`
- `GeneID:93776218;947203;`
- `GO:GO:0003677; GO:0005737; GO:0006289; GO:0006974; GO:0009314; GO:0009380; GO:0009381; GO:0009432`

## Notes

UvrABC system protein C (Protein UvrC) (Excinuclease ABC subunit C)
