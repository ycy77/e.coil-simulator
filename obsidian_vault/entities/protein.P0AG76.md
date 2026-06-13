---
entity_id: "protein.P0AG76"
entity_type: "protein"
name: "sbcD"
source_database: "UniProt"
source_id: "P0AG76"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "sbcD yajA b0398 JW0388"
---

# sbcD

`protein.P0AG76`

## Static

- Type: `protein`
- Source: `UniProt:P0AG76`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: SbcCD cleaves DNA hairpin structures. These structures can inhibit DNA replication and are intermediates in certain DNA recombination reactions. The complex acts as a 3'->5' double strand exonuclease that can open hairpins. It also has a 5' single-strand endonuclease activity. An sbcD mutation (sbcD::kan) permits the stable propagation of bacteriophage containing a long palindromic nucleotide sequence; sbcD and sbcC form an operon in E. coli K-12 . SbcD belongs to a subgroup of phosphoesterases that are associated with recombination and DNA repair .

## Biological Role

Component of ATP-dependent structure-specific DNA nuclease (complex.ecocyc.CPLX0-3957).

## Annotation

FUNCTION: SbcCD cleaves DNA hairpin structures. These structures can inhibit DNA replication and are intermediates in certain DNA recombination reactions. The complex acts as a 3'->5' double strand exonuclease that can open hairpins. It also has a 5' single-strand endonuclease activity.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3957|complex.ecocyc.CPLX0-3957]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0398|gene.b0398]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AG76`
- `KEGG:ecj:JW0388;eco:b0398;ecoc:C3026_01935;`
- `GeneID:93777062;945049;`
- `GO:GO:0000014; GO:0003677; GO:0004529; GO:0006260; GO:0006274; GO:0006281; GO:0006310; GO:0008408; GO:1990238; GO:1990391`

## Notes

Nuclease SbcCD subunit D
