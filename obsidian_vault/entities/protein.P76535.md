---
entity_id: "protein.P76535"
entity_type: "protein"
name: "murQ"
source_database: "UniProt"
source_id: "P76535"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "murQ yfeU b2428 JW2421"
---

# murQ

`protein.P76535`

## Static

- Type: `protein`
- Source: `UniProt:P76535`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Specifically catalyzes the cleavage of the D-lactyl ether substituent of MurNAc 6-phosphate, producing GlcNAc 6-phosphate and D-lactate. Is required for growth on MurNAc as the sole source of carbon and energy. Together with AnmK, is also required for the utilization of anhydro-N-acetylmuramic acid (anhMurNAc) either imported from the medium or derived from its own cell wall murein, and thus plays a role in cell wall recycling. {ECO:0000269|PubMed:15983044, ECO:0000269|PubMed:16452451}. MurQ catalyzes the cleavage of the lactyl ether moiety of N-acetylmuramic acid 6-phosphate (MurNAc-6-P), acting in one of the pathways that recycle murein components . MurQ is the only MurNAc-6-P etherase in E. coli . A reaction mechanism involving β-elimination/hydration has been proposed . Further studies support a mechanism involving syn elimination of lactate followed by syn addition of water. Structural modelling and site-directed mutagenesis implicated the Glu83 and Glu114 residues in catalysis and suggested that Glu83 is required for protonation of the departing lactate . A murQ null mutant strain that is non-polar on murP can not grow on N-acetylmuramic acid as the sole source of carbon and energy. When grown on other carbon sources, a murQ null mutant accumulates MurNAc 6-phosphate . Review:

## Biological Role

Component of N-acetylmuramic acid 6-phosphate etherase (complex.ecocyc.CPLX0-7732).

## Enriched Pathways

- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Specifically catalyzes the cleavage of the D-lactyl ether substituent of MurNAc 6-phosphate, producing GlcNAc 6-phosphate and D-lactate. Is required for growth on MurNAc as the sole source of carbon and energy. Together with AnmK, is also required for the utilization of anhydro-N-acetylmuramic acid (anhMurNAc) either imported from the medium or derived from its own cell wall murein, and thus plays a role in cell wall recycling. {ECO:0000269|PubMed:15983044, ECO:0000269|PubMed:16452451}.

## Pathways

- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7732|complex.ecocyc.CPLX0-7732]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2428|gene.b2428]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76535`
- `KEGG:ecj:JW2421;eco:b2428;ecoc:C3026_13490;`
- `GeneID:946893;`
- `GO:GO:0009254; GO:0016803; GO:0016835; GO:0046348; GO:0097173; GO:0097175; GO:0097367`
- `EC:4.2.1.126`

## Notes

N-acetylmuramic acid 6-phosphate etherase (MurNAc-6-P etherase) (EC 4.2.1.126) (N-acetylmuramic acid 6-phosphate hydrolase) (N-acetylmuramic acid 6-phosphate lyase)
