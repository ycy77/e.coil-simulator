---
entity_id: "gene.b0661"
entity_type: "gene"
name: "miaB"
source_database: "NCBI RefSeq"
source_id: "gene-b0661"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0661"
  - "miaB"
---

# miaB

`gene.b0661`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0661`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

miaB (gene.b0661) is a gene entity. It encodes miaB (protein.P0AEI1). Encoded protein function: FUNCTION: Catalyzes the methylthiolation of N6-(dimethylallyl)adenosine (i(6)A), leading to the formation of 2-methylthio-N6-(dimethylallyl)adenosine (ms(2)i(6)A) at position 37 in tRNAs that read codons beginning with uridine. {ECO:0000255|HAMAP-Rule:MF_01864, ECO:0000269|PubMed:10572129}. EcoCyc product frame: G6364-MONOMER. EcoCyc synonyms: yleA. Genomic coordinates: 693531-694955. EcoCyc protein note: MiaB is an isopentenyl-adenosine tRNA methylthiolase. Most E. coli tRNAs that read codons starting with U contain the modified base 2-methylthio-N6-isopentenyladenosine-37 (ms2i6A37) . MiaB is required for both sulfur insertion and methylation at carbon 2 of N6-isopentenyladenosine-37 in tRNA, yielding the final modified ms2i6A37 tRNA . MiaB is a member of the Radical SAM protein superfamily and was originally reported to bind two 4Fe-4S clusters . From studies in E. coli strain C6, the reaction is thought to take place in two steps: thiolation followed by methylation . It is thought that the G7511 "YgfZ protein" is involved in the repair/exchange of the spent cluster of both MiaB and the homologous enzyme G6435 RimO . MiaB interacts with CPLX0-7682 "NfuA" and EG12181-MONOMER "GrxD"...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AEI1|protein.P0AEI1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0002260,ECOCYC:G6364,GeneID:945260`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:693531-694955:-; feature_type=gene
