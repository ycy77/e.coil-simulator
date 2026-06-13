---
entity_id: "protein.P0A930"
entity_type: "protein"
name: "wza"
source_database: "UniProt"
source_id: "P0A930"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000250}; Multi-pass membrane protein {ECO:0000250}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "wza b2062 JW2047"
---

# wza

`protein.P0A930`

## Static

- Type: `protein`
- Source: `UniProt:P0A930`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000250}; Multi-pass membrane protein {ECO:0000250}.

## Enriched Summary

FUNCTION: Probably involved in the export of the extracellular polysaccharide colanic acid from the cell to medium. wza is located within a cluster of genes that are responsible for production of the extracellular polysaccharide, CPD-21504 "colanic acid" (CA) and based on sequence similarity it may be involved in a CA export system . Wza is a member of the outer membrane auxiliary (OMA) protein family . Much of the information known about Wza comes from experiments characterizing Wza from the group 1 capsule producing strain Escherichia coli serotype K30 (WzaK30); wza from E. coli K-12 can complement a wza defect in E. coli K30 . The Δwza mutant of an EG10820 overexpressing, CA producing strain of E. coli K-12 MG1655 grows as misshapen rods and spheres . WzaK30 is a surface exposed outer membrane lipoprotein that forms a multimeric 'secretin-like' structure . Insertional inactivation of wza in E. coli strain E69 serotype O9a:K30 results in loss of the K30 capsular layer although K30 polysaccharide is still produced . WzaK30 forms ring-like octameric structures arranged as tetramers of dimers . WzaK30 contains a transmembrane domain that is a novel α-helical barrel structure and a large periplasmic domain that forms the bulk of the structure. The protein has a large central cavity that is open to the extracellular region . Wza plays a role in protecting E...

## Biological Role

Component of polysaccharide export complex (complex.ecocyc.CPLX0-7529).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

FUNCTION: Probably involved in the export of the extracellular polysaccharide colanic acid from the cell to medium.

## Pathways

- `eco02020` Two-component system (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7529|complex.ecocyc.CPLX0-7529]] `EcoCyc` `database` - EcoCyc component coefficient=8 | EcoCyc protcplxs.col coefficient=8

## Incoming Edges (1)

- `encodes` <-- [[gene.b2062|gene.b2062]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A930`
- `KEGG:ecj:JW2047;eco:b2062;ecoc:C3026_11600;`
- `GeneID:93775129;946558;`
- `GO:GO:0000271; GO:0006811; GO:0009279; GO:0015159; GO:0015288; GO:0015774; GO:0046377; GO:0046930`

## Notes

Putative polysaccharide export protein Wza
