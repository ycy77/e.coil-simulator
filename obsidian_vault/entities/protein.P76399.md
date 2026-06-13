---
entity_id: "protein.P76399"
entity_type: "protein"
name: "mdtC"
source_database: "UniProt"
source_id: "P76399"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mdtC yegO b2076 JW2061"
---

# mdtC

`protein.P76399`

## Static

- Type: `protein`
- Source: `UniProt:P76399`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: The MdtABC tripartite complex confers resistance against novobiocin and deoxycholate. MdtABC requires TolC for its function. {ECO:0000255|HAMAP-Rule:MF_01424, ECO:0000269|PubMed:12107133, ECO:0000269|PubMed:12107134}. MdtBC is the resistance-nodulation-division (RND) family permease of a tripartite efflux pump that is implicated in resistance to antibiotics, bile salt derivatives and SDS. MdtC contains 6 predicted transmembrane domains . MdtB and MdtC comprise a heteromultimeric transmembrane complex; the purified active complex contains MdtB and MdtC in a 2:1 ratio . The mdtC Keio collection mutant (BW25113 ΔmdtC::kan) shows a significant increase in swimming motility .

## Biological Role

Component of multidrug efflux pump MdtABC-TolC (complex.ecocyc.TRANS-CPLX-202).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: The MdtABC tripartite complex confers resistance against novobiocin and deoxycholate. MdtABC requires TolC for its function. {ECO:0000255|HAMAP-Rule:MF_01424, ECO:0000269|PubMed:12107133, ECO:0000269|PubMed:12107134}.

## Pathways

- `eco02020` Two-component system (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.TRANS-CPLX-202|complex.ecocyc.TRANS-CPLX-202]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2076|gene.b2076]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76399`
- `KEGG:ecj:JW2061;eco:b2076;ecoc:C3026_11675;`
- `GeneID:946608;`
- `GO:GO:0005886; GO:0015125; GO:0015721; GO:0042908; GO:0042910; GO:0098567; GO:0140330; GO:1990281`

## Notes

Multidrug resistance protein MdtC (Multidrug transporter MdtC)
