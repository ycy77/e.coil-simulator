---
entity_id: "protein.P0AAP1"
entity_type: "protein"
name: "dgcC"
source_database: "UniProt"
source_id: "P0AAP1"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dgcC adrA yaiC b0385 JW0376"
---

# dgcC

`protein.P0AAP1`

## Static

- Type: `protein`
- Source: `UniProt:P0AAP1`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: A probable diguanylate cyclase. The last member of a cascade of expressed proteins, its expression requires DgcM. DgcC production induces biosynthesis of cellulose in some E.coli isolates, but not in K12 strains. Cyclic-di-GMP is a second messenger which controls cell surface-associated traits in bacteria. {ECO:0000269|PubMed:11260463, ECO:0000269|PubMed:19707751}.

## Biological Role

Component of diguanylate cyclase DgcC (complex.ecocyc.CPLX0-8556).

## Enriched Pathways

- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

FUNCTION: A probable diguanylate cyclase. The last member of a cascade of expressed proteins, its expression requires DgcM. DgcC production induces biosynthesis of cellulose in some E.coli isolates, but not in K12 strains. Cyclic-di-GMP is a second messenger which controls cell surface-associated traits in bacteria. {ECO:0000269|PubMed:11260463, ECO:0000269|PubMed:19707751}.

## Pathways

- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8556|complex.ecocyc.CPLX0-8556]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0385|gene.b0385]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AAP1`
- `KEGG:ecj:JW0376;eco:b0385;ecoc:C3026_01865;`
- `GeneID:75170359;945037;`
- `GO:GO:0005525; GO:0005886; GO:0042802; GO:0043709; GO:0046872; GO:0052621; GO:1902201; GO:2001008`
- `EC:2.7.7.65`

## Notes

Probable diguanylate cyclase DgcC (DGC) (EC 2.7.7.65)
