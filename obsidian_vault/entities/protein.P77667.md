---
entity_id: "protein.P77667"
entity_type: "protein"
name: "sufA"
source_database: "UniProt"
source_id: "P77667"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "sufA ydiC b1684 JW1674"
---

# sufA

`protein.P77667`

## Static

- Type: `protein`
- Source: `UniProt:P77667`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Member of gene cluster sufABCDSE that mediates iron-sulfur cluster assembly under oxidative stress and iron limitation conditions (PubMed:17941825). Binds [2Fe-2S] and [4Fe-4S] clusters by mobilizing sulfur atoms provided by the SufS-SufE cysteine desulfurase system and then transfers the assembled Fe-S clusters to target proteins including ferredoxin and aconitase (PubMed:17350000, PubMed:19366265). Seems to act as a Fe-S cluster carrier rather than a scaffold, this role being performed by SufB and SufC (PubMed:19810706, PubMed:23018275). {ECO:0000269|PubMed:17350000, ECO:0000269|PubMed:17941825, ECO:0000269|PubMed:19366265, ECO:0000269|PubMed:19810706, ECO:0000269|PubMed:23018275}.

## Biological Role

Component of [Fe-S] cluster insertion protein SufA (complex.ecocyc.CPLX0-7824).

## Annotation

FUNCTION: Member of gene cluster sufABCDSE that mediates iron-sulfur cluster assembly under oxidative stress and iron limitation conditions (PubMed:17941825). Binds [2Fe-2S] and [4Fe-4S] clusters by mobilizing sulfur atoms provided by the SufS-SufE cysteine desulfurase system and then transfers the assembled Fe-S clusters to target proteins including ferredoxin and aconitase (PubMed:17350000, PubMed:19366265). Seems to act as a Fe-S cluster carrier rather than a scaffold, this role being performed by SufB and SufC (PubMed:19810706, PubMed:23018275). {ECO:0000269|PubMed:17350000, ECO:0000269|PubMed:17941825, ECO:0000269|PubMed:19366265, ECO:0000269|PubMed:19810706, ECO:0000269|PubMed:23018275}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7824|complex.ecocyc.CPLX0-7824]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1684|gene.b1684]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77667`
- `KEGG:ecj:JW1674;eco:b1684;ecoc:C3026_09645;`
- `GeneID:93775839;949014;`
- `GO:GO:0005737; GO:0005829; GO:0006979; GO:0016226; GO:0042803; GO:0046872; GO:0051537; GO:0051539; GO:0051604; GO:1990230`

## Notes

Iron-sulfur cluster assembly protein SufA
