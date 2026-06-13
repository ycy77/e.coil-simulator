---
entity_id: "gene.b2406"
entity_type: "gene"
name: "xapB"
source_database: "NCBI RefSeq"
source_id: "gene-b2406"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2406"
  - "xapB"
---

# xapB

`gene.b2406`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2406`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

xapB (gene.b2406) is a gene entity. It encodes xapB (protein.P45562). Encoded protein function: FUNCTION: Uptake of xanthosine (PubMed:11466294). Can also transport other nucleosides such as inosine, adenosine, cytidine, uridine and thymidine (PubMed:11466294). Transport is driven by a proton motive force (PubMed:11466294). {ECO:0000269|PubMed:11466294}. EcoCyc product frame: XAPB-MONOMER. Genomic coordinates: 2522729-2523985. EcoCyc protein note: XapB is a probable xanthosine transporter. The xapB gene is located in a xanthosine-inducible operon with xapA, encoding xanthosine phosphorylase . Growth on xanthosine is greatly reduced in xapB mutants, and XapB was demonstrated to fractionate with the cell membrane. XapB is a member of the major facilitator superfamily of transporters and shares a high degree of similarity with the nucleoside transporter NupG . XapB therefore is probably a xanthosine/proton symporter. Imported xanthosine is cleaved by XapA to yield xanthine which can be used in nucleotide synthesis or as a nitrogen source, and ribose-1-phosphate which can be used as a carbon source.

## Biological Role

Activated by rpoD (protein.P00579), rpoS (protein.P13445), rpoN (protein.P24255).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P45562|protein.P45562]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=xapB; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=xapB; function=+
- `activates` <-- [[protein.P24255|protein.P24255]] `RegulonDB` `S` - sigma=sigma54; target=xapB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0007925,ECOCYC:EG13159,GeneID:946868`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2522729-2523985:-; feature_type=gene
