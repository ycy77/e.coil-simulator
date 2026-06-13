---
entity_id: "gene.b0049"
entity_type: "gene"
name: "apaH"
source_database: "NCBI RefSeq"
source_id: "gene-b0049"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0049"
  - "apaH"
---

# apaH

`gene.b0049`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0049`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

apaH (gene.b0049) is a gene entity. It encodes apaH (protein.P05637). Encoded protein function: FUNCTION: Hydrolyzes diadenosine 5',5'''-P1,P4-tetraphosphate to yield ADP. {ECO:0000269|PubMed:6317672}. EcoCyc product frame: EG10048-MONOMER. EcoCyc synonyms: cfcB. Genomic coordinates: 50380-51222. EcoCyc protein note: Diadenosine tetraphosphate (Ap4A) is a side product of aminoacyl-tRNA synthetases, including E. coli LYSU-CPLX LysU. Diadenosine tetraphosphatase (diadenosine 5', 5'''-P1, P4-tetraphosphate pyrophosphohydrolase, ApaH) hydrolyzes Ap4A and related molecules . ApaH decaps RNA molecules that contain Ap4 and Gp4 caps at the 5' end, generating a diphosphorylated RNA product . It has also been shown that ApaH can cleave both methylated and non-methylated NpnN caps . Epistasis experiments suggest an RNA decay pathway involving the consecutive actions of ApaH followed by G7459-MONOMER RppH, triggering the degradation of Np4-capped RNAs . Substrate specificity and reaction kinetics have been examined . ApaH cleaves after the second phosphate group of the adenosine moiety . Hydrolysis of, and potential inhibition by, pppGpp, a "Magic Spot Nucleotide" involved in the stringent response was observed for ApaH despite the lack of a Nudix hydrolase domain...

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P05637|protein.P05637]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0000167,ECOCYC:EG10048,GeneID:944770`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:50380-51222:-; feature_type=gene
