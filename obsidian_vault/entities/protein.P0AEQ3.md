---
entity_id: "protein.P0AEQ3"
entity_type: "protein"
name: "glnH"
source_database: "UniProt"
source_id: "P0AEQ3"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000305|PubMed:3027504}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "glnH b0811 JW0796"
---

# glnH

`protein.P0AEQ3`

## Static

- Type: `protein`
- Source: `UniProt:P0AEQ3`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000305|PubMed:3027504}.

## Enriched Summary

FUNCTION: Involved in a glutamine-transport system GlnHPQ. {ECO:0000269|PubMed:3027504}. GlnH is the periplasmic binding protein of an L-glutamine ABC transport system. Early studies reported the purification of a glutamine binding protein released by cold osmotic shock treatment of whole cells of E. coli K12 and K10 derived strains . glnH encodes a periplasmic L-glutamine binding protein that is required for growth on L-glutamine as sole carbon source . Purified GlnH binds L-glutamine with µM affinity (KD = 5 x 10-7M) ; L-glutamine binding induces conformational change in the protein . Purifed, crystallized GlnH consists of two globular domains connected by two peptide linkers (hinges); glutamine binds in a cleft between the two domains; binding induces large scale movement of the two hinges and the ligand is completely buried within the protein

## Biological Role

Component of L-glutamine ABC transporter (complex.ecocyc.ABC-12-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Involved in a glutamine-transport system GlnHPQ. {ECO:0000269|PubMed:3027504}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-12-CPLX|complex.ecocyc.ABC-12-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b0811|gene.b0811]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AEQ3`
- `KEGG:ecj:JW0796;eco:b0811;ecoc:C3026_05105;`
- `GeneID:93776617;944872;`
- `GO:GO:0006868; GO:0015276; GO:0016020; GO:0016597; GO:0030288; GO:0055052; GO:0070406; GO:1903803`

## Notes

Glutamine-binding periplasmic protein (GlnBP)
