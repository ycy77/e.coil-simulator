---
entity_id: "gene.b3499"
entity_type: "gene"
name: "rlmJ"
source_database: "NCBI RefSeq"
source_id: "gene-b3499"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3499"
  - "rlmJ"
---

# rlmJ

`gene.b3499`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3499`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rlmJ (gene.b3499) is a gene entity. It encodes rlmJ (protein.P37634). Encoded protein function: FUNCTION: Specifically methylates the adenine in position 2030 of 23S rRNA. Nascent 23S rRNA seems to be the natural substrate. Appears to be not necessary for ribosome assembly. Required for the utilization of extracellular DNA as the sole source of carbon and energy (PubMed:11591672, PubMed:16707682). {ECO:0000255|HAMAP-Rule:MF_00934, ECO:0000269|PubMed:11591672, ECO:0000269|PubMed:16707682, ECO:0000269|PubMed:22847818, ECO:0000269|PubMed:23945937}. EcoCyc product frame: EG12234-MONOMER. EcoCyc synonyms: yhiR. Genomic coordinates: 3645385-3646227. EcoCyc protein note: RlmJ is the methyltransferase responsible for methylation of 23S rRNA at the N6 position of the A2030 nucleotide. In vitro, RlmJ can methylate A2030 most efficiently in free 23S rRNA, but not in assembled 50S ribosomal subunits . Lack of RlmJ does not affect ribosome assembly. The abundance of only a limited number of proteins is affected by lack of 23S rRNA modification at A2030 . Crystal structures of the enzyme have been solved, allowing the identification of substrate binding sites. Site-directed mutagenesis of predicted active site residues confirmed their importance . rlmJ is a homologue of the H. influenzae competence gene comJ...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37634|protein.P37634]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0011428,ECOCYC:EG12234,GeneID:948012`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3645385-3646227:+; feature_type=gene
