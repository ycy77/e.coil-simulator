---
entity_id: "gene.b0226"
entity_type: "gene"
name: "dinJ"
source_database: "NCBI RefSeq"
source_id: "gene-b0226"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0226"
  - "dinJ"
---

# dinJ

`gene.b0226`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0226`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dinJ (gene.b0226) is a gene entity. It encodes dinJ (protein.Q47150). Encoded protein function: FUNCTION: Antitoxin component of a type II toxin-antitoxin (TA) system (PubMed:17263853). A labile antitoxin that counteracts the effect of cognate toxin YafQ (PubMed:17263853). YafQ and DinJ together bind their own promoter, and repress its expression (PubMed:24898247). There are 2 operators with imperfect inverted repeats (IR) in the dinJ promoter, YafQ-(DinJ)2-YafQ only binds to the first (most upstream) of them to repress transcription; binding to a single IR is sufficient for activity in vivo and in vitro (PubMed:24898247). DinJ alone is as potent a transcriptional repressor as the heterotetramer and also only needs to bind 1 IR to act (PubMed:24898247). {ECO:0000269|PubMed:17263853, ECO:0000269|PubMed:24898247}.; FUNCTION: Cell death governed by the MazE-MazF and DinJ-YafQ TA systems seems to play a role in biofilm formation (PubMed:19707553). {ECO:0000269|PubMed:19707553}. EcoCyc product frame: G6110-MONOMER. EcoCyc synonyms: sosA. Genomic coordinates: 246242-246502. EcoCyc protein note: DinJ acts as the antitoxin of the YafQ toxin by binding to YafQ and abolishing its RNase activity. DinJ can be specifically degraded by the Lon and ClpXP proteases . DinJ belongs to the ribbon-helix-helix (RHH) family of transcription factors...

## Biological Role

Repressed by nac (protein.Q47005). Activated by ygfI (protein.P52044).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q47150|protein.Q47150]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P52044|protein.P52044]] `RegulonDB` `C` - regulator=SrsR; target=dinJ; function=+
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=dinJ; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0000764,ECOCYC:G6110,GeneID:944914`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:246242-246502:-; feature_type=gene
