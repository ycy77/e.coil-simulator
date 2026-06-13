---
entity_id: "protein.P13458"
entity_type: "protein"
name: "sbcC"
source_database: "UniProt"
source_id: "P13458"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "sbcC rmuA b0397 JW0387"
---

# sbcC

`protein.P13458`

## Static

- Type: `protein`
- Source: `UniProt:P13458`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: SbcCD cleaves DNA hairpin structures. These structures can inhibit DNA replication and are intermediates in certain DNA recombination reactions. The complex acts as a 3'->5' double strand exonuclease that can open hairpins. It also has a 5' single-strand endonuclease activity. An sbcC mutation (sbcC201) overcomes the inviability of long palindromic nucleotide sequences . sbcC and sbcD form an operon in E. coli K-12 . SbcC is a member of the SMC (structural maintenance of chromosomes) family and contains conserved ATP binding motifs at each terminus and an internal coiled-coil domain interrupted by a central spacer which contains a half zinc-finger motif .

## Biological Role

Component of ATP-dependent structure-specific DNA nuclease (complex.ecocyc.CPLX0-3957).

## Annotation

FUNCTION: SbcCD cleaves DNA hairpin structures. These structures can inhibit DNA replication and are intermediates in certain DNA recombination reactions. The complex acts as a 3'->5' double strand exonuclease that can open hairpins. It also has a 5' single-strand endonuclease activity.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3957|complex.ecocyc.CPLX0-3957]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0397|gene.b0397]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P13458`
- `KEGG:ecj:JW0387;eco:b0397;ecoc:C3026_01930;`
- `GeneID:949076;`
- `GO:GO:0000014; GO:0004529; GO:0005524; GO:0006260; GO:0006274; GO:0006281; GO:0006302; GO:0006310; GO:0008296; GO:0016887; GO:1990238; GO:1990391`

## Notes

Nuclease SbcCD subunit C
