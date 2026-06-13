---
entity_id: "protein.P0A7P5"
entity_type: "protein"
name: "rpmH"
source_database: "UniProt"
source_id: "P0A7P5"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rpmH rimA ssaF b3703 JW3680"
---

# rpmH

`protein.P0A7P5`

## Static

- Type: `protein`
- Source: `UniProt:P0A7P5`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

Large ribosomal subunit protein bL34 (50S ribosomal protein L34) The L34 protein is a component of the 50S subunit of the ribosome. L34 can be isolated in a complex with 5S rRNA, tRNA, and other proteins of the large ribosomal subunit . Assembly of L34 into the 50S ribosomal subunit is dependent on L4, L22 and L24 . L34 can be crosslinked to L23 . L34 is one of six proteins that is completely lost from ribosomes in post-stationary cells . L34 was identified as "antizyme 2", an inhibitor of the biosynthetic ornithine and arginine decarboxylases; these enzymes are involved in the biosynthesis of polyamines . In vitro and outside the context of the ribosome, L34 and a number of additional ribosomal proteins show "antizyme" inhibition of ornithine decarboxylase . L34 physically interacts with ornithine and arginine decarboxylase, and overexpression of L34 decreases the production of polyamines in vivo . Levels of L34 increase in response to polyamines; the effect is thought to be due to an increase in the level of transcription of rpmH . SHAPE probing showed that the 5' UTR of the rpmH-rnpA mRNA folds into three major hairpin helices; EG10862-MONOMER binds tightly to helix 2 and may induce a conformational change in the 5' UTR . The rimA mutant, likely an allele of rpmH , has a cold-sensitive growth and ribosome assembly defect . An rpmH null mutant is viable...

## Biological Role

Component of 50S ribosomal subunit (complex.ecocyc.CPLX0-3962).

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

Large ribosomal subunit protein bL34 (50S ribosomal protein L34)

## Pathways

- `eco03010` Ribosome (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3962|complex.ecocyc.CPLX0-3962]] `EcoCyc` `database` - EcoCyc component coefficient=
- `represses` --> [[reaction.ecocyc.ARGDECARBOX-RXN|reaction.ecocyc.ARGDECARBOX-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (1)

- `encodes` <-- [[gene.b3703|gene.b3703]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A7P5`
- `KEGG:ecj:JW3680;eco:b3703;ecoc:C3026_20075;`
- `GeneID:948216;99708231;99810388;`
- `GO:GO:0002181; GO:0003735; GO:0005737; GO:0022625`

## Notes

Large ribosomal subunit protein bL34 (50S ribosomal protein L34)
