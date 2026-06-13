---
entity_id: "protein.P0ACZ2"
entity_type: "protein"
name: "etp"
source_database: "UniProt"
source_id: "P0ACZ2"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "etp yccY b0982 JW5132"
---

# etp

`protein.P0ACZ2`

## Static

- Type: `protein`
- Source: `UniProt:P0ACZ2`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Dephosphorylates etk. Etk and Etp are a tyrosine kinase-tyrosine phosphatase pair. Etp can dephosphorylate the phosphotyrosine residues of Etk in vitro. In contrast to the related phosphatase, Wzb, Etp has minimal effect on biosynthesis of colanic acid . Mutations in etp lead to the accumulation of RpoH in an inactive phosphorylated form, and thus, decreased transcription of heat shock genes. etp mutant strains accumulate phosphoproteins including Etk, and display a temperature-sensitive growth phenotype at 43 °C . The operon encoding YmcD, YmcC, YmcB, YmcA, YccZ, Etp, and Etk was characterized in the enteropathogenic E. coli strain O127:H6. There, all seven gene products are required for the production of the G4C capsule polysaccharide . That operon may not be expressed in E. coli K-12, because the promoter region that was mapped in E. coli O127:H6 is inactivated in E. coli K-12 by the insertion of an IS1 element 15 bp upstream of the YmcD translation start site . Etp: "E. coli phosphotyrosine phosphatase"

## Biological Role

Catalyzes PROTEIN-TYROSINE-PHOSPHATASE-RXN (reaction.ecocyc.PROTEIN-TYROSINE-PHOSPHATASE-RXN).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Dephosphorylates etk.

## Pathways

- `eco02020` Two-component system (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.PROTEIN-TYROSINE-PHOSPHATASE-RXN|reaction.ecocyc.PROTEIN-TYROSINE-PHOSPHATASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0982|gene.b0982]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ACZ2`
- `KEGG:ecj:JW5132;eco:b0982;ecoc:C3026_05990;`
- `GeneID:75171057;945236;`
- `GO:GO:0004725`
- `EC:3.1.3.48`

## Notes

Low molecular weight protein-tyrosine-phosphatase Etp (EC 3.1.3.48)
