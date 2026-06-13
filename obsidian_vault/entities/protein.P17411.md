---
entity_id: "protein.P17411"
entity_type: "protein"
name: "chbF"
source_database: "UniProt"
source_id: "P17411"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "chbF celF ydjD b1734 JW1723"
---

# chbF

`protein.P17411`

## Static

- Type: `protein`
- Source: `UniProt:P17411`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Hydrolyzes a wide variety of P-beta-glucosides including cellobiose-6P, salicin-6P, arbutin-6P, gentiobiose-6P, methyl-beta-glucoside-6P and p-nitrophenyl-beta-D-glucopyranoside-6P. Is also able to hydrolyze phospho-N,N'-diacetylchitobiose. {ECO:0000269|PubMed:10572139, ECO:0000269|PubMed:10913117}. ChbF is a monoacetylchitobiose-6-phosphate hydrolase encoded as part of the chb operon, which encodes enzymes involved in growth on CHITOBIOSE as the sole source of carbon and energy . ChbF belongs to family 4 of the glycosylhydrolase superfamily . ChbF hdrolyzes the reaction product of ChbG to glucosamine-6-phosphate and N-acetylglucosamine and also cleaves diacetylchitotriose-phosphate to diacetyl-chitobiose and glucosamine-6-phosphate. ChbF is unable to utilize diacetylchitobiose-phosphate, the product of the ChbBCA PTS transporter . Substrate specificity of the enzyme was investigated by ; unfortunately, chitobiose derivatives were not among the tested substrates. A ΔchbF strain is unable to grow on diacetylchitobiose as the sole source of carbon and energy . ChbF: "N,N'-diacetylchitobiose F"

## Biological Role

Catalyzes 6-phospho-beta-D-glucosyl-(1->4)-D-glucose 6-phosphoglucohydrolase (reaction.R00839). Component of monoacetylchitobiose-6-phosphate hydrolase (complex.ecocyc.CPLX0-7979).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00500` Starch and sucrose metabolism (KEGG)

## Annotation

FUNCTION: Hydrolyzes a wide variety of P-beta-glucosides including cellobiose-6P, salicin-6P, arbutin-6P, gentiobiose-6P, methyl-beta-glucoside-6P and p-nitrophenyl-beta-D-glucopyranoside-6P. Is also able to hydrolyze phospho-N,N'-diacetylchitobiose. {ECO:0000269|PubMed:10572139, ECO:0000269|PubMed:10913117}.

## Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00500` Starch and sucrose metabolism (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00839|reaction.R00839]] `KEGG` `database` - via EC:3.2.1.86
- `is_component_of` --> [[complex.ecocyc.CPLX0-7979|complex.ecocyc.CPLX0-7979]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b1734|gene.b1734]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P17411`
- `KEGG:ecj:JW1723;eco:b1734;ecoc:C3026_09910;`
- `GeneID:946266;`
- `GO:GO:0005829; GO:0005975; GO:0008706; GO:0016616; GO:0042802; GO:0046872; GO:0052777`
- `EC:3.2.1.86`

## Notes

6-phospho-beta-glucosidase (EC 3.2.1.86) (Cellobiose-6-phosphate hydrolase) (Phospho-chitobiase)
