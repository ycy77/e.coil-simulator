---
entity_id: "protein.P0AG00"
entity_type: "protein"
name: "wzzE"
source_database: "UniProt"
source_id: "P0AG00"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_02025, ECO:0000305}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_02025}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "wzzE wzz yifC b3785 JW5601"
---

# wzzE

`protein.P0AG00`

## Static

- Type: `protein`
- Source: `UniProt:P0AG00`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_02025, ECO:0000305}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_02025}.

## Enriched Summary

FUNCTION: Modulates the polysaccharide chain length of enterobacterial common antigen (ECA). Required for the assembly of the phosphoglyceride-linked form of ECA (ECA(PG)) and the water-soluble cyclic form of ECA (ECA(CYC)). {ECO:0000269|PubMed:10515954, ECO:0000269|PubMed:16199561}. The assembly of enterobacterial common antigen (ECA) occurs by a Wzx/Wzy-dependent pathway (see ). wzzE is located within a gene cluster that encodes the enzymes required for ECA synthesis and assembly; WzzE functions to modulate the length of CPD-21605 ECAPG polysaccharide chains . Typically, ECAPG chain lengths are 1 to 14 repeats long with a modal value of 6 or 7; wzzE mutants display a random, non-modal distribution of ECAPG polysaccharide chain lengths . wzzE is also required for the synthesis of cyclic ECA (CPD0-2646 ECACYC) . The lipid III flippase EG11486-MONOMER WzxE, ECA polymerase FUC4NACTRANS-MONOMER WzyE, and WzzE may function as a multiprotein complex . WzyE and WzzE were shown in TAX-29471 to form a complex in vivo with stoichiometry of approximately eight WzzE to one WzyE. WzyE is positioned in the center of a transmembrane cavity, or lumen, formed by the transmembrane helices of the eight WzzE molecules. The nascent polymer forms inside the lumen, and the length of the polymer is limited by the lumen's depth...

## Annotation

FUNCTION: Modulates the polysaccharide chain length of enterobacterial common antigen (ECA). Required for the assembly of the phosphoglyceride-linked form of ECA (ECA(PG)) and the water-soluble cyclic form of ECA (ECA(CYC)). {ECO:0000269|PubMed:10515954, ECO:0000269|PubMed:16199561}.

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b3785|gene.b3785]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AG00`
- `KEGG:ecj:JW5601;eco:b3785;ecoc:C3026_20495;`
- `GeneID:93778159;944815;`
- `GO:GO:0004713; GO:0005886; GO:0009246`

## Notes

ECA polysaccharide chain length modulation protein
