---
entity_id: "protein.P0AB93"
entity_type: "protein"
name: "arsB"
source_database: "UniProt"
source_id: "P0AB93"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "arsB arsF b3502 JW3469"
---

# arsB

`protein.P0AB93`

## Static

- Type: `protein`
- Source: `UniProt:P0AB93`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: Involved in arsenical resistance. Thought to form the channel of an arsenite pump (By similarity). {ECO:0000250}. Based on sequence similarity with the R773-plasmid encoded arsenite resistance operon, ArsB is a transporter and ArsC is an arsenate reductase . The chromosomally encoded operon, however, lacks arsA, which encodes a putative ATP-binding protein . Transport through ArsB occurs through a metalloid:proton antiport mechanism . Expression of arsA from the R773 plasmid increases resistance to As(III) and Sb(III) showing ArsB can act alone in metalloid:proton antiport or as part of an ATP-dependent ABC transporter . Antimonite stimulates uptake of arsenite, but arsenite inhibits uptake of antimonite suggesting co-transport of the two compounds possibly as six-membered, co-polymer rings . Deletion mutants of the chromosomal arsRBC operon exhibit 10-20 times more sensitivity to arsenite and 5-10 times more sensitivity to antimonite and arsenate than the parental strain . Expression of the cloned arsRBC conferred increased arsenite, arsenate, and antimonite resistance compared with wild-type as well as when expressed in an arsRBC deletion strain . Accumulation of arsenite in cells increased upon deletion of arsRBC and then decreased upon expression of arsRBC from a plasmid . Expression of arsRBC is induced by antimonite , arsenate, and arsenite...

## Biological Role

Component of arsenite/antimonite:H+ antiporter (complex.ecocyc.CPLX-7).

## Annotation

FUNCTION: Involved in arsenical resistance. Thought to form the channel of an arsenite pump (By similarity). {ECO:0000250}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX-7|complex.ecocyc.CPLX-7]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3502|gene.b3502]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AB93`
- `KEGG:ecj:JW3469;eco:b3502;ecoc:C3026_18970;`
- `GeneID:93778490;948011;`
- `GO:GO:0005886; GO:0008490; GO:0015699; GO:0015700; GO:0042960; GO:0046685`

## Notes

Arsenical pump membrane protein (Arsenic efflux pump protein)
