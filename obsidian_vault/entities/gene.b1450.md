---
entity_id: "gene.b1450"
entity_type: "gene"
name: "mcbR"
source_database: "NCBI RefSeq"
source_id: "gene-b1450"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1450"
  - "mcbR"
---

# mcbR

`gene.b1450`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1450`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mcbR (gene.b1450) is a gene entity. It encodes mcbR (protein.P76114). Encoded protein function: FUNCTION: Important for biofilm formation. Represses expression of McbA by binding to its promoter region, which prevents colanic acid overproduction and mucoidy. {ECO:0000269|PubMed:18309357}. EcoCyc product frame: G6761-MONOMER. EcoCyc synonyms: yncC. Genomic coordinates: 1520262-1520927. EcoCyc protein note: McbR is a member of the FadR C-terminal domain (FCD) family of the GntR superfamily of transcriptional regulators . It is probable that McbR binds to DNA as a dimer . Residues of McbR that could interact with DNA-binding sites are Lys38 with the α2-helix and Thr49 with the α3-helix. In addition, Arg34 and Arg52 are also important for the DNA-binding site . McbR (YncC) regulates biofilm formation and mucoidity by repressing expression of mcbA (ybiM) . McbA belongs to the YhcN family of periplasmic proteins and is induced by the quorum-sensing signal autoinducer 2 (AI-2) . McbR is negatively autoregulated and, in addition, repressed by YgiV . Expression of mcbR is induced by overexpression of the lsr operon regulators LsrR and LsrK, the quorum-sensing regulator MqsR, and the AI-2 exporter TqsA . McbR carries a helix-turn-helix DNA-binding motif (aa 37-56) and represses transcription of mcbA by binding to the promoter region of mcbA...

## Biological Role

Repressed by ygiV (protein.Q46866).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76114|protein.P76114]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q46866|protein.Q46866]] `RegulonDB` `S` - regulator=YgiV; target=mcbR; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004837,ECOCYC:G6761,GeneID:946014`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1520262-1520927:+; feature_type=gene
