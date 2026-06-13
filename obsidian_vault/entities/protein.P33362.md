---
entity_id: "protein.P33362"
entity_type: "protein"
name: "yehZ"
source_database: "UniProt"
source_id: "P33362"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yehZ osmF b2131 JW2119"
---

# yehZ

`protein.P33362`

## Static

- Type: `protein`
- Source: `UniProt:P33362`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Part of an ABC transporter complex involved in low-affinity glycine betaine uptake. Binds glycine betaine with low affinity. {ECO:0000269|PubMed:26325238}. OsmF is the periplasmic binding component of a low affinity glycine betaine ABC transporter; OsmF binds the osmoprotectants glycine betaine, choline-0-sulfate and dimethylsulfopropionate with low (mM) affinities . apoYehZ contains a type II periplasmic binding fold consisting of two domains (A and B) with two connecting loops . Expression of an osmF-phoA fusion is induced by growth in a medium of high osmolarity . An osmFlacZ transcriptional fusion is induced by both osmotic shock and entry into stationary phase .

## Biological Role

Component of glycine betaine ABC transporter, non-osmoregulatory (complex.ecocyc.ABC-40-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of an ABC transporter complex involved in low-affinity glycine betaine uptake. Binds glycine betaine with low affinity. {ECO:0000269|PubMed:26325238}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-40-CPLX|complex.ecocyc.ABC-40-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2131|gene.b2131]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P33362`
- `KEGG:ecj:JW2119;eco:b2131;ecoc:C3026_11950;`
- `GeneID:946681;`
- `GO:GO:0006865; GO:0015838; GO:0016020; GO:0022857; GO:0031460; GO:0042597; GO:0055052; GO:0071474`

## Notes

Glycine betaine-binding protein YehZ
