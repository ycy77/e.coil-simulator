---
entity_id: "protein.P0AEL0"
entity_type: "protein"
name: "fdoI"
source_database: "UniProt"
source_id: "P0AEL0"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fdoI b3892 JW3863"
---

# fdoI

`protein.P0AEL0`

## Static

- Type: `protein`
- Source: `UniProt:P0AEL0`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: Allows to use formate as major electron donor during aerobic respiration. Subunit gamma is probably the cytochrome b556(FDO) component of the formate dehydrogenase. fdoI encodes the γ subunit of formate dehydrogenase O. It has 45% amino acid identity (over an alignment of 156 residues) with the heme b binding, γ subunit (FdnI) of formate dehydrogenase-N . Both the N- and C-terminus of FdoI appear to be located in the cytoplasm and it is predicted to have 4 transmembrane regions .

## Biological Role

Component of formate dehydrogenase O (complex.ecocyc.CPLX0-13310), formate dehydrogenase O subcomplex (complex.ecocyc.FORMATEDEHYDROGO-CPLX).

## Enriched Pathways

- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

FUNCTION: Allows to use formate as major electron donor during aerobic respiration. Subunit gamma is probably the cytochrome b556(FDO) component of the formate dehydrogenase.

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

- `encodes` <-- [[gene.b3892|gene.b3892]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AEL0`
- `KEGG:ecj:JW3863;eco:b3892;ecoc:C3026_21040;`
- `GeneID:93778046;948383;`
- `GO:GO:0005886; GO:0006788; GO:0006974; GO:0008863; GO:0009055; GO:0009061; GO:0009326; GO:0015944; GO:0016020; GO:0019645; GO:0036397; GO:0045333; GO:0046872`

## Notes

Formate dehydrogenase, cytochrome b556(fdo) subunit (Aerobic formate dehydrogenase cytochrome b556 subunit) (FDH-Z subunit gamma) (Formate dehydrogenase-O subunit gamma)
