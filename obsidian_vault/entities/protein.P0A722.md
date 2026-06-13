---
entity_id: "protein.P0A722"
entity_type: "protein"
name: "lpxA"
source_database: "UniProt"
source_id: "P0A722"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "lpxA b0181 JW0176"
---

# lpxA

`protein.P0A722`

## Static

- Type: `protein`
- Source: `UniProt:P0A722`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Involved in the biosynthesis of lipid A, a phosphorylated glycolipid that anchors the lipopolysaccharide to the outer membrane of the cell.

## Biological Role

Component of acyl-[acyl-carrier-protein]—UDP-N-acetylglucosamine O-acyltransferase (complex.ecocyc.UDPNACETYLGLUCOSAMACYLTRANS-CPLX).

## Enriched Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)

## Annotation

FUNCTION: Involved in the biosynthesis of lipid A, a phosphorylated glycolipid that anchors the lipopolysaccharide to the outer membrane of the cell.

## Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.UDPNACETYLGLUCOSAMACYLTRANS-CPLX|complex.ecocyc.UDPNACETYLGLUCOSAMACYLTRANS-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3

## Incoming Edges (1)

- `encodes` <-- [[gene.b0181|gene.b0181]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A722`
- `KEGG:ecj:JW0176;eco:b0181;ecoc:C3026_00830;`
- `GeneID:93777244;944849;`
- `GO:GO:0005737; GO:0005829; GO:0008780; GO:0009103; GO:0009245; GO:0016020; GO:0042802`
- `EC:2.3.1.129`

## Notes

Acyl-[acyl-carrier-protein]--UDP-N-acetylglucosamine O-acyltransferase (UDP-N-acetylglucosamine acyltransferase) (EC 2.3.1.129)
