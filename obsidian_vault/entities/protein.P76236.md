---
entity_id: "protein.P76236"
entity_type: "protein"
name: "cdgI"
source_database: "UniProt"
source_id: "P76236"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "cdgI yeaI b1785 JW1774"
---

# cdgI

`protein.P76236`

## Static

- Type: `protein`
- Source: `UniProt:P76236`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Catalyzes the synthesis of cyclic-di-GMP (c-di-GMP) via the condensation of 2 GTP molecules. {ECO:0000250|UniProtKB:P31129}. CdgI contains an N-terminal MASE4 (Membrane-Associated SEnsor) domain with eight predicted transmembrane domains followed by a C-terminal degenerate diguanylate cyclase (GGDEF) domain that is located in the cytoplasm . CdgI belongs to the core set of eight GGDEF/EAL domain proteins that is absolutely conserved in a set of 61 E. coli genomes containing pathogenic, commensal and probiotic strains . A cdgI deletion mutant shows 30-fold increased early biofilm formation and 4-fold increased swimming motility. The motility phenotype is complemented by wild type cdgI, but not a mutant where the degenerate GGDEF motif, EGEVF in CdgI, was changed to EGAVF, suggesting that CdgI may indeed be a functional diguanylate cyclase. Deletion of cdgI does not alter the concentration of c-di-GMP inside the cell . Expression of cdgI may be dependent on σS under high salt, but not other stress conditions . No expression was seen in LB medium . G6971 was significantly upregulated in simulated microgravity . CdgI: "c-di-GMP binding protein I"

## Annotation

FUNCTION: Catalyzes the synthesis of cyclic-di-GMP (c-di-GMP) via the condensation of 2 GTP molecules. {ECO:0000250|UniProtKB:P31129}.

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b1785|gene.b1785]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76236`
- `KEGG:ecj:JW1774;eco:b1785;`
- `GeneID:75171852;946366;`
- `GO:GO:0005525; GO:0005886; GO:0043709; GO:0046872; GO:0052621; GO:1902201`
- `EC:2.7.7.65`

## Notes

Probable diguanylate cyclase CdgI (DGC) (EC 2.7.7.65)
