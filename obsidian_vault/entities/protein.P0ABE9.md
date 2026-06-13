---
entity_id: "protein.P0ABE9"
entity_type: "protein"
name: "cynT"
source_database: "UniProt"
source_id: "P0ABE9"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "cynT b0339 JW0330"
---

# cynT

`protein.P0ABE9`

## Static

- Type: `protein`
- Source: `UniProt:P0ABE9`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Reversible hydration of carbon dioxide. Carbon dioxide formed in the bicarbonate-dependent decomposition of cyanate by cyanase (CynS) diffuses out of the cell faster than it would be hydrated to bicarbonate, so the apparent function of this enzyme is to catalyze the hydration of carbon dioxide and thus prevent depletion of cellular bicarbonate. {ECO:0000269|PubMed:1740425}. E. coli encodes two carbonic anhydrases, CynT (carbonic anhydrase 1) and Can (CPLX0-7521). The enzymes belong to Clade A and Clade B of the β class of carbonic anhydrases, respectively . cynT is encoded in an operon with EG10175, the gene encoding CYANLY-CPLX, and its expression is inducible by cyanate . The biological role of the CynT carbonic anhydrase is to prevent the depletion of endogenous bicarbonate due to rapid loss of CO2, the product of the cyanase-catalyzed reaction, by diffusion out of the cell . The enzyme behaves as an oligomer of two or four subunits, depending on the presence of bicarbonate . Inhibition of CynT activity by CPD0-1626 has been investigated . At atmospheric concentrations of CO2, a cynT mutant is more sensitive to cyanate than a cynS mutant and can not utilize cyanate as the sole source of nitrogen, although it produces active cyanase. However, at a high pCO2 of 3%, it behaves like the wild type...

## Biological Role

Catalyzes carbonate hydro-lyase (carbon-dioxide-forming); (reaction.R00132). Component of carbonic anhydrase 1 (complex.ecocyc.CARBODEHYDRAT-CPLX).

## Enriched Pathways

- `eco00910` Nitrogen metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Reversible hydration of carbon dioxide. Carbon dioxide formed in the bicarbonate-dependent decomposition of cyanate by cyanase (CynS) diffuses out of the cell faster than it would be hydrated to bicarbonate, so the apparent function of this enzyme is to catalyze the hydration of carbon dioxide and thus prevent depletion of cellular bicarbonate. {ECO:0000269|PubMed:1740425}.

## Pathways

- `eco00910` Nitrogen metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00132|reaction.R00132]] `KEGG` `database` - via EC:4.2.1.1
- `is_component_of` --> [[complex.ecocyc.CARBODEHYDRAT-CPLX|complex.ecocyc.CARBODEHYDRAT-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0339|gene.b0339]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ABE9`
- `KEGG:ecj:JW0330;eco:b0339;ecoc:C3026_01660;ecoc:C3026_24830;`
- `GeneID:75202502;946548;`
- `GO:GO:0004089; GO:0005737; GO:0008270; GO:0009440; GO:0015976; GO:0042802`
- `EC:4.2.1.1`

## Notes

Carbonic anhydrase 1 (EC 4.2.1.1) (Carbonate dehydratase 1)
