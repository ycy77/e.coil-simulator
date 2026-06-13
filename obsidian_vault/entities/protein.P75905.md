---
entity_id: "protein.P75905"
entity_type: "protein"
name: "pgaC"
source_database: "UniProt"
source_id: "P75905"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pgaC ycdQ b1022 JW1007"
---

# pgaC

`protein.P75905`

## Static

- Type: `protein`
- Source: `UniProt:P75905`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}.

## Enriched Summary

FUNCTION: Probable N-acetylglucosaminyltransferase that catalyzes the polymerization of single monomer units of UDP-N-acetylglucosamine to produce the linear homomer poly-beta-1,6-N-acetyl-D-glucosamine (PGA), a biofilm adhesin polysaccharide. {ECO:0000269|PubMed:15090514, ECO:0000269|PubMed:18359807}.

## Biological Role

Component of poly-N-acetyl-D-glucosamine synthase (complex.ecocyc.CPLX0-7994).

## Enriched Pathways

- `eco00543` Exopolysaccharide biosynthesis (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

FUNCTION: Probable N-acetylglucosaminyltransferase that catalyzes the polymerization of single monomer units of UDP-N-acetylglucosamine to produce the linear homomer poly-beta-1,6-N-acetyl-D-glucosamine (PGA), a biofilm adhesin polysaccharide. {ECO:0000269|PubMed:15090514, ECO:0000269|PubMed:18359807}.

## Pathways

- `eco00543` Exopolysaccharide biosynthesis (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7994|complex.ecocyc.CPLX0-7994]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1022|gene.b1022]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P75905`
- `KEGG:ecj:JW1007;eco:b1022;`
- `GeneID:945606;`
- `GO:GO:0005886; GO:0008375; GO:0016740; GO:0043708`
- `EC:2.4.1.-`

## Notes

Poly-beta-1,6-N-acetyl-D-glucosamine synthase (PGA synthase) (Poly-beta-1,6-GlcNAc synthase) (EC 2.4.1.-) (Biofilm PGA synthesis protein PgaC) (N-acetylglucosaminyltransferase PgaC)
