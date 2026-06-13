---
entity_id: "protein.P69432"
entity_type: "protein"
name: "pgaD"
source_database: "UniProt"
source_id: "P69432"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pgaD ycdP b1021 JW1006"
---

# pgaD

`protein.P69432`

## Static

- Type: `protein`
- Source: `UniProt:P69432`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}.

## Enriched Summary

FUNCTION: Required for the synthesis of poly-beta-1,6-N-acetyl-D-glucosamine (PGA), a biofilm adhesin polysaccharide. May assist the glycosyltransferase PgaC in the polymerization of PGA. {ECO:0000269|PubMed:15090514, ECO:0000269|PubMed:18359807, ECO:0000269|PubMed:19460094}.

## Biological Role

Component of poly-N-acetyl-D-glucosamine synthase (complex.ecocyc.CPLX0-7994).

## Enriched Pathways

- `eco00543` Exopolysaccharide biosynthesis (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

FUNCTION: Required for the synthesis of poly-beta-1,6-N-acetyl-D-glucosamine (PGA), a biofilm adhesin polysaccharide. May assist the glycosyltransferase PgaC in the polymerization of PGA. {ECO:0000269|PubMed:15090514, ECO:0000269|PubMed:18359807, ECO:0000269|PubMed:19460094}.

## Pathways

- `eco00543` Exopolysaccharide biosynthesis (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7994|complex.ecocyc.CPLX0-7994]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1021|gene.b1021]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P69432`
- `KEGG:ecj:JW1006;eco:b1021;ecoc:C3026_06210;`
- `GeneID:75171097;947503;`
- `GO:GO:0005886; GO:0043708; GO:0043709`

## Notes

Biofilm PGA synthesis protein PgaD
