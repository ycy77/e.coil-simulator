---
entity_id: "protein.P0AD70"
entity_type: "protein"
name: "ampH"
source_database: "UniProt"
source_id: "P0AD70"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:22001512}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ampH yaiH b0376 JW5052"
---

# ampH

`protein.P0AD70`

## Static

- Type: `protein`
- Source: `UniProt:P0AD70`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:22001512}.

## Enriched Summary

FUNCTION: Hydrolyzes the cross-linked dimers tetrapentapeptide (D45) and tetratetrapeptide (D44). Removes the terminal D-alanine from muropeptides and disaccharide pentapeptide M5 with a C-terminal D-Ala-D-Ala dipeptide. Associated with recycling and remodeling of peptidoglycan (PG). Also displays a low beta-lactamase activity. {ECO:0000269|PubMed:22001512}. AmpH is a penicillin-binding protein that catalyzes both DD-carboxypeptidase and DD-endopeptidase activities . AmpH is a bifunctional class C penicillin-binding protein with a probable role in peptidoglycan remodelling and/or recycling. AmpH binds a range of β-lactams, including penicillin G . Though AmpH is similar to class C β-lactamases, it has no detectable β-lactamase activity . AmpH may influence or contain a weak DD-carboxypeptidase activity . Purified AmpH cleaves the DD peptide bridge in cross-linked muropeptides in vitro . Purified AmpH removes the D-alanine from muropeptides with a C-terminal D-alanyl-D-alanine dipeptide . Purified AmpH binds Bocillin . AmpH has a 23-residue amino-terminal signal sequence which is cleaved in the mature protein . AmpH is membrane-associated . Loss of AmpH function has no effect on its own, but can lead to morphological defects in a strain lacking at least two other major penicillin-binding proteins .

## Biological Role

Catalyzes RXN-16649 (reaction.ecocyc.RXN-16649), RXN0-3461 (reaction.ecocyc.RXN0-3461).

## Annotation

FUNCTION: Hydrolyzes the cross-linked dimers tetrapentapeptide (D45) and tetratetrapeptide (D44). Removes the terminal D-alanine from muropeptides and disaccharide pentapeptide M5 with a C-terminal D-Ala-D-Ala dipeptide. Associated with recycling and remodeling of peptidoglycan (PG). Also displays a low beta-lactamase activity. {ECO:0000269|PubMed:22001512}.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN-16649|reaction.ecocyc.RXN-16649]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-3461|reaction.ecocyc.RXN0-3461]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0376|gene.b0376]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AD70`
- `KEGG:ecj:JW5052;eco:b0376;`
- `GeneID:93777086;946904;`
- `GO:GO:0004175; GO:0004180; GO:0005886; GO:0006508; GO:0008360; GO:0008658; GO:0009253; GO:0071555`
- `EC:3.4.-.-`

## Notes

D-alanyl-D-alanine-carboxypeptidase/endopeptidase AmpH (EC 3.4.-.-) (DD-alanine-endopeptidase) (DD-carboxypeptidase) (Penicillin-binding protein AmpH)
