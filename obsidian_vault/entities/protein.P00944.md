---
entity_id: "protein.P00944"
entity_type: "protein"
name: "xylA"
source_database: "UniProt"
source_id: "P00944"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "xylA b3565 JW3537"
---

# xylA

`protein.P00944`

## Static

- Type: `protein`
- Source: `UniProt:P00944`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

Xylose isomerase (EC 5.3.1.5) (D-xylulose keto-isomerase) Xylose isomerase catalyzes the conversion of D-xylose to D-xylulose, the first reaction in the XYLCAT-PWY pathway . Two conserved histidine residues, H101 and H271, were shown to be essential for catalytic activity . The fluorescence of two conserved tryptophan residues, W49 and W188, is quenched during binding of xylose, and W49 was shown to be essential for catalytic activity . The presence of Mg2+, Mn2+ or Co2+ protects the enzyme from thermal denaturation . Expression of xylose isomerase is induced in the presence of xylose and is under catabolite repression . An amber mutation has been generated . Reviews:

## Biological Role

Catalyzes alpha-D-glucose aldose-ketose-isomerase (reaction.R00307). Component of xylose isomerase (complex.ecocyc.XYLISOM-CPLX).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

Xylose isomerase (EC 5.3.1.5) (D-xylulose keto-isomerase)

## Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00307|reaction.R00307]] `KEGG` `database` - via EC:5.3.1.5
- `is_component_of` --> [[complex.ecocyc.XYLISOM-CPLX|complex.ecocyc.XYLISOM-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3565|gene.b3565]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P00944`
- `KEGG:ecj:JW3537;eco:b3565;ecoc:C3026_19330;`
- `GeneID:948141;`
- `GO:GO:0000287; GO:0005737; GO:0009045; GO:0042803; GO:0042843`
- `EC:5.3.1.5`

## Notes

Xylose isomerase (EC 5.3.1.5) (D-xylulose keto-isomerase)
