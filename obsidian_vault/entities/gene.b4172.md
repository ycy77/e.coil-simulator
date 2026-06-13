---
entity_id: "gene.b4172"
entity_type: "gene"
name: "hfq"
source_database: "NCBI RefSeq"
source_id: "gene-b4172"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4172"
  - "hfq"
---

# hfq

`gene.b4172`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4172`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hfq (gene.b4172) is a gene entity. It encodes hfq (protein.P0A6X3). Encoded protein function: FUNCTION: RNA chaperone that binds small regulatory RNA (sRNAs) and mRNAs to facilitate mRNA translational regulation in response to envelope stress, environmental stress and changes in metabolite concentrations. Involved in the regulation of stress responses mediated by the sigma factors RpoS, sigma-E and sigma-32 (PubMed:17158661). Binds with high specificity to tRNAs (PubMed:18230766). Binds sRNA antitoxin RalA (PubMed:24748661). In vitro, stimulates synthesis of long tails by poly(A) polymerase I (PubMed:10677490). Required for RNA phage Qbeta replication (PubMed:805130). Seems to play a role in persister cell formation; upon overexpression decreases persister cell formation while deletion increases persister formation (PubMed:19909729). {ECO:0000269|PubMed:10677490, ECO:0000269|PubMed:17158661, ECO:0000269|PubMed:18230766, ECO:0000269|PubMed:19909729, ECO:0000269|PubMed:24748661, ECO:0000269|PubMed:805130}. EcoCyc product frame: EG10438-MONOMER. Genomic coordinates: 4400288-4400596. EcoCyc protein note: Hfq is an RNA chaperone and major global regulator of cell physiology. The E. coli K-12 Hfq was discovered as a host factor (HF-I) required for wild-type bacteriophage Q beta (Qβ) replication...

## Biological Role

Repressed by crp (protein.P0ACJ8), nac (protein.Q47005). Activated by rpoD (protein.P00579), rpoH (protein.P0AGB3).

## Enriched Pathways

- `eco02024` Quorum sensing (KEGG)
- `eco03018` RNA degradation (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A6X3|protein.P0A6X3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=hfq; function=+
- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=hfq; function=+
- `represses` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=hfq; function=-
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=hfq; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0013659,ECOCYC:EG10438,GeneID:948689`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4400288-4400596:+; feature_type=gene
