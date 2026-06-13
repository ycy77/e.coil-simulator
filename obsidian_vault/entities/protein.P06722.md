---
entity_id: "protein.P06722"
entity_type: "protein"
name: "mutH"
source_database: "UniProt"
source_id: "P06722"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mutH mutR prv b2831 JW2799"
---

# mutH

`protein.P06722`

## Static

- Type: `protein`
- Source: `UniProt:P06722`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Sequence-specific endonuclease that cleaves unmethylated GATC sequences. It is involved in DNA mismatch repair.

## Biological Role

Component of methyl-directed mismatch repair system (complex.ecocyc.MUTHLS-CPLX).

## Enriched Pathways

- `eco03430` Mismatch repair (KEGG)

## Annotation

FUNCTION: Sequence-specific endonuclease that cleaves unmethylated GATC sequences. It is involved in DNA mismatch repair.

## Pathways

- `eco03430` Mismatch repair (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.MUTHLS-CPLX|complex.ecocyc.MUTHLS-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2831|gene.b2831]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P06722`
- `KEGG:ecj:JW2799;eco:b2831;ecoc:C3026_15550;`
- `GeneID:947299;`
- `GO:GO:0000018; GO:0003677; GO:0004519; GO:0005737; GO:0006298; GO:0006304; GO:0016787; GO:0032300; GO:0043765`

## Notes

DNA mismatch repair protein MutH (Methyl-directed mismatch repair protein)
