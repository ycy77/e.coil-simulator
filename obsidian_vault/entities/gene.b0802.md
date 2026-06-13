---
entity_id: "gene.b0802"
entity_type: "gene"
name: "ybiJ"
source_database: "NCBI RefSeq"
source_id: "gene-b0802"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0802"
  - "ybiJ"
---

# ybiJ

`gene.b0802`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0802`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ybiJ (gene.b0802) is a gene entity. It encodes ybiJ (protein.P0AAX3). Encoded protein function: Uncharacterized protein YbiJ EcoCyc product frame: EG12422-MONOMER. Genomic coordinates: 837665-837925. EcoCyc protein note: Expression of ybiJ is induced by 2,4-dinitrotoluene (2,4-DNT), 2,4,6-trinitrotoluene (2,4,6-TNT), 1,3-dinitrobenzene (1,3-DNB) , and by exposure to hydroquinone . Induction by hydroquinone is abolished in a yhaJ mutant . The actual inducer of these compounds is most likely a degradation product of the compounds . The orthologous gene in E. coli Nissle 1917 and CFT073 has a role in motility biofilm formation . ybiJ was in the top 20 genes with increased transcription and translation in response to extreme acid stress (pH 4.4 compared to pH 5.8) as measured by mRNA levels by RT-qPCR and by ribosome coverage of its transcripts using RNA-Seq .

## Biological Role

Repressed by lrp (protein.P0ACJ0). Activated by yhaJ (protein.P67660).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AAX3|protein.P0AAX3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P67660|protein.P67660]] `RegulonDB` `S` - regulator=YhaJ; target=ybiJ; function=+
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB|EcoCyc` `S` - regulator=Lrp; target=ybiJ; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0002741,ECOCYC:EG12422,GeneID:945433`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:837665-837925:-; feature_type=gene
