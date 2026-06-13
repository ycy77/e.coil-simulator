---
entity_id: "protein.P02919"
entity_type: "protein"
name: "mrcB"
source_database: "UniProt"
source_id: "P02919"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Single-pass type II membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mrcB pbpF ponB b0149 JW0145"
---

# mrcB

`protein.P02919`

## Static

- Type: `protein`
- Source: `UniProt:P02919`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Single-pass type II membrane protein.

## Enriched Summary

FUNCTION: Cell wall formation. Synthesis of cross-linked peptidoglycan from the lipid intermediates. The enzyme has a penicillin-insensitive transglycosylase N-terminal domain (formation of linear glycan strands) and a penicillin-sensitive transpeptidase C-terminal domain (cross-linking of the peptide subunits).

## Biological Role

Catalyzes R06177 (reaction.R06177), [poly-N-acetyl-D-glucosaminyl-(1->4)-(N-acetyl-D-muramoylpentapeptide)]-diphosphoundecaprenol:[N-acetyl-D-glucosaminyl-(1->4)-N-acetyl-D-muramoylpentapeptide]-diphosphoundecaprenol polysaccharidetransferase (reaction.R06178), R06179 (reaction.R06179). Component of peptidoglycan glycosyltransferase / peptidoglycan DD-transpeptidase MrcB (complex.ecocyc.CPLX0-3951), penicillin binding protein 1Bγ (complex.ecocyc.CPLX0-8300).

## Enriched Pathways

- `eco00550` Peptidoglycan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Cell wall formation. Synthesis of cross-linked peptidoglycan from the lipid intermediates. The enzyme has a penicillin-insensitive transglycosylase N-terminal domain (formation of linear glycan strands) and a penicillin-sensitive transpeptidase C-terminal domain (cross-linking of the peptide subunits).

## Pathways

- `eco00550` Peptidoglycan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (5)

- `catalyzes` --> [[reaction.R06177|reaction.R06177]] `KEGG` `database` - via EC:2.4.99.28
- `catalyzes` --> [[reaction.R06178|reaction.R06178]] `KEGG` `database` - via EC:2.4.99.28
- `catalyzes` --> [[reaction.R06179|reaction.R06179]] `KEGG` `database` - via EC:2.4.99.28
- `is_component_of` --> [[complex.ecocyc.CPLX0-3951|complex.ecocyc.CPLX0-3951]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.CPLX0-8300|complex.ecocyc.CPLX0-8300]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0149|gene.b0149]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P02919`
- `KEGG:ecj:JW0145;eco:b0149;ecoc:C3026_00655;`
- `GeneID:944843;`
- `GO:GO:0005886; GO:0006508; GO:0008360; GO:0008658; GO:0008955; GO:0009002; GO:0009252; GO:0009274; GO:0016020; GO:0030288; GO:0046677; GO:0051518; GO:0071433`
- `EC:2.4.99.28; 3.4.16.4`

## Notes

Penicillin-binding protein 1B (PBP-1b) (PBP1b) (Murein polymerase) [Includes: Penicillin-insensitive transglycosylase (EC 2.4.99.28) (Peptidoglycan TGase) (Peptidoglycan glycosyltransferase); Penicillin-sensitive transpeptidase (EC 3.4.16.4) (DD-transpeptidase)]
