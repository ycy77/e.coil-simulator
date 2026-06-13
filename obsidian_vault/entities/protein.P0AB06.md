---
entity_id: "protein.P0AB06"
entity_type: "protein"
name: "mepK"
source_database: "UniProt"
source_id: "P0AB06"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mepK ycbK b0926 JW0909"
---

# mepK

`protein.P0AB06`

## Static

- Type: `protein`
- Source: `UniProt:P0AB06`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: L,D-endopeptidase that cleaves meso-diaminopimelic acid (mDAP)-mDAP cross-links in peptidoglycan (PubMed:30940749). It works in conjunction with other elongation-specific D,D-endopeptidases to make space for efficient incorporation of nascent peptidoglycan strands into the sacculus and thus enable cell wall expansion (PubMed:30940749). In vitro, is able to cleave the mDAP cross-links of soluble muropeptides and of intact peptidoglycan sacculi (PubMed:30940749). Shows a weak D,D-endopeptidase activity (PubMed:30940749). {ECO:0000269|PubMed:30940749}. MepK is an L,D-endopeptidase which cleaves the cross-bridges between meso-diaminopimelic acid residues (mDAP-mDAP or 3→3 cross-links) in peptidoglycan. Peptidoglycan isolated from a ΔmepK strain contains an increased percentage of soluble muropeptides containing mDAP-mDAP linkages compared to wild type; purified MepK cleaves 'tri-tetra' muropeptides (ie. peptidoglycan dimers containing an mDAP3-mDAP3 crosslink) to produce tripeptide and tetrapeptide disaccharides...

## Biological Role

Catalyzes RXN0-5407 (reaction.ecocyc.RXN0-5407).

## Annotation

FUNCTION: L,D-endopeptidase that cleaves meso-diaminopimelic acid (mDAP)-mDAP cross-links in peptidoglycan (PubMed:30940749). It works in conjunction with other elongation-specific D,D-endopeptidases to make space for efficient incorporation of nascent peptidoglycan strands into the sacculus and thus enable cell wall expansion (PubMed:30940749). In vitro, is able to cleave the mDAP cross-links of soluble muropeptides and of intact peptidoglycan sacculi (PubMed:30940749). Shows a weak D,D-endopeptidase activity (PubMed:30940749). {ECO:0000269|PubMed:30940749}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5407|reaction.ecocyc.RXN0-5407]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0926|gene.b0926]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AB06`
- `KEGG:ecj:JW0909;eco:b0926;ecoc:C3026_05690;`
- `GeneID:93776488;945538;`
- `GO:GO:0004175; GO:0006508; GO:0008237; GO:0009254; GO:0030288; GO:0046872; GO:0071555`
- `EC:3.4.-.-`

## Notes

Peptidoglycan L,D-endopeptidase MepK (EC 3.4.-.-) (Murein endopeptidase K)
