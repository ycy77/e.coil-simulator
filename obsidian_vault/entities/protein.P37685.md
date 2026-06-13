---
entity_id: "protein.P37685"
entity_type: "protein"
name: "aldB"
source_database: "UniProt"
source_id: "P37685"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "aldB yiaX b3588 JW3561"
---

# aldB

`protein.P37685`

## Static

- Type: `protein`
- Source: `UniProt:P37685`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the NADP(+)-dependent oxidation of diverse aldehydes to their corresponding carboxylic acids, with a preference for acetaldehyde and chloroacetaldehyde (PubMed:15659684). May play a role in detoxifying aldehydes present during stationary phase (Probable). Cannot use NAD(+) instead of NADP(+) as the electron acceptor. To a lesser extent is also able to oxidize propionaldehyde (propanal), benzaldehyde, mafosfamide, and 4-hydroperoxycyclophosphamide. Does not use either glyceraldehyde or glycolaldehyde as substrates (PubMed:15659684). {ECO:0000269|PubMed:15659684, ECO:0000305|PubMed:7768815}.

## Biological Role

Component of aldehyde dehydrogenase B (complex.ecocyc.CPLX0-3482).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Catalyzes the NADP(+)-dependent oxidation of diverse aldehydes to their corresponding carboxylic acids, with a preference for acetaldehyde and chloroacetaldehyde (PubMed:15659684). May play a role in detoxifying aldehydes present during stationary phase (Probable). Cannot use NAD(+) instead of NADP(+) as the electron acceptor. To a lesser extent is also able to oxidize propionaldehyde (propanal), benzaldehyde, mafosfamide, and 4-hydroperoxycyclophosphamide. Does not use either glyceraldehyde or glycolaldehyde as substrates (PubMed:15659684). {ECO:0000269|PubMed:15659684, ECO:0000305|PubMed:7768815}.

## Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3482|complex.ecocyc.CPLX0-3482]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b3588|gene.b3588]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37685`
- `KEGG:ecj:JW3561;eco:b3588;ecoc:C3026_19455;`
- `GeneID:948104;`
- `GO:GO:0004029; GO:0006974; GO:0016491; GO:0045471; GO:0140088`
- `EC:1.2.1.4`

## Notes

Aldehyde dehydrogenase B (EC 1.2.1.4) (Acetaldehyde dehydrogenase)
