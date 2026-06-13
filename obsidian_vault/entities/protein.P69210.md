---
entity_id: "protein.P69210"
entity_type: "protein"
name: "mdtI"
source_database: "UniProt"
source_id: "P69210"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mdtI ydgE b1599 JW1591"
---

# mdtI

`protein.P69210`

## Static

- Type: `protein`
- Source: `UniProt:P69210`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: Catalyzes the excretion of spermidine. Can also confer resistance to deoxycholate and SDS. {ECO:0000269|PubMed:11566977, ECO:0000269|PubMed:18039771}. MdtI is one of two integral membrane subunits which constitute a heterodimeric multidrug / spermidine efflux transporter. MdtI (Em109) shares 33% sequence identity with the multidrug efflux pump, EmrE; purified MdtJ doesn't bind TPP+ and cannot form mixed oligomers with EmrE in vitro . Expression of chromosomal mdtJI is very low in both the presence and absence of spermidine .

## Biological Role

Component of multidrug/spermidine efflux pump (complex.ecocyc.YDGEF-CPLX).

## Annotation

FUNCTION: Catalyzes the excretion of spermidine. Can also confer resistance to deoxycholate and SDS. {ECO:0000269|PubMed:11566977, ECO:0000269|PubMed:18039771}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.YDGEF-CPLX|complex.ecocyc.YDGEF-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1599|gene.b1599]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P69210`
- `KEGG:ecj:JW1591;eco:b1599;ecoc:C3026_09210;`
- `GeneID:93775747;947333;`
- `GO:GO:0005886; GO:0015199; GO:0015220; GO:0015297; GO:0015606; GO:0015871; GO:0031460; GO:1902495; GO:1903711; GO:1990961`

## Notes

Spermidine export protein MdtI
