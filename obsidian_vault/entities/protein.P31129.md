---
entity_id: "protein.P31129"
entity_type: "protein"
name: "dgcZ"
source_database: "UniProt"
source_id: "P31129"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dgcZ ydeG ydeH b1535 JW1528"
---

# dgcZ

`protein.P31129`

## Static

- Type: `protein`
- Source: `UniProt:P31129`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the synthesis of cyclic-di-GMP (c-di-GMP) via the condensation of 2 GTP molecules (PubMed:18713317, PubMed:19460094, PubMed:20582742). May act as a zinc sensor that controls, via c-di-GMP, post-translational events (PubMed:23769666). Overexpression leads to a strong repression of swimming; swimming returnes to normal when residues 206-207 are both mutated to Ala. Overexpression also leads to a reduction in flagellar abundance and a 20-fold increase in c-di-GMP levels in vivo. Required for aminoglycoside-mediated induction of biofilm formation, it also plays a lesser role in biofilm production in response to other classes of translation inhibitors. The c-di-GMP produced by this enzyme up-regulates poly-GlcNAc production as well as the biofilm synthesis protein PgaD, although c-di-GMP is probably not the main inducing principle. C-di-GMP is a second messenger which controls cell surface-associated traits in bacteria (PubMed:19460094). {ECO:0000269|PubMed:19460094, ECO:0000269|PubMed:20582742, ECO:0000269|PubMed:23769666, ECO:0000305|PubMed:18713317}.

## Biological Role

Component of diguanylate cyclase DgcZ (complex.ecocyc.CPLX0-7802).

## Annotation

FUNCTION: Catalyzes the synthesis of cyclic-di-GMP (c-di-GMP) via the condensation of 2 GTP molecules (PubMed:18713317, PubMed:19460094, PubMed:20582742). May act as a zinc sensor that controls, via c-di-GMP, post-translational events (PubMed:23769666). Overexpression leads to a strong repression of swimming; swimming returnes to normal when residues 206-207 are both mutated to Ala. Overexpression also leads to a reduction in flagellar abundance and a 20-fold increase in c-di-GMP levels in vivo. Required for aminoglycoside-mediated induction of biofilm formation, it also plays a lesser role in biofilm production in response to other classes of translation inhibitors. The c-di-GMP produced by this enzyme up-regulates poly-GlcNAc production as well as the biofilm synthesis protein PgaD, although c-di-GMP is probably not the main inducing principle. C-di-GMP is a second messenger which controls cell surface-associated traits in bacteria (PubMed:19460094). {ECO:0000269|PubMed:19460094, ECO:0000269|PubMed:20582742, ECO:0000269|PubMed:23769666, ECO:0000305|PubMed:18713317}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7802|complex.ecocyc.CPLX0-7802]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1535|gene.b1535]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P31129`
- `KEGG:ecj:JW1528;eco:b1535;ecoc:C3026_08870;`
- `GeneID:946075;`
- `GO:GO:0005525; GO:0005886; GO:0008270; GO:0042802; GO:0042803; GO:0043709; GO:0052621; GO:0060187; GO:1900233; GO:1902201; GO:1902209`
- `EC:2.7.7.65`

## Notes

Diguanylate cyclase DgcZ (DGC) (EC 2.7.7.65) (Zinc-sensory diguanylate cyclase)
