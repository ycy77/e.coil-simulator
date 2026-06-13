---
entity_id: "protein.P16682"
entity_type: "protein"
name: "phnD"
source_database: "UniProt"
source_id: "P16682"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "phnD psiD b4105 JW4066"
---

# phnD

`protein.P16682`

## Static

- Type: `protein`
- Source: `UniProt:P16682`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Phosphonate binding protein that is part of the phosphonate uptake system. Exhibits high affinity for 2-aminoethylphosphonate, and somewhat less affinity to ethylphosphonate, methylphosphonate, phosphonoacetate and phenylphosphonate. {ECO:0000269|PubMed:16751609}. phnD encodes the periplasmic binding protein of an ATP-dependent phosphonate/phosphate uptake system that is considered to be cryptic in E. coli K-12. Purified PhnD binds the naturally occurring phosphonates, 2-aminoethylphosphonate, ethylphosphonate and methylphosphonate with high affinity (estimated Kds of d of 50µM) . PhnD has been used in the development of a phosphonate biosensor . psiD: phosphate starvation inducible

## Biological Role

Component of phosphonate/phosphate ABC transporter (complex.ecocyc.ABC-23-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Phosphonate binding protein that is part of the phosphonate uptake system. Exhibits high affinity for 2-aminoethylphosphonate, and somewhat less affinity to ethylphosphonate, methylphosphonate, phosphonoacetate and phenylphosphonate. {ECO:0000269|PubMed:16751609}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-23-CPLX|complex.ecocyc.ABC-23-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b4105|gene.b4105]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P16682`
- `KEGG:ecj:JW4066;eco:b4105;ecoc:C3026_22180;`
- `GeneID:75203255;948624;`
- `GO:GO:0015716; GO:0042597; GO:0043190; GO:0055085`

## Notes

Phosphonates-binding periplasmic protein
