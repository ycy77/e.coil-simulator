---
entity_id: "protein.P76397"
entity_type: "protein"
name: "mdtA"
source_database: "UniProt"
source_id: "P76397"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Peripheral membrane protein {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mdtA yegM b2074 JW5338"
---

# mdtA

`protein.P76397`

## Static

- Type: `protein`
- Source: `UniProt:P76397`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Peripheral membrane protein {ECO:0000305}.

## Enriched Summary

FUNCTION: The MdtABC tripartite complex confers resistance against novobiocin and deoxycholate. MdtABC requires TolC for its function. {ECO:0000269|PubMed:12107133, ECO:0000269|PubMed:12107134}. MdtA is the membrane fusion protein (MFP) of a tripartite efflux pump that is implicated in resistance to antibiotics, bile salt derivatives and SDS. MdtA exhibits 47% similarity and 28% identity to the AcrA membrane fusion protein .

## Biological Role

Component of multidrug efflux pump MdtABC-TolC (complex.ecocyc.TRANS-CPLX-202).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: The MdtABC tripartite complex confers resistance against novobiocin and deoxycholate. MdtABC requires TolC for its function. {ECO:0000269|PubMed:12107133, ECO:0000269|PubMed:12107134}.

## Pathways

- `eco02020` Two-component system (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.TRANS-CPLX-202|complex.ecocyc.TRANS-CPLX-202]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2074|gene.b2074]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76397`
- `KEGG:ecj:JW5338;eco:b2074;ecoc:C3026_11665;`
- `GeneID:946604;`
- `GO:GO:0015125; GO:0015562; GO:0015721; GO:0042908; GO:0098567; GO:0140330; GO:1990281`

## Notes

Multidrug resistance protein MdtA (Multidrug transporter MdtA)
