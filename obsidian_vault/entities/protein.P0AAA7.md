---
entity_id: "protein.P0AAA7"
entity_type: "protein"
name: "wzxE"
source_database: "UniProt"
source_id: "P0AAA7"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_02024, ECO:0000305}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_02024}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "wzxE wzx yifJ b3792 JW3766"
---

# wzxE

`protein.P0AAA7`

## Static

- Type: `protein`
- Source: `UniProt:P0AAA7`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_02024, ECO:0000305}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_02024}.

## Enriched Summary

FUNCTION: Mediates the transbilayer movement of Und-PP-GlcNAc-ManNAcA-Fuc4NAc (lipid III) from the inner to the outer leaflet of the cytoplasmic membrane during the assembly of enterobacterial common antigen (ECA). Required for the assembly of the phosphoglyceride-linked form of ECA (ECA(PG)) and the water-soluble cyclic form of ECA (ECA(CYC)). Could also mediate the translocation of Und-PP-GlcNAc. {ECO:0000269|PubMed:12621029, ECO:0000269|PubMed:16199561}. The assembly of enterobacterial common antigen (ECA) occurs by a Wzx/Wzy-dependent pathway (see ). wzxE encodes lipid IIIECA flippase - an inner membrane protein that mediates translocation, or 'flipping', of the undecaprenyl pyrophosphate-linked trisaccharide repeating unit (Fuc4NAc-ManNAcA-GlcNAc-P-P-undecaprenol) of ECA across the membrane bilayer . Null mutations in wzxE (wzxE::cm) result in accumulation of lipid IIIECA which is lethal in the absence of the flippases G7097-MONOMER WzxC for Und-PP-linked repeat units of colanic acid and RFBX-MONOMER WzxB for Und-PP-linked repeat units of O-antigen (and see ). WzxE mediates transport of the water soluble compound, N-acetylglucosaminylpyrophosphorylnerol (GlcNAc-P-P-Ner) into everted membrane vesicles; a pyrophosphoryl-linked saccharide and an unsaturated α-isoprene unit appear to be critical for WzeE-mediated transport...

## Biological Role

Catalyzes TRANS-RXN0-279 (reaction.ecocyc.TRANS-RXN0-279). Transports hν (molecule.ecocyc.Light).

## Annotation

FUNCTION: Mediates the transbilayer movement of Und-PP-GlcNAc-ManNAcA-Fuc4NAc (lipid III) from the inner to the outer leaflet of the cytoplasmic membrane during the assembly of enterobacterial common antigen (ECA). Required for the assembly of the phosphoglyceride-linked form of ECA (ECA(PG)) and the water-soluble cyclic form of ECA (ECA(CYC)). Could also mediate the translocation of Und-PP-GlcNAc. {ECO:0000269|PubMed:12621029, ECO:0000269|PubMed:16199561}.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-279|reaction.ecocyc.TRANS-RXN0-279]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b3792|gene.b3792]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AAA7`
- `KEGG:ecj:JW3766;eco:b3792;ecoc:C3026_20530;`
- `GeneID:93778152;948294;`
- `GO:GO:0005886; GO:0009246; GO:0140303`

## Notes

Lipid III flippase
