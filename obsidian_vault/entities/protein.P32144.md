---
entity_id: "protein.P32144"
entity_type: "protein"
name: "csqR"
source_database: "UniProt"
source_id: "P32144"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "csqR yihW b3884 JW5567"
---

# csqR

`protein.P32144`

## Static

- Type: `protein`
- Source: `UniProt:P32144`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Involved in the regulation of the sulfoquinovose operon (PubMed:24463506, PubMed:30372406). Represses the expression of the yihUTS operon and of the yihV and csqR genes. Binds DNA inside the spacer between the bidirectional transcription units comprising the yihUTS operon and the yihV gene, and upstream the csqR gene itself (PubMed:30372406). {ECO:0000269|PubMed:30372406, ECO:0000305|PubMed:24463506}. CsqR, formerly known as YihW and hypothesized to be a transcriptional regulator , functions as a repressor for genes of catabolism of sulfoquinovose (SQ), a hydrolysis product of sulfoquinovosyl diacylglycerol (SQDG) . CsqR belongs to the DeoR family of transcription factors and contains a helix-turn-helix motif to bind DNA in its N-terminal domain . It acts as a carbon source-dependent dual regulator involved in sustaining baseline growth in the absence of the lac operon . CsqR is likely involved in regulation of lactose metabolism and functions either in a complementary or opposite manner to a global regulator of carbohydrate metabolism, cAMP-CRP, and functions as a sugar-dependent dual regulator . Genome-wide CsqR binding sites were determined in vivo by the chromatin immunoprecipitation method combined with lambda exonuclease digestion (ChIP-exo) in glucose M9 minimal medium...

## Biological Role

Component of CsqR-6-sulfo-D-quinovose (complex.ecocyc.CPLX0-8286).

## Annotation

FUNCTION: Involved in the regulation of the sulfoquinovose operon (PubMed:24463506, PubMed:30372406). Represses the expression of the yihUTS operon and of the yihV and csqR genes. Binds DNA inside the spacer between the bidirectional transcription units comprising the yihUTS operon and the yihV gene, and upstream the csqR gene itself (PubMed:30372406). {ECO:0000269|PubMed:30372406, ECO:0000305|PubMed:24463506}.

## Outgoing Edges (6)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8286|complex.ecocyc.CPLX0-8286]] `EcoCyc` `database` - EcoCyc component coefficient=
- `represses` --> [[gene.b3880|gene.b3880]] `RegulonDB` `S` - regulator=CsqR; target=yihS; function=-
- `represses` --> [[gene.b3881|gene.b3881]] `RegulonDB` `S` - regulator=CsqR; target=yihT; function=-
- `represses` --> [[gene.b3882|gene.b3882]] `RegulonDB` `S` - regulator=CsqR; target=yihU; function=-
- `represses` --> [[gene.b3883|gene.b3883]] `RegulonDB` `S` - regulator=CsqR; target=yihV; function=-
- `represses` --> [[gene.b3884|gene.b3884]] `RegulonDB` `S` - regulator=CsqR; target=csqR; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b3884|gene.b3884]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P32144`
- `KEGG:ecj:JW5567;eco:b3884;ecoc:C3026_20995;`
- `GeneID:75204555;948381;`
- `GO:GO:0000987; GO:0003677; GO:0003700; GO:0006355; GO:0098531; GO:2000143`

## Notes

HTH-type transcriptional repressor CsqR (Regulator of sulfoquinovose catabolism)
