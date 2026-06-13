---
entity_id: "protein.P32714"
entity_type: "protein"
name: "mdtP"
source_database: "UniProt"
source_id: "P32714"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000305}; Lipid-anchor {ECO:0000255|PROSITE-ProRule:PRU00303}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mdtP yjcP b4080 JW4041"
---

# mdtP

`protein.P32714`

## Static

- Type: `protein`
- Source: `UniProt:P32714`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000305}; Lipid-anchor {ECO:0000255|PROSITE-ProRule:PRU00303}.

## Enriched Summary

FUNCTION: Could be involved in resistance to puromycin, acriflavine and tetraphenylarsonium chloride. {ECO:0000269|PubMed:11257026}. mdtP encodes a putative multidrug resistance protein; MdtP from E. coli K-12 W3110 has 26% sequence identity and 47% similarity (over 466 residues) with OprM - the Pseudomonas aeruginosa outer membrane component of the MexAB multidrug resistance pump; deletion of mdtP from strain W3110 results in increased susceptibility to acriflavin, puromycin and tetraphenylarsonium chloride . MdtP is the outer membrane component of a putative efflux pump implicated in resistance to sulfonamide antibiotics . sdsP: sulfa drug sensitivity mdtP: multi drug transporter

## Biological Role

Component of putative multidrug efflux pump MdtNOP (complex.ecocyc.CPLX0-7807).

## Annotation

FUNCTION: Could be involved in resistance to puromycin, acriflavine and tetraphenylarsonium chloride. {ECO:0000269|PubMed:11257026}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7807|complex.ecocyc.CPLX0-7807]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b4080|gene.b4080]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P32714`
- `KEGG:ecj:JW4041;eco:b4080;ecoc:C3026_22055;`
- `GeneID:948583;`
- `GO:GO:0009279; GO:0015562; GO:0016020; GO:0022857; GO:0046677; GO:0055085; GO:1990351`

## Notes

Multidrug resistance outer membrane protein MdtP
