---
entity_id: "protein.P75800"
entity_type: "protein"
name: "pdeI"
source_database: "UniProt"
source_id: "P75800"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305|PubMed:39689163}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pdeI yliE b0833 JW0817"
---

# pdeI

`protein.P75800`

## Static

- Type: `protein`
- Source: `UniProt:P75800`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305|PubMed:39689163}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: May act as a diguanylate cyclase (DGC) that catalyzes the synthesis of cyclic di-GMP (c-di-GMP) (PubMed:39689163). Probably functions as a membrane-associated sensor that integrates environmental signals with c-di-GMP production under complex regulatory mechanisms (PubMed:39689163). It increases c-di-GMP levels, promoting persister cell formation (PubMed:39689163). It is involved in biofilm formation, and may be especially crucial in the initial stages of biofilm formation, potentially responding to surface-associated cues to modulate c-di-GMP levels and promote attachment (PubMed:39689163). Overexpression reduces biofilm formation (PubMed:19460094). {ECO:0000269|PubMed:19460094, ECO:0000269|PubMed:39689163}. PdeI was initially predicted to be a c-di-GMP-specific phosphodiesterase but has since been shown to increase c-di-GMP and referred to as a c-di-GMP synthase . Overexpression of pdeI reduces biofilm formation . PdeI is predicted to be an inner membrane protein consisting of two transmembrane domains that flank a predicted periplasmic CHASE (cyclases/histidine kinases associated sensory) domain, followed by a divergent CACHE domain, a HAMP domain, a degenerate GGDEF domain, and a C-terminal EAL domain . A screen for suppressors of the motility defect of a EG12252 ΔpdeH mutant identified activating mutations in E...

## Biological Role

Catalyzes cyclic bis(3->5')diguanylate 3-guanylylhydrolase (reaction.R08991).

## Annotation

FUNCTION: May act as a diguanylate cyclase (DGC) that catalyzes the synthesis of cyclic di-GMP (c-di-GMP) (PubMed:39689163). Probably functions as a membrane-associated sensor that integrates environmental signals with c-di-GMP production under complex regulatory mechanisms (PubMed:39689163). It increases c-di-GMP levels, promoting persister cell formation (PubMed:39689163). It is involved in biofilm formation, and may be especially crucial in the initial stages of biofilm formation, potentially responding to surface-associated cues to modulate c-di-GMP levels and promote attachment (PubMed:39689163). Overexpression reduces biofilm formation (PubMed:19460094). {ECO:0000269|PubMed:19460094, ECO:0000269|PubMed:39689163}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.R08991|reaction.R08991]] `KEGG` `database` - via EC:3.1.4.52

## Incoming Edges (1)

- `encodes` <-- [[gene.b0833|gene.b0833]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P75800`
- `KEGG:ecj:JW0817;eco:b0833;ecoc:C3026_05220;`
- `GeneID:945462;`
- `GO:GO:0005886; GO:0061940; GO:0071111; GO:1900190`
- `EC:2.7.7.65`

## Notes

Probable cyclic di-GMP synthase PdeI (EC 2.7.7.65) (c-di-GMP synthetase) (c-di-GMP-specific phosphodiesterase)
