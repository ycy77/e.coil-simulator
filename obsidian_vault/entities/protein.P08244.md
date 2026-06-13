---
entity_id: "protein.P08244"
entity_type: "protein"
name: "pyrF"
source_database: "UniProt"
source_id: "P08244"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pyrF b1281 JW1273"
---

# pyrF

`protein.P08244`

## Static

- Type: `protein`
- Source: `UniProt:P08244`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the decarboxylation of orotidine 5'-monophosphate (OMP) to uridine 5'-monophosphate (UMP).

## Biological Role

Component of orotidine-5'-phosphate decarboxylase (complex.ecocyc.OROTPDECARB-CPLX).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Catalyzes the decarboxylation of orotidine 5'-monophosphate (OMP) to uridine 5'-monophosphate (UMP).

## Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.OROTPDECARB-CPLX|complex.ecocyc.OROTPDECARB-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1281|gene.b1281]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P08244`
- `KEGG:ecj:JW1273;eco:b1281;ecoc:C3026_07520;`
- `GeneID:947121;`
- `GO:GO:0004590; GO:0005737; GO:0005829; GO:0006207; GO:0015949; GO:0016831; GO:0044205`
- `EC:4.1.1.23`

## Notes

Orotidine 5'-phosphate decarboxylase (EC 4.1.1.23) (OMP decarboxylase) (OMPDCase) (OMPdecase)
