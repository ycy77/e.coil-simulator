---
entity_id: "protein.P0AEN8"
entity_type: "protein"
name: "fucU"
source_database: "UniProt"
source_id: "P0AEN8"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fucU b2804 JW2775"
---

# fucU

`protein.P0AEN8`

## Static

- Type: `protein`
- Source: `UniProt:P0AEN8`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Involved in the anomeric conversion of L-fucose. Catalyzes also the interconversion of beta-pyran and beta-furan forms of D-ribose. {ECO:0000269|PubMed:15060078, ECO:0000269|PubMed:19524593}. Utilizing NMR techniques, FucU was shown to catalyze the anomeric conversion of fucose. The enzyme also exhibits pyranase activity (catalyzing the interconversion of the pyranose and furanose forms) for D-ribose . FucU was previously shown to be an L-fucose binding protein with a KD for L-fucose of 1.61 mM . A crystal structure of FucU bound to L-fucose has been solved, showing a decameric toroidal structure that can be viewed as a pentamer of homodimers. Two adjacent subunits contribute to each active site. Site-directed mutagenesis of potential active site residues showed that Tyr111, His22, and Asp64 are required for catalytic activity. A reaction mechanism was proposed . Overexpression of FucU leads to increased resistance against xanthorrhizol .

## Biological Role

Component of L-fucose mutarotase (complex.ecocyc.CPLX0-7645).

## Enriched Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)

## Annotation

FUNCTION: Involved in the anomeric conversion of L-fucose. Catalyzes also the interconversion of beta-pyran and beta-furan forms of D-ribose. {ECO:0000269|PubMed:15060078, ECO:0000269|PubMed:19524593}.

## Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7645|complex.ecocyc.CPLX0-7645]] `EcoCyc` `database` - EcoCyc component coefficient=10 | EcoCyc protcplxs.col coefficient=10

## Incoming Edges (1)

- `encodes` <-- [[gene.b2804|gene.b2804]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AEN8`
- `KEGG:ecj:JW2775;eco:b2804;ecoc:C3026_15415;`
- `GeneID:93779194;945842;`
- `GO:GO:0005737; GO:0006004; GO:0016857; GO:0036373; GO:0042354; GO:0042802; GO:0042806; GO:0062193`
- `EC:5.1.3.29; 5.4.99.62`

## Notes

L-fucose mutarotase (EC 5.1.3.29) (D-ribose pyranase) (EC 5.4.99.62) (Fucose 1-epimerase) (Type-2 mutarotase)
