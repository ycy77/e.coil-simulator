---
entity_id: "protein.P33667"
entity_type: "protein"
name: "selU"
source_database: "UniProt"
source_id: "P33667"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "selU ybbB b0503 JW0491"
---

# selU

`protein.P33667`

## Static

- Type: `protein`
- Source: `UniProt:P33667`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Involved in the post-transcriptional modification of the uridine at the wobble position (U34) of tRNA(Lys), tRNA(Glu) and tRNA(Gln) (PubMed:14594807, PubMed:22983156, PubMed:24971911, PubMed:29862510). Catalyzes the conversion of 2-thiouridine (S2U-RNA) to 2-selenouridine (Se2U-RNA) (PubMed:14594807, PubMed:24971911, PubMed:29862510). Acts in a two-step process involving geranylation of 2-thiouridine (S2U) to S-geranyl-2-thiouridine (geS2U) and subsequent selenation of the latter derivative to 2-selenouridine (Se2U) in the tRNA chain (PubMed:24971911, PubMed:29862510). {ECO:0000269|PubMed:14594807, ECO:0000269|PubMed:22983156, ECO:0000269|PubMed:24971911, ECO:0000269|PubMed:29862510}. tRNA 2-selenouridine synthase (SelU) is responsible for formation of the special selenium-containing wobble base of the three tRNAs tRNALys, tRNAGlu, and tRNAGln . The enzyme catalyzes formation of 5-methylaminomethyl-2-selenouridine (mnm5se2U) from 5-methylaminomethyl-2-thiouridine and SePO3. Purified SelU was shown to contain tRNA . SelU was found to have high substrate specificity, using the geranyl (C10) pyrophosphate most efficiently and in the micromolar range to add a prenyl group to the sulfur atom in the first anticodon position of tRNAGluUUC, tRNALysUUU and tRNAGlnUUG (carboxy)5-methylaminomethyl-2-thiouridine-modified nucleotides...

## Biological Role

Catalyzes 5-methylaminomethyl-2-(Se-phospho)selenouridine34 phosphohydrolase (reaction.R12583), RXN0-2281 (reaction.ecocyc.RXN0-2281). Bound by Magnesium cation (molecule.C00305).

## Annotation

FUNCTION: Involved in the post-transcriptional modification of the uridine at the wobble position (U34) of tRNA(Lys), tRNA(Glu) and tRNA(Gln) (PubMed:14594807, PubMed:22983156, PubMed:24971911, PubMed:29862510). Catalyzes the conversion of 2-thiouridine (S2U-RNA) to 2-selenouridine (Se2U-RNA) (PubMed:14594807, PubMed:24971911, PubMed:29862510). Acts in a two-step process involving geranylation of 2-thiouridine (S2U) to S-geranyl-2-thiouridine (geS2U) and subsequent selenation of the latter derivative to 2-selenouridine (Se2U) in the tRNA chain (PubMed:24971911, PubMed:29862510). {ECO:0000269|PubMed:14594807, ECO:0000269|PubMed:22983156, ECO:0000269|PubMed:24971911, ECO:0000269|PubMed:29862510}.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R12583|reaction.R12583]] `KEGG` `database` - via EC:2.9.1.3
- `catalyzes` --> [[reaction.ecocyc.RXN0-2281|reaction.ecocyc.RXN0-2281]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b0503|gene.b0503]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P33667`
- `KEGG:ecj:JW0491;eco:b0503;ecoc:C3026_02470;`
- `GeneID:947063;`
- `GO:GO:0002098; GO:0016765; GO:0043828; GO:0070329`
- `EC:2.9.1.3`

## Notes

tRNA 2-selenouridine synthase (EC 2.9.1.3) (Selenophosphate-dependent tRNA 2-selenouridine synthase)
