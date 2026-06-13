---
entity_id: "protein.P80645"
entity_type: "protein"
name: "ssuD"
source_database: "UniProt"
source_id: "P80645"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ssuD ycbN b0935 JW0918"
---

# ssuD

`protein.P80645`

## Static

- Type: `protein`
- Source: `UniProt:P80645`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Involved in desulfonation of aliphatic sulfonates. Catalyzes the conversion of pentanesulfonate to sulfite and pentaldehyde and is able to desulfonate a wide range of sulfonated substrates including C-2 to C-10 unsubstituted linear alkanesulfonates, substituted ethanesulfonic acids and sulfonated buffers. {ECO:0000269|PubMed:10480865}. E. coli can utilize alkanesulfonates as a sulfur source for growth. The ssuD gene encodes an FMNH2-dependent alkanesulfonate monooxygenase with a broad substrate range. It was reported that the enzyme is able to desulfonate C-2 to C-10 unsubstituted alkanesulfonates, substituted ethanesulfonic acids, N-phenyltaurine, 4-phenyl-1-butanesulfonate and certain sulfonated buffers. The best substrates for the monooxygenase were CPD0-2546, CPD0-2547 and CPD0-1957 . High expression levels of ssuD and a relatively longer lag period appear to be required for the utilization of short-carbon-chain sulfonates, taurine, methanesulfonate and L-cysteate, in tauD cynN double mutants; however whether SsuD directly cleaves taurine is not known. Subsequent experimentation found that the sulfate-starvation status of the cells and uptake of extracellular sulfate may play a role in repressing the induction of utilizing sulfur sources from alkanesulfonates...

## Biological Role

Component of FMNH2-dependent alkanesulfonate monooxygenase (complex.ecocyc.CPLX0-225).

## Enriched Pathways

- `eco00920` Sulfur metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Involved in desulfonation of aliphatic sulfonates. Catalyzes the conversion of pentanesulfonate to sulfite and pentaldehyde and is able to desulfonate a wide range of sulfonated substrates including C-2 to C-10 unsubstituted linear alkanesulfonates, substituted ethanesulfonic acids and sulfonated buffers. {ECO:0000269|PubMed:10480865}.

## Pathways

- `eco00920` Sulfur metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-225|complex.ecocyc.CPLX0-225]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b0935|gene.b0935]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P80645`
- `KEGG:ecj:JW0918;eco:b0935;ecoc:C3026_05740;`
- `GeneID:945557;`
- `GO:GO:0008726; GO:0009408; GO:0010438; GO:0042802; GO:0046306; GO:0051289; GO:1990201`
- `EC:1.14.14.5`

## Notes

Alkanesulfonate monooxygenase (EC 1.14.14.5) (FMNH2-dependent aliphatic sulfonate monooxygenase) (Sulfate starvation-induced protein 6) (SSI6)
