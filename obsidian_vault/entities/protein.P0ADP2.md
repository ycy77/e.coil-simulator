---
entity_id: "protein.P0ADP2"
entity_type: "protein"
name: "yigI"
source_database: "UniProt"
source_id: "P0ADP2"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305|PubMed:35876515}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yigI b3820 JW5588"
---

# yigI

`protein.P0ADP2`

## Static

- Type: `protein`
- Source: `UniProt:P0ADP2`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305|PubMed:35876515}.

## Enriched Summary

FUNCTION: Displays thioesterase activity against medium- to long-chain acyl-CoA substrates (PubMed:35876515). Is involved in the thioesterase-dependent beta-oxidation pathway of (9Z,11E)-octadecadienoate (conjugated linoleic acid or CLA), along with TesB and FadM (PubMed:35876515). In vitro, is active against decanoyl-CoA and palmitoyl-CoA (hexadecanoyl-CoA), but not with acetyl-, butyl- or benzoyl-CoA (PubMed:35876515). Lacks general lipase or amidase activity (PubMed:35876515). Likely plays an important and specific role under natural conditions in permitting the metabolism of unusual carbon sources (PubMed:35876515). {ECO:0000269|PubMed:35876515}. This cytosolic acyl-CoA thioesterase is involved in thioesterase-dependent β-oxidation of fatty acids in E. coli . It participates in the degradation of conjugated linoleic acid (CLA), overlapping in its substrate specificities with two other cytosolic thioesterases in E. coli, EG10995 and G6244; the three genes differ in the conditions under which they are expressed . Computational prediction of its structure shows high sequence similarity and structural alignment with a thioesterase from TAX-70863 including a hot-dog fold characteristic of thioesterases...

## Biological Role

Catalyzes ACYL-COA-HYDROLASE-RXN (reaction.ecocyc.ACYL-COA-HYDROLASE-RXN), PALMITOYL-COA-HYDROLASE-RXN (reaction.ecocyc.PALMITOYL-COA-HYDROLASE-RXN), RXN-9628 (reaction.ecocyc.RXN-9628).

## Annotation

FUNCTION: Displays thioesterase activity against medium- to long-chain acyl-CoA substrates (PubMed:35876515). Is involved in the thioesterase-dependent beta-oxidation pathway of (9Z,11E)-octadecadienoate (conjugated linoleic acid or CLA), along with TesB and FadM (PubMed:35876515). In vitro, is active against decanoyl-CoA and palmitoyl-CoA (hexadecanoyl-CoA), but not with acetyl-, butyl- or benzoyl-CoA (PubMed:35876515). Lacks general lipase or amidase activity (PubMed:35876515). Likely plays an important and specific role under natural conditions in permitting the metabolism of unusual carbon sources (PubMed:35876515). {ECO:0000269|PubMed:35876515}.

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.ACYL-COA-HYDROLASE-RXN|reaction.ecocyc.ACYL-COA-HYDROLASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.PALMITOYL-COA-HYDROLASE-RXN|reaction.ecocyc.PALMITOYL-COA-HYDROLASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-9628|reaction.ecocyc.RXN-9628]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3820|gene.b3820]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ADP2`
- `KEGG:ecj:JW5588;eco:b3820;ecoc:C3026_20675;`
- `GeneID:93778117;948338;`
- `GO:GO:0005829; GO:0006629; GO:0016289; GO:0032787; GO:0047617`
- `EC:3.1.2.20`

## Notes

Medium/long-chain acyl-CoA thioesterase YigI (EC 3.1.2.20)
