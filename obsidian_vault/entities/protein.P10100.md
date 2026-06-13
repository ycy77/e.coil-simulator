---
entity_id: "protein.P10100"
entity_type: "protein"
name: "rlpA"
source_database: "UniProt"
source_id: "P10100"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell membrane {ECO:0000255|HAMAP-Rule:MF_02071}; Lipid-anchor {ECO:0000255|HAMAP-Rule:MF_02071, ECO:0000305|PubMed:3316191}. Note=Localizes at the septal ring. Is also associated with some other structures/complexes along the cell cylinder. {ECO:0000269|PubMed:19684127, ECO:0000269|PubMed:19880599}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rlpA b0633 JW0628"
---

# rlpA

`protein.P10100`

## Static

- Type: `protein`
- Source: `UniProt:P10100`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell membrane {ECO:0000255|HAMAP-Rule:MF_02071}; Lipid-anchor {ECO:0000255|HAMAP-Rule:MF_02071, ECO:0000305|PubMed:3316191}. Note=Localizes at the septal ring. Is also associated with some other structures/complexes along the cell cylinder. {ECO:0000269|PubMed:19684127, ECO:0000269|PubMed:19880599}.

## Enriched Summary

FUNCTION: Lytic transglycosylase with a strong preference for naked glycan strands that lack stem peptides. {ECO:0000255|HAMAP-Rule:MF_02071}. rlpA encodes a minor lipoprotein; the unprocessed protein has an apparent molecular weight of 54 kDa (by SDS-PAGE) despite a calculated molecular weight of ~36 kDa; in vitro expression of a mature protein is inhibited by treatment with the signal peptidase II inhibitor, globomycin; the protein incorporates 3H-labeled palmitate and 3H-labeled glycerol in vitro . A truncated version of RlpA (first 102 residues) suppresses the conditional lethal phenotype of a EG10760 prc null mutation by an unknown mechanism . An RlpA fluorescent fusion protein (RlpA-RFP) accumulates at cell division sites, but is also localized elsewhere in the cell envelope; the isolated, labeled SPOR domain of RlpA (residues 281-362) accumulates at division sites and not in any other nonhomogenous pattern; deletion of rlpA does not result in cell growth or division defects (see also ). The isolated, labeled SPOR domain of RlpA localizes to septal peptidoglycan in purified E. coli sacculi; septal accumulation is greatly reduced in sacculi (from amidase mutants) that lack a-denuded-peptidoglycan denuded glycans and is increased in sacculi (from lytic transglycosylase mutants) that contain a higher level of denuded glycans...

## Annotation

FUNCTION: Lytic transglycosylase with a strong preference for naked glycan strands that lack stem peptides. {ECO:0000255|HAMAP-Rule:MF_02071}.

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b0633|gene.b0633]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P10100`
- `KEGG:ecj:JW0628;eco:b0633;ecoc:C3026_03165;`
- `GeneID:945241;`
- `GO:GO:0000270; GO:0005886; GO:0008932; GO:0009279; GO:0042834; GO:0043093; GO:0071555`
- `EC:4.2.2.-`

## Notes

Endolytic peptidoglycan transglycosylase RlpA (EC 4.2.2.-) (Rare lipoprotein A)
