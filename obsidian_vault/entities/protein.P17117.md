---
entity_id: "protein.P17117"
entity_type: "protein"
name: "nfsA"
source_database: "UniProt"
source_id: "P17117"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nfsA mda18 mdaA ybjB b0851 JW0835"
---

# nfsA

`protein.P17117`

## Static

- Type: `protein`
- Source: `UniProt:P17117`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the reduction of nitroaromatic compounds using NADPH. Has a broad electron acceptor specificity. Reduces nitrofurazone by a ping-pong bi-bi mechanism possibly to generate a two-electron transfer product. Major oxygen-insensitive nitroreductase in E.coli. {ECO:0000269|PubMed:8755878}. The nfsA-encoded nitroreductase is the major oxygen-insensitive nitroreductase present in E. coli. NfsA uses only NADPH and has broad electron acceptor specificity . The physiologically relevant substrates may be quinones . Nitroreductases can be used as prodrug activators in cancer therapy . NfsA catalyzes the reduction of nitrocompounds using a ping-pong Bi-Bi mechanism, transferring two electrons . The mechanism for two-electron reduction of quinones is most consistent with a single-step hydride transfer . Turnover of the enzyme is limited by the oxidative half-reaction . The reduction of nitrocompounds to hydroxylamines occurs via a nitroso intermediate; ascorbate inhibition patterns suggest that the reduction of the nitroso intermediate occurs directly by NADPH rather than enzymatically . The R203 residue plays a key role in binding the NADPH substrate , and F42 is important for activity . A single amino acid substitution, E99G, transforms NfsA into an active flavin reductase...

## Biological Role

Component of NADPH-dependent nitroreductase / NADPH-dependent quinone reductase (complex.ecocyc.CPLX0-244).

## Enriched Pathways

- `eco00633` Nitrotoluene degradation (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Catalyzes the reduction of nitroaromatic compounds using NADPH. Has a broad electron acceptor specificity. Reduces nitrofurazone by a ping-pong bi-bi mechanism possibly to generate a two-electron transfer product. Major oxygen-insensitive nitroreductase in E.coli. {ECO:0000269|PubMed:8755878}.

## Pathways

- `eco00633` Nitrotoluene degradation (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-244|complex.ecocyc.CPLX0-244]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0851|gene.b0851]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P17117`
- `KEGG:ecj:JW0835;eco:b0851;ecoc:C3026_05310;`
- `GeneID:945483;`
- `GO:GO:0003955; GO:0005829; GO:0010181; GO:0042803`
- `EC:1.-.-.-`

## Notes

Oxygen-insensitive NADPH nitroreductase (EC 1.-.-.-) (Modulator of drug activity A)
