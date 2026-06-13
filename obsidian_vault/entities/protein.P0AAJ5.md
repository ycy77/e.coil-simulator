---
entity_id: "protein.P0AAJ5"
entity_type: "protein"
name: "fdoH"
source_database: "UniProt"
source_id: "P0AAJ5"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell membrane; Single-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fdoH b3893 JW3864"
---

# fdoH

`protein.P0AAJ5`

## Static

- Type: `protein`
- Source: `UniProt:P0AAJ5`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell membrane; Single-pass membrane protein.

## Enriched Summary

FUNCTION: Allows to use formate as major electron donor during aerobic respiration. The beta chain is an electron transfer unit containing 4 cysteine clusters involved in the formation of iron-sulfur centers. Electrons are transferred from the gamma chain to the molybdenum cofactor of the alpha subunit (By similarity). {ECO:0000250}. fdoH encodes the β subunit of formate dehydrogenase O. It has 100% amino acid identity with FdnH, the [4Fe-4S] containing β subunit of formate dehydrogenase-N. FdoH is essentially hydrophilic in nature with one predicted α helical region at the C-terminus. The topological orientation of FdoH appears to be the reverse of FdnH, with the bulk of the protein located in the cytoplasm however the use or reporter fusions to determine toplogy of Tat-dependent proteins has been brought into question .

## Biological Role

Component of formate dehydrogenase O (complex.ecocyc.CPLX0-13310), formate dehydrogenase O subcomplex (complex.ecocyc.FORMATEDEHYDROGO-CPLX).

## Enriched Pathways

- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

FUNCTION: Allows to use formate as major electron donor during aerobic respiration. The beta chain is an electron transfer unit containing 4 cysteine clusters involved in the formation of iron-sulfur centers. Electrons are transferred from the gamma chain to the molybdenum cofactor of the alpha subunit (By similarity). {ECO:0000250}.

## Pathways

- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-13310|complex.ecocyc.CPLX0-13310]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=3
- `is_component_of` --> [[complex.ecocyc.FORMATEDEHYDROGO-CPLX|complex.ecocyc.FORMATEDEHYDROGO-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b3893|gene.b3893]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AAJ5`
- `KEGG:ecj:JW3864;eco:b3893;ecoc:C3026_21045;`
- `GeneID:86861996;93778045;948395;`
- `GO:GO:0005886; GO:0006788; GO:0009061; GO:0009326; GO:0015944; GO:0016020; GO:0019645; GO:0022904; GO:0036397; GO:0045333; GO:0046872; GO:0051539`

## Notes

Formate dehydrogenase-O iron-sulfur subunit (Aerobic formate dehydrogenase iron-sulfur subunit) (FDH-Z subunit beta) (Formate dehydrogenase-O subunit beta)
