---
entity_id: "protein.P0AGG8"
entity_type: "protein"
name: "tldD"
source_database: "UniProt"
source_id: "P0AGG8"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "tldD yhdO b3244 JW3213"
---

# tldD

`protein.P0AGG8`

## Static

- Type: `protein`
- Source: `UniProt:P0AGG8`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Metalloprotease involved in CcdA degradation. Suppresses the inhibitory activity of the carbon storage regulator (CsrA). {ECO:0000269|PubMed:12029038}. TldD and TldE form a stable heterodimeric complex with protease activity. TldD contains a metalloprotease-like HExxxH motif; the two His residues were shown to coordinate a metal ion in the crystal structure. A His262Ala mutant in the HExxxH motif lacks activity . A ΔtldD mutant harboring the pMccB17 plasmid accumulates the unprocessed Microcin B17 precursor protein, in contrast to wild type, which processes and exports Microcin B17 from the cell . A tldD mutant exhibits resistance to the F plasmid-encoded LetD DNA gyrase inhibitor , but only in the presence of the LetD inhibitor LetA . A csrA mutation suppresses the Tld phenotype of a tldD mutant . TldD: "tolerant for letD expression D" Reviews:

## Biological Role

Component of metalloprotease TldDE (complex.ecocyc.CPLX0-8539).

## Annotation

FUNCTION: Metalloprotease involved in CcdA degradation. Suppresses the inhibitory activity of the carbon storage regulator (CsrA). {ECO:0000269|PubMed:12029038}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8539|complex.ecocyc.CPLX0-8539]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b3244|gene.b3244]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AGG8`
- `KEGG:ecj:JW3213;eco:b3244;ecoc:C3026_17645;`
- `GeneID:75173414;947749;`
- `GO:GO:0005506; GO:0005829; GO:0008237; GO:0008270; GO:0016485; GO:1905368`
- `EC:3.4.-.-`

## Notes

Metalloprotease TldD (EC 3.4.-.-)
