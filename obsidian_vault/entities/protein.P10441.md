---
entity_id: "protein.P10441"
entity_type: "protein"
name: "lpxB"
source_database: "UniProt"
source_id: "P10441"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "lpxB pgsB b0182 JW0177"
---

# lpxB

`protein.P10441`

## Static

- Type: `protein`
- Source: `UniProt:P10441`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Condensation of UDP-2,3-diacylglucosamine and 2,3-diacylglucosamine-1-phosphate to form lipid A disaccharide, a precursor of lipid A, a phosphorylated glycolipid that anchors the lipopolysaccharide to the outer membrane of the cell.

## Biological Role

Component of lipid A disaccharide synthase (complex.ecocyc.CPLX0-7415).

## Enriched Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Condensation of UDP-2,3-diacylglucosamine and 2,3-diacylglucosamine-1-phosphate to form lipid A disaccharide, a precursor of lipid A, a phosphorylated glycolipid that anchors the lipopolysaccharide to the outer membrane of the cell.

## Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7415|complex.ecocyc.CPLX0-7415]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0182|gene.b0182]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P10441`
- `KEGG:ecj:JW0177;eco:b0182;ecoc:C3026_00835;`
- `GeneID:93777243;944838;`
- `GO:GO:0005543; GO:0005737; GO:0008915; GO:0009245; GO:0019897; GO:0031234; GO:0042802`
- `EC:2.4.1.182`

## Notes

Lipid-A-disaccharide synthase (EC 2.4.1.182)
