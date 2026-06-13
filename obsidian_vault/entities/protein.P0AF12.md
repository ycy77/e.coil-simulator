---
entity_id: "protein.P0AF12"
entity_type: "protein"
name: "mtnN"
source_database: "UniProt"
source_id: "P0AF12"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mtnN mtn pfs yadA b0159 JW0155"
---

# mtnN

`protein.P0AF12`

## Static

- Type: `protein`
- Source: `UniProt:P0AF12`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the irreversible cleavage of the glycosidic bond in both 5'-methylthioadenosine (MTA) and S-adenosylhomocysteine (SAH/AdoHcy) to adenine and the corresponding thioribose, 5'-methylthioribose and S-ribosylhomocysteine, respectively (PubMed:16101288, PubMed:3911944). Also cleaves 5'-deoxyadenosine, a toxic by-product of radical S-adenosylmethionine (SAM) enzymes, into 5-deoxyribose and adenine. Thus, is required for in vivo function of the radical SAM enzymes biotin synthase and lipoic acid synthase, that are inhibited by 5'-deoxyadenosine accumulation (PubMed:15911379). Can also use 5'-isobutylthioadenosine, 5'-n-butylthioadenosine, S-adenosyl-D-homocysteine, decarboxylated adenosylhomocysteine, deaminated adenosylhomocysteine and S-2-aza-adenosylhomocysteine as substrates in vitro (PubMed:3911944). {ECO:0000269|PubMed:15911379, ECO:0000269|PubMed:16101288, ECO:0000269|PubMed:3911944}.

## Biological Role

Catalyzes S-adenosyl-L-homocysteine homocysteinylribohydrolase (reaction.R00194), 5'-deoxyadenosine ribohydrolase (reaction.R12621). Component of 5'-methylthioadenosine/S-adenosylhomocysteine nucleosidase (complex.ecocyc.CPLX0-1541).

## Enriched Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

FUNCTION: Catalyzes the irreversible cleavage of the glycosidic bond in both 5'-methylthioadenosine (MTA) and S-adenosylhomocysteine (SAH/AdoHcy) to adenine and the corresponding thioribose, 5'-methylthioribose and S-ribosylhomocysteine, respectively (PubMed:16101288, PubMed:3911944). Also cleaves 5'-deoxyadenosine, a toxic by-product of radical S-adenosylmethionine (SAM) enzymes, into 5-deoxyribose and adenine. Thus, is required for in vivo function of the radical SAM enzymes biotin synthase and lipoic acid synthase, that are inhibited by 5'-deoxyadenosine accumulation (PubMed:15911379). Can also use 5'-isobutylthioadenosine, 5'-n-butylthioadenosine, S-adenosyl-D-homocysteine, decarboxylated adenosylhomocysteine, deaminated adenosylhomocysteine and S-2-aza-adenosylhomocysteine as substrates in vitro (PubMed:3911944). {ECO:0000269|PubMed:15911379, ECO:0000269|PubMed:16101288, ECO:0000269|PubMed:3911944}.

## Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R00194|reaction.R00194]] `KEGG` `database` - via EC:3.2.2.9
- `catalyzes` --> [[reaction.R12621|reaction.R12621]] `KEGG` `database` - via EC:3.2.2.9
- `is_component_of` --> [[complex.ecocyc.CPLX0-1541|complex.ecocyc.CPLX0-1541]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0159|gene.b0159]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AF12`
- `KEGG:ecj:JW0155;eco:b0159;ecoc:C3026_00725;`
- `GeneID:93777267;948542;`
- `GO:GO:0005829; GO:0008782; GO:0008930; GO:0019284; GO:0019509; GO:0042802; GO:0042803; GO:0046124; GO:0110052`
- `EC:3.2.2.9`

## Notes

5'-methylthioadenosine/S-adenosylhomocysteine nucleosidase (MTA/SAH nucleosidase) (MTAN) (EC 3.2.2.9) (5'-deoxyadenosine nucleosidase) (DOA nucleosidase) (dAdo nucleosidase) (5'-methylthioadenosine nucleosidase) (MTA nucleosidase) (S-adenosylhomocysteine nucleosidase) (AdoHcy nucleosidase) (SAH nucleosidase) (SRH nucleosidase)
