---
entity_id: "protein.P0A9M5"
entity_type: "protein"
name: "gpt"
source_database: "UniProt"
source_id: "P0A9M5"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Peripheral membrane protein {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gpt gpp gxu b0238 JW0228"
---

# gpt

`protein.P0A9M5`

## Static

- Type: `protein`
- Source: `UniProt:P0A9M5`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Peripheral membrane protein {ECO:0000305}.

## Enriched Summary

FUNCTION: Purine salvage pathway enzyme that catalyzes the transfer of the ribosyl-5-phosphate group from 5-phospho-alpha-D-ribose 1-diphosphate (PRPP) to the N9 position of the 6-oxopurines guanine and xanthine to form the corresponding ribonucleotides GMP (guanosine 5'-monophosphate) and XMP (xanthosine 5'-monophosphate), with the release of PPi. To a lesser extent, also acts on hypoxanthine (PubMed:3886014, PubMed:9100006). Does not ribophosphorylate adenine (PubMed:3886014). {ECO:0000269|PubMed:3886014, ECO:0000269|PubMed:9100006}.

## Biological Role

Catalyzes XMP:pyrophosphate phosphoribosyltransferase (reaction.R02142). Component of xanthine-guanine phosphoribosyltransferase (complex.ecocyc.GPT-CPLX).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

FUNCTION: Purine salvage pathway enzyme that catalyzes the transfer of the ribosyl-5-phosphate group from 5-phospho-alpha-D-ribose 1-diphosphate (PRPP) to the N9 position of the 6-oxopurines guanine and xanthine to form the corresponding ribonucleotides GMP (guanosine 5'-monophosphate) and XMP (xanthosine 5'-monophosphate), with the release of PPi. To a lesser extent, also acts on hypoxanthine (PubMed:3886014, PubMed:9100006). Does not ribophosphorylate adenine (PubMed:3886014). {ECO:0000269|PubMed:3886014, ECO:0000269|PubMed:9100006}.

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R02142|reaction.R02142]] `KEGG` `database` - via EC:2.4.2.22
- `is_component_of` --> [[complex.ecocyc.GPT-CPLX|complex.ecocyc.GPT-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b0238|gene.b0238]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A9M5`
- `KEGG:ecj:JW0228;eco:b0238;ecoc:C3026_01130;ecoc:C3026_23865;`
- `GeneID:93777155;944817;`
- `GO:GO:0000287; GO:0000310; GO:0004422; GO:0005829; GO:0005886; GO:0006166; GO:0032263; GO:0032264; GO:0032265; GO:0032991; GO:0042802; GO:0051289; GO:0052657; GO:0097216`
- `EC:2.4.2.-; 2.4.2.22`

## Notes

Xanthine-guanine phosphoribosyltransferase (XGPRT) (EC 2.4.2.-) (EC 2.4.2.22) (Xanthine phosphoribosyltransferase)
