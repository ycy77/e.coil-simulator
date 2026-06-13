---
entity_id: "protein.P0A7F6"
entity_type: "protein"
name: "speD"
source_database: "UniProt"
source_id: "P0A7F6"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "speD b0120 JW0116"
---

# speD

`protein.P0A7F6`

## Static

- Type: `protein`
- Source: `UniProt:P0A7F6`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the decarboxylation of S-adenosylmethionine to S-adenosylmethioninamine (dcAdoMet), the propylamine donor required for the synthesis of the polyamines spermine and spermidine from the diamine putrescine. S-adenosylmethionine (AdoMet) decarboxylase (SpeD) is an important enzyme of polyamine biosynthesis in all domains of life. It catalyzes the removal of the carboxylate group of S-adenosyl-L-methionine, producing S-adenosyl-L-methioninamine. This compound then acts as the n-propylamine group donor for the synthesis of spermidine from putrescine by SPERMIDINESYN-CPLX. Inhibition of AdoMet decarboxylase by spermidine appears to be the most significant physiological regulator of polyamine biosynthesis, probably limiting it when the intracellular spermidine concentration becomes excessive . This enzyme belongs to a small class of decarboxylating enzymes that utilize covalently bound pyruvate (pyruvoyl group). Class 1 enzymes are found in bacteria and archaea, while Class 2 are found in eukaryotes. These two classes show almost no detectable sequence homology with each other and do not show similarity to other known pyruvoyl-dependent amino acid decarboxylases. Class 1A enzymes are found primarily in Gram-negative bacteria, including E. coli, while Class 1B enzymes are found in some Gram-positive bacteria and archaea...

## Biological Role

Catalyzes S-adenosyl-L-methionine carboxy-lyase [S-adenosyl 3-(methylsulfanyl)propylamine-forming] (reaction.R00178). Component of S-adenosylmethionine decarboxylase (complex.ecocyc.SAMDECARB-CPLX).

## Enriched Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00330` Arginine and proline metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

FUNCTION: Catalyzes the decarboxylation of S-adenosylmethionine to S-adenosylmethioninamine (dcAdoMet), the propylamine donor required for the synthesis of the polyamines spermine and spermidine from the diamine putrescine.

## Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00330` Arginine and proline metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00178|reaction.R00178]] `KEGG` `database` - via EC:4.1.1.50
- `is_component_of` --> [[complex.ecocyc.SAMDECARB-CPLX|complex.ecocyc.SAMDECARB-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b0120|gene.b0120]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A7F6`
- `KEGG:ecj:JW0116;eco:b0120;ecoc:C3026_00505;`
- `GeneID:93777316;947719;`
- `GO:GO:0000287; GO:0004014; GO:0005829; GO:0008295; GO:0097264`
- `EC:4.1.1.50`

## Notes

S-adenosylmethionine decarboxylase proenzyme (AdoMetDC) (SAMDC) (EC 4.1.1.50) [Cleaved into: S-adenosylmethionine decarboxylase beta chain; S-adenosylmethionine decarboxylase alpha chain]
