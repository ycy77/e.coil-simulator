---
entity_id: "protein.P38097"
entity_type: "protein"
name: "dgcE"
source_database: "UniProt"
source_id: "P38097"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dgcE yegE b2067 JW2052"
---

# dgcE

`protein.P38097`

## Static

- Type: `protein`
- Source: `UniProt:P38097`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Catalyzes the synthesis of cyclic-di-GMP (c-di-GMP) via the condensation of 2 GTP molecules (By similarity). Involved in the control of the switch from cell motility to adhesion via regulation of cellular levels of c-di-GMP (PubMed:20303158). Part of a signaling cascade that regulates curli biosynthesis (PubMed:23708798). The cascade is composed of two c-di-GMP control modules, in which c-di-GMP controlled by the DgcE/PdeH pair (module I) regulates the activity of the DgcM/PdeR pair (module II), which in turn regulates activity of the transcription factor MlrA and expression of the master biofilm regulator csgD (PubMed:23708798). {ECO:0000250|UniProtKB:P31129, ECO:0000269|PubMed:20303158, ECO:0000269|PubMed:23708798}.

## Biological Role

Component of diguanylate cyclase DgcE (complex.ecocyc.CPLX0-8535).

## Enriched Pathways

- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

FUNCTION: Catalyzes the synthesis of cyclic-di-GMP (c-di-GMP) via the condensation of 2 GTP molecules (By similarity). Involved in the control of the switch from cell motility to adhesion via regulation of cellular levels of c-di-GMP (PubMed:20303158). Part of a signaling cascade that regulates curli biosynthesis (PubMed:23708798). The cascade is composed of two c-di-GMP control modules, in which c-di-GMP controlled by the DgcE/PdeH pair (module I) regulates the activity of the DgcM/PdeR pair (module II), which in turn regulates activity of the transcription factor MlrA and expression of the master biofilm regulator csgD (PubMed:23708798). {ECO:0000250|UniProtKB:P31129, ECO:0000269|PubMed:20303158, ECO:0000269|PubMed:23708798}.

## Pathways

- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8535|complex.ecocyc.CPLX0-8535]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2067|gene.b2067]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P38097`
- `KEGG:ecj:JW2052;eco:b2067;ecoc:C3026_11625;`
- `GeneID:946600;`
- `GO:GO:0005525; GO:0005886; GO:0046872; GO:0052621; GO:1900231`
- `EC:2.7.7.65`

## Notes

Probable diguanylate cyclase DgcE (DGC) (EC 2.7.7.65)
