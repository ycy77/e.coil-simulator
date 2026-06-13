---
entity_id: "protein.P0A6W3"
entity_type: "protein"
name: "mraY"
source_database: "UniProt"
source_id: "P0A6W3"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_00038, ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_00038, ECO:0000269|PubMed:15919996}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mraY murX b0087 JW0085"
---

# mraY

`protein.P0A6W3`

## Static

- Type: `protein`
- Source: `UniProt:P0A6W3`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_00038, ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_00038, ECO:0000269|PubMed:15919996}.

## Enriched Summary

FUNCTION: Catalyzes the initial step of the lipid cycle reactions in the biosynthesis of the cell wall peptidoglycan: transfers peptidoglycan precursor phospho-MurNAc-pentapeptide from UDP-MurNAc-pentapeptide onto the lipid carrier undecaprenyl phosphate, yielding undecaprenyl-pyrophosphoryl-MurNAc-pentapeptide, known as lipid I. {ECO:0000255|HAMAP-Rule:MF_00038, ECO:0000269|PubMed:1846850, ECO:0000269|PubMed:215212}. Phospho-N-acetylmuramoyl-pentapeptide transferase catalyzes the first step of the lipid cycle reactions in the biosynthetic pathway of cell wall peptidoglycans . MraY is of interest as an antibacterial drug target and has been used to assess high-throughput screening performance using the BioAssay Ontology .

## Biological Role

Catalyzes UDP-N-acetylmuramoyl-L-alanyl-D-glutamyl-meso-2,6-diaminopimelyl-D-alanyl-D-alanine:undecaprenyl-phosphate transferase (reaction.ecocyc.PHOSNACMURPENTATRANS-RXN). Bound by Magnesium cation (molecule.C00305).

## Enriched Pathways

- `eco00550` Peptidoglycan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01502` Vancomycin resistance (KEGG)

## Annotation

FUNCTION: Catalyzes the initial step of the lipid cycle reactions in the biosynthesis of the cell wall peptidoglycan: transfers peptidoglycan precursor phospho-MurNAc-pentapeptide from UDP-MurNAc-pentapeptide onto the lipid carrier undecaprenyl phosphate, yielding undecaprenyl-pyrophosphoryl-MurNAc-pentapeptide, known as lipid I. {ECO:0000255|HAMAP-Rule:MF_00038, ECO:0000269|PubMed:1846850, ECO:0000269|PubMed:215212}.

## Pathways

- `eco00550` Peptidoglycan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01502` Vancomycin resistance (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.PHOSNACMURPENTATRANS-RXN|reaction.ecocyc.PHOSNACMURPENTATRANS-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b0087|gene.b0087]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A6W3`
- `KEGG:ecj:JW0085;eco:b0087;ecoc:C3026_00340;`
- `GeneID:93777347;944814;`
- `GO:GO:0005886; GO:0008360; GO:0008963; GO:0009252; GO:0016020; GO:0044038; GO:0046872; GO:0051301; GO:0051992; GO:0071555`
- `EC:2.7.8.13`

## Notes

Phospho-N-acetylmuramoyl-pentapeptide-transferase (EC 2.7.8.13) (UDP-MurNAc-pentapeptide phosphotransferase)
