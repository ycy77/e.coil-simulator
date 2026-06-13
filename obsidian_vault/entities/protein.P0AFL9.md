---
entity_id: "protein.P0AFL9"
entity_type: "protein"
name: "pqiA"
source_database: "UniProt"
source_id: "P0AFL9"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:27795327}; Multi-pass membrane protein {ECO:0000269|PubMed:27795327}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pqiA pqi5A b0950 JW0933"
---

# pqiA

`protein.P0AFL9`

## Static

- Type: `protein`
- Source: `UniProt:P0AFL9`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:27795327}; Multi-pass membrane protein {ECO:0000269|PubMed:27795327}.

## Enriched Summary

FUNCTION: Component of a transport pathway that contributes to membrane integrity. {ECO:0000269|PubMed:27795327}. PqiA is an inner membrane protein with six transmembrane regions . pqiA, pqiB and pqiC form an operon which is a member of the soxRS regulon ; expression is induced during exponential growth, by paraquat and other agents known to produce superoxide radicals within cells, such as menadione, phenazine methosulfate, and plumbagin, but not by hydrogen peroxide, ethanol nor heat shock . Expression increases under carbon or phosphate starvation or during stationary phase in an RpoS dependent manner; expression is regulated independently by SoxS and RpoS . A pqiA mutant has no obvious phenotype, including no change in resistance to oxidants . pqiABC, letAB and ABC-45-CPLX "mlaFEDCB" are related loci; pqiABC (and letAB) are predicted to encode inter-membrane transport pathways that contribute to membrane integrity; simultaneous deletion of pqiABC and letAB in a ΔmlaD background increases sensitivity to EDTA and SDS; expression of pqiABC from a plasmid complements the SDS-EDTA hypersensitivity of a Δ(mlaD pqiB letB) strain; the substrate for transport is not known .

## Annotation

FUNCTION: Component of a transport pathway that contributes to membrane integrity. {ECO:0000269|PubMed:27795327}.

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b0950|gene.b0950]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AFL9`
- `KEGG:ecj:JW0933;eco:b0950;ecoc:C3026_05815;`
- `GeneID:93776464;944999;`
- `GO:GO:0005886; GO:0006950; GO:0016020; GO:0061024`

## Notes

Intermembrane transport protein PqiA (Paraquat-inducible protein A)
