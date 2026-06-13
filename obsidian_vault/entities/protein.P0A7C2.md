---
entity_id: "protein.P0A7C2"
entity_type: "protein"
name: "lexA"
source_database: "UniProt"
source_id: "P0A7C2"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "lexA exrA spr tsl umuA b4043 JW4003"
---

# lexA

`protein.P0A7C2`

## Static

- Type: `protein`
- Source: `UniProt:P0A7C2`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Represses a number of genes involved in the response to DNA damage (SOS response), including recA and lexA. Binds to the 16 bp palindromic sequence 5'-CTGTATATATATACAG-3'. In the presence of single-stranded DNA, RecA interacts with LexA causing an autocatalytic cleavage which disrupts the DNA-binding part of LexA, leading to derepression of the SOS regulon and eventually DNA repair. Implicated in hydroxy radical-mediated cell death induced by hydroxyurea treatment (PubMed:20005847). The SOS response controls an apoptotic-like death (ALD) induced (in the absence of the mazE-mazF toxin-antitoxin module) in response to DNA damaging agents that is mediated by RecA and LexA (PubMed:22412352). Genetic interactions among priB, dam, lexA, nagC, polA, rdgB, rdgB, rep and uup link the PriA-PriB replication restart pathway to DNA double-strand break repair (PubMed:36326440). {ECO:0000255|HAMAP-Rule:MF_00015, ECO:0000269|PubMed:20005847, ECO:0000269|PubMed:22412352, ECO:0000269|PubMed:36326440, ECO:0000269|PubMed:7027255, ECO:0000269|PubMed:7027256}.

## Biological Role

Component of DNA-binding transcriptional repressor LexA (complex.ecocyc.PC00010).

## Annotation

FUNCTION: Represses a number of genes involved in the response to DNA damage (SOS response), including recA and lexA. Binds to the 16 bp palindromic sequence 5'-CTGTATATATATACAG-3'. In the presence of single-stranded DNA, RecA interacts with LexA causing an autocatalytic cleavage which disrupts the DNA-binding part of LexA, leading to derepression of the SOS regulon and eventually DNA repair. Implicated in hydroxy radical-mediated cell death induced by hydroxyurea treatment (PubMed:20005847). The SOS response controls an apoptotic-like death (ALD) induced (in the absence of the mazE-mazF toxin-antitoxin module) in response to DNA damaging agents that is mediated by RecA and LexA (PubMed:22412352). Genetic interactions among priB, dam, lexA, nagC, polA, rdgB, rdgB, rep and uup link the PriA-PriB replication restart pathway to DNA double-strand break repair (PubMed:36326440). {ECO:0000255|HAMAP-Rule:MF_00015, ECO:0000269|PubMed:20005847, ECO:0000269|PubMed:22412352, ECO:0000269|PubMed:36326440, ECO:0000269|PubMed:7027255, ECO:0000269|PubMed:7027256}.

## Outgoing Edges (24)

- `is_component_of` --> [[complex.ecocyc.PC00010|complex.ecocyc.PC00010]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `represses` --> [[gene.b0060|gene.b0060]] `RegulonDB` `S` - regulator=LexA; target=polB; function=-
- `represses` --> [[gene.b0779|gene.b0779]] `RegulonDB` `C` - regulator=LexA; target=uvrB; function=-
- `represses` --> [[gene.b0799|gene.b0799]] `RegulonDB` `S` - regulator=LexA; target=dinG; function=-
- `represses` --> [[gene.b0800|gene.b0800]] `RegulonDB` `S` - regulator=LexA; target=ybiB; function=-
- `represses` --> [[gene.b0890|gene.b0890]] `RegulonDB` `S` - regulator=LexA; target=ftsK; function=-
- `represses` --> [[gene.b1061|gene.b1061]] `RegulonDB` `C` - regulator=LexA; target=dinI; function=-
- `represses` --> [[gene.b1184|gene.b1184]] `RegulonDB` `S` - regulator=LexA; target=umuC; function=-
- `represses` --> [[gene.b1728|gene.b1728]] `RegulonDB` `S` - regulator=LexA; target=ydjM; function=-
- `represses` --> [[gene.b1808|gene.b1808]] `RegulonDB` `S` - regulator=LexA; target=yoaA; function=-
- `represses` --> [[gene.b1860|gene.b1860]] `RegulonDB` `S` - regulator=LexA; target=ruvB; function=-
- `represses` --> [[gene.b1861|gene.b1861]] `RegulonDB` `S` - regulator=LexA; target=ruvA; function=-
- `represses` --> [[gene.b2616|gene.b2616]] `RegulonDB` `S` - regulator=LexA; target=recN; function=-
- `represses` --> [[gene.b2698|gene.b2698]] `RegulonDB` `S` - regulator=LexA; target=recX; function=-
- `represses` --> [[gene.b2699|gene.b2699]] `RegulonDB` `S` - regulator=LexA; target=recA; function=-
- `represses` --> [[gene.b2819|gene.b2819]] `RegulonDB` `C` - regulator=LexA; target=recD; function=-
- `represses` --> [[gene.b2820|gene.b2820]] `RegulonDB` `C` - regulator=LexA; target=recB; function=-
- `represses` --> [[gene.b2821|gene.b2821]] `RegulonDB` `C` - regulator=LexA; target=ptrA; function=-
- `represses` --> [[gene.b3065|gene.b3065]] `RegulonDB` `S` - regulator=LexA; target=rpsU; function=-
- `represses` --> [[gene.b3066|gene.b3066]] `RegulonDB` `S` - regulator=LexA; target=dnaG; function=-
- `represses` --> [[gene.b3067|gene.b3067]] `RegulonDB` `S` - regulator=LexA; target=rpoD; function=-
- `represses` --> [[gene.b4043|gene.b4043]] `RegulonDB` `C` - regulator=LexA; target=lexA; function=-
- `represses` --> [[gene.b4044|gene.b4044]] `RegulonDB` `C` - regulator=LexA; target=dinF; function=-
- `represses` --> [[gene.b4347|gene.b4347]] `RegulonDB` `S` - regulator=LexA; target=symE; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b4043|gene.b4043]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A7C2`
- `KEGG:ecj:JW4003;eco:b4043;ecoc:C3026_21850;`
- `GeneID:86861555;93777788;948544;`
- `GO:GO:0000976; GO:0001217; GO:0003677; GO:0004252; GO:0005829; GO:0006260; GO:0006281; GO:0006351; GO:0006508; GO:0006974; GO:0009432; GO:0032993; GO:0042802; GO:0043565; GO:0045892`
- `EC:3.4.21.88`

## Notes

LexA repressor (EC 3.4.21.88)
