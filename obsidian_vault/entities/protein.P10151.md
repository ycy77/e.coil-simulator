---
entity_id: "protein.P10151"
entity_type: "protein"
name: "leuO"
source_database: "UniProt"
source_id: "P10151"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "leuO b0076 JW0075"
---

# leuO

`protein.P10151`

## Static

- Type: `protein`
- Source: `UniProt:P10151`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: A global transcription factor. Activates transcription of the 9 following operons; yjjQ-bglJ, yjjP, acrEF, ybdO, yjcRQP, casABCDE12, rhsD-ybbC, fepE and gltF, in most cases it probably interferes with silencing by H-NS and activates transcription. Represses transcription of the 3 following operons; uxaCA, sdaCB and btsT. H-NS repression of the bgl operon, leading to the ability to metabolize some beta-glucosides. It also directly activates the bgl operon. Activation is H-NS and BglJ-RcsB independent. {ECO:0000269|PubMed:19429622, ECO:0000269|PubMed:20659289, ECO:0000269|PubMed:20952573, ECO:0000269|PubMed:9422614}. LeuO is a dual transcriptional regulator that regulates genes involved in leucine biosynthesis , genes involved in the utilization of certain β-glucosides , and genes encoding LuxR-type transcription factors . It is also involved in the bacterial stringent response . An in vivo genetic selection (SELEX) and phenotype microarray analysis revealed several multidrug resistance genes as targets for LeuO, including acrEF, ygcLKJIH-ygbTF, and mdtNOP (sdsRQP). mdtNOP (sdsRQP) is involved in sensitivity control against sulfa drugs...

## Biological Role

Component of DNA-binding transcriptional dual activator LeuO-(2S)-2-isopropylmalate (complex.ecocyc.CPLX0-13604).

## Annotation

FUNCTION: A global transcription factor. Activates transcription of the 9 following operons; yjjQ-bglJ, yjjP, acrEF, ybdO, yjcRQP, casABCDE12, rhsD-ybbC, fepE and gltF, in most cases it probably interferes with silencing by H-NS and activates transcription. Represses transcription of the 3 following operons; uxaCA, sdaCB and btsT. H-NS repression of the bgl operon, leading to the ability to metabolize some beta-glucosides. It also directly activates the bgl operon. Activation is H-NS and BglJ-RcsB independent. {ECO:0000269|PubMed:19429622, ECO:0000269|PubMed:20659289, ECO:0000269|PubMed:20952573, ECO:0000269|PubMed:9422614}.

## Outgoing Edges (19)

- `activates` --> [[gene.b0076|gene.b0076]] `RegulonDB` `S` - regulator=LeuO; target=leuO; function=-+
- `activates` --> [[gene.b2754|gene.b2754]] `RegulonDB` `C` - regulator=LeuO; target=cas2; function=+
- `activates` --> [[gene.b2755|gene.b2755]] `RegulonDB` `S` - regulator=LeuO; target=cas1; function=+
- `activates` --> [[gene.b2756|gene.b2756]] `RegulonDB` `S` - regulator=LeuO; target=casE; function=+
- `activates` --> [[gene.b2757|gene.b2757]] `RegulonDB` `C` - regulator=LeuO; target=casD; function=+
- `activates` --> [[gene.b2758|gene.b2758]] `RegulonDB` `C` - regulator=LeuO; target=casC; function=+
- `activates` --> [[gene.b2759|gene.b2759]] `RegulonDB` `C` - regulator=LeuO; target=casB; function=+
- `activates` --> [[gene.b2760|gene.b2760]] `RegulonDB` `S` - regulator=LeuO; target=casA; function=+
- `activates` --> [[gene.b3721|gene.b3721]] `RegulonDB` `S` - regulator=LeuO; target=bglB; function=+
- `activates` --> [[gene.b3722|gene.b3722]] `RegulonDB` `S` - regulator=LeuO; target=bglF; function=+
- `activates` --> [[gene.b3723|gene.b3723]] `RegulonDB` `S` - regulator=LeuO; target=bglG; function=+
- `activates` --> [[gene.b4365|gene.b4365]] `RegulonDB` `S` - regulator=LeuO; target=yjjQ; function=+
- `activates` --> [[gene.b4366|gene.b4366]] `RegulonDB` `S` - regulator=LeuO; target=bglJ; function=+
- `is_component_of` --> [[complex.ecocyc.CPLX0-13604|complex.ecocyc.CPLX0-13604]] `EcoCyc` `database` - EcoCyc component coefficient=
- `represses` --> [[gene.b0076|gene.b0076]] `RegulonDB` `S` - regulator=LeuO; target=leuO; function=-+
- `represses` --> [[gene.b0644|gene.b0644]] `RegulonDB` `S` - regulator=LeuO; target=ybeQ; function=-
- `represses` --> [[gene.b2984|gene.b2984]] `RegulonDB` `S` - regulator=LeuO; target=yghR; function=-
- `represses` --> [[gene.b2985|gene.b2985]] `RegulonDB` `S` - regulator=LeuO; target=yghS; function=-
- `represses` --> [[gene.b3214|gene.b3214]] `RegulonDB` `S` - regulator=LeuO; target=gltF; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b0076|gene.b0076]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P10151`
- `KEGG:ecj:JW0075;eco:b0076;`
- `GeneID:949034;`
- `GO:GO:0003700; GO:0006355; GO:0032993; GO:0043565`

## Notes

HTH-type transcriptional regulator LeuO
