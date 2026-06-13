---
entity_id: "gene.b0447"
entity_type: "gene"
name: "decR"
source_database: "NCBI RefSeq"
source_id: "gene-b0447"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0447"
  - "decR"
---

# decR

`gene.b0447`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0447`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

decR (gene.b0447) is a gene entity. It encodes decR (protein.P0ACJ5). Encoded protein function: FUNCTION: Plays a role in L-cysteine detoxification. Binds to the dlsT(yhaO)-yhaM operon promoter in the presence but not absence of L-cysteine; activates transcription from the dlsT(yhaO)-yhaM operon. No other DNA target was identified in strain K12 / BW25113. Thiosulfate does not activate its transcription function. Overexpression doubles hydrogen sulfide production in the presence of cysteine. {ECO:0000269|Ref.1}. EcoCyc product frame: G6247-MONOMER. EcoCyc synonyms: ybaO, cyuR. Genomic coordinates: 468383-468841. EcoCyc protein note: DecR contains a helix-turn-helix motif to bind DNA in its N-terminal domain, and it appears to belong to the AsnC family of transcription factors (TFs) . DecR was confirmed as a TF through an integrated workflow comprised of computational prediction, knowledge-based classification, and experimental validation of candidate TFs at the genome scale . DecR is a regulator with an important role in cysteine detoxification . The absence of decR increases the inhibitory effect on bacterial growth caused by cysteine . The presence of cysteine improves the interaction between DecR and the promoter region of the operon yhaOM, thereby causing activation . Compared to known global TFs, DecR exhibits some interesting regulatory features...

## Biological Role

Activated by soxS (protein.P0A9E2).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ACJ5|protein.P0ACJ5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0A9E2|protein.P0A9E2]] `RegulonDB` `S` - regulator=SoxS; target=decR; function=+

## External IDs

- `Dbxref:ASAP:ABE-0001553,ECOCYC:G6247,GeneID:945091`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:468383-468841:+; feature_type=gene
