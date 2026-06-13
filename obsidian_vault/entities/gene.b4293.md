---
entity_id: "gene.b4293"
entity_type: "gene"
name: "fecI"
source_database: "NCBI RefSeq"
source_id: "gene-b4293"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4293"
  - "fecI"
---

# fecI

`gene.b4293`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4293`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fecI (gene.b4293) is a gene entity. It encodes fecI (protein.P23484). Encoded protein function: FUNCTION: Sigma factors are initiation factors that promote the attachment of RNA polymerase to specific initiation sites and are then released. This sigma factor regulates transcriptional activation of the fecABCDE operon which mediates ferric citrate transport. {ECO:0000269|PubMed:2254251}. EcoCyc product frame: PD00440. Genomic coordinates: 4517714-4518235. EcoCyc protein note: FecI (σ19) belongs to the subfamily of "iron starvation sigmas" within the Extracytoplasmic Function (ECF) family of sigma factors . The only known target for transcription initiation by CPLX0-221 is the fecABCDE operon promoter . This limited role is typical for the minor sigma factors. FecI was first described as a protein that regulates the expression of genes involved in the transport of ferric citrate and was later shown to be the sigma factor that enables transcription from the fec transport operon promoter upstream of fecA . In vitro, transcription by CPLX0-221 is highest at 25°C and is stimulated by the presence of potassium glutamate...

## Biological Role

Repressed by slyA (protein.P0A8W2), fur (protein.P0A9A9). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P23484|protein.P23484]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `C` - sigma=sigma70; target=fecI; function=+
- `represses` <-- [[protein.P0A8W2|protein.P0A8W2]] `RegulonDB` `S` - regulator=SlyA; target=fecI; function=-
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `C` - regulator=Fur; target=fecI; function=-

## External IDs

- `Dbxref:ASAP:ABE-0014072,ECOCYC:EG10291,GeneID:946839`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4517714-4518235:-; feature_type=gene
