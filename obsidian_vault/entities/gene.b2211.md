---
entity_id: "gene.b2211"
entity_type: "gene"
name: "yojI"
source_database: "NCBI RefSeq"
source_id: "gene-b2211"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2211"
  - "yojI"
---

# yojI

`gene.b2211`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2211`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yojI (gene.b2211) is a gene entity. It encodes yojI (protein.P33941). Encoded protein function: FUNCTION: Mediates resistance to the antibacterial peptide microcin J25, when expressed from a multicopy vector. Functions as an efflux pump for microcin J25, with the help of the outer membrane channel TolC. {ECO:0000269|PubMed:15866933}. EcoCyc product frame: YOJI-MONOMER. EcoCyc synonyms: yojJ. Genomic coordinates: 2306972-2308615. EcoCyc protein note: YojI is a member of the ABC superfamily of transporters . Sequence analysis suggests that yojI encodes an ABC-type exporter with six hydrophobic transmembrane segments and a single nucleotide-binding domain . Overexpression of yojI from a plasmid vector confers resistance to the peptide antibiotic, microcin J25; this resistance phenotype is abolished when a tolC null allele is present suggesting that YojI and TolC are components of an efflux system that can export microcin J25; YojI can substitute for McjD, the natural, plasmid encoded microcin J25 exporter . Expression of yojI is upregulated by guanosine 3',5'-bispyrophosphate (ppGpp) . The transcriptional regulator, Lrp, upregulates yojI expression . yojI is one of 35 efflux-encoding genes that have been deleted or inactivated in 'Efflux KnockOut-35' (EKO-35) - a K-12 BW25133-derived strain that lacks 35 efflux pumps and can be used as a platform to study their function .

## Biological Role

Repressed by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), fur (protein.P0A9A9).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P33941|protein.P33941]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=yojI; function=-

## External IDs

- `Dbxref:ASAP:ABE-0007303,ECOCYC:EG12070,GeneID:946705`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2306972-2308615:-; feature_type=gene
