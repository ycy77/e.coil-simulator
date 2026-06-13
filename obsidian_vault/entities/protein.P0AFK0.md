---
entity_id: "protein.P0AFK0"
entity_type: "protein"
name: "pmbA"
source_database: "UniProt"
source_id: "P0AFK0"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pmbA tldE b4235 JW4194"
---

# pmbA

`protein.P0AFK0`

## Static

- Type: `protein`
- Source: `UniProt:P0AFK0`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Metalloprotease involved in CcdA degradation. Suppresses the inhibitory activity of the carbon storage regulator (CsrA). {ECO:0000269|PubMed:12029038}. TldD and TldE form a stable heterodimeric complex with protease activity . tldE mutants harboring the pMccB17 plasmid show impaired production of Microcin B17 ; a deletion mutant accumulates the unprocessed Microcin B17 precursor protein, in contrast to wild type, which processes and exports Microcin B17 from the cell . A tldE mutant exhibits resistance to the F plasmid-encoded LetD DNA gyrase inhibitor , but only in the presence of the LetD inhibitor LetA . A csrA mutation suppresses the Tld phenotype of a tldE mutant . PmbA: "production of Microcin B17, locus A" TldE: "tolerant for letD expression E" Reviews:

## Biological Role

Component of metalloprotease TldDE (complex.ecocyc.CPLX0-8539).

## Annotation

FUNCTION: Metalloprotease involved in CcdA degradation. Suppresses the inhibitory activity of the carbon storage regulator (CsrA). {ECO:0000269|PubMed:12029038}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8539|complex.ecocyc.CPLX0-8539]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b4235|gene.b4235]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AFK0`
- `KEGG:ecj:JW4194;eco:b4235;ecoc:C3026_22860;`
- `GeneID:75169756;75203543;948750;`
- `GO:GO:0005737; GO:0005829; GO:0008237; GO:0016485; GO:1905368`
- `EC:3.4.-.-`

## Notes

Metalloprotease PmbA (EC 3.4.-.-) (Protein TldE)
