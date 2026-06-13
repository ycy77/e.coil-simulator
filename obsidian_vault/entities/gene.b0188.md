---
entity_id: "gene.b0188"
entity_type: "gene"
name: "tilS"
source_database: "NCBI RefSeq"
source_id: "gene-b0188"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0188"
  - "tilS"
---

# tilS

`gene.b0188`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0188`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

tilS (gene.b0188) is a gene entity. It encodes tilS (protein.P52097). Encoded protein function: FUNCTION: Ligates lysine onto the cytidine present at position 34 of the AUA codon-specific tRNA(Ile) that contains the anticodon CAU, in an ATP-dependent manner. Cytidine is converted to lysidine, thus changing the amino acid specificity of the tRNA from methionine to isoleucine. This enzyme is essential for viability. EcoCyc product frame: G6096-MONOMER. EcoCyc synonyms: yaeN, mesJ. Genomic coordinates: 212331-213629. EcoCyc protein note: TilS is a tRNAIle-lysidine synthetase, the enzyme responsible for modifying the wobble base of the CAU anticodon of tRNAIle at the keto group in position 2 of C34 such that it exhibits proper recognition of the AUA codon rather than the AUG codon . This modification is necessary and sufficient for correct charging of the tRNA with isoleucine (not methionine) . TilS recognizes and modifies the precursor form of tRNAIle, thus ensuring the fidelity and avoiding errors in translation. Unmodified C34 is only found in pre-tRNAIle; mature tRNAIle contains the modified L34 base. Thus, it is not possible to generate mischarged Met-tRNAIleCAU . TilS recognizes the anticodon loop, the anticodon stem, and the acceptor stem of tRNA, allowing it to discriminate between tRNAIle and tRNAMet, which are structurally similar and share the same anticodon loop...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P52097|protein.P52097]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0000638,ECOCYC:G6096,GeneID:944889`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:212331-213629:+; feature_type=gene
