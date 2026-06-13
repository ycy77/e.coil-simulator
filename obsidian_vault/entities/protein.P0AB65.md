---
entity_id: "protein.P0AB65"
entity_type: "protein"
name: "yccX"
source_database: "UniProt"
source_id: "P0AB65"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yccX b0968 JW5131"
---

# yccX

`protein.P0AB65`

## Static

- Type: `protein`
- Source: `UniProt:P0AB65`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

Acylphosphatase (EC 3.6.1.7) (Acylphosphate phosphohydrolase) yccX encodes an acylphosphatase with relatively low catalytic efficiency, but very high structural stability . A C5-C49 disulfide bond is not required for catalytic activity , but accelerates protein folding . The functional role of the enzyme in vivo is unknown . An NMR solution structure of YccX has been determined . A crystal structure of YccX was obtained to 2.55 Å resolution. A 3D model of this structure differs from the NMR structure in multiple ways, including the presence of an additional short alpha helix (residues 81-86) and an intertwined dimer in the C-terminal edge where the C-terminal β-strand was swapped between two protomers. This structure differs from the Pyrococcus horikoshii AcP dimer . yccX shows differential codon adaptation, resulting in differential translation efficiency signatures, in thermophilic microbes. It was therefore predicted to play a role in the heat shock response. A yccX deletion mutant was shown to be more sensitive than wild-type specifically to heat shock, but not other stresses...

## Biological Role

Catalyzes acetyl phosphate phosphohydrolase (reaction.R00317), acyl phosphate phosphohydrolase (reaction.R00539), ACYLPHOSPHATASE-RXN (reaction.ecocyc.ACYLPHOSPHATASE-RXN).

## Enriched Pathways

- `eco00620` Pyruvate metabolism (KEGG)
- `eco00627` Aminobenzoate degradation (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

Acylphosphatase (EC 3.6.1.7) (Acylphosphate phosphohydrolase)

## Pathways

- `eco00620` Pyruvate metabolism (KEGG)
- `eco00627` Aminobenzoate degradation (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R00317|reaction.R00317]] `KEGG` `database` - via EC:3.6.1.7
- `catalyzes` --> [[reaction.R00539|reaction.R00539]] `KEGG` `database` - via EC:3.6.1.7
- `catalyzes` --> [[reaction.ecocyc.ACYLPHOSPHATASE-RXN|reaction.ecocyc.ACYLPHOSPHATASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0968|gene.b0968]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AB65`
- `KEGG:ecj:JW5131;eco:b0968;ecoc:C3026_05915;`
- `GeneID:93776446;945304;`
- `GO:GO:0003998; GO:0009408`
- `EC:3.6.1.7`

## Notes

Acylphosphatase (EC 3.6.1.7) (Acylphosphate phosphohydrolase)
