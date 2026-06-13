---
entity_id: "protein.P76398"
entity_type: "protein"
name: "mdtB"
source_database: "UniProt"
source_id: "P76398"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01423}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_01423}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mdtB yegN b2075 JW2060"
---

# mdtB

`protein.P76398`

## Static

- Type: `protein`
- Source: `UniProt:P76398`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01423}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_01423}.

## Enriched Summary

FUNCTION: The MdtABC tripartite complex confers resistance against novobiocin and deoxycholate. MdtABC requires TolC for its function. {ECO:0000255|HAMAP-Rule:MF_01423, ECO:0000269|PubMed:12107133, ECO:0000269|PubMed:12107134}. MdtBC is the resistance-nodulation-division (RND) family permease of a tripartite efflux pump that is implicated in resistance to antibiotics, bile salt derivatives and SDS. MdtB contains 6 predicted transmembrane domains . MdtB and MdtC comprise a heteromultimeric transmembrane complex; the purified active complex contains MdtB and MdtC in a 2:1 ratio . mdtB is one of 35 efflux-encoding genes that have been deleted or inactivated in 'Efflux KnockOut-35' (EKO-35) - a K-12 BW25133-derived strain that lacks 35 efflux pumps and can be used as a platform to study their function . The mdtB Keio collection mutant (BW25113 ΔmdtB::kan) shows a significant increase in swimming motility .

## Biological Role

Component of multidrug efflux pump MdtABC-TolC (complex.ecocyc.TRANS-CPLX-202).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: The MdtABC tripartite complex confers resistance against novobiocin and deoxycholate. MdtABC requires TolC for its function. {ECO:0000255|HAMAP-Rule:MF_01423, ECO:0000269|PubMed:12107133, ECO:0000269|PubMed:12107134}.

## Pathways

- `eco02020` Two-component system (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.TRANS-CPLX-202|complex.ecocyc.TRANS-CPLX-202]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2075|gene.b2075]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76398`
- `KEGG:ecj:JW2060;eco:b2075;ecoc:C3026_11670;`
- `GeneID:946606;`
- `GO:GO:0005886; GO:0015125; GO:0015721; GO:0042908; GO:0042910; GO:0098567; GO:0140330; GO:1990281`

## Notes

Multidrug resistance protein MdtB (Multidrug transporter MdtB)
