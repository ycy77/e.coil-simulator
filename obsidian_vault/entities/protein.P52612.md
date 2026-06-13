---
entity_id: "protein.P52612"
entity_type: "protein"
name: "fliI"
source_database: "UniProt"
source_id: "P52612"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fliI fla AIII flaC b1941 JW1925"
---

# fliI

`protein.P52612`

## Static

- Type: `protein`
- Source: `UniProt:P52612`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Probable catalytic subunit of a protein translocase for flagellum-specific export, or a proton translocase involved in local circuits at the flagellum. May be involved in a specialized protein export pathway that proceeds without signal peptide cleavage. FliI is a cytoplasmic component of the flagellar export apparatus and serves as the ATPase of the apparatus, providing the energy for translocation of export substrates across the cytoplasmic membrane . The structure of FliI missing the N-terminal 18 amino acids was determined by X-ray crystallography to a resolution of 2.4 Å .

## Biological Role

Component of flagellar export assembly apparatus (complex.ecocyc.CPLX0-7451).

## Enriched Pathways

- `eco02040` Flagellar assembly (KEGG)

## Annotation

FUNCTION: Probable catalytic subunit of a protein translocase for flagellum-specific export, or a proton translocase involved in local circuits at the flagellum. May be involved in a specialized protein export pathway that proceeds without signal peptide cleavage.

## Pathways

- `eco02040` Flagellar assembly (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7451|complex.ecocyc.CPLX0-7451]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=6

## Incoming Edges (1)

- `encodes` <-- [[gene.b1941|gene.b1941]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P52612`
- `KEGG:ecj:JW1925;eco:b1941;ecoc:C3026_10995;`
- `GeneID:93775244;946457;`
- `GO:GO:0005524; GO:0005737; GO:0006935; GO:0009288; GO:0015986; GO:0016887; GO:0030254; GO:0030257; GO:0042802; GO:0044780; GO:0045259; GO:0071973; GO:0120102; GO:1902600`
- `EC:7.1.2.2`

## Notes

Flagellum-specific ATP synthase (EC 7.1.2.2)
