---
entity_id: "gene.b0076"
entity_type: "gene"
name: "leuO"
source_database: "NCBI RefSeq"
source_id: "gene-b0076"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0076"
  - "leuO"
---

# leuO

`gene.b0076`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0076`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

leuO (gene.b0076) is a gene entity. It encodes leuO (protein.P10151). Encoded protein function: FUNCTION: A global transcription factor. Activates transcription of the 9 following operons; yjjQ-bglJ, yjjP, acrEF, ybdO, yjcRQP, casABCDE12, rhsD-ybbC, fepE and gltF, in most cases it probably interferes with silencing by H-NS and activates transcription. Represses transcription of the 3 following operons; uxaCA, sdaCB and btsT. H-NS repression of the bgl operon, leading to the ability to metabolize some beta-glucosides. It also directly activates the bgl operon. Activation is H-NS and BglJ-RcsB independent. {ECO:0000269|PubMed:19429622, ECO:0000269|PubMed:20659289, ECO:0000269|PubMed:20952573, ECO:0000269|PubMed:9422614}. EcoCyc product frame: PD00519. Genomic coordinates: 84368-85312. EcoCyc protein note: LeuO is a dual transcriptional regulator that regulates genes involved in leucine biosynthesis , genes involved in the utilization of certain β-glucosides , and genes encoding LuxR-type transcription factors . It is also involved in the bacterial stringent response . An in vivo genetic selection (SELEX) and phenotype microarray analysis revealed several multidrug resistance genes as targets for LeuO, including acrEF, ygcLKJIH-ygbTF, and mdtNOP (sdsRQP). mdtNOP (sdsRQP) is involved in sensitivity control against sulfa drugs...

## Biological Role

Repressed by hns (protein.P0ACF8), lrp (protein.P0ACJ0), leuO (protein.P10151), nac (protein.Q47005). Activated by rpoD (protein.P00579), slyA (protein.P0A8W2), lrp (protein.P0ACJ0), leuO (protein.P10151), lrhA (protein.P36771).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P10151|protein.P10151]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (9)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=leuO; function=+
- `activates` <-- [[protein.P0A8W2|protein.P0A8W2]] `RegulonDB` `S` - regulator=SlyA; target=leuO; function=+
- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P10151|protein.P10151]] `RegulonDB` `S` - regulator=LeuO; target=leuO; function=-+
- `activates` <-- [[protein.P36771|protein.P36771]] `RegulonDB` `S` - regulator=LrhA; target=leuO; function=+
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `C` - regulator=H-NS; target=leuO; function=-
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P10151|protein.P10151]] `RegulonDB` `S` - regulator=LeuO; target=leuO; function=-+
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=leuO; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0000280,ECOCYC:EG10531,GeneID:949034`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:84368-85312:+; feature_type=gene
