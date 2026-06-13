---
entity_id: "protein.P0A9L5"
entity_type: "protein"
name: "ppiC"
source_database: "UniProt"
source_id: "P0A9L5"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ppiC parVA b3775 JW3748"
---

# ppiC

`protein.P0A9L5`

## Static

- Type: `protein`
- Source: `UniProt:P0A9L5`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: PPIases accelerate the folding of proteins (Probable). It prefers amino acid residues with hydrophobic side chains like leucine and phenylalanine in the P1 position of the peptides substrates. {ECO:0000305}. ppiC encodes a peptidyl-prolyl cis-trans isomerase (PPIase), parvulin, which defines a new family of PPIases . Unlike other PPIases, the enzymatic activity of parvulin is not inhibited by FK506 or cyclosporin A . The natural compound juglone specifically and irreversibly inactivates parvulin by covalent modification . EG11384-MONOMER AhpC has been identified as a specific interaction partner of PpiC . Additional substrates were identified by pull-down assays and co-IP . The stereospecificity of the enzyme has been studied , and a solution structure of PpiC has been determined . Mutants in predicted active site residues were assayed for potential substrate binding and PPIase activity . A ppiC mutant is more sensitive to oxidative stress than wild type . A strain containing non-polar deletions of all six cytoplasmic PPIases (Δ6ppi) shows a growth defect at 37°C in rich media and at 43°C in both rich and minimal media . Resequencing of multiple isolates of the MG1655 strain has identified several genetic variations compared to the reference sequence, including a single-nucleotide polymorphism in the yifO-ppiC intergenic region...

## Biological Role

Catalyzes PEPTIDYLPROLYL-ISOMERASE-RXN (reaction.ecocyc.PEPTIDYLPROLYL-ISOMERASE-RXN).

## Annotation

FUNCTION: PPIases accelerate the folding of proteins (Probable). It prefers amino acid residues with hydrophobic side chains like leucine and phenylalanine in the P1 position of the peptides substrates. {ECO:0000305}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.PEPTIDYLPROLYL-ISOMERASE-RXN|reaction.ecocyc.PEPTIDYLPROLYL-ISOMERASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3775|gene.b3775]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A9L5`
- `KEGG:ecj:JW3748;eco:b3775;ecoc:C3026_20445;`
- `GeneID:45134414;93778170;948285;`
- `GO:GO:0003755; GO:0005737`
- `EC:5.2.1.8`

## Notes

Peptidyl-prolyl cis-trans isomerase C (PPIase C) (EC 5.2.1.8) (Par10) (Parvulin) (Rotamase C)
