---
entity_id: "protein.P69212"
entity_type: "protein"
name: "mdtJ"
source_database: "UniProt"
source_id: "P69212"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mdtJ ydgF b1600 JW1592"
---

# mdtJ

`protein.P69212`

## Static

- Type: `protein`
- Source: `UniProt:P69212`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: Catalyzes the excretion of spermidine. Can also confer resistance to deoxycholate and SDS. {ECO:0000269|PubMed:11566977, ECO:0000269|PubMed:18039771}. MdtJ is one of two integral membrane subunits which constitute a heterodimeric multidrug / spermidine efflux transporter. MdtJ (Em121) shares 32% sequence identity with the multidrug efflux pump, EmrE; purified MdtJ doesn't bind TPP+ and cannot form mixed oligomers with EmrE in vitro . Expression of chromosomal mdtJI is very low in both the presence and absence of spermidine . Transcription of mdtUJI is induced by spermidine at pH 9; translation of MdtU is required for spermidine-mediated expression of MdtJ . mdtJ is one of 35 efflux-encoding genes that have been deleted or inactivated in 'Efflux KnockOut-35' (EKO-35) - a K-12 BW25133-derived strain that lacks 35 efflux pumps and can be used as a platform to study their function .

## Biological Role

Component of multidrug/spermidine efflux pump (complex.ecocyc.YDGEF-CPLX).

## Annotation

FUNCTION: Catalyzes the excretion of spermidine. Can also confer resistance to deoxycholate and SDS. {ECO:0000269|PubMed:11566977, ECO:0000269|PubMed:18039771}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.YDGEF-CPLX|complex.ecocyc.YDGEF-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1600|gene.b1600]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P69212`
- `KEGG:ecj:JW1592;eco:b1600;ecoc:C3026_09215;`
- `GeneID:93775748;946139;`
- `GO:GO:0005886; GO:0015199; GO:0015220; GO:0015297; GO:0015606; GO:0015871; GO:0031460; GO:1902495; GO:1903711; GO:1990961`

## Notes

Spermidine export protein MdtJ
