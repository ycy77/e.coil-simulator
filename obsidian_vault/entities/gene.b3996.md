---
entity_id: "gene.b3996"
entity_type: "gene"
name: "nudC"
source_database: "NCBI RefSeq"
source_id: "gene-b3996"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3996"
  - "nudC"
---

# nudC

`gene.b3996`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3996`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nudC (gene.b3996) is a gene entity. It encodes nudC (protein.P32664). Encoded protein function: FUNCTION: mRNA decapping enzyme that specifically removes the nicotinamide adenine dinucleotide (NAD) cap from a subset of mRNAs by hydrolyzing the diphosphate linkage to produce nicotinamide mononucleotide (NMN) and 5' monophosphate mRNA (PubMed:25533955, PubMed:27428510, PubMed:27561816). The NAD-cap is present at the 5'-end of some mRNAs and stabilizes RNA against 5'-processing (PubMed:25533955). Has preference for mRNAs with a 5'-end purine (PubMed:27428510). Catalyzes the hydrolysis of a broad range of dinucleotide pyrophosphates, but uniquely prefers the reduced form of NADH (PubMed:25533955, PubMed:7829480). {ECO:0000269|PubMed:25533955, ECO:0000269|PubMed:27428510, ECO:0000269|PubMed:27561816, ECO:0000269|PubMed:7829480}. EcoCyc product frame: EG11702-MONOMER. EcoCyc synonyms: yjaD. Genomic coordinates: 4196903-4197676.

## Biological Role

Repressed by nac (protein.Q47005).

## Enriched Pathways

- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco04146` Peroxisome (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P32664|protein.P32664]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=nudC; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0013063,ECOCYC:EG11702,GeneID:948498`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4196903-4197676:+; feature_type=gene
