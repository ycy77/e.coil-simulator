---
entity_id: "protein.P76342"
entity_type: "protein"
name: "msrP"
source_database: "UniProt"
source_id: "P76342"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:16042411}. Note=Attached to the inner membrane when interacting with the MsrQ subunit."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "msrP yedY b1971 JW1954"
---

# msrP

`protein.P76342`

## Static

- Type: `protein`
- Source: `UniProt:P76342`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:16042411}. Note=Attached to the inner membrane when interacting with the MsrQ subunit.

## Enriched Summary

FUNCTION: Part of the MsrPQ system that repairs oxidized periplasmic proteins containing methionine sulfoxide residues (Met-O), using respiratory chain electrons (PubMed:26641313). Thus protects these proteins from oxidative-stress damage caused by reactive species of oxygen and chlorine (PubMed:26641313). MsrPQ is essential for the maintenance of envelope integrity under bleach stress, rescuing a wide series of structurally unrelated periplasmic proteins from methionine oxidation, including the primary periplasmic chaperone SurA and the lipoprotein Pal (PubMed:26641313). The catalytic subunit MsrP is non-stereospecific, being able to reduce both (R-) and (S-) diastereoisomers of methionine sulfoxide (PubMed:26641313). Can catalyze the reduction of a variety of substrates in vitro, including dimethyl sulfoxide, trimethylamine N-oxide, phenylmethyl sulfoxide and L-methionine sulfoxide (PubMed:15355966, PubMed:30945846). Cannot reduce cyclic N-oxides (PubMed:15355966). Shows no activity as sulfite oxidase (PubMed:15355966). {ECO:0000269|PubMed:15355966, ECO:0000269|PubMed:26641313, ECO:0000269|PubMed:30945846}. MsrP (formerly YedY) is a periplasmic methionine sulfoxide reductase; MsrP and MsrQ, an inner membrane, heme-binding, quinol dehydrogenase, function together to protect periplasmic proteins from oxidative damage in vivo...

## Biological Role

Component of periplasmic protein-L-methionine sulfoxide reducing system (complex.ecocyc.CPLX0-8213).

## Annotation

FUNCTION: Part of the MsrPQ system that repairs oxidized periplasmic proteins containing methionine sulfoxide residues (Met-O), using respiratory chain electrons (PubMed:26641313). Thus protects these proteins from oxidative-stress damage caused by reactive species of oxygen and chlorine (PubMed:26641313). MsrPQ is essential for the maintenance of envelope integrity under bleach stress, rescuing a wide series of structurally unrelated periplasmic proteins from methionine oxidation, including the primary periplasmic chaperone SurA and the lipoprotein Pal (PubMed:26641313). The catalytic subunit MsrP is non-stereospecific, being able to reduce both (R-) and (S-) diastereoisomers of methionine sulfoxide (PubMed:26641313). Can catalyze the reduction of a variety of substrates in vitro, including dimethyl sulfoxide, trimethylamine N-oxide, phenylmethyl sulfoxide and L-methionine sulfoxide (PubMed:15355966, PubMed:30945846). Cannot reduce cyclic N-oxides (PubMed:15355966). Shows no activity as sulfite oxidase (PubMed:15355966). {ECO:0000269|PubMed:15355966, ECO:0000269|PubMed:26641313, ECO:0000269|PubMed:30945846}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8213|complex.ecocyc.CPLX0-8213]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1971|gene.b1971]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76342`
- `KEGG:ecj:JW1954;eco:b1971;`
- `GeneID:946484;`
- `GO:GO:0016491; GO:0016672; GO:0016675; GO:0030091; GO:0030288; GO:0043546; GO:0046872; GO:1901530`
- `EC:1.8.5.-`

## Notes

Protein-methionine-sulfoxide reductase catalytic subunit MsrP (EC 1.8.5.-)
