---
entity_id: "protein.P76330"
entity_type: "protein"
name: "dgcQ"
source_database: "UniProt"
source_id: "P76330"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dgcQ yedQ b1956 JW5832"
---

# dgcQ

`protein.P76330`

## Static

- Type: `protein`
- Source: `UniProt:P76330`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Catalyzes the synthesis of cyclic-di-GMP (c-di-GMP) via the condensation of 2 GTP molecules (By similarity). Cyclic-di-GMP is a second messenger which controls cell surface-associated traits in bacteria. Involved in the regulation of cellulose production (PubMed:20303158). {ECO:0000250|UniProtKB:P31129, ECO:0000269|PubMed:20303158}. DgcQ is a probable inner membrane protein with two predicted transmembrane domains and a C-terminal GGDEF domain with diguanylate cyclase activity . The N-terminal CHASE (Cyclases/Histidine kinases Associated Sensory) domain is predicted to be periplasmic . The C terminus is predicted to localize to the cytoplasm . DgcQ is implicated in phage N4 infection . The diguanylate cyclase domain of DgcQ physically interacts with PyrB, the catalytic subunit of ASPCARBTRANS-CPLX (PyrBI), an enzyme involved in de novoUMP biosynthesis. The diguanylate cyclase activity of this domain is activated by UTP and inhibited by CARBAMYUL-L-ASPARTATE, the product of PyrBI . In the commensal E. coli strain 1094, DgcQ is a regulator that constitutively activates cellulose production under all tested environmental conditions . Expression of dgcQ is dependent on σS under a number of stress conditions and increases during transition into stationary phase . DgcQ does not appear to act as a global regulator of gene expression...

## Biological Role

Catalyzes RXN0-5359 (reaction.ecocyc.RXN0-5359).

## Enriched Pathways

- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

FUNCTION: Catalyzes the synthesis of cyclic-di-GMP (c-di-GMP) via the condensation of 2 GTP molecules (By similarity). Cyclic-di-GMP is a second messenger which controls cell surface-associated traits in bacteria. Involved in the regulation of cellulose production (PubMed:20303158). {ECO:0000250|UniProtKB:P31129, ECO:0000269|PubMed:20303158}.

## Pathways

- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5359|reaction.ecocyc.RXN0-5359]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1956|gene.b1956]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76330`
- `KEGG:ecj:JW5832;eco:b1956;`
- `GeneID:946471;`
- `GO:GO:0005525; GO:0005886; GO:0030244; GO:0043709; GO:0046872; GO:0052621; GO:1902201`
- `EC:2.7.7.65`

## Notes

Probable diguanylate cyclase DgcQ (DGC) (EC 2.7.7.65) (Cellulose synthesis regulatory protein)
