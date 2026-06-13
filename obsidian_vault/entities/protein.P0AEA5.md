---
entity_id: "protein.P0AEA5"
entity_type: "protein"
name: "cyoE"
source_database: "UniProt"
source_id: "P0AEA5"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:8253713}; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "cyoE b0428 JW0418"
---

# cyoE

`protein.P0AEA5`

## Static

- Type: `protein`
- Source: `UniProt:P0AEA5`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:8253713}; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: Converts heme B (protoheme IX) to heme O by substitution of the vinyl group on carbon 2 of heme B porphyrin ring with a hydroxyethyl farnesyl side group. {ECO:0000269|PubMed:1336371, ECO:0000269|PubMed:8253713}. The CyoE protein, heme O synthase, catalyzes the synthesis of heme O, which is essential for the catalytic functions of the cytochrome bo oxidase complex . At one time it was thought that CyoE was a fifth subunit of the cytochrome bo oxidase, but it was shown that a 28 kDa polypeptide which co-purifies with the cytochrome bo oxidase complex appears even in a cyoE deletion strain .

## Biological Role

Catalyzes heme o biosynthesis (reaction.ecocyc.HEMEOSYN-RXN). Bound by Magnesium cation (molecule.C00305).

## Enriched Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco00860` Porphyrin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Converts heme B (protoheme IX) to heme O by substitution of the vinyl group on carbon 2 of heme B porphyrin ring with a hydroxyethyl farnesyl side group. {ECO:0000269|PubMed:1336371, ECO:0000269|PubMed:8253713}.

## Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco00860` Porphyrin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.HEMEOSYN-RXN|reaction.ecocyc.HEMEOSYN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b0428|gene.b0428]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AEA5`
- `KEGG:ecj:JW0418;eco:b0428;ecoc:C3026_02090;`
- `GeneID:75170446;75202853;945073;`
- `GO:GO:0005886; GO:0008495; GO:0048034`
- `EC:2.5.1.141`

## Notes

Protoheme IX farnesyltransferase (EC 2.5.1.141) (Heme B farnesyltransferase) (Heme O synthase)
