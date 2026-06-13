---
entity_id: "protein.P0AD03"
entity_type: "protein"
name: "letA"
source_database: "UniProt"
source_id: "P0AD03"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:27795327}; Multi-pass membrane protein {ECO:0000269|PubMed:27795327}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "letA yebS b1833 JW1822"
---

# letA

`protein.P0AD03`

## Static

- Type: `protein`
- Source: `UniProt:P0AD03`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:27795327}; Multi-pass membrane protein {ECO:0000269|PubMed:27795327}.

## Enriched Summary

FUNCTION: Could be part, together with LetB, of a system that transports lipids between the inner membrane and the outer membrane (Probable). Contributes to membrane integrity (PubMed:27795327). {ECO:0000269|PubMed:27795327, ECO:0000305|PubMed:32359438}. LetA is an inner membrane protein with six transmembrane regions . letAB, pqiABC and ABC-45-CPLX "mlaFEDCB" are related loci; letAB (and pqiABC) are predicted to encode inter-membrane transport pathways that contribute to membrane integrity; simultaneous deletion of letAB and pqiABC in a ΔmlaD background increases sensitivity to EDTA and SDS; the substrate for transport is not known (see also ). letA shows differential codon adaptation, resulting in differential translation efficiency signatures, in thermophilic microbes. It was therefore predicted to play a role in the heat shock response. A letA deletion mutant was shown to be more sensitive than wild-type specifically to heat shock, but not other stresses . A letA'-'lacZ fusion is induced in cells that produce truncated lipopolysaccharide or have other membrane defects . letA: lipophilic envelope-spanning tunnel

## Annotation

FUNCTION: Could be part, together with LetB, of a system that transports lipids between the inner membrane and the outer membrane (Probable). Contributes to membrane integrity (PubMed:27795327). {ECO:0000269|PubMed:27795327, ECO:0000305|PubMed:32359438}.

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b1833|gene.b1833]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AD03`
- `KEGG:ecj:JW1822;eco:b1833;ecoc:C3026_10445;`
- `GeneID:75171904;946353;`
- `GO:GO:0005886; GO:0009408; GO:0061024`

## Notes

Lipophilic envelope-spanning tunnel protein A (Intermembrane transport protein LetA)
