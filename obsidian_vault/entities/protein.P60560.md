---
entity_id: "protein.P60560"
entity_type: "protein"
name: "guaC"
source_database: "UniProt"
source_id: "P60560"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "guaC b0104 JW0101"
---

# guaC

`protein.P60560`

## Static

- Type: `protein`
- Source: `UniProt:P60560`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the irreversible NADPH-dependent deamination of GMP to IMP. It functions in the conversion of nucleobase, nucleoside and nucleotide derivatives of G to A nucleotides, and in maintaining the intracellular balance of A and G nucleotides.

## Biological Role

Catalyzes inosine-5'-phosphate:NADP+ oxidoreductase (aminating); (reaction.R01134). Component of GMP reductase (complex.ecocyc.GMP-REDUCT-CPLX).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

FUNCTION: Catalyzes the irreversible NADPH-dependent deamination of GMP to IMP. It functions in the conversion of nucleobase, nucleoside and nucleotide derivatives of G to A nucleotides, and in maintaining the intracellular balance of A and G nucleotides.

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R01134|reaction.R01134]] `KEGG` `database` - via EC:1.7.1.7
- `is_component_of` --> [[complex.ecocyc.GMP-REDUCT-CPLX|complex.ecocyc.GMP-REDUCT-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b0104|gene.b0104]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P60560`
- `KEGG:ecj:JW0101;eco:b0104;ecoc:C3026_00425;`
- `GeneID:86862613;93777331;948986;`
- `GO:GO:0003920; GO:0005737; GO:0005829; GO:0015951; GO:0032264; GO:0042802; GO:0046872; GO:1902560`
- `EC:1.7.1.7`

## Notes

GMP reductase (EC 1.7.1.7) (Guanosine 5'-monophosphate oxidoreductase) (Guanosine monophosphate reductase)
