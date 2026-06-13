---
entity_id: "protein.P0A6U8"
entity_type: "protein"
name: "glgA"
source_database: "UniProt"
source_id: "P0A6U8"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "glgA b3429 JW3392"
---

# glgA

`protein.P0A6U8`

## Static

- Type: `protein`
- Source: `UniProt:P0A6U8`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Synthesizes alpha-1,4-glucan chains using ADP-glucose. Glycogen synthase is a glycosyltransferase, the second enzyme in the glycogen biosynthesis pathway. It catalyzes the addition of a glucosyl unit from ADP-glucose to the non-reducing end of glycogen. Lys15 may be involved in binding of ADP-glucose . A conserved region around Cys379 is predicted to form a loop structure and is involved in the interaction with ADP-glucose . Lys277 may be required for catalysis . Further site-directed mutagenesis identified residues essential for catalytic activity and ADP-glucose binding . Crystal structures of the wild-type and mutant GlgA in various conformations have been solved, suggesting the location of catalytic residues . A structure of GlgA with bound oligosaccharide indicates that long-chain glycans only bind to the N-terminal domain, ensuring unencumbered interdomain movement and efficient catalysis . Native glycogen synthase binds to metal affinity columns and may thus bind Mg2+, like its human homolog . Glycogen synthase from E. coli B can exist in homodimeric, -trimeric and -tetrameric form . However, all crystal structures obtained of the K-12 enzyme show a monomeric form . Review:

## Biological Role

Catalyzes GLYCOGENSYN-RXN (reaction.ecocyc.GLYCOGENSYN-RXN).

## Enriched Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

FUNCTION: Synthesizes alpha-1,4-glucan chains using ADP-glucose.

## Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.GLYCOGENSYN-RXN|reaction.ecocyc.GLYCOGENSYN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3429|gene.b3429]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A6U8`
- `KEGG:ecj:JW3392;eco:b3429;ecoc:C3026_18590;`
- `GeneID:75173587;75202274;947932;`
- `GO:GO:0004373; GO:0005829; GO:0005978; GO:0006974; GO:0009011`
- `EC:2.4.1.21`

## Notes

Glycogen synthase (EC 2.4.1.21) (Starch [bacterial glycogen] synthase)
