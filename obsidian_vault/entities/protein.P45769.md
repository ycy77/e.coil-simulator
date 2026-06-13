---
entity_id: "protein.P45769"
entity_type: "protein"
name: "yhdZ"
source_database: "UniProt"
source_id: "P45769"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Peripheral membrane protein {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yhdZ b3271 JW3239"
---

# yhdZ

`protein.P45769`

## Static

- Type: `protein`
- Source: `UniProt:P45769`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Peripheral membrane protein {ECO:0000305}.

## Enriched Summary

FUNCTION: Probably part of a binding-protein-dependent transport system YdhWXYZ for an amino acid. Probably responsible for energy coupling to the transport system. YhdZ is predicted to be the ATP-binding subunit of a putative ABC transporter; YhdZ contains sequence motifs conserved in ATP-binding cassette (ABC) proteins .

## Biological Role

Component of putative transport complex, ABC superfamily (complex.ecocyc.ABC-52-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Probably part of a binding-protein-dependent transport system YdhWXYZ for an amino acid. Probably responsible for energy coupling to the transport system.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-52-CPLX|complex.ecocyc.ABC-52-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b3271|gene.b3271]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P45769`
- `KEGG:ecj:JW3239;eco:b3271;ecoc:C3026_17795;`
- `GeneID:947763;`
- `GO:GO:0005524; GO:0005886; GO:0015424; GO:0015833; GO:0016020; GO:0016887; GO:0042626; GO:0043190; GO:0055052`

## Notes

Uncharacterized amino-acid ABC transporter ATP-binding protein YhdZ
