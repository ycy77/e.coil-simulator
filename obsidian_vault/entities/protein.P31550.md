---
entity_id: "protein.P31550"
entity_type: "protein"
name: "thiB"
source_database: "UniProt"
source_id: "P31550"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:12182833}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "thiB tbpA yabL b0068 JW0067"
---

# thiB

`protein.P31550`

## Static

- Type: `protein`
- Source: `UniProt:P31550`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:12182833}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex ThiBPQ involved in thiamine import (PubMed:12175925). Binds thiamine, thiamine phosphate and thiamine diphosphate with high affinity (PubMed:12182833, PubMed:18177053). {ECO:0000269|PubMed:12175925, ECO:0000269|PubMed:12182833, ECO:0000269|PubMed:18177053}. thiB encodes the periplasmic, substrate binding protein of an ATP-dependent thiamin uptake system. Purified ThiB binds thiamine and its phosphate esters - thiamine phosphate and thiamine diphosphate . Purified ThiB binds thiamine with a 1:1 stoichiometry and with high affinity; KD = 0.8 µM . The crystal structure of ThiB consists of two domains linked by a flexible hinge region of two crossovers; thiamine phosphate binds in a cleft located between the two domains . Purified ThiB binds thiamine, thiamine phosphate and thiamine diphosphate with high affinity (KD = 3.8 nM, 2.3 nM and 7.4 nM respectively) . A thiamin pyrophosphate (TPP)-sensing riboswitch is located upstream of thiB; TPP sensing by the riboswitch represses gene expression at the translational level and possibly at the transcriptional level; the riboswitch down-regulates translation by a mechanism that sequesters the ribosome binding site .

## Biological Role

Component of thiamine ABC transporter (complex.ecocyc.ABC-32-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex ThiBPQ involved in thiamine import (PubMed:12175925). Binds thiamine, thiamine phosphate and thiamine diphosphate with high affinity (PubMed:12182833, PubMed:18177053). {ECO:0000269|PubMed:12175925, ECO:0000269|PubMed:12182833, ECO:0000269|PubMed:18177053}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-32-CPLX|complex.ecocyc.ABC-32-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b0068|gene.b0068]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P31550`
- `KEGG:ecj:JW0067;eco:b0068;`
- `GeneID:946306;`
- `GO:GO:0015888; GO:0016020; GO:0030288; GO:0030975; GO:0030976; GO:0055052; GO:0071934`

## Notes

Thiamine-binding periplasmic protein
