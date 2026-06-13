---
entity_id: "protein.P0AFY6"
entity_type: "protein"
name: "sbmA"
source_database: "UniProt"
source_id: "P0AFY6"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "sbmA b0377 JW0368"
---

# sbmA

`protein.P0AFY6`

## Static

- Type: `protein`
- Source: `UniProt:P0AFY6`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}.

## Enriched Summary

FUNCTION: Uptake of antimicrobial peptides. Required for the transport of microcin B17 (MccB17), microcin 25 (Mcc25) and proline-rich antimicrobial peptides (such as Cathelicidin-3, Arasin 1 and Dro/Drosocin) into the cell. {ECO:0000269|PubMed:17725560, ECO:0000269|PubMed:3543211, ECO:0000269|PubMed:36997646, ECO:0000269|PubMed:7768835, ECO:0000305|PubMed:26860543}.

## Biological Role

Component of peptide antibiotic transporter (complex.ecocyc.CPLX0-8097).

## Annotation

FUNCTION: Uptake of antimicrobial peptides. Required for the transport of microcin B17 (MccB17), microcin 25 (Mcc25) and proline-rich antimicrobial peptides (such as Cathelicidin-3, Arasin 1 and Dro/Drosocin) into the cell. {ECO:0000269|PubMed:17725560, ECO:0000269|PubMed:3543211, ECO:0000269|PubMed:36997646, ECO:0000269|PubMed:7768835, ECO:0000305|PubMed:26860543}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8097|complex.ecocyc.CPLX0-8097]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0377|gene.b0377]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AFY6`
- `KEGG:ecj:JW0368;eco:b0377;`
- `GeneID:946884;`
- `GO:GO:0005524; GO:0005886; GO:0015031; GO:0015291; GO:0015638; GO:0015833; GO:0042803; GO:0042884; GO:0042885; GO:0046677; GO:1904680`

## Notes

Peptide antibiotic transporter SbmA
