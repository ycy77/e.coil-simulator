---
entity_id: "gene.b3824"
entity_type: "gene"
name: "rhtB"
source_database: "NCBI RefSeq"
source_id: "gene-b3824"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3824"
  - "rhtB"
---

# rhtB

`gene.b3824`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3824`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rhtB (gene.b3824) is a gene entity. It encodes rhtB (protein.P0AG34). Encoded protein function: FUNCTION: Conducts the efflux of homoserine and homoserine lactone. {ECO:0000269|PubMed:10386596}. EcoCyc product frame: RHTB-MONOMER. EcoCyc synonyms: yigK. Genomic coordinates: 4008439-4009059. EcoCyc protein note: RhtB can mediate the export of L-homoserine, L-homoserine lactone and L-threonine; the physiological role of the transporter remains uncertain. Multicopy expression of rhtB confers increased resistance to L-homoserine, L-homoserine lactone, L-threonine , S-methyl methionine and possibly L-serine . Disruption or deletion of rhtB decreases resistance to L-homoserine and L-homoserine lactone , L-serine and DL-β-hydroxynorvaline and L-threonine . Multicopy expression of rhtB increases homoserine production in homoserine producer strains of E. coli; disruption of rhtB (rhtB::cat) decreases production . Multicopy expression of rhtB increases threonine production in a threonine producing strain of E. coli . RhtB contains 6 predicted transmembrane regions and is the prototype member of the Resistance to Homoserine/Threonine (RhtB) family of transporters within the LysE superfamily . rht: resistance to homoserine and threonine .

## Biological Role

Activated by lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AG34|protein.P0AG34]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0012490,ECOCYC:EG11469,GeneID:948316`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4008439-4009059:-; feature_type=gene
