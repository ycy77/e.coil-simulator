---
entity_id: "protein.P76372"
entity_type: "protein"
name: "wzzB"
source_database: "UniProt"
source_id: "P76372"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:16079137}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:16079137}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "wzzB cld rol wzz b2027 JW5836"
---

# wzzB

`protein.P76372`

## Static

- Type: `protein`
- Source: `UniProt:P76372`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:16079137}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:16079137}.

## Enriched Summary

FUNCTION: Confers a modal distribution of chain length on the O-antigen component of lipopolysaccharide (LPS). Gives rise to a reduced number of short chain molecules and increases in numbers of longer molecules. wzzB encodes the O-antigen co-polymerase (also called the O-antigen chain length regulator) of a Wzx/Wzy-dependent pathway of O-antigen synthesis; Wzz family proteins are required to regulate the length distribution of lipid-linked polysaccharides during polymerization at the periplasmic face of the inner membrane (see ). WzzB is a group 1a polysaccharide co-polymerase (PCP1a); E. coli K-12 also contains a group 1b PCP - EG11295-MONOMER WzzE - which regulates the length of enterobacterial common antigen (see ). E. coli K-12 is phenotypically rough and does not express O-antigen due to mutations in the rfb region; an engineered strain of E. coli K-12 with all rfb genes intact synthesizes CPD0-2249 O16 antigen . Early studies identified wzz genes (formerly rol for "regulator of O length" or cld for "chain length determinant") in O-antigen producing E. coli strains . In K-12 strains engineered to produced O specific polysaccharide WzzB functions together with the corresponding RFBX-MONOMER Wzx family flippase and EG11982-MONOMER Wzy family polymerase for translocation and synthesis of lipid-linked O16 antigen (see ). WzzB appears to be present as a dimer in the membrane...

## Annotation

FUNCTION: Confers a modal distribution of chain length on the O-antigen component of lipopolysaccharide (LPS). Gives rise to a reduced number of short chain molecules and increases in numbers of longer molecules.

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b2027|gene.b2027]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76372`
- `KEGG:ecj:JW5836;eco:b2027;ecoc:C3026_11425;`
- `GeneID:946553;`
- `GO:GO:0004713; GO:0005886; GO:0009103`

## Notes

Chain length determinant protein (Polysaccharide antigen chain regulator)
