---
entity_id: "protein.P37025"
entity_type: "protein"
name: "thpR"
source_database: "UniProt"
source_id: "P37025"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "thpR ligT yadP b0147 JW5011"
---

# thpR

`protein.P37025`

## Static

- Type: `protein`
- Source: `UniProt:P37025`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Hydrolyzes RNA 2',3'-cyclic phosphodiester to an RNA 2'-phosphomonoester (PubMed:25239919). In vitro, can also ligate 5' and 3' half-tRNA molecules with 2',3'-cyclic phosphate and 5'-hydroxyl termini, respectively, to the product containing the 2'-5' phosphodiester linkage. This reaction does not require ATP and is reversible (PubMed:6347395, PubMed:8940112). {ECO:0000269|PubMed:25239919, ECO:0000269|PubMed:6347395, ECO:0000269|PubMed:8940112}. ThpR belongs to the family of two-histidine (2H) phosphoesterase enzymes and has been shown to be an "end healing" cyclic phosphodiesterase (CPDase) that hydrolyzes RNA 2',3'-cyclic phosphodiesters . Biophysical characterization of ThpR and comparison to two other cyclic nucleotide phosphodiesterases from yeast and Arabidopsis has been reported. ThpR appears to exist as a monomer in solution . A crystal structure of ThpR in complex with 2'-AMP has been solved at 2 Å resolution, implicating His43 as a general acid catalyst and His125 as a general base catalyst. Arg130 may have a role in stabilizing the transition state. Site-directed mutagenesis of these amino acids confirmed their importance for catalytic activity . ThpR was initially identified as a "2'-5' RNA ligase" that catalyzes the ligation and cleavage of 2'-5' linkages in RNA, a reversible transesterification reaction, in vitro...

## Biological Role

Catalyzes RXN-15952 (reaction.ecocyc.RXN-15952), RXN0-5062 (reaction.ecocyc.RXN0-5062).

## Annotation

FUNCTION: Hydrolyzes RNA 2',3'-cyclic phosphodiester to an RNA 2'-phosphomonoester (PubMed:25239919). In vitro, can also ligate 5' and 3' half-tRNA molecules with 2',3'-cyclic phosphate and 5'-hydroxyl termini, respectively, to the product containing the 2'-5' phosphodiester linkage. This reaction does not require ATP and is reversible (PubMed:6347395, PubMed:8940112). {ECO:0000269|PubMed:25239919, ECO:0000269|PubMed:6347395, ECO:0000269|PubMed:8940112}.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN-15952|reaction.ecocyc.RXN-15952]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-5062|reaction.ecocyc.RXN0-5062]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0147|gene.b0147]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37025`
- `KEGG:ecj:JW5011;eco:b0147;ecoc:C3026_00640;`
- `GeneID:93777280;944848;`
- `GO:GO:0004113; GO:0008664`
- `EC:3.1.4.58`

## Notes

RNA 2',3'-cyclic phosphodiesterase (RNA 2',3'-CPDase) (EC 3.1.4.58) (Two-histidine 2',3'-cyclic phosphodiesterase acting on RNA)
