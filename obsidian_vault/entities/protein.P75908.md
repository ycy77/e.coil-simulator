---
entity_id: "protein.P75908"
entity_type: "protein"
name: "dgcT"
source_database: "UniProt"
source_id: "P75908"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dgcT ycdT b1025 JW5143"
---

# dgcT

`protein.P75908`

## Static

- Type: `protein`
- Source: `UniProt:P75908`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Probably catalyzes the synthesis of cyclic-di-GMP (c-di-GMP) via the condensation of 2 GTP molecules. Overexpression leads to a strong repression of swimming; swimming returns to normal when residues 359-360 are both mutated to Ala. Overexpression also leads to a 20-fold increase in c-di-GMP levels in vivo. Cyclic-di-GMP is a second messenger which controls cell surface-associated traits in bacteria. {ECO:0000269|PubMed:18713317}. DgcT is a diguanylate cyclase that regulates motility; the effect on motility is probably mediated by the second messenger molecule c-di-GMP . DgcT has an N-terminal MASE4 (Membrane-Associated SEnsor) domain, which includes eight transmembrane segments . The MASE4 domain is followed by the diguanylate cyclase (GGDEF) domain . Overexpression of DgcT represses swimming behavior . Expression of DgcT is repressed by CsrA, which interacts directly with the 5' leader sequence of the dgcT mRNA and modulates the stability of the message . DgcT: diguanylate cyclase T . Related review:

## Biological Role

Catalyzes RXN0-5359 (reaction.ecocyc.RXN0-5359).

## Annotation

FUNCTION: Probably catalyzes the synthesis of cyclic-di-GMP (c-di-GMP) via the condensation of 2 GTP molecules. Overexpression leads to a strong repression of swimming; swimming returns to normal when residues 359-360 are both mutated to Ala. Overexpression also leads to a 20-fold increase in c-di-GMP levels in vivo. Cyclic-di-GMP is a second messenger which controls cell surface-associated traits in bacteria. {ECO:0000269|PubMed:18713317}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5359|reaction.ecocyc.RXN0-5359]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1025|gene.b1025]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P75908`
- `KEGG:ecj:JW5143;eco:b1025;`
- `GeneID:945593;`
- `GO:GO:0005525; GO:0005886; GO:0046872; GO:0052621; GO:0061939; GO:0090609`
- `EC:2.7.7.65`

## Notes

Probable diguanylate cyclase DgcT (DGC) (EC 2.7.7.65)
