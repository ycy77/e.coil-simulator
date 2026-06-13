---
entity_id: "protein.P32715"
entity_type: "protein"
name: "mdtO"
source_database: "UniProt"
source_id: "P32715"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305|PubMed:15919996}; Multi-pass membrane protein {ECO:0000305|PubMed:15919996}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mdtO yjcQ b4081 JW4042"
---

# mdtO

`protein.P32715`

## Static

- Type: `protein`
- Source: `UniProt:P32715`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305|PubMed:15919996}; Multi-pass membrane protein {ECO:0000305|PubMed:15919996}.

## Enriched Summary

FUNCTION: Could be involved in resistance to puromycin, acriflavine and tetraphenylarsonium chloride. MdtO is an uncharacterized component of a putative multidrug efflux pump . mdtO is one of 35 efflux-encoding genes that have been deleted or inactivated in 'Efflux KnockOut-35' (EKO-35) - a K-12 BW25133-derived strain that lacks 35 efflux pumps and can be used as a platform to study their function . In the Transporter Classification Database, MdtO is a member of the Aromatic Acid Exporter (ArAE) family . sdsQ: sulfa drug sensitivity mdtO: multi drug transporter

## Biological Role

Component of putative multidrug efflux pump MdtNOP (complex.ecocyc.CPLX0-7807).

## Annotation

FUNCTION: Could be involved in resistance to puromycin, acriflavine and tetraphenylarsonium chloride.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7807|complex.ecocyc.CPLX0-7807]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b4081|gene.b4081]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P32715`
- `KEGG:ecj:JW4042;eco:b4081;ecoc:C3026_22060;`
- `GeneID:948582;`
- `GO:GO:0005886; GO:0015546; GO:0016020; GO:0046677; GO:0055085; GO:1902599; GO:1990351`

## Notes

Multidrug resistance protein MdtO
