---
entity_id: "protein.P30140"
entity_type: "protein"
name: "thiH"
source_database: "UniProt"
source_id: "P30140"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "thiH b3990 JW3953"
---

# thiH

`protein.P30140`

## Static

- Type: `protein`
- Source: `UniProt:P30140`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the radical-mediated cleavage of tyrosine to 2-iminoacetate and 4-cresol. {ECO:0000269|PubMed:17403671, ECO:0000269|PubMed:17969213}. 2-Iminoacetate synthase (tyrosine lyase, ThiH) participates in the synthesis of the thiazole moiety of thiamine . ThiH cleaves the Cα-Cβ bond of TYR, forming CPD-12279 (dehydroglycine) and generating CPD-108 (p-cresol) as a by-product. 2-iminoacetate is one of the three substrates required for the thiazole cyclization reaction catalyzed by ThiG . ThiH is a radical SAM enzyme that utilizes a [4Fe-4S] cluster to reductively cleave S-ADENOSYLMETHIONINE to yield methionine and a 5'-deoxyadenosyl radical. The radical abstracts a phenolic hydrogen atom from TYR, which then undergoes Cα-Cβ bond cleavage . ThiG and ThiH purify in a large multimeric complex . Because CPD-12279 is unstable and undergoes hydrolysis to glyoxylate and ammonium, complex formation between ThiG and ThiH may ensure that it is passed directly to ThiG, where it is incorporated into the thiazole carboxylate . Growth of a thiH mutant requires the presence of thiazole or thiamine . Reviews:

## Biological Role

Catalyzes L-tyrosine 4-methylphenol-lyase (2-iminoacetate-forming) (reaction.R10246), RXN-11319 (reaction.ecocyc.RXN-11319). Component of thiazole synthase (complex.ecocyc.CPLX0-3949). Bound by a [4Fe-4S] iron-sulfur cluster (molecule.ecocyc.CPD-7).

## Enriched Pathways

- `eco00730` Thiamine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Catalyzes the radical-mediated cleavage of tyrosine to 2-iminoacetate and 4-cresol. {ECO:0000269|PubMed:17403671, ECO:0000269|PubMed:17969213}.

## Pathways

- `eco00730` Thiamine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R10246|reaction.R10246]] `KEGG` `database` - via EC:4.1.99.19
- `catalyzes` --> [[reaction.ecocyc.RXN-11319|reaction.ecocyc.RXN-11319]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_component_of` --> [[complex.ecocyc.CPLX0-3949|complex.ecocyc.CPLX0-3949]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## Incoming Edges (2)

- `binds` <-- [[molecule.ecocyc.CPD-7|molecule.ecocyc.CPD-7]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b3990|gene.b3990]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P30140`
- `KEGG:ecj:JW3953;eco:b3990;ecoc:C3026_21550;`
- `GeneID:948494;`
- `GO:GO:0005506; GO:0006974; GO:0009228; GO:0009229; GO:0036355; GO:0051539; GO:1902508`
- `EC:4.1.99.19`

## Notes

2-iminoacetate synthase (EC 4.1.99.19) (Dehydroglycine synthase) (Tyrosine lyase)
