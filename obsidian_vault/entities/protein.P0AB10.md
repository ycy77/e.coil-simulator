---
entity_id: "protein.P0AB10"
entity_type: "protein"
name: "pqiC"
source_database: "UniProt"
source_id: "P0AB10"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000269|PubMed:27795327}; Lipid-anchor {ECO:0000255|PROSITE-ProRule:PRU00303}; Periplasmic side {ECO:0000269|PubMed:27795327}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pqiC ymbA b0952 JW5127"
---

# pqiC

`protein.P0AB10`

## Static

- Type: `protein`
- Source: `UniProt:P0AB10`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000269|PubMed:27795327}; Lipid-anchor {ECO:0000255|PROSITE-ProRule:PRU00303}; Periplasmic side {ECO:0000269|PubMed:27795327}.

## Enriched Summary

FUNCTION: Component of a transport pathway that contributes to membrane integrity. {ECO:0000269|PubMed:27795327}. PqiC is a periplasmic facing, outer membrane lipoprotein; PqiC interacts with PqiB and the hetero-oligomer may bridge the inner and outer membrane; PqiC also forms homo-oligomers (see further ). pqiA, pqiB and pqiC form an operon; expression of a PqiC-PhoA fusion protein is induced by SoxC when exponentially growing cells are exposed to paraquat . pqiABC, letAB and ABC-45-CPLX "mlaFEDCB" are related loci; pqiABC (and letAB) are predicted to encode inter-membrane transport pathways that contribute to membrane integrity; simultaneous deletion of pqiABC and letAB in a ΔmlaD background increases sensitivity to EDTA and SDS; expression of pqiABC from a plasmid complements the SDS-EDTA hypersensitivity of a Δ(mlaD pqiB letB) strain; the substrate for transport is not known .

## Annotation

FUNCTION: Component of a transport pathway that contributes to membrane integrity. {ECO:0000269|PubMed:27795327}.

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b0952|gene.b0952]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AB10`
- `KEGG:ecj:JW5127;eco:b0952;ecoc:C3026_05825;`
- `GeneID:75204043;946972;`
- `GO:GO:0009279; GO:0030288; GO:0042802; GO:0061024`

## Notes

Intermembrane transport lipoprotein PqiC
