---
entity_id: "protein.P76008"
entity_type: "protein"
name: "ldcA"
source_database: "UniProt"
source_id: "P76008"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:10428950}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ldcA ycgQ b1192 JW1181"
---

# ldcA

`protein.P76008`

## Static

- Type: `protein`
- Source: `UniProt:P76008`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:10428950}.

## Enriched Summary

FUNCTION: Releases the terminal D-alanine residue from the cytoplasmic tetrapeptide recycling product L-Ala-gamma-D-Glu-meso-Dap-D-Ala. To a lesser extent, can also cleave D-Ala from murein derivatives containing the tetrapeptide, i.e. MurNAc-tetrapeptide, UDP-MurNAc-tetrapeptide, GlcNAc-MurNAc-tetrapeptide, and GlcNAc-anhMurNAc-tetrapeptide. Does not act on murein sacculi or cross-linked muropeptides. The tripeptides produced by the LcdA reaction can then be reused as peptidoglycan building blocks; LcdA is thereby involved in murein recycling. Is also essential for viability during stationary phase. {ECO:0000269|PubMed:10428950, ECO:0000269|PubMed:18535144}.

## Biological Role

Component of murein tetrapeptide carboxypeptidase (complex.ecocyc.CPLX0-8616).

## Annotation

FUNCTION: Releases the terminal D-alanine residue from the cytoplasmic tetrapeptide recycling product L-Ala-gamma-D-Glu-meso-Dap-D-Ala. To a lesser extent, can also cleave D-Ala from murein derivatives containing the tetrapeptide, i.e. MurNAc-tetrapeptide, UDP-MurNAc-tetrapeptide, GlcNAc-MurNAc-tetrapeptide, and GlcNAc-anhMurNAc-tetrapeptide. Does not act on murein sacculi or cross-linked muropeptides. The tripeptides produced by the LcdA reaction can then be reused as peptidoglycan building blocks; LcdA is thereby involved in murein recycling. Is also essential for viability during stationary phase. {ECO:0000269|PubMed:10428950, ECO:0000269|PubMed:18535144}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8616|complex.ecocyc.CPLX0-8616]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1192|gene.b1192]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76008`
- `KEGG:ecj:JW1181;eco:b1192;ecoc:C3026_07015;`
- `GeneID:945756;`
- `GO:GO:0004180; GO:0005829; GO:0006508; GO:0008236; GO:0008360; GO:0009252; GO:0009254; GO:0042803; GO:0061787; GO:0071555; GO:0106415`
- `EC:3.4.17.13`

## Notes

Murein tetrapeptide carboxypeptidase (EC 3.4.17.13) (LD-carboxypeptidase A) (Muramoyltetrapeptide carboxypeptidase)
