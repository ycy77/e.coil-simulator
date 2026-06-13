---
entity_id: "protein.P0AF61"
entity_type: "protein"
name: "ghoS"
source_database: "UniProt"
source_id: "P0AF61"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ghoS arT yjdK b4128 JW4089"
---

# ghoS

`protein.P0AF61`

## Static

- Type: `protein`
- Source: `UniProt:P0AF61`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Antitoxin component of a type V toxin-antitoxin (TA) system. Neutralizes the toxic effects of toxin GhoT by digesting ghoT transcripts in a sequence-specific manner (PubMed:22941047). In concert with GhoT is involved in reducing cell growth during antibacterial stress (PubMed:24373067). Overexpression leads to transcript level reduction of 20 other mRNAs involved in purine or pyrimidine synthesis and transport. Not seen to bind its own promoter DNA (PubMed:22941047). {ECO:0000269|PubMed:22941047, ECO:0000269|PubMed:24373067}. GhoS is the antitoxin of a novel type V toxin-antitoxin system. GhoS is a sequence-specific endoribonuclease that specifically cleaves sites within the ghoT coding region of the ghoST transcript, thereby limiting translation of the GhoT toxin . ghoT is one of a small set of coding regions that do not contain cleavage sites for the G7572-MONOMER MqsR toxin, whereas the ghoS coding region contains three consensus MqsR cleavage sites. Thus, in the presence of MqsR, the ghoS-encoding 5' region of the ghoST transcript is degraded, thereby enriching for the ghoT-encoding 3' region . A solution structure of GhoS has been determined and showed structural similarity to sequence-specific endoribonucleases that preferentially cleave single-stranded RNA...

## Biological Role

Catalyzes RXN0-5509 (reaction.ecocyc.RXN0-5509).

## Annotation

FUNCTION: Antitoxin component of a type V toxin-antitoxin (TA) system. Neutralizes the toxic effects of toxin GhoT by digesting ghoT transcripts in a sequence-specific manner (PubMed:22941047). In concert with GhoT is involved in reducing cell growth during antibacterial stress (PubMed:24373067). Overexpression leads to transcript level reduction of 20 other mRNAs involved in purine or pyrimidine synthesis and transport. Not seen to bind its own promoter DNA (PubMed:22941047). {ECO:0000269|PubMed:22941047, ECO:0000269|PubMed:24373067}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5509|reaction.ecocyc.RXN0-5509]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b4128|gene.b4128]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AF61`
- `KEGG:ecj:JW4089;eco:b4128;`
- `GeneID:93777704;948646;`
- `GO:GO:0004521; GO:0016787`
- `EC:3.1.-.-`

## Notes

Endoribonuclease antitoxin GhoS (EC 3.1.-.-) (Antitoxin GhoS)
